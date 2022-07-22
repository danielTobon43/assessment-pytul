from enum import Enum


class StatusEnum(str, Enum):
    approved: str = "approved"
    rejected: str = "rejected"
