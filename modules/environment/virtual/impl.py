from modules.environment.interface import Environment
from modules.runner.subprocess.impl import Subprocess
from src import ENVIRONMENT_VARIABLES


class Virtual(Environment):

    @classmethod
    def init(cls) -> None:
        Subprocess.run(["python -m venv .venv"], environment=ENVIRONMENT_VARIABLES)
