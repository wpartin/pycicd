from modules.environment.virtual.impl import Virtual
from modules.framework.tox.impl import Tox
from modules.parser.args.impl import Args
from modules.version.semantic.impl import SemanticVersion


def main():
    args = Args.parse()

    Virtual.init()

    if args.command == "tox":
        Tox.run(args.workdir)

    if args.command == "version":
        return SemanticVersion.generate()


if __name__ == "__main__":
    main()
