import os

from modules.environment.interface import Environment


class Variables(Environment):

    @classmethod
    def init(cls, variables: dict[str, str] = None) -> dict[str, str]:
        environment = os.environ.copy()

        if variables is None:
            return environment

        for variable in variables:
            if variable is None:
                continue

            environment[variable] = variables[variable]

        return environment
