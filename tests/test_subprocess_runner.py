from modules.runner.subprocess.impl import Subprocess


class TestSubprocessRunner:

    def test_run(self) -> None:
        Subprocess.run(["ls tests"])
