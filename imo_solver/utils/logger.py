"""
Logging utilities for IMO solver
Simple thread-safe logging using a global shared file handle.

NOTE: setup_logging() now tracks the current log filename and skips re-opening
if the same file is already open. This prevents the truncation bug where
Momus Agent's logs were lost when MomusPostEnhancementAgent called setup_logging()
with the same log file path.
"""

import os
import sys
import signal
import atexit
import threading
from typing import Optional
import json
from datetime import datetime

# Global shared log file - accessible from all threads in same process
_log_file = None
_log_filename = None  # Track current log filename
_log_lock = threading.Lock()
_api_log_file = None
_api_log_filename = None  # Track current API log filename
_api_log_lock = threading.Lock()
_atexit_registered = False  # Track if atexit handler is registered


def setup_logging(log_filename: Optional[str] = None, force_new: bool = False):
    """
    Setup logging to file.

    Behavior:
    - If same file is already open: skip re-opening (prevents truncation bug)
    - If opening a new/different file: use "w" mode for fresh start
    - If force_new=True: always truncate and start fresh

    Args:
        log_filename: Path to log file
        force_new: If True, always truncate existing file even if same file is open.
    """
    global _log_file, _log_filename, _api_log_file, _api_log_filename, _atexit_registered

    if not log_filename:
        return

    # Normalize path for comparison
    log_filename = os.path.abspath(log_filename)
    base, _ = os.path.splitext(log_filename)
    api_log_path = f"{base}_api_log.jsonl"

    # If same file is already open and not forcing new, skip re-opening
    # This is the KEY fix: prevents MomusPostEnhancementAgent from truncating Momus logs
    if _log_file is not None and _log_filename == log_filename and not force_new:
        print(f"Log file already open, continuing to use: {log_filename}")
        return

    # Close existing files if switching to a different file or forcing new
    if _log_file is not None:
        close_logging()

    # Create directory if needed
    os.makedirs(
        os.path.dirname(log_filename) if os.path.dirname(log_filename) else ".",
        exist_ok=True,
    )

    # Always use "w" mode when opening (first time or switching files)
    # The truncation bug is prevented by skipping re-open for same file above
    mode = "w"

    _log_file = open(log_filename, mode, encoding="utf-8")
    _log_filename = log_filename
    print(f"Logging problem-solving process to: {log_filename}")

    # Setup API JSONL log (streaming, one JSON per line)
    _api_log_file = open(api_log_path, mode, encoding="utf-8")
    _api_log_filename = api_log_path
    print(f"Logging API calls to: {api_log_path}")

    # Register cleanup handlers only once
    if not _atexit_registered:
        atexit.register(close_logging)
        signal.signal(signal.SIGINT, lambda s, f: (close_logging(), sys.exit(0)))
        _atexit_registered = True


def log_print(*args, **kwargs):
    """Print to console and log file. Thread-safe."""
    message = " ".join(str(arg) for arg in args)
    print(*args, **kwargs)

    if _log_file:
        with _log_lock:
            try:
                _log_file.write(message + "\n")
                _log_file.flush()
            except Exception:
                pass


def system_print(*args, **kwargs):
    """Print to console only (not logged)."""
    print(*args, **kwargs)


def close_logging():
    """Close log files."""
    global _log_file, _log_filename, _api_log_file, _api_log_filename

    if _log_file:
        try:
            _log_file.close()
        except Exception:
            pass
        _log_file = None
        _log_filename = None

    if _api_log_file:
        try:
            _api_log_file.close()
        except Exception:
            pass
        _api_log_file = None
        _api_log_filename = None


def api_log_event(event: dict):
    """Append API call event to JSONL log. Thread-safe, writes immediately."""
    global _api_log_file

    event.setdefault("timestamp", datetime.utcnow().isoformat())

    if _api_log_file:
        with _api_log_lock:
            try:
                _api_log_file.write(json.dumps(event, ensure_ascii=False) + "\n")
                _api_log_file.flush()
            except Exception:
                pass
