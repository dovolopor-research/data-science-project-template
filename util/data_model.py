from enum import Enum, unique


@unique
class Env(Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"
