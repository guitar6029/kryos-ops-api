from enum import Enum


class OperatorRole(str, Enum):
    operator = "operator"
    supervisor = "supervisor"
    admin = "admin"
