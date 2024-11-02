from modules.framework.interface import Framework
from modules.runner.subprocess.impl import Subprocess


class Tox(Framework):

    @classmethod
    def run(cls, directory: str) -> None:
        if cls.__is_installed() != 0:

            print("tox is not installed")
            cls.__install()

        Subprocess.run([f".venv/bin/tox --workdir {directory[0]}"])

    @classmethod
    def __install(cls) -> None:
        Subprocess.run([".venv/bin/pip install tox --upgrade"])

    @classmethod
    def __is_installed(cls) -> bool:
        return Subprocess.run(["tox --version"]) == 0
