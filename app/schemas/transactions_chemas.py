from pydantic import BaseModel

class CreateTransaction(BaseModel):
    buyer_wallet: str
    amount: int
    project_id: int
