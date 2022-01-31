from dataclasses import dataclass, field


@dataclass
class DataClassWithDefaults:
    static_default: str = field(default='this is static default value')
    factory_default: list = field(default_factory=list)


print(DataClassWithDefaults())
