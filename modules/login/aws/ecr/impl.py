from modules.login.interface import Login
from modules.runner.subprocess.impl import Subprocess
from src import ENVIRONMENT_VARIABLES


class Ecr(Login):

    @classmethod
    def login(cls, tool: str = "docker") -> None:
        Subprocess.run(
            [
                f"""
            {tool} login \
            -u AWS \
            -p $(aws ecr get-login-password --region {ENVIRONMENT_VARIABLES["AWS_REGION"]}) \
            {ENVIRONMENT_VARIABLES["DOCKER_BASE_IMAGE_PATH"]}
            """
            ]
        )
