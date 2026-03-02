"""
Common utilities for the IMO problem solving agent system.

Contains configuration management, logging, API functions, and other
shared utilities that can be reused across different agent implementations.
"""

import os
import sys
import json
import time
import random
import signal
import atexit
import yaml
import requests
import argparse
from typing import Dict, Any, Optional


def parse_args():
    """Parse command line arguments for the IMO solver."""
    parser = argparse.ArgumentParser(description="IMO Problem Solver")
    parser.add_argument("problem_file", type=str, help="Path to the problem file")
    parser.add_argument("--log", type=str, help="Log output to file")
    parser.add_argument(
        "--config",
        type=str,
        default="imo_solver/config/huang_yang_config.yaml",
        help="Path to config file",
    )
    parser.add_argument(
        "--prompts",
        type=str,
        default="imo_solver/prompts/huang_yang_prompts.yaml",
        help="Path to prompts file",
    )
    parser.add_argument(
        "--max_runs", type=int, default=2, help="Maximum number of runs"
    )

    return parser.parse_args()


# --- CONFIGURATION ---
DEFAULT_MODEL = "gemini-2.5-pro"

# Global variables for logging
_log_file = None
_original_print = print


# Configuration management
class ConfigManager:
    """Manages configuration from YAML files with support for separate base models and roles files"""

    def __init__(
        self,
        config_path: Optional[str] = None,
        prompts_path: Optional[str] = None,
        base_models_path: Optional[str] = None,
    ):
        self.config = {}
        self.models = {}
        self.roles = {}
        self.execution = {}
        self.retry = {}
        self.logging_config = {}
        self.prompts = {}
        self.role_prompts = {}
        self.interaction_prompts = {}
        self.templates = {}
        self.behaviors = {}  # Store loaded behaviors
        self.behaviors_config = {}  # Store behavior configuration
        self.last_api_usage = {}  # Store last API call usage metadata

        # Support two architecture patterns:
        # 1. Single config file (legacy format)
        # 2. Separate base_models_config.yaml + roles config file (new format)

        if base_models_path and os.path.exists(base_models_path):
            # New architecture: Load base models first
            self.load_base_models(base_models_path)

        if config_path and os.path.exists(config_path):
            self.load_config(config_path)

        if prompts_path and os.path.exists(prompts_path):
            self.load_prompts(prompts_path)

        # Load behaviors if configured
        if self.behaviors_config.get("enabled", False):
            self.load_behaviors()

    def load_base_models(self, base_models_path: str):
        """Load base model definitions from separate YAML file"""
        with open(base_models_path, "r") as f:
            base_config = yaml.safe_load(f)

        # Load models from base file
        self.models = base_config.get("models", {})

    def load_config(self, config_path: str):
        """Load configuration from YAML file (roles, execution, etc.)"""
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        # If models are defined in this file, merge with base models
        # (allows legacy single-file configs to still work)
        file_models = self.config.get("models", {})
        if file_models:
            self.models.update(file_models)

        self.roles = self.config.get("roles", {})
        self.execution = self.config.get("execution", {})
        self.retry = self.config.get("retry", {})
        self.logging_config = self.config.get("logging", {})
        self.behaviors_config = self.config.get("behaviors", {})

    def load_prompts(self, prompts_path: str):
        """Load prompts from YAML file"""
        with open(prompts_path, "r") as f:
            prompts_config = yaml.safe_load(f)

        self.prompts = prompts_config.get("prompts", {})
        self.role_prompts = prompts_config.get("role_prompts", {})
        self.interaction_prompts = prompts_config.get("interaction_prompts", {})
        self.templates = prompts_config.get("templates", {})

    def get_model_for_role(self, role: str) -> Dict[str, Any]:
        """Get model configuration for a specific role"""
        if role not in self.roles:
            return {}

        role_config = self.roles[role]
        model_name = role_config.get("model")

        if model_name not in self.models:
            return {}

        model_config = self.models[model_name].copy()
        provider = model_config.get("provider", "gemini")
        gemini_model = model_config.get("gemini_model", model_name)

        # Merge role-specific params with model defaults
        params = model_config.get("default_params", {}).copy()
        role_params = role_config.get("params", {})

        # Deep merge for nested dictionaries (especially reasoning parameters)
        for key, value in role_params.items():
            if (
                key == "reasoning"
                and isinstance(value, dict)
                and key in params
                and isinstance(params[key], dict)
            ):
                # Special handling for reasoning parameters - merge rather than replace
                params[key] = params[key].copy()
                params[key].update(value)
            else:
                # Normal parameter override
                params[key] = value

        return {
            "model_name": model_name,
            "gemini_model": gemini_model,
            "provider": provider,
            "params": params,
        }

    def get_prompt(self, prompt_name: str) -> str:
        """Get a prompt by name"""
        return self.prompts.get(prompt_name, "")

    def get_role_prompt(self, role: str, prompt_type: str = "system_prompt") -> str:
        """Get a specific prompt for a role"""
        if role not in self.role_prompts:
            return ""

        prompt_key = self.role_prompts[role].get(prompt_type, "")
        if not prompt_key:
            return ""

        return self.get_prompt(prompt_key)

    def get_template(self, template_name: str, **kwargs) -> str:
        """Get and format a template with provided parameters"""
        template = self.templates.get(template_name, "")
        if template and kwargs:
            # Safe formatting - replace placeholders one by one to avoid issues with curly braces in content
            result = template
            for key, value in kwargs.items():
                placeholder = "{" + key + "}"
                if placeholder in result:
                    # Convert value to string and replace
                    result = result.replace(placeholder, str(value))
            return result
        return template

    def load_behaviors(self):
        """Load behaviors from file if configured"""
        behaviors_file = self.behaviors_config.get("behaviors_file")
        if not behaviors_file or not os.path.exists(behaviors_file):
            log_print(f"Warning: Behaviors file not found: {behaviors_file}")
            return

        try:
            with open(behaviors_file, "r") as f:
                behaviors_text = f.read()

            # Store the formatted behaviors text
            self.behaviors["formatted_text"] = behaviors_text

            # Optionally sample behaviors if configured
            sample_size = self.behaviors_config.get("sample_size")
            random_sample = self.behaviors_config.get("random_sample", False)

            if sample_size and sample_size > 0:
                # Parse behaviors from the formatted text
                lines = behaviors_text.split("\n\n")
                if random_sample and len(lines) > sample_size:
                    import random
                    lines = random.sample(lines, sample_size)
                elif len(lines) > sample_size:
                    lines = lines[:sample_size]

                self.behaviors["formatted_text"] = "\n\n".join(lines)

            log_print(f"✓ Loaded behaviors from {behaviors_file}")

        except Exception as e:
            log_print(f"Error loading behaviors: {e}")

    def get_role_prompt_with_behaviors(self, role: str, prompt_type: str = "system_prompt") -> str:
        """Get a role prompt and inject behaviors if applicable"""
        prompt = self.get_role_prompt(role, prompt_type)

        # Inject behaviors if this is a prover system prompt and behaviors are loaded
        if (role == "prover" and prompt_type == "system_prompt" and
            self.behaviors and "{behaviors}" in prompt):
            behaviors_text = self.behaviors.get("formatted_text", "")
            prompt = prompt.replace("{behaviors}", behaviors_text)

        return prompt


# --- HELPER FUNCTIONS ---
def get_prompt_required(prompt_name: str, config_manager: ConfigManager) -> str:
    """Get prompt from config, raise error if not found"""
    if not config_manager or not config_manager.prompts:
        raise ValueError(
            "Prompts configuration not loaded. Please ensure the prompts file is available."
        )

    prompt = config_manager.get_prompt(prompt_name)
    if not prompt:
        raise ValueError(
            f"Required prompt '{prompt_name}' not found in the prompts file"
        )
    return prompt


def get_role_prompt_required(
    role: str, prompt_type: str, config_manager: ConfigManager
) -> str:
    """Get role prompt from config, raise error if not found. Injects behaviors if applicable."""
    if not config_manager or not config_manager.role_prompts:
        raise ValueError(
            "Role prompts configuration not loaded. Please ensure the prompts file is available."
        )

    # Use the new method that handles behavior injection
    prompt = config_manager.get_role_prompt_with_behaviors(role, prompt_type)
    if not prompt:
        raise ValueError(
            f"Required prompt for role '{role}' type '{prompt_type}' not found in the prompts file"
        )
    return prompt


def get_template_required(
    template_name: str, config_manager: ConfigManager, **kwargs
) -> str:
    """Get template from config and format it, raise error if not found"""
    if not config_manager or not config_manager.templates:
        raise ValueError(
            "Templates configuration not loaded. Please ensure the prompts file is available."
        )

    template = config_manager.get_template(template_name, **kwargs)
    if not template:
        raise ValueError(
            f"Required template '{template_name}' not found in the prompts file"
        )
    return template


# --- LOGGING FUNCTIONS ---
def log_print(*args, **kwargs):
    """
    Log print function - outputs to both console and log file (if logging is enabled).
    Use this for problem-solving process information that should be preserved.
    """
    global _log_file

    message = " ".join(str(arg) for arg in args)

    # Always print to console
    _original_print(*args, **kwargs)

    # Also write to log file if logging is active
    if _log_file:
        _log_file.write(message + "\n")
        _log_file.flush()


def system_print(*args, **kwargs):
    """
    System print function - outputs only to console.
    Use this for system messages, user interaction, and information that
    doesn't need to be in the problem-solving log.
    """
    _original_print(*args, **kwargs)


def setup_logging(log_filename=None):
    """Setup logging to file"""
    global _log_file

    if log_filename:
        _log_file = open(log_filename, "w")
        system_print(f"Logging problem-solving process to: {log_filename}")

        def cleanup():
            global _log_file
            if _log_file:
                _log_file.close()
                _log_file = None

        atexit.register(cleanup)

        def signal_handler(sig, frame):  # pragma: no cover
            cleanup()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)


def safe_exit(code=0):
    """Safely exit the program"""
    global _log_file
    if _log_file:
        _log_file.close()
        _log_file = None
    sys.exit(code)


# --- OPENROUTER API FUNCTIONS ---
def send_openrouter_request(
    system_prompt,
    question_prompt,
    model_name=None,
    config_manager: ConfigManager = None,
    **params,
):
    """Send request to OpenRouter API"""
    if not config_manager:
        raise ValueError("config_manager parameter is required")
    manager = config_manager

    # Get API key - check environment variable first, then file
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        # Try to read from file
        api_key_file = "openrouter_api_key.txt"
        if os.path.exists(api_key_file):
            with open(api_key_file, "r") as f:
                api_key = f.read().strip()

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found. Set environment variable or create openrouter_api_key.txt file. Get one from https://openrouter.ai"
        )

    # Use default model if not specified
    if not model_name:
        model_config = manager.models.get(DEFAULT_MODEL, {})
        model_name = model_config.get("openrouter_model", DEFAULT_MODEL)

    # Build base headers (Accept set per-attempt based on streaming mode)
    base_headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Optional headers for better attribution
    site_url = os.environ.get("OR_SITE_URL")
    app_name = os.environ.get("OR_APP_NAME", "IMO-Agent")
    if site_url:
        base_headers["HTTP-Referer"] = site_url
    if app_name:
        base_headers["X-Title"] = app_name
    # Be explicit about UA to avoid proxy/CDN quirks
    user_agent = os.environ.get("OR_USER_AGENT", f"IMO-Agent/1.0 ({app_name})")
    base_headers["User-Agent"] = user_agent

    # Extract private metadata (e.g., role name) then process reasoning parameters if present
    role_name = params.pop("_role_name", None)
    processed_params = params.copy()

    # Handle reasoning parameter for OpenRouter API
    if "reasoning" in processed_params:
        reasoning_config = processed_params.pop("reasoning")

        # Convert reasoning config to OpenRouter format
        if isinstance(reasoning_config, dict):
            # Handle effort parameter
            if "effort" in reasoning_config:
                effort = reasoning_config["effort"]
                max_tokens_val = processed_params.get("max_tokens", 32768)

                # Calculate reasoning budget based on effort
                effort_ratios = {"high": 0.8, "medium": 0.5, "low": 0.2}
                if effort in effort_ratios:
                    budget_tokens = max(int(max_tokens_val * effort_ratios[effort]), 1)
                    processed_params["reasoning"] = {"max_tokens": budget_tokens}

                    if manager.logging_config.get("log_api_requests", True):
                        log_print(
                            f"[Reasoning] Effort: {effort}, Budget: {budget_tokens} tokens"
                        )

            # Handle direct max_tokens specification
            elif "max_tokens" in reasoning_config:
                budget_tokens = max(int(reasoning_config["max_tokens"]), 1)
                processed_params["reasoning"] = {"max_tokens": budget_tokens}

                if manager.logging_config.get("log_api_requests", True):
                    log_print(f"[Reasoning] Direct budget: {budget_tokens} tokens")

            # Handle exclude parameter
            if "exclude" in reasoning_config:
                if "reasoning" not in processed_params:
                    processed_params["reasoning"] = {}
                processed_params["reasoning"]["exclude"] = reasoning_config["exclude"]

            # Handle enabled parameter (for DeepSeek V3.1 thinking mode)
            if "enabled" in reasoning_config:
                if "reasoning" not in processed_params:
                    processed_params["reasoning"] = {}
                processed_params["reasoning"]["enabled"] = reasoning_config["enabled"]

                if manager.logging_config.get("log_api_requests", True):
                    enabled_status = (
                        "enabled" if reasoning_config["enabled"] else "disabled"
                    )
                    log_print(f"[Reasoning] DeepSeek thinking mode: {enabled_status}")

        # Handle boolean reasoning parameter (legacy compatibility)
        elif reasoning_config is True:
            processed_params["reasoning"] = {}
        elif reasoning_config is False:
            processed_params["reasoning"] = {"exclude": True}

    # Build request payload
    data = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question_prompt},
        ],
        # Default to non-stream unless explicitly requested via params
        "stream": bool(processed_params.pop("stream", False)),
        **processed_params,
    }

    # Send request with retries
    max_retries = manager.retry.get("max_retries", 5)
    base_delay = manager.retry.get("base_delay", 1.0)
    # Timeouts (allow override via env or config)
    connect_timeout = float(
        os.environ.get("OR_TIMEOUT_CONNECT", manager.retry.get("connect_timeout", 30))
    )
    read_timeout = float(
        os.environ.get("OR_TIMEOUT_READ", manager.retry.get("read_timeout", 600))
    )

    disable_gzip_next = False
    for attempt in range(max_retries):
        try:
            # Prepare API log event
            try:
                from .logger import api_log_event
            except Exception:
                api_log_event = None
            api_event = {
                "provider": "openrouter",
                "model": model_name,
                "role": role_name,
                "attempt": attempt + 1,
                "request": {
                    "system_prompt": system_prompt,
                    "question_prompt": question_prompt,
                    "params": processed_params,
                },
            }
            if manager.logging_config.get("log_api_requests", True):
                log_print(f"\n[OpenRouter Request - Attempt {attempt + 1}]")
                log_print(f"Model: {model_name}")
                log_print(
                    f"Parameters: {json.dumps({k: v for k, v in data.items() if k != 'messages'}, indent=2)}"
                )
                log_print(f"Timeouts: connect={connect_timeout}s, read={read_timeout}s")

            # Align headers and transport with requested streaming mode
            use_stream = bool(data.get("stream", False))
            headers = base_headers.copy()
            headers["Accept"] = (
                "text/event-stream" if use_stream else "application/json"
            )
            # Optional fallback: disable gzip if prior decode failed
            if disable_gzip_next:
                headers["Accept-Encoding"] = "identity"
            # Optional: force connection close on retries to avoid stale proxies
            if attempt > 0:
                headers["Connection"] = "close"

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                stream=use_stream,
                timeout=(connect_timeout, read_timeout),
            )

            if response.status_code == 200:
                try:
                    # Parse Server-Sent Events if applicable (transport streamed or server responded with SSE)
                    ctype = response.headers.get("Content-Type", "").lower()
                    is_sse = "text/event-stream" in ctype or bool(
                        data.get("stream", False)
                    )
                    if is_sse:
                        content_acc = []
                        reasoning_acc = []
                        usage_last = {}
                        last_error = None
                        for raw in response.iter_lines(decode_unicode=True):
                            if not raw:
                                continue  # heartbeats
                            line = raw.strip()
                            if not line.startswith("data:"):
                                continue
                            payload = line[len("data:") :].strip()
                            if payload == "[DONE]":
                                break
                            try:
                                evt = json.loads(payload)
                            except Exception:
                                continue
                            # OpenRouter error envelope inside SSE
                            if "error" in evt and evt["error"]:
                                last_error = evt["error"]
                                continue
                            choice = (evt.get("choices") or [{}])[0]
                            delta = choice.get("delta") or {}
                            msg = choice.get("message") or {}
                            piece = delta.get("content") or msg.get("content") or ""
                            if piece:
                                content_acc.append(piece)
                            if "reasoning" in msg and msg["reasoning"]:
                                reasoning_acc.append(msg["reasoning"])
                            usage_last = evt.get("usage", usage_last)
                        content_joined = "".join(content_acc).strip()
                        if not content_joined and last_error:
                            # Log embedded error details for diagnosis
                            log_print(f"[OpenRouter SSE Error] {last_error}")
                            if "api_event" in locals() and api_log_event:
                                api_event.update(
                                    {"success": False, "error": last_error}
                                )
                                api_log_event(api_event)
                            return None
                        if not content_joined:
                            # Fallback: some providers send the final message once without deltas
                            # Try to read any remaining content body if available
                            try:
                                remainder = response.raw.read(decode_content=True)
                                if remainder:
                                    try:
                                        fallback_obj = json.loads(remainder)
                                        if (
                                            "choices" in fallback_obj
                                            and fallback_obj["choices"]
                                        ):
                                            msg = fallback_obj["choices"][0].get(
                                                "message", {}
                                            )
                                            content_joined = (
                                                msg.get("content") or ""
                                            ).strip()
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                            if not content_joined:
                                log_print(
                                    "[SSE Warning] No content in stream; check provider route or parameters"
                                )
                        if "api_event" in locals() and api_log_event:
                            api_event.update(
                                {
                                    "success": True,
                                    "response": {
                                        "text": content_joined,
                                        "reasoning": (
                                            "\n".join(reasoning_acc)
                                            if reasoning_acc
                                            else None
                                        ),
                                        "usage": usage_last or {},
                                    },
                                }
                            )
                            api_log_event(api_event)
                        return content_joined if content_joined else None
                    # Otherwise, normal JSON body (non-stream)
                    result = response.json()
                except json.JSONDecodeError as e:
                    log_print(f"[API Error] Invalid JSON response: {e}")
                    log_print(f"[API Error] Status: {response.status_code}")
                    headers_dict = dict(response.headers)
                    log_print(f"[API Error] Headers: {headers_dict}")
                    if "X-Request-Id" in headers_dict:
                        log_print(
                            f"[API Error] X-Request-Id: {headers_dict['X-Request-Id']}"
                        )
                    # Attempt robust preview of body
                    raw_bytes = None
                    try:
                        raw_bytes = response.content
                    except Exception:
                        raw_bytes = None
                    body_text = (
                        raw_bytes.decode("utf-8", errors="ignore")
                        if raw_bytes
                        else response.text
                    ) or ""
                    body_preview = body_text[:500] if body_text else "<empty>"
                    log_print(f"[API Error] Response text (first 500): {body_preview}")
                    body_blank = not body_text.strip()
                    # If body is effectively empty, try an immediate streaming fallback this same attempt
                    if body_blank:
                        disable_gzip_next = True
                        try:
                            fb_headers = base_headers.copy()
                            fb_headers["Accept"] = "text/event-stream"
                            fb_headers["Accept-Encoding"] = "identity"
                            fb_headers["Connection"] = "close"
                            fb_payload = dict(data)
                            fb_payload["stream"] = True
                            fb_resp = requests.post(
                                "https://openrouter.ai/api/v1/chat/completions",
                                headers=fb_headers,
                                json=fb_payload,
                                stream=True,
                                timeout=(connect_timeout, read_timeout),
                            )
                            if fb_resp.status_code == 200:
                                ctype_fb = fb_resp.headers.get(
                                    "Content-Type", ""
                                ).lower()
                                if "text/event-stream" in ctype_fb:
                                    content_acc = []
                                    reasoning_acc = []
                                    usage_last = {}
                                    for raw in fb_resp.iter_lines(decode_unicode=True):
                                        if not raw:
                                            continue
                                        line = raw.strip()
                                        if not line.startswith("data:"):
                                            continue
                                        payload = line[len("data:") :].strip()
                                        if payload == "[DONE]":
                                            break
                                        try:
                                            evt = json.loads(payload)
                                        except Exception:
                                            continue
                                        choice = (evt.get("choices") or [{}])[0]
                                        delta = choice.get("delta") or {}
                                        msg = choice.get("message") or {}
                                        piece = (
                                            delta.get("content")
                                            or msg.get("content")
                                            or ""
                                        )
                                        if piece:
                                            content_acc.append(piece)
                                        if "reasoning" in msg and msg["reasoning"]:
                                            reasoning_acc.append(msg["reasoning"])
                                        usage_last = evt.get("usage", usage_last)
                                    joined = "".join(content_acc).strip()
                                    if joined:
                                        if manager.logging_config.get(
                                            "log_api_requests", True
                                        ):
                                            log_print(
                                                "[Fallback] Parsed SSE after blank JSON body"
                                            )
                                        if "api_event" in locals() and api_log_event:
                                            api_event.update(
                                                {
                                                    "success": True,
                                                    "response": {
                                                        "text": joined,
                                                        "reasoning": (
                                                            "\n".join(reasoning_acc)
                                                            if reasoning_acc
                                                            else None
                                                        ),
                                                        "usage": usage_last or {},
                                                    },
                                                }
                                            )
                                            api_log_event(api_event)
                                        return joined
                        except Exception:
                            pass
                    if attempt < max_retries - 1:
                        delay = base_delay * (2**attempt)
                        log_print(
                            f"[Retry] Waiting {delay}s before retry {attempt + 2}/{max_retries}"
                        )
                        time.sleep(delay)
                        continue
                    else:
                        return None

                if "choices" in result and result["choices"]:
                    message = result["choices"][0]["message"]
                    content = message["content"]
                    reasoning = message.get("reasoning")

                    # Log reasoning if available
                    if "reasoning" in message and message["reasoning"]:
                        reasoning = message["reasoning"]
                        if manager.logging_config.get("log_api_requests", True):
                            log_print(
                                f"[Response received - {len(content)} characters, reasoning: {len(reasoning)} characters]"
                            )
                        if manager.logging_config.get("log_reasoning", False):
                            log_print("\n--- REASONING ---")
                            log_print(reasoning)
                            log_print("--- END REASONING ---\n")
                    else:
                        if manager.logging_config.get("log_api_requests", True):
                            log_print(
                                f"[Response received - {len(content)} characters]"
                            )

                    # Log usage statistics if available
                    usage = result.get("usage")
                    if usage:
                        usage = result["usage"]
                        if manager.logging_config.get("log_api_requests", True):
                            prompt_tokens = usage.get("prompt_tokens", 0)
                            completion_tokens = usage.get("completion_tokens", 0)
                            reasoning_tokens = usage.get("reasoning_tokens", 0)
                            total_tokens = usage.get("total_tokens", 0)
                            log_print(
                                f"[Token usage - Prompt: {prompt_tokens}, Completion: {completion_tokens}, Reasoning: {reasoning_tokens}, Total: {total_tokens}]"
                            )
                    # API JSON event logging
                    if "api_event" in locals() and api_log_event:
                        api_event.update(
                            {
                                "success": True,
                                "response": {
                                    "text": content,
                                    "reasoning": reasoning,
                                    "usage": usage or {},
                                },
                            }
                        )
                        api_log_event(api_event)
                    return content
                else:
                    raise ValueError("Invalid response format from OpenRouter")
            else:
                raise ValueError(
                    f"OpenRouter API error: {response.status_code} - {response.text}"
                )

        except Exception as e:
            log_print(f"Request failed (attempt {attempt + 1}/{max_retries}): {e}")
            # Log failed event
            if "api_event" in locals() and api_log_event:
                api_event.update({"success": False, "error": str(e)})
                api_log_event(api_event)

            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt) + random.uniform(0, 1)
                log_print(f"Retrying in {delay:.1f} seconds...")
                time.sleep(delay)
            else:
                log_print(f"All retries exhausted. Error: {e}")
                return None

    return None


def send_gemini_request(
    system_prompt,
    question_prompt,
    model_name="gemini-2.5-flash",
    config_manager: ConfigManager = None,
    **params,
):
    """Send request to Gemini API directly"""
    if not config_manager:
        raise ValueError("config_manager parameter is required")
    manager = config_manager

    # Get API key - check environment variable first, then file
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        # Try to read from file in multiple locations
        possible_paths = [
            "gemini.key",
            "gemini_key.txt",
            "../gemini.key",
            "../gemini_key.txt",
            "../../gemini.key",
            "../../gemini_key.txt",
        ]
        for api_key_file in possible_paths:
            if os.path.exists(api_key_file):
                with open(api_key_file, "r") as f:
                    api_key = f.read().strip()
                break

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Set environment variable or create gemini.key / gemini_key.txt file. Get one from https://ai.google.dev/"
        )

    # Extract private metadata (e.g., role name)
    role_name = params.pop("_role_name", None)

    # Build headers
    headers = {"x-goog-api-key": api_key, "Content-Type": "application/json"}

    # Process parameters for Gemini format
    generation_config = {}

    # Map common parameters
    if "temperature" in params:
        generation_config["temperature"] = params["temperature"]
    if "top_p" in params:
        generation_config["topP"] = params["top_p"]
    if "max_tokens" in params:
        generation_config["maxOutputTokens"] = params["max_tokens"]

    # Handle thinking budget - direct or through reasoning config
    total_tokens = params.get("max_tokens", 32768)

    # Check for direct thinking_budget parameter first
    if "thinking_budget" in params:
        thinking_budget = params["thinking_budget"]
        generation_config["thinking_config"] = {"thinking_budget": thinking_budget}

        if manager.logging_config.get("log_api_requests", True):
            log_print(
                f"[Gemini Direct] Thinking budget: {thinking_budget} tokens, Output budget: {total_tokens} tokens"
            )

    # Fallback to reasoning config for backward compatibility
    elif "reasoning" in params:
        reasoning_config = params["reasoning"]
        if isinstance(reasoning_config, dict):
            if "effort" in reasoning_config:
                effort = reasoning_config["effort"]
                # Set explicit thinking budget limits
                thinking_budgets = {"high": 8192, "medium": 4096, "low": 2048}
                if effort in thinking_budgets:
                    thinking_budget = thinking_budgets[effort]
                    generation_config["thinking_config"] = {
                        "thinking_budget": thinking_budget
                    }

                    if manager.logging_config.get("log_api_requests", True):
                        log_print(
                            f"[Gemini Reasoning] Effort: {effort}, Thinking budget: {thinking_budget} tokens, Output budget: {total_tokens} tokens"
                        )

    # Build request URL
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"

    # Build request payload
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": f"{system_prompt}\n\n{question_prompt}"}],
            }
        ],
        "generationConfig": generation_config,
    }

    # Send request with retries
    max_retries = int(
        os.environ.get("GEM_MAX_RETRIES", manager.retry.get("max_retries", 5))
    )
    base_delay = float(
        os.environ.get("GEM_BASE_DELAY", manager.retry.get("base_delay", 1.0))
    )
    connect_timeout = float(
        os.environ.get("GEM_TIMEOUT_CONNECT", manager.retry.get("connect_timeout", 30))
    )
    read_timeout = float(
        os.environ.get("GEM_TIMEOUT_READ", manager.retry.get("read_timeout", 600))
    )

    for attempt in range(max_retries):
        try:
            try:
                from .logger import api_log_event
            except Exception:
                api_log_event = None

            api_event = {
                "provider": "gemini",
                "model": model_name,
                "role": role_name,
                "attempt": attempt + 1,
                "request": {
                    "system_prompt": system_prompt,
                    "question_prompt": question_prompt,
                    "generation_config": generation_config,
                },
            }
            if manager.logging_config.get("log_api_requests", True):
                log_print(f"\n[Gemini Request - Attempt {attempt + 1}]")
                log_print(f"Model: {model_name}")
                log_print(f"Parameters: {json.dumps(generation_config, indent=2)}")
                log_print(
                    f"Timeouts: connect={connect_timeout}s, read={read_timeout}s"
                )

            response = requests.post(
                url,
                headers=headers,
                json=data,
                timeout=(connect_timeout, read_timeout),
            )

            if response.status_code == 200:
                try:
                    result = response.json()
                except json.JSONDecodeError as e:
                    log_print(f"[Gemini Error] Invalid JSON response: {e}")
                    log_print(f"[Gemini Error] Response text: {response.text[:500]}...")
                    if attempt < max_retries - 1:
                        delay = base_delay * (2**attempt)
                        log_print(
                            f"[Retry] Waiting {delay}s before retry {attempt + 2}/{max_retries}"
                        )
                        time.sleep(delay)
                        continue
                    else:
                        return None

                if "candidates" in result and result["candidates"]:
                    candidate = result["candidates"][0]

                    # Check finish reason
                    finish_reason = candidate.get("finishReason", "UNKNOWN")
                    if finish_reason == "MAX_TOKENS":
                        log_print(
                            "[Gemini Warning] Response truncated due to token limit"
                        )

                    # Extract content
                    content = candidate.get("content", {})
                    parts = content.get("parts", [])

                    # Combine all text parts
                    text_content = ""
                    thinking_content = ""

                    for part in parts:
                        if "text" in part and part["text"]:
                            text_content += part["text"]
                        if (
                            "thought" in part and part["thought"]
                        ):  # In case thoughts are separate
                            thinking_content += part["thought"]

                    # Log response details and store usage metadata
                    usage = result.get("usageMetadata", {})
                    thoughts_tokens = usage.get("thoughtsTokenCount", 0)
                    candidate_tokens = usage.get("candidatesTokenCount", 0)
                    total_tokens = usage.get("totalTokenCount", 0)
                    
                    # Store usage in config manager for later access
                    manager.last_api_usage = {
                        "thinking_tokens": thoughts_tokens,
                        "output_tokens": candidate_tokens,
                        "total_tokens": total_tokens,
                        "provider": "gemini"
                    }
                    
                    if manager.logging_config.get("log_api_requests", True):
                        log_print(
                            f"[Gemini Response] Text: {len(text_content)} chars, Thoughts: {thoughts_tokens} tokens, Output: {candidate_tokens} tokens, Total: {total_tokens} tokens"
                        )

                        # Log thinking content if available and requested
                        if thinking_content and manager.logging_config.get(
                            "log_reasoning", False
                        ):
                            log_print("\n--- GEMINI THINKING ---")
                            log_print(thinking_content)
                            log_print("--- END THINKING ---\n")
                    # API JSON event logging
                    if "api_event" in locals() and api_log_event:
                        usage_meta = result.get("usageMetadata", {})
                        api_event.update(
                            {
                                "success": True,
                                "response": {
                                    "text": text_content,
                                    "reasoning": thinking_content,
                                    "usage": usage_meta,
                                },
                            }
                        )
                        api_log_event(api_event)

                    return text_content if text_content else None
                else:
                    raise ValueError("Invalid response format from Gemini API")
            else:
                error_msg = response.text
                if response.status_code == 400:
                    # Parse error for better debugging
                    try:
                        error_json = response.json()
                        error_msg = error_json.get("error", {}).get(
                            "message", error_msg
                        )
                    except:
                        pass
                raise ValueError(
                    f"Gemini API error: {response.status_code} - {error_msg}"
                )

        except Exception as e:
            log_print(f"Request failed (attempt {attempt + 1}/{max_retries}): {e}")
            # Log failed event
            if "api_event" in locals() and api_log_event:
                api_event.update({"success": False, "error": str(e)})
                api_log_event(api_event)

            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt) + random.uniform(0, 1)
                log_print(f"Retrying in {delay:.1f} seconds...")
                time.sleep(delay)
            else:
                log_print(f"All retries exhausted. Error: {e}")
                return None

    return None


def send_together_request(
    system_prompt,
    question_prompt,
    model_name="deepseek-ai/DeepSeek-V3.1",
    config_manager: ConfigManager = None,
    **params,
):
    """Send request to Together AI API using the together Python library"""
    if not config_manager:
        raise ValueError("config_manager parameter is required")
    manager = config_manager

    # Get API key - check environment variable first, then file
    api_key = os.environ.get("TOGETHER_API_KEY")
    if not api_key:
        # Try to read from file in multiple locations
        possible_paths = [
            "together_api_key.txt",
            "together_key.txt",  # Current directory
            "../together_api_key.txt",
            "../together_key.txt",  # Parent directory
            "../../together_api_key.txt",
            "../../together_key.txt",  # Grandparent directory
        ]
        for api_key_file in possible_paths:
            if os.path.exists(api_key_file):
                with open(api_key_file, "r") as f:
                    api_key = f.read().strip()
                break

    if not api_key:
        raise ValueError(
            "TOGETHER_API_KEY not found. Set environment variable or create together_api_key.txt or together_key.txt file. Get one from https://api.together.xyz/"
        )

    # Import Together library
    try:
        from together import Together
    except ImportError:
        raise ImportError("Together library not installed. Run: pip install together")

    # Initialize Together client
    client = Together(api_key=api_key)

    # Extract private metadata (e.g., role name)
    role_name = params.pop("_role_name", None)

    # Process parameters for Together format
    processed_params = {}

    # Map common parameters
    if "temperature" in params:
        processed_params["temperature"] = params["temperature"]
    if "top_p" in params:
        processed_params["top_p"] = params["top_p"]
    if "max_tokens" in params:
        processed_params["max_tokens"] = params["max_tokens"]
    if "frequency_penalty" in params:
        processed_params["frequency_penalty"] = params["frequency_penalty"]
    if "presence_penalty" in params:
        processed_params["presence_penalty"] = params["presence_penalty"]

    # Handle thinking/reasoning mode
    enable_thinking = False
    if "reasoning" in params:
        reasoning_config = params["reasoning"]
        # Together AI doesn't support reasoning token length control
        # Just enable/disable thinking mode based on presence of reasoning config
        if isinstance(reasoning_config, dict):
            # If reasoning config exists and not explicitly disabled, enable thinking
            enable_thinking = not reasoning_config.get("exclude", False)
        elif reasoning_config:
            enable_thinking = True

        if manager.logging_config.get("log_api_requests", True):
            thinking_status = "enabled" if enable_thinking else "disabled"
            log_print(f"[Together AI] DeepSeek V3.1 thinking mode: {thinking_status}")

    # Build chat template kwargs
    chat_template_kwargs = {}
    if enable_thinking:
        chat_template_kwargs["thinking"] = True

    # Combine system and user prompts into messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question_prompt},
    ]

    # Send request with retries
    max_retries = manager.retry.get("max_retries", 5)
    base_delay = manager.retry.get("base_delay", 1.0)

    for attempt in range(max_retries):
        try:
            # Prepare API log event
            try:
                from .logger import api_log_event
            except Exception:
                api_log_event = None

            api_event = {
                "provider": "together",
                "model": model_name,
                "role": role_name,
                "attempt": attempt + 1,
                "request": {
                    "system_prompt": system_prompt,
                    "question_prompt": question_prompt,
                    "params": processed_params,
                    "thinking_enabled": enable_thinking,
                },
            }

            if manager.logging_config.get("log_api_requests", True):
                log_print(f"\n[Together AI Request - Attempt {attempt + 1}]")
                log_print(f"Model: {model_name}")
                log_print(f"Thinking mode: {enable_thinking}")
                log_print(f"Parameters: {json.dumps(processed_params, indent=2)}")

            # Decide whether to use streaming based on configuration
            use_streaming = processed_params.pop("stream", True)

            if use_streaming:
                # Create streaming request
                stream = client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    chat_template_kwargs=(
                        chat_template_kwargs if chat_template_kwargs else None
                    ),
                    stream=True,
                    **processed_params,
                )

                # Process streaming response
                content_acc = []
                reasoning_acc = []

                for chunk in stream:
                    if chunk.choices and len(chunk.choices) > 0:
                        delta = chunk.choices[0].delta

                        # Collect reasoning tokens if present
                        if hasattr(delta, "reasoning") and delta.reasoning:
                            reasoning_acc.append(delta.reasoning)

                        # Collect content tokens if present
                        if hasattr(delta, "content") and delta.content:
                            content_acc.append(delta.content)

                # Combine accumulated content
                content = "".join(content_acc)
                reasoning = "".join(reasoning_acc) if reasoning_acc else None

                # Log response details
                if manager.logging_config.get("log_api_requests", True):
                    log_print(f"[Together AI Response] Content: {len(content)} chars")
                    if reasoning:
                        log_print(
                            f"[Together AI Response] Reasoning: {len(reasoning)} chars"
                        )

                # Log reasoning if requested
                if reasoning and manager.logging_config.get("log_reasoning", False):
                    log_print("\n--- THINKING PROCESS ---")
                    log_print(reasoning)
                    log_print("--- END THINKING ---\n")

                # Log successful API event
                if api_event and api_log_event:
                    api_event.update(
                        {
                            "success": True,
                            "response": {
                                "text": content,
                                "reasoning": reasoning,
                            },
                        }
                    )
                    api_log_event(api_event)

                return content if content else None

            else:
                # Non-streaming request
                response = client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    chat_template_kwargs=(
                        chat_template_kwargs if chat_template_kwargs else None
                    ),
                    stream=False,
                    **processed_params,
                )

                # Extract content from response
                if response.choices and len(response.choices) > 0:
                    message = response.choices[0].message
                    content = message.content if hasattr(message, "content") else ""
                    reasoning = (
                        message.reasoning if hasattr(message, "reasoning") else None
                    )

                    # Log response details
                    if manager.logging_config.get("log_api_requests", True):
                        log_print(
                            f"[Together AI Response] Content: {len(content)} chars"
                        )
                        if reasoning:
                            log_print(
                                f"[Together AI Response] Reasoning: {len(reasoning)} chars"
                            )

                    # Log reasoning if requested
                    if reasoning and manager.logging_config.get("log_reasoning", False):
                        log_print("\n--- THINKING PROCESS ---")
                        log_print(reasoning)
                        log_print("--- END THINKING ---\n")

                    # Log successful API event
                    if api_event and api_log_event:
                        api_event.update(
                            {
                                "success": True,
                                "response": {
                                    "text": content,
                                    "reasoning": reasoning,
                                },
                            }
                        )
                        api_log_event(api_event)

                    return content if content else None
                else:
                    raise ValueError("No response from Together AI")

        except Exception as e:
            log_print(f"Request failed (attempt {attempt + 1}/{max_retries}): {e}")

            # Log failed event
            if "api_event" in locals() and api_log_event:
                api_event.update({"success": False, "error": str(e)})
                api_log_event(api_event)

            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt) + random.uniform(0, 1)
                log_print(f"Retrying in {delay:.1f} seconds...")
                time.sleep(delay)
            else:
                log_print(f"All retries exhausted. Error: {e}")
                return None

    return None


def send_deepseek_request(
    system_prompt,
    question_prompt,
    model_name="deepseek-chat",
    config_manager: ConfigManager = None,
    **params,
):
    """Send request to DeepSeek API directly"""
    if not config_manager:
        raise ValueError("config_manager parameter is required")
    manager = config_manager

    # Get API key - check environment variable first, then file
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        # Try to read from file in multiple locations
        possible_paths = [
            "deepseek_key.txt",
            "../deepseek_key.txt",
            "../../deepseek_key.txt",
        ]
        for api_key_file in possible_paths:
            if os.path.exists(api_key_file):
                with open(api_key_file, "r") as f:
                    api_key = f.read().strip()
                break

    if not api_key:
        raise ValueError(
            "DEEPSEEK_API_KEY not found. Set environment variable or create deepseek_key.txt file. Get one from https://platform.deepseek.com/"
        )

    # Extract private metadata (e.g., role name)
    role_name = params.pop("_role_name", None)

    # Build headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Process parameters for DeepSeek format
    processed_params = {}

    # Map common parameters
    if "temperature" in params:
        processed_params["temperature"] = params["temperature"]
    if "top_p" in params:
        processed_params["top_p"] = params["top_p"]
    if "max_tokens" in params:
        processed_params["max_tokens"] = params["max_tokens"]
    if "frequency_penalty" in params:
        processed_params["frequency_penalty"] = params["frequency_penalty"]
    if "presence_penalty" in params:
        processed_params["presence_penalty"] = params["presence_penalty"]

    # Handle reasoning configuration for deepseek-reasoner model
    if model_name == "deepseek-reasoner":
        # DeepSeek reasoner model enables thinking mode automatically
        # No special parameters needed, the model will include reasoning in response
        if manager.logging_config.get("log_api_requests", True):
            log_print("[DeepSeek] Using reasoner model with thinking mode enabled")

    # Handle reasoning parameter if present (for compatibility)
    if "reasoning" in params:
        reasoning_config = params["reasoning"]
        if isinstance(reasoning_config, dict):
            # Log reasoning configuration but don't send to API
            # DeepSeek handles reasoning internally
            if "effort" in reasoning_config and manager.logging_config.get(
                "log_api_requests", True
            ):
                log_print(
                    f"[DeepSeek] Reasoning effort: {reasoning_config['effort']} (handled by model)"
                )

    # Build request URL
    url = "https://api.deepseek.com/chat/completions"

    # Build request payload
    data = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question_prompt},
        ],
        "stream": False,
        **processed_params,
    }

    # Send request with retries
    max_retries = manager.retry.get("max_retries", 5)
    base_delay = manager.retry.get("base_delay", 1.0)

    for attempt in range(max_retries):
        try:
            try:
                from .logger import api_log_event
            except Exception:
                api_log_event = None

            api_event = {
                "provider": "deepseek",
                "model": model_name,
                "role": role_name,
                "attempt": attempt + 1,
                "request": {
                    "system_prompt": system_prompt,
                    "question_prompt": question_prompt,
                    "params": processed_params,
                },
            }
            if manager.logging_config.get("log_api_requests", True):
                log_print(f"\n[DeepSeek Request - Attempt {attempt + 1}]")
                log_print(f"Model: {model_name}")
                log_print(f"Parameters: {json.dumps(processed_params, indent=2)}")

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                try:
                    result = response.json()
                except json.JSONDecodeError as e:
                    log_print(f"[DeepSeek Error] Invalid JSON response: {e}")
                    log_print(
                        f"[DeepSeek Error] Response text: {response.text[:500]}..."
                    )
                    if attempt < max_retries - 1:
                        delay = base_delay * (2**attempt)
                        log_print(
                            f"[Retry] Waiting {delay}s before retry {attempt + 2}/{max_retries}"
                        )
                        time.sleep(delay)
                        continue
                    else:
                        return None

                if "choices" in result and result["choices"]:
                    choice = result["choices"][0]
                    message = choice.get("message", {})
                    content = message.get("content", "")

                    # Extract reasoning content if present (for deepseek-reasoner)
                    reasoning_content = message.get("reasoning_content", "")

                    # Log response details
                    if manager.logging_config.get("log_api_requests", True):
                        usage = result.get("usage", {})
                        prompt_tokens = usage.get("prompt_tokens", 0)
                        completion_tokens = usage.get("completion_tokens", 0)
                        reasoning_tokens = usage.get("reasoning_tokens", 0)
                        if (
                            reasoning_tokens == 0
                            and "completion_tokens_details" in usage
                        ):
                            reasoning_tokens = usage["completion_tokens_details"].get(
                                "reasoning_tokens", 0
                            )
                        total_tokens = usage.get("total_tokens", 0)

                        log_print(f"[DeepSeek Response] Content: {len(content)} chars")
                        if reasoning_content:
                            log_print(
                                f"[DeepSeek Response] Reasoning: {len(reasoning_content)} chars"
                            )
                        log_print(
                            f"[Token usage - Prompt: {prompt_tokens}, Completion: {completion_tokens}, Reasoning: {reasoning_tokens}, Total: {total_tokens}]"
                        )

                        # Log reasoning content if available and requested
                        if reasoning_content and manager.logging_config.get(
                            "log_reasoning", False
                        ):
                            log_print("\n--- DEEPSEEK REASONING ---")
                            log_print(reasoning_content)
                            log_print("--- END REASONING ---\n")

                    # API JSON event logging
                    if "api_event" in locals() and api_log_event:
                        api_event.update(
                            {
                                "success": True,
                                "response": {
                                    "text": content,
                                    "reasoning": reasoning_content,
                                    "usage": result.get("usage", {}),
                                },
                            }
                        )
                        api_log_event(api_event)

                    return content if content else None
                else:
                    raise ValueError("Invalid response format from DeepSeek API")
            else:
                error_msg = response.text
                try:
                    error_json = response.json()
                    error_msg = error_json.get("error", {}).get("message", error_msg)
                except:
                    pass
                raise ValueError(
                    f"DeepSeek API error: {response.status_code} - {error_msg}"
                )

        except Exception as e:
            log_print(f"Request failed (attempt {attempt + 1}/{max_retries}): {e}")
            # Log failed event
            if "api_event" in locals() and api_log_event:
                api_event.update({"success": False, "error": str(e)})
                api_log_event(api_event)

            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt) + random.uniform(0, 1)
                log_print(f"Retrying in {delay:.1f} seconds...")
                time.sleep(delay)
            else:
                log_print(f"All retries exhausted. Error: {e}")
                return None

    return None


def send_vllm_request(
    system_prompt,
    question_prompt,
    model_name="qwen2.5-72b-instruct",
    config_manager: ConfigManager = None,
    vllm_endpoint: str = None,
    **params,
):
    """Send request to local VLLM server using OpenAI-compatible API

    Args:
        vllm_endpoint: Optional endpoint URL. Priority:
            1. vllm_endpoint parameter (from model config)
            2. VLLM_ENDPOINT environment variable
            3. vllm_endpoint.txt file
            4. Default: http://localhost:8000
    """
    if not config_manager:
        raise ValueError("config_manager parameter is required")
    manager = config_manager

    # Get VLLM endpoint with priority: param > env > file > default
    if not vllm_endpoint:
        vllm_endpoint = os.environ.get("VLLM_ENDPOINT")

    if not vllm_endpoint:
        # Try to read from file in multiple locations
        possible_paths = [
            "vllm_endpoint.txt",
            "../vllm_endpoint.txt",
            "../../vllm_endpoint.txt",
        ]
        for endpoint_file in possible_paths:
            if os.path.exists(endpoint_file):
                with open(endpoint_file, "r") as f:
                    vllm_endpoint = f.read().strip()
                break

    if not vllm_endpoint:
        # Default to localhost
        vllm_endpoint = "http://localhost:8000"
        log_print(
            f"[VLLM] No endpoint specified, using default: {vllm_endpoint}"
        )
    else:
        if manager.logging_config.get("log_api_requests", True):
            log_print(f"[VLLM] Using endpoint: {vllm_endpoint}")

    # Get optional API key for VLLM server
    vllm_api_key = os.environ.get("VLLM_API_KEY")
    if not vllm_api_key:
        # Try to read from file in multiple locations
        possible_paths = [
            "vllm_api_key.txt",
            "../vllm_api_key.txt",
            "../../vllm_api_key.txt",
        ]
        for api_key_file in possible_paths:
            if os.path.exists(api_key_file):
                with open(api_key_file, "r") as f:
                    vllm_api_key = f.read().strip()
                break

    # Extract private metadata (e.g., role name)
    role_name = params.pop("_role_name", None)

    # Build headers
    headers = {
        "Content-Type": "application/json",
    }
    if vllm_api_key:
        headers["Authorization"] = f"Bearer {vllm_api_key}"

    # Process parameters for VLLM format (OpenAI-compatible)
    processed_params = {}

    # Map common parameters
    if "temperature" in params:
        processed_params["temperature"] = params["temperature"]
    if "top_p" in params:
        processed_params["top_p"] = params["top_p"]
    if "max_tokens" in params:
        processed_params["max_tokens"] = params["max_tokens"]
    if "frequency_penalty" in params:
        processed_params["frequency_penalty"] = params["frequency_penalty"]
    if "presence_penalty" in params:
        processed_params["presence_penalty"] = params["presence_penalty"]

    # Handle reasoning/thinking mode for VLLM
    # VLLM supports reasoning via chat_template_kwargs (for Qwen3, DeepSeek-R1, etc.)
    chat_template_kwargs = {}

    if manager.logging_config.get("log_api_requests", True):
        log_print(f"[VLLM DEBUG] Model name: {model_name}")
        log_print(f"[VLLM DEBUG] Reasoning in params: {'reasoning' in params}")
        if "reasoning" in params:
            log_print(f"[VLLM DEBUG] Reasoning config: {params['reasoning']}")

    if "reasoning" in params:
        reasoning_config = params["reasoning"]

        if isinstance(reasoning_config, dict):
            # Check if thinking mode should be enabled
            enable_thinking = reasoning_config.get("enabled", True)

            # For Qwen3 models, use enable_thinking parameter
            if "qwen" in model_name.lower():
                chat_template_kwargs["enable_thinking"] = enable_thinking

                if manager.logging_config.get("log_api_requests", True):
                    thinking_status = "enabled" if enable_thinking else "disabled"
                    log_print(f"[VLLM] Qwen3 thinking mode: {thinking_status}")
            else:
                # For other models, log but don't fail
                if manager.logging_config.get("log_api_requests", True):
                    log_print(f"[VLLM] Reasoning config provided but model may not support it")
                    log_print(f"[VLLM DEBUG] Model name '{model_name}' does not contain 'qwen'")

        elif reasoning_config is False:
            # Explicitly disable thinking
            if "qwen" in model_name.lower():
                chat_template_kwargs["enable_thinking"] = False
                if manager.logging_config.get("log_api_requests", True):
                    log_print("[VLLM] Qwen3 thinking mode: disabled")

    # Build request URL - use chat completions endpoint
    url = f"{vllm_endpoint.rstrip('/')}/v1/chat/completions"

    # Build request payload
    data = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question_prompt},
        ],
        "stream": False,
        **processed_params,
    }

    # Add chat_template_kwargs if any
    if chat_template_kwargs:
        data["extra_body"] = {"chat_template_kwargs": chat_template_kwargs}
        if manager.logging_config.get("log_api_requests", True):
            log_print(f"[VLLM DEBUG] Added chat_template_kwargs: {chat_template_kwargs}")
    else:
        if manager.logging_config.get("log_api_requests", True):
            log_print("[VLLM DEBUG] No chat_template_kwargs to add")

    # Send request with retries
    max_retries = manager.retry.get("max_retries", 5)
    base_delay = manager.retry.get("base_delay", 1.0)

    for attempt in range(max_retries):
        try:
            try:
                from .logger import api_log_event
            except Exception:
                api_log_event = None

            api_event = {
                "provider": "vllm",
                "model": model_name,
                "endpoint": vllm_endpoint,
                "role": role_name,
                "attempt": attempt + 1,
                "request": {
                    "system_prompt": system_prompt,
                    "question_prompt": question_prompt,
                    "params": processed_params,
                },
            }
            if manager.logging_config.get("log_api_requests", True):
                log_print(f"\n[VLLM Request - Attempt {attempt + 1}]")
                log_print(f"Endpoint: {vllm_endpoint}")
                log_print(f"Model: {model_name}")
                log_print(f"Parameters: {json.dumps(processed_params, indent=2)}")
                if "extra_body" in data:
                    log_print(f"Extra Body: {json.dumps(data['extra_body'], indent=2)}")

            response = requests.post(url, headers=headers, json=data, timeout=None)

            if response.status_code == 200:
                try:
                    result = response.json()
                except json.JSONDecodeError as e:
                    log_print(f"[VLLM Error] Invalid JSON response: {e}")
                    log_print(f"[VLLM Error] Response text: {response.text[:500]}...")
                    if attempt < max_retries - 1:
                        delay = base_delay * (2**attempt)
                        log_print(
                            f"[Retry] Waiting {delay}s before retry {attempt + 2}/{max_retries}"
                        )
                        time.sleep(delay)
                        continue
                    else:
                        return None

                if "choices" in result and result["choices"]:
                    choice = result["choices"][0]
                    message = choice.get("message", {})
                    content = message.get("content", "")

                    # Extract reasoning content if present (for Qwen3, DeepSeek-R1, etc.)
                    # In VLLM's response format: response.choices[0].message.reasoning_content
                    reasoning_content = message.get("reasoning_content", "") or ""

                    # DEBUG: Log full message structure to diagnose reasoning_content issue
                    if manager.logging_config.get("log_api_requests", True):
                        log_print(f"[VLLM DEBUG] Full message keys: {list(message.keys())}")
                        log_print(f"[VLLM DEBUG] reasoning_content in message: {'reasoning_content' in message}")
                        if 'reasoning_content' in message:
                            log_print(f"[VLLM DEBUG] reasoning_content value: {repr(message['reasoning_content'])}")

                    # Log response details
                    if manager.logging_config.get("log_api_requests", True):
                        usage = result.get("usage", {})
                        prompt_tokens = usage.get("prompt_tokens", 0)
                        completion_tokens = usage.get("completion_tokens", 0)
                        total_tokens = usage.get("total_tokens", 0)

                        log_print(f"[VLLM Response] Content: {len(content)} chars")
                        if reasoning_content:
                            log_print(f"[VLLM Response] Reasoning: {len(reasoning_content)} chars")
                        log_print(
                            f"[Token usage - Prompt: {prompt_tokens}, Completion: {completion_tokens}, Total: {total_tokens}]"
                        )

                        # Log reasoning content if available and requested
                        if reasoning_content and manager.logging_config.get("log_reasoning", False):
                            log_print("\n--- VLLM REASONING/THINKING ---")
                            log_print(reasoning_content)
                            log_print("--- END REASONING ---\n")

                    # API JSON event logging
                    if "api_event" in locals() and api_log_event:
                        api_event.update(
                            {
                                "success": True,
                                "response": {
                                    "text": content,
                                    "reasoning": reasoning_content if reasoning_content else None,
                                    "usage": result.get("usage", {}),
                                },
                            }
                        )
                        api_log_event(api_event)

                    return content if content else None
                else:
                    raise ValueError("Invalid response format from VLLM server")
            else:
                error_msg = response.text
                try:
                    error_json = response.json()
                    error_msg = error_json.get("error", {}).get("message", error_msg)
                except:
                    pass
                raise ValueError(
                    f"VLLM server error: {response.status_code} - {error_msg}"
                )

        except Exception as e:
            log_print(f"Request failed (attempt {attempt + 1}/{max_retries}): {e}")
            # Log failed event
            if "api_event" in locals() and api_log_event:
                api_event.update({"success": False, "error": str(e)})
                api_log_event(api_event)

            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt) + random.uniform(0, 1)
                log_print(f"Retrying in {delay:.1f} seconds...")
                time.sleep(delay)
            else:
                log_print(f"All retries exhausted. Error: {e}")
                return None

    return None


def send_role_based_request(
    system_prompt, question_prompt, role="prover", config_manager: ConfigManager = None, 
    return_usage: bool = False
):
    """
    Send request using role-specific model and parameters from config
    
    Args:
        system_prompt: System prompt text
        question_prompt: User question/prompt text
        role: Role name to use for model selection
        config_manager: ConfigManager instance
        return_usage: If True, return tuple of (content, usage_dict). If False, return just content.
    
    Returns:
        If return_usage=False: content string
        If return_usage=True: tuple of (content, usage_dict)
    """
    if not config_manager:
        raise ValueError("config_manager parameter is required")
    manager = config_manager

    # Get model configuration for the role
    model_config = manager.get_model_for_role(role)

    if not model_config:
        log_print(
            f"Warning: No configuration found for role '{role}'. Using default Gemini model."
        )
        content = send_gemini_request(
            system_prompt,
            question_prompt,
            DEFAULT_MODEL,
            config_manager=manager,
            _role_name=role,
        )
        if return_usage:
            return content, manager.last_api_usage.copy()
        return content

    # Extract model name, provider, and parameters
    provider = model_config.get("provider", "gemini")
    gemini_model = model_config.get("gemini_model")
    params = model_config.get("params", {})

    if manager.logging_config.get("verbose", True):
        log_print(f"\n[Role: {role}]")
        log_print(f"Provider: {provider}")
        log_print(f"Using Gemini model: {gemini_model}")

    # Route to appropriate API based on provider
    if provider != "gemini":
        raise ValueError(
            f"Unsupported provider '{provider}' for role '{role}'. "
            "This repository supports native Gemini models only."
        )
    if not gemini_model:
        raise ValueError(
            f"No gemini_model specified for role '{role}' with provider 'gemini'"
        )

    content = send_gemini_request(
        system_prompt,
        question_prompt,
        gemini_model,
        config_manager=manager,
        _role_name=role,
        **params,
    )
    if return_usage:
        return content, manager.last_api_usage.copy()
    return content


# --- UTILITY FUNCTIONS ---
def validate_environment():
    """Validate required environment variables and configuration"""
    gemini_key = os.environ.get("GEMINI_API_KEY")

    if not gemini_key:
        possible_paths = [
            "gemini.key",
            "gemini_key.txt",
            "../gemini.key",
            "../gemini_key.txt",
            "../../gemini.key",
            "../../gemini_key.txt",
        ]
        for api_key_file in possible_paths:
            if os.path.exists(api_key_file):
                with open(api_key_file, "r") as f:
                    gemini_key = f.read().strip()
                if gemini_key:
                    break

    if not gemini_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Set GEMINI_API_KEY or create gemini.key (or gemini_key.txt). "
            "Get one from https://ai.google.dev/"
        )


def initialize_config(
    config_path: str = None, prompts_path: str = None, base_models_path: str = None
) -> ConfigManager:
    """Initialize and return a configured ConfigManager instance

    Args:
        config_path: Path to roles/execution config file
        prompts_path: Path to prompts file
        base_models_path: Path to base models file (optional, for new architecture)
    """
    # Auto-detect base models path if not provided
    if base_models_path is None and config_path:
        # Try to find base_models_config.yaml in same directory
        config_dir = os.path.dirname(config_path)
        potential_base_path = os.path.join(config_dir, "base_models_config.yaml")
        if os.path.exists(potential_base_path):
            base_models_path = potential_base_path

    config_manager = ConfigManager(config_path, prompts_path, base_models_path)

    # Verify prompts are loaded
    if not config_manager.prompts:
        system_print(f"Warning: Could not load prompts from {prompts_path}")
        system_print("Some functionality may be limited without prompts configuration.")

    # Verify models are loaded
    if not config_manager.models:
        system_print(
            f"Warning: No models loaded from {config_path} or {base_models_path}"
        )
        system_print("Please ensure model configurations are available.")

    return config_manager


# Missing functions from original utils.py
def safe_exit(code=0):
    """Safely exit the program"""
    from .logger import close_logging

    close_logging()
    sys.exit(code)


def parse_args():
    """Parse command line arguments for the IMO solver"""
    import argparse

    parser = argparse.ArgumentParser(description="IMO Problem Solver")
    parser.add_argument("problem_file", type=str, help="Path to the problem file")
    parser.add_argument("--log", type=str, help="Log output to file")
    parser.add_argument(
        "--config",
        type=str,
        default="imo_solver/config/huang_yang_config.yaml",
        help="Path to config file",
    )
    parser.add_argument(
        "--prompts",
        type=str,
        default="imo_solver/prompts/huang_yang_prompts.yaml",
        help="Path to prompts file",
    )
    parser.add_argument(
        "--max_runs", type=int, default=2, help="Maximum number of runs"
    )

    return parser.parse_args()


# Import logger functions to maintain compatibility
try:
    from .logger import log_print, system_print
except ImportError:
    # Fallback if logger module has issues
    def log_print(*args, **kwargs):
        print(*args, **kwargs)

    def system_print(*args, **kwargs):
        print(*args, **kwargs)


print = system_print
