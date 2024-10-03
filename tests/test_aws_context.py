import pytest
from context.aws import AwsContext
from models.definable_context_inputs import DefinableContextInputs


class TestAwsContext:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.context_inputs = DefinableContextInputs(
            build_agent="master",
            business_unit="test"
        )
        self.aws_context = AwsContext(self.context_inputs)

    def test_aws_context_to_map(self):
        context_map = self.aws_context.to_map()
        assert isinstance(context_map, dict)
        assert 'build_agent' in context_map
        assert context_map['build_agent'] == "master"

    def test_aws_context_to_string(self):
        context_string = str(self.aws_context)
        assert isinstance(context_string, str)
