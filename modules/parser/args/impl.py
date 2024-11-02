import argparse

from modules.parser.interface import Parser


class Args(Parser):
    parser = argparse.ArgumentParser(description="Inputs for the pycicd cli utility.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    @classmethod
    def parse(cls, args: list[str] = None) -> argparse.Namespace:

        cls.__create_command(
            name="tox",
            description="Runs the tox framework for your package.",
            arguments={"workdir": "The directory to run tox against."},
        )

        cls.__create_command(
            name="version", description="Creates a unique semantic version at runtime."
        )

        return cls.parser.parse_args(args)

    @classmethod
    def __create_command(
        cls,
        name: str,
        description: str,
        subcommands: dict[str, str] = None,
        arguments: dict[str, str] = None,
    ):

        parser = cls.subparsers.add_parser(name, help=description)

        if arguments is not None:
            cls.__create_arguments(arguments, parser)

        if subcommands is None:
            return

        subcommand = parser.add_subparsers(dest="subcommand", required=True)

        for command, command_description in subcommands.items():
            cls.__create_arguments(
                arguments, subcommand.add_parser(command, help=command_description)
            )

    @classmethod
    def __create_arguments(
        cls, arguments: dict[str, str], parser: argparse.ArgumentParser
    ) -> None:

        for argument, description in arguments.items():
            parser.add_argument(argument, action="append", help=description)
