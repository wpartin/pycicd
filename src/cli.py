import argparse

from version.semantic import SemanticVersion


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CLI tool for CICD related functions.")
    parser.add_argument("command", choices=[
        "aws_context", "version"
    ], help="Command to execute")
    parser.add_argument("action", choices=[
        "get", "set"
    ], nargs='?', help="Action to perform on the context (get or set)")
    parser.add_argument("key", nargs='?', help="Key to get or set in the context")
    parser.add_argument("value", nargs='?', help="Value to set for the specified key (only required for 'set')")

    return parser.parse_args()


def main():
    args = parse_args()

    command = args.command

    if command == "version":
        return SemanticVersion.generate()

    if command == "help":
        print("""
Available commands:
aws_context <sub-command> <key>
    calling aws_context directly will return the entire map
    --sub-commands:
        get
        set
version
""")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
