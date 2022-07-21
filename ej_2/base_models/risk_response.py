from pydantic import BaseModel, Field

from ej_2.enums.status_enum import StatusEnum
from ej_2.enums.risk_enum import RiskEnum


class RiskResponse(BaseModel):
    user_id: int = Field(gt=-1)
    product_name: RiskEnum = Field()
    status: StatusEnum = Field()
    amount: int = Field(gt=-1)
