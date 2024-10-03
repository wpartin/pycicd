from utils.retry_commands import retry_function
from utils.retry_commands import retry_shell


class TestCommands:

    def test_retry_function(self):
        attempt = 0

        def test_func():
            nonlocal attempt
            print("Simulating work... Attempt:", attempt + 1)
            if attempt < 2:
                attempt += 1
                raise ValueError("Simulated failure!")
            return "Success on attempt: {}".format(attempt + 1)

        retries = 3
        delay = 1
        max_concurrent = 1

        output = retry_function(test_func, retries, delay, max_concurrent)

        assert output == "Success on attempt: 3"

    def test_retry_shell_command(self):
        output = retry_shell(command="ls")

        assert "test_retry_commands.py" in output
