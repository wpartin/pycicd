import subprocess
import sys

from modules.runner.interface import Runner
from src import ENVIRONMENT_VARIABLES


class Subprocess(Runner):

    @classmethod
    def run(
        cls, command: list[str], environment: dict[str, str] = ENVIRONMENT_VARIABLES
    ) -> bytes:

        cmd = command

        if len(cmd) == 1:
            cmd[0].strip()

        try:
            return subprocess.run(
                cmd, check=True, env=ENVIRONMENT_VARIABLES, shell=True
            ).stdout

        except Exception as e:
            print(f"The subprocess failed to run: {e}")
            sys.exit(1)
