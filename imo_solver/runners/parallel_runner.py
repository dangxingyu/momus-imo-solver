"""
Parallel runner for IMO solver agents
"""

import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List, Optional, Type

from ..agents.base_agent import BaseAgent, SolutionStatus
from ..agents.huang_yang_agent import HuangYangAgent


def run_single_agent(
    agent_id: int,
    problem_file: str,
    log_dir: str,
    agent_class: Type[BaseAgent] = HuangYangAgent,
    config_path: str = "imo_solver/config/huang_yang_config.yaml",
    prompts_path: str = "imo_solver/prompts/huang_yang_prompts.yaml",
    base_models_path: Optional[str] = None,
    max_runs: Optional[int] = None,
) -> tuple:
    """
    Worker function to run a single agent instance

    Returns:
        (agent_id, status, time_taken)
    """
    import random

    # Stagger API requests
    delay = agent_id * 2 + random.uniform(0, 2)
    time.sleep(delay)

    print(f"[Agent {agent_id:02d}] Starting after {delay:.1f}s delay...")

    # Create log file path
    log_file = os.path.join(log_dir, f"agent_{agent_id:02d}.log")

    # Create agent instance with new architecture support
    agent = agent_class(
        config_path=config_path,
        prompts_path=prompts_path,
        base_models_path=base_models_path,
        log_file=log_file,
    )

    # Get max_runs from config if not specified
    if max_runs is None:
        max_runs = agent.config_manager.execution.get("max_runs", 2)

    # Run agent
    start_time = time.time()
    status = agent.run_from_file(problem_file, max_runs=max_runs)
    time_taken = time.time() - start_time

    return (agent_id, status, time_taken)


def run_parallel(
    problem_file: str,
    num_agents: int = None,
    agent_class: Type[BaseAgent] = HuangYangAgent,
    log_dir: str = None,
    max_workers: Optional[int] = None,
    config_path: str = "imo_solver/config/huang_yang_config.yaml",
    prompts_path: str = "imo_solver/prompts/huang_yang_prompts.yaml",
    base_models_path: Optional[str] = None,
    max_runs: Optional[int] = None,
) -> List[tuple]:
    """
    Run multiple agents in parallel

    Args:
        problem_file: Path to problem file
        num_agents: Number of parallel agents
        agent_class: Agent class to use
        log_dir: Directory for log files
        max_workers: Maximum worker processes
        config_path: Path to config file
        prompts_path: Path to prompts file

    Returns:
        List of (agent_id, status, time_taken) tuples
    """
    # Load config to get default values if not specified
    from ..utils.config_utils import ConfigManager

    config_manager = ConfigManager(config_path, prompts_path, base_models_path)

    # Use config defaults if not specified
    execution_config = config_manager.execution
    if num_agents is None:
        num_agents = execution_config.get("num_agents", 10)
    if log_dir is None:
        # Use unified logging structure - caller should provide full path now
        base_log_dir = execution_config.get("base_log_dir", "./logs")
        log_dir = os.path.join(base_log_dir, "parallel")
    if max_workers is None and execution_config.get("max_workers") is not None:
        max_workers = execution_config.get("max_workers")

    # Create log directory
    os.makedirs(log_dir, exist_ok=True)

    # Set max workers
    if max_workers is None:
        max_workers = min(num_agents, os.cpu_count() or 4)

    print(f"{'='*60}")
    print("Parallel Agent Execution")
    print(f"{'='*60}")
    print(f"Problem: {problem_file}")
    print(f"Agents: {num_agents}")
    print(f"Agent Class: {agent_class.__name__}")
    print(f"Workers: {max_workers}")
    print(f"{'='*60}\n")

    results = []
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Submit all agents
        futures = {
            executor.submit(
                run_single_agent,
                i + 1,
                problem_file,
                log_dir,
                agent_class,
                config_path,
                prompts_path,
                base_models_path,
                max_runs,
            ): i
            + 1
            for i in range(num_agents)
        }

        # Process results as they complete
        for future in as_completed(futures):
            agent_id = futures[future]
            try:
                agent_id, status, time_taken = future.result()
                results.append((agent_id, status, time_taken))

                # Print status
                if status == SolutionStatus.SOLVED:
                    print(f"[Agent {agent_id:02d}] ✓ SOLVED ({time_taken:.1f}s)")
                else:
                    print(
                        f"[Agent {agent_id:02d}] ✗ {status.value} ({time_taken:.1f}s)"
                    )

            except Exception as e:
                print(f"[Agent {agent_id:02d}] ✗ ERROR: {e}")
                results.append((agent_id, SolutionStatus.ERROR, 0))

    # Summary
    total_time = time.time() - start_time
    solved = sum(1 for _, status, _ in results if status == SolutionStatus.SOLVED)

    print(f"\n{'='*60}")
    print("Summary")
    print(f"{'='*60}")
    print(f"Total time: {total_time:.1f}s")
    print(f"Success rate: {solved}/{num_agents} ({100*solved/num_agents:.1f}%)")

    if solved > 0:
        print("✓ At least one agent found a solution!")
    else:
        print("✗ No agents found a solution")

    # Save summary.json for unified structure
    try:
        import json

        summary = {
            "problem_file": problem_file,
            "agent_class": agent_class.__name__,
            "total_agents": num_agents,
            "solved_agents": solved,
            "success_rate": solved / num_agents,
            "total_time": total_time,
            "agent_results": [
                (aid, status.value, time_taken) for aid, status, time_taken in results
            ],
        }
        summary_file = os.path.join(log_dir, "summary.json")
        with open(summary_file, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"Results saved to: {summary_file}")
    except Exception as e:
        print(f"Warning: Could not save summary.json: {e}")

    return results
