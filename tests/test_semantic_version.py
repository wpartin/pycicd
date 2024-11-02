from modules.version.semantic.impl import SemanticVersion


class TestSemanticVersion:

    def test_generate_version(self):
        version = SemanticVersion.generate()

        print(version)
        assert isinstance(version, str)
