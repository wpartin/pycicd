from collections.abc import MutableMapping


class DefinableContextInputs(MutableMapping):

    def __init__(
            self,
            build_agent=None,
            business_unit=None,
            create_semantic_version=None,
            docker_tool_version=None,
            environments=None,
            pyenv_version=None,
            tags=None,
            team=None,
            terraform_backend=None,
            terraform_version=None
    ):
        self.build_agent = build_agent
        self.business_unit = business_unit
        self.create_semantic_version = create_semantic_version
        self.docker_tool_version = docker_tool_version
        self.environments = environments if environments else []
        self.pyenv_version = pyenv_version
        self.tags = tags if tags else {}
        self.team = team
        self.terraform_backend = terraform_backend
        self.terraform_version = terraform_version

    def __len__(self):
        return len(self._get_property_names())

    def __iter__(self):
        return iter(self._get_property_names())

    def __getitem__(self, key):
        return getattr(self, key, None)

    def __setitem__(self, key, value):
        if key in self._get_property_names():
            setattr(self, key, value)
        else:
            raise KeyError(f"{key} is not a valid attribute")

    def __delitem__(self, key):
        if key in self._get_property_names():
            setattr(self, key, None)
        else:
            raise KeyError(f"{key} is not a valid attribute")

    def _get_property_names(self):
        return self.items()

    def key_set(self):
        return {key: value for key, value in self.__dict__.items()}

    def get(self, key):
        return getattr(self, key, None)
