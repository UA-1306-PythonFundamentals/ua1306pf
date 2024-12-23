"""
Homework Tracker Script

This script evaluates the completion of homework assignments by different authors 
and provides a color-coded summary of their statuses. It traverses a directory 
structure to identify homework tasks and generates a formatted report.

Modules:
    BColors: A utility class for terminal color formatting.

Functions:
    check_task(tasks: List[str]) -> List[str]:
        Compares a list of completed tasks against a predefined list of tasks 
        and formats their status using ANSI color codes.

    gather_homework_data(hw_dir: Path) -> Dict[str, List[str]]:
        Traverses the directory structure to gather data on completed tasks 
        for each author.

    print_homework_status(homework_data: Dict[str, List[str]]) -> None:
        Prints the formatted status of homework tasks for each author.

    main() -> None:
        Executes the main logic of the script, including directory traversal, 
        data processing, and result output.

Usage:
    - Place all homework files in the `hw` directory under the current working directory.
    - Ensure the directory structure follows the pattern `<root>/hw/<task>/<author>/`.
    - Run the script to generate a color-coded report showing completed and 
      missing homework tasks.

Dependencies:
    - Requires Python 3.6 or higher.
    - Requires the `os` and `pathlib` modules.

Color Code Legend:
    - Green: Completed tasks.
    - Red: Missing tasks.

Example Output:
    Author               | Tasks
    --------------------------------------------------
    author1              | hw02 hw03 hw04 hw05 hw06 hw07 hw08 hw09 hw10 hw11
    author2              | hw02 hw03 hw04 hw05 hw06 hw07 hw08 hw09 hw10 hw11
"""

import os
from pathlib import Path
from typing import List, Dict


class BColors:
    """Provides ANSI escape sequences for colored terminal output."""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def check_task(tasks: List[str]) -> List[str]:
    """
    Compares a list of completed tasks against a predefined list of all tasks
    and formats their status using color codes.

    Args:
        tasks (List[str]): List of completed tasks.

    Returns:
        List[str]: List of formatted task statuses.
    """
    all_tasks = [f"hw{str(i).zfill(2)}" for i in range(2, 12)]
    return [
        (
            f"{BColors.OKGREEN}{task}{BColors.ENDC}"
            if task in tasks
            else f"{BColors.FAIL}{task}{BColors.ENDC}"
        )
        for task in all_tasks
    ]


def gather_homework_data(hw_dir: Path) -> Dict[str, List[str]]:
    """
    Traverses the directory structure to gather homework data for authors.

    Args:
        hw_dir (Path): The base directory for homework files.

    Returns:
        Dict[str, List[str]]: Dictionary where keys are authors and values
                              are lists of completed tasks.
    """
    homework_data = {}
    if not hw_dir.exists() or not hw_dir.is_dir():
        raise FileNotFoundError(
            f"The directory {hw_dir} does not exist or is not a directory."
        )

    for root, _, _ in os.walk(hw_dir):
        path_parts = Path(root).parts
        if len(path_parts) >= 7:  # Ensure the directory structure is deep enough
            author = path_parts[6]
            task = path_parts[5]
            if author in homework_data:
                homework_data[author].append(task)
            else:
                homework_data[author] = [task]

    return homework_data


def print_homework_status(homework_data: Dict[str, List[str]]) -> None:
    """
    Prints the homework status for each author in a formatted table.

    Args:
        homework_data (Dict[str, List[str]]): Dictionary containing homework data.
    """
    print(f"{'Author':<20} | Tasks")
    print("-" * 50)
    for author, tasks in homework_data.items():
        task_statuses = check_task(tasks)
        print(f"{author:<20} | {' '.join(task_statuses)}")


def main():
    """
    Main function to execute the script logic.
    """
    hw_dir = Path(os.getcwd()) / "hw"
    try:
        homework_data = gather_homework_data(hw_dir)
        print_homework_status(homework_data)
    except FileNotFoundError as e:
        print(f"{BColors.FAIL}{e}{BColors.ENDC}")


if __name__ == "__main__":
    main()
