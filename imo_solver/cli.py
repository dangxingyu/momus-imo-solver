"""
Command line interface for IMO Solver package
"""

import sys
import os
import argparse
from pathlib import Path

from .agents.huang_yang_agent import HuangYangAgent
from .agents.momus_agent import MomusAgent
from .agents.base_agent import SolutionStatus
from .runners.parallel_runner import run_parallel
from .utils.config_utils import ConfigManager


def get_agent_class(agent_type):
    """Get agent class from string"""
    agents = {
        "momus": MomusAgent,
        "huang_yang": HuangYangAgent,
    }
    return agents.get(agent_type.lower(), MomusAgent)


def main():
    """Main CLI entry point for single agent solving"""
    parser = argparse.ArgumentParser(description='IMO Problem Solver')
    
    # Problem input (either file, text, or JSON metadata, but not multiple)
    problem_group = parser.add_mutually_exclusive_group(required=True)
    problem_group.add_argument('problem_file', nargs='?', type=str, help='Path to problem file')
    problem_group.add_argument('--problem-text', type=str, help='Problem statement as text (enclose in quotes)')
    problem_group.add_argument('--json-file', type=str, help='Path to JSON file with problem metadata')
    
    parser.add_argument('--agent', type=str, default='momus',
                       choices=['momus', 'huang_yang'],
                       help='Agent type to use (default: momus)')
    parser.add_argument('--log', type=str, help='Log output to file')
    parser.add_argument('--config', type=str, required=True, help='Path to roles config file')
    parser.add_argument('--prompts', type=str, required=True, help='Path to prompts file')
    parser.add_argument('--base-models', type=str, help='Path to base models file (optional, auto-detected if not provided)')
    parser.add_argument('--max-runs', type=int, default=None, help='Maximum number of runs (default: use config file value)')
    args = parser.parse_args()

    # Get agent class
    agent_class = get_agent_class(args.agent)

    # Use provided configs (required)
    config_path = args.config
    prompts_path = args.prompts
    base_models_path = args.base_models

    # Handle unified logging for single agent
    log_file = args.log
    if log_file is None:
        # Load config to get base_log_dir for unified structure
        from .utils.config_utils import ConfigManager

        config_manager = ConfigManager(config_path, prompts_path, base_models_path)
        base_log_dir = config_manager.execution.get("base_log_dir", "./logs")

        # Create single subdirectory with timestamp
        from datetime import datetime

        if args.problem_file:
            problem_name = Path(args.problem_file).stem
        else:
            problem_name = "text_problem"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        single_log_dir = os.path.join(base_log_dir, "single")
        os.makedirs(single_log_dir, exist_ok=True)
        log_file = os.path.join(single_log_dir, f"{problem_name}_{timestamp}.log")

    # Create agent with new architecture support
    agent = agent_class(
        config_path=config_path,
        prompts_path=prompts_path,
        base_models_path=base_models_path,
        log_file=log_file,
    )
    
    # Run agent based on input type
    if args.problem_text:
        print(f"[DEBUG] Using problem text: {args.problem_text}")
        status, _ = agent.run(args.problem_text, args.max_runs)
    elif args.json_file:
        # For non-discussion agents using JSON, extract problem text
        import json
        print(f"[DEBUG] Extracting problem text from JSON: {args.json_file}")
        with open(args.json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        problem_text = json_data.get('problem_text', '')
        if not problem_text:
            print("Error: No problem_text found in JSON file")
            sys.exit(1)
        status, _ = agent.run(problem_text, args.max_runs)
    else:
        print(f"[DEBUG] Using problem file: {args.problem_file}")
        status = agent.run_from_file(args.problem_file, args.max_runs)

    # Exit with appropriate code
    sys.exit(0 if status == SolutionStatus.SOLVED else 1)


def parallel_main():
    """CLI entry point for parallel execution"""
    parser = argparse.ArgumentParser(description="Parallel IMO Agent Runner")
    parser.add_argument("problem_file", type=str, help="Path to problem file")
    parser.add_argument(
        "-n",
        "--num-agents",
        type=int,
        default=None,
        help="Number of parallel agents (default: use config file value)",
    )
    parser.add_argument(
        "--agent",
        type=str,
        default="momus",
        choices=["momus", "huang_yang"],
        help="Agent type to use (default: momus)",
    )
    parser.add_argument(
        "-d",
        "--log-dir",
        type=str,
        default=None,
        help="Directory for log files (default: use config file value)",
    )
    parser.add_argument(
        "-w", "--max-workers", type=int, help="Maximum worker processes"
    )
    parser.add_argument(
        "-t", "--timeout", type=int, help="Timeout per agent in seconds"
    )
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to roles config file",
    )
    parser.add_argument(
        "--prompts", type=str, required=True, help="Path to prompts file"
    )
    parser.add_argument(
        "--base-models",
        type=str,
        help="Path to base models file (optional, auto-detected if not provided)",
    )

    args = parser.parse_args()

    # Get agent class
    agent_class = get_agent_class(args.agent)

    # Use provided configs (required)
    config_path = args.config
    prompts_path = args.prompts
    base_models_path = args.base_models

    # Load config to get default values
    config_manager = ConfigManager(config_path, prompts_path, base_models_path)

    # Use config defaults if not specified
    execution_config = config_manager.execution
    num_agents = (
        args.num_agents
        if args.num_agents is not None
        else execution_config.get("num_agents", 10)
    )

    # Unified logging: create parallel subdirectory
    base_log_dir = execution_config.get("base_log_dir", "./logs")
    if args.log_dir is not None:
        log_dir = args.log_dir
    else:
        from datetime import datetime
        from pathlib import Path

        problem_name = Path(args.problem_file).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_dir = os.path.join(base_log_dir, "parallel", f"{problem_name}_{timestamp}")

    results = run_parallel(
        problem_file=args.problem_file,
        num_agents=num_agents,
        agent_class=agent_class,
        log_dir=log_dir,
        max_workers=args.max_workers,
        config_path=config_path,
        prompts_path=prompts_path,
        base_models_path=base_models_path,
    )

    # Exit with success if any agent solved it
    sys.exit(
        0 if any(status == SolutionStatus.SOLVED for _, status, _ in results) else 1
    )


def test_main():
    """Enhanced CLI entry point for test suite (inspired by run_test_suite.py)"""
    import os
    import json
    import time
    from pathlib import Path
    from datetime import datetime
    from concurrent.futures import ProcessPoolExecutor, as_completed
    from imo_solver.runners.parallel_runner import run_single_agent

    parser = argparse.ArgumentParser(
        description="IMO Test Suite Runner - Parallel execution for policy agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single-agent test on one file
  imo-test --single imo24SL/A1.md --config imo_solver/config/huang_yang_config.yaml --prompts imo_solver/prompts/huang_yang_prompts.yaml
  
  # Directory test (loads .txt and .md files)
  imo-test --problems imo24SL --config imo_solver/config/huang_yang_config.yaml --prompts imo_solver/prompts/huang_yang_prompts.yaml --num-agents 5
        """,
    )

    # Problem specification
    parser.add_argument(
        "--problems",
        type=str,
        default=None,
        help="Problems directory (.txt/.md files). Required unless --single is set.",
    )
    parser.add_argument(
        "--single", type=str, help="Run single problem file instead of directory"
    )

    # Agent configuration
    parser.add_argument(
        "--agent",
        type=str,
        default="momus",
        choices=["momus", "huang_yang"],
        help="Agent type to use (default: momus)",
    )
    parser.add_argument(
        "--num-agents",
        type=int,
        default=None,
        help="Number of agents per problem for statistical reliability (default: use config file value)",
    )

    # Configuration files (required)
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to roles config file",
    )
    parser.add_argument(
        "--prompts", type=str, required=True, help="Path to prompts file"
    )
    parser.add_argument(
        "--base-models",
        type=str,
        help="Path to base models file (optional, auto-detected if not provided)",
    )

    # Output configuration
    parser.add_argument(
        "--logs",
        type=str,
        default=None,
        help="Logs directory (default: use config file value)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Results summary file (default: use config file value)",
    )

    args = parser.parse_args()

    if not args.single and not args.problems:
        parser.error("Either --single or --problems must be provided.")

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Use provided configs (required)
    config_path = args.config
    prompts_path = args.prompts
    base_models_path = args.base_models

    # Load config to get default values
    config_manager = ConfigManager(config_path, prompts_path, base_models_path)

    # Use config defaults if not specified
    execution_config = config_manager.execution
    num_agents = (
        args.num_agents
        if args.num_agents is not None
        else execution_config.get("num_agents", 1)
    )

    # Unified logging: create test subdirectory
    base_log_dir = execution_config.get("base_log_dir", "./logs")
    if args.logs is not None:
        logs_base_dir = args.logs
    else:
        logs_base_dir = os.path.join(base_log_dir, "test")

    # Get agent class
    agent_class = get_agent_class(args.agent)

    # Create log directory with agent type and timestamp (unified structure)
    log_dir = os.path.join(logs_base_dir, f"{args.agent}_{timestamp}")

    # Print configuration
    print("=" * 70)
    print("IMO TEST SUITE - Enhanced")
    print("=" * 70)
    print(f"Agent: {args.agent}")
    print(f"Agents per problem: {num_agents}")
    if args.single:
        print(f"Single problem: {args.single}")
    else:
        print(f"Problems directory: {args.problems}")
    print(f"Config: {config_path}")
    print(f"Prompts: {prompts_path}")
    if base_models_path:
        print(f"Base models: {base_models_path}")
    print(f"Log directory: {logs_base_dir}")
    print("=" * 70)

    # Initialize success variable
    success = False

    if args.single:
        # Single problem test - always use proper directory structure like run_test_suite.py
        problem_name = Path(args.single).stem
        problem_log_dir = os.path.join(log_dir, problem_name)

        print(f"Running {num_agents} {args.agent} agents on {problem_name}...")

        # Always use run_parallel for consistent directory structure
        results = run_parallel(
            problem_file=args.single,
            num_agents=num_agents,
            agent_class=agent_class,
            config_path=config_path,
            prompts_path=prompts_path,
            base_models_path=base_models_path,
            log_dir=problem_log_dir,  # Use problem-specific directory
        )
        solved_count = sum(
            1 for _, status, _ in results if status == SolutionStatus.SOLVED
        )
        print(f"Results: {solved_count}/{num_agents} agents solved the problem")
        success = solved_count > 0

    else:
        # Full test suite - always use batch processing for consistent directory structure
        # Enhanced test suite with multiple agents per problem and batch processing

        problems_path = Path(args.problems)
        problem_files = sorted(
            [str(f) for f in problems_path.glob("*.txt")]
            + [str(f) for f in problems_path.glob("*.md")]
        )

        if not problem_files:
            print(f"❌ No problems found in {args.problems}")
            sys.exit(1)

        # Get batch size and max workers from config
        batch_size = config_manager.execution.get("batch_size", 3)
        max_workers = config_manager.execution.get("max_workers")

        # Calculate total tasks: batch_size * num_agents
        total_concurrent_tasks = batch_size * num_agents
        if max_workers is None:
            max_workers = min(total_concurrent_tasks, os.cpu_count() or 4)

        print(f"Found {len(problem_files)} problems")
        print(f"Running {num_agents} {args.agent} agents per problem...")
        print(f"Batch size: {batch_size}, Max workers: {max_workers}")
        print(f"Total concurrent tasks: {total_concurrent_tasks}")

        os.makedirs(log_dir, exist_ok=True)
        start_time = time.time()

        # Split problems into batches
        problem_batches = []
        for i in range(0, len(problem_files), batch_size):
            problem_batches.append(problem_files[i : i + batch_size])

        print(
            f"Processing {len(problem_files)} problems in {len(problem_batches)} batches"
        )
        print("=" * 70)

        all_results = {}
        total_solved = 0
        total_problems = len(problem_files)

        def process_problem_batch(batch_problems):
            """Process batch_size problems with num_agents each = batch_size * num_agents total tasks"""
            # run_single_agent is already imported at the top of test_main

            batch_results = {}
            batch_solved = 0

            # Calculate total tasks for this batch
            total_tasks = len(batch_problems) * num_agents
            print(
                f"  Processing batch: {len(batch_problems)} problems × {num_agents} agents = {total_tasks} tasks"
            )

            # Create all problem log directories
            for problem_file in batch_problems:
                problem_name = Path(problem_file).stem
                problem_log_dir = os.path.join(log_dir, problem_name)
                os.makedirs(problem_log_dir, exist_ok=True)

            # Submit ALL tasks at once: batch_size * num_agents tasks
            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                futures = {}

                # Submit all agent tasks for all problems in this batch
                for problem_file in batch_problems:
                    problem_name = Path(problem_file).stem
                    problem_log_dir = os.path.join(log_dir, problem_name)

                    for agent_id in range(1, num_agents + 1):
                        future = executor.submit(
                            run_single_agent,
                            agent_id,
                            problem_file,
                            problem_log_dir,
                            agent_class,
                            config_path,
                            prompts_path,
                            base_models_path,
                            None,
                        )
                        futures[future] = (problem_name, agent_id)

                # Collect results by problem
                problem_results = {}
                completed_tasks = 0

                for future in as_completed(futures):
                    problem_name, agent_id = futures[future]
                    completed_tasks += 1

                    try:
                        agent_id_result, status, time_taken = future.result()

                        if problem_name not in problem_results:
                            problem_results[problem_name] = []
                        problem_results[problem_name].append(
                            (agent_id_result, status, time_taken)
                        )

                        # Print status
                        if status == SolutionStatus.SOLVED:
                            print(
                                f"  [{problem_name}] Agent {agent_id:02d} ✓ SOLVED ({time_taken:.1f}s)"
                            )
                        else:
                            print(
                                f"  [{problem_name}] Agent {agent_id:02d} ✗ {status.value} ({time_taken:.1f}s)"
                            )

                    except Exception as e:
                        print(f"  [{problem_name}] Agent {agent_id:02d} ✗ ERROR: {e}")
                        if problem_name not in problem_results:
                            problem_results[problem_name] = []
                        problem_results[problem_name].append(
                            (agent_id, SolutionStatus.ERROR, 0)
                        )

            # Summarize results for each problem
            for problem_file in batch_problems:
                problem_name = Path(problem_file).stem

                if problem_name in problem_results:
                    results = problem_results[problem_name]
                    solved_count = sum(
                        1 for _, status, _ in results if status == SolutionStatus.SOLVED
                    )
                    success_rate = solved_count / num_agents

                    if solved_count > 0:
                        print(
                            f"✅ {problem_name}: {solved_count}/{num_agents} solved ({success_rate:.0%})"
                        )
                        batch_solved += 1
                    else:
                        print(f"❌ {problem_name}: 0/{num_agents} solved")

                    batch_results[problem_name] = {
                        "solved_agents": solved_count,
                        "total_agents": num_agents,
                        "success_rate": success_rate,
                        "problem_solved": solved_count > 0,
                        "agent_results": [
                            (aid, status.value, time_taken)
                            for aid, status, time_taken in results
                        ],
                    }
                else:
                    print(f"❌ {problem_name}: No results")
                    batch_results[problem_name] = {
                        "solved_agents": 0,
                        "total_agents": num_agents,
                        "success_rate": 0.0,
                        "problem_solved": False,
                    }

            return batch_results, batch_solved

        # Process batches sequentially but problems within each batch in parallel
        for batch_num, batch_problems in enumerate(problem_batches, 1):
            print(
                f"\nBatch {batch_num}/{len(problem_batches)}: Processing {len(batch_problems)} problems..."
            )
            batch_results, batch_solved = process_problem_batch(batch_problems)
            all_results.update(batch_results)
            total_solved += batch_solved
            print(
                f"Batch {batch_num} complete: {batch_solved}/{len(batch_problems)} problems solved"
            )

        total_time = time.time() - start_time

        # Save summary
        summary = {
            "agent": agent_class.__name__,
            "config_path": config_path,
            "prompts_path": prompts_path,
            "base_models_path": base_models_path,
            "total_problems": total_problems,
            "solved_problems": total_solved,
            "success_rate": total_solved / total_problems if total_problems > 0 else 0,
            "agents_per_problem": num_agents,
            "total_time": total_time,
            "results": all_results,
        }

        # Save results file in the same log directory
        results_file = os.path.join(log_dir, "results.json")
        with open(results_file, "w") as f:
            json.dump(summary, f, indent=2)

        print(
            f"\nEnhanced test completed: {total_solved}/{total_problems} problems solved ({summary['success_rate']:.1%})"
        )
        success = total_solved > 0

    print("\n" + "=" * 70)
    print(
        f"🎯 Test {'completed successfully' if success else 'completed with failures'}"
    )
    print("=" * 70)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
