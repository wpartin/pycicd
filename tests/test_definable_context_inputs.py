from models.definable_context_inputs import DefinableContextInputs


class TestDefinableContextInputs:

    def test_build_agent(self):
        context_inputs = DefinableContextInputs(
            build_agent="master"
        )

        assert context_inputs["build_agent"] == "master"

    def test_business_unit(self):
        context_inputs = DefinableContextInputs(
            business_unit="test"
        )

        assert context_inputs["business_unit"] == "test"

    def test_create_semantic_version(self):
        context_inputs = DefinableContextInputs(
            create_semantic_version=False
        )

        assert not context_inputs["create_semantic_version"]

    def test_docker_tool_version(self):
        context_inputs = DefinableContextInputs(
            docker_tool_version="24.0.7"
        )

        assert context_inputs["docker_tool_version"] == "24.0.7"

    def test_environments(self):
        context_inputs = DefinableContextInputs(
            environments=["develop", "staging"]
        )

        assert context_inputs["environments"] == ["develop", "staging"]

    def test_pyenv_version(self):
        context_inputs = DefinableContextInputs(
            pyenv_version="3.12"
        )

        assert context_inputs["pyenv_version"] == "3.12"

    def test_tags(self):
        context_inputs = DefinableContextInputs(
            tags={
                "Environment": "Testing",
                "Python": True
            }
        )

        assert context_inputs["tags"] == {
            "Environment": "Testing",
            "Python": True
        }

    def test_team(self):
        context_inputs = DefinableContextInputs(
            team="testers"
        )

        assert context_inputs["team"] == "testers"

    def test_terraform_backend(self):
        context_inputs = DefinableContextInputs(
            terraform_backend="."
        )

        assert context_inputs["terraform_backend"] == "."

    def test_terraform_version(self):
        context_inputs = DefinableContextInputs(
            terraform_version="1.9.0"
        )

        assert context_inputs["terraform_version"] == "1.9.0"
