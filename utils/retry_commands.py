import time
import subprocess
import random
from threading import Semaphore
from typing import Callable, Any


def retry_shell(command: str, retries: int = 3, delay: int = 5, max_concurrent: int = 1):
    """
    Retry a command a specified number of times with a delay, jitter, and concurrency control.

    :param command: Command to execute (as a string).
    :param retries: Number of retries.
    :param delay: Base delay between retries in seconds.
    :param max_concurrent: Maximum number of concurrent command executions.
    :return: The output of the command if successful, else None.
    """
    semaphore = Semaphore(max_concurrent)  # Create a semaphore with a maximum concurrency limit

    for attempt in range(retries):
        try:
            print(f"Attempt {attempt + 1}/{retries}...")

            with semaphore:  # Acquire a semaphore slot
                result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

            print("Command succeeded.")
            return result.stdout

        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e.stderr}")
            if attempt < retries - 1:  # Don't wait after the last attempt
                jitter = random.uniform(0, delay)  # Add random jitter in the range [0, delay)
                wait_time = (delay + jitter)
                print(f"Retrying in {wait_time / 60:.2f} minutes...")
                time.sleep(wait_time)  # Wait with jitter

    print("All attempts failed.")
    return None


def retry_function(
        func: Callable[..., Any], retries: int = 3, delay: int = 5, max_concurrent: int = 1, *args, **kwargs) -> Any:
    """
    Retry a function a specified number of times with a delay, jitter, and concurrency control.

    :param func: Function to execute.
    :param retries: Number of retries.
    :param delay: Base delay between retries in seconds.
    :param max_concurrent: Maximum number of concurrent function executions.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :return: The return value of the function if successful, else None.
    """
    semaphore = Semaphore(max_concurrent)  # Create a semaphore with a maximum concurrency limit

    for attempt in range(retries):
        try:
            print(f"Attempt {attempt + 1}/{retries}...")

            with semaphore:  # Acquire a semaphore slot
                result = func(*args, **kwargs)
                print("Function succeeded.")
                return result

        except Exception as e:  # Catch any exception raised by the function
            print(f"Function failed with error: {e}")
            if attempt < retries - 1:  # Do not wait after the last attempt
                jitter = random.uniform(0, delay)  # Add random jitter in the range [0, delay)
                wait_time = (delay + jitter)
                print(f"Retrying in {wait_time / 60:.2f} seconds...")
                time.sleep(wait_time)  # Wait with jitter

    print("All attempts failed.")

    return None
