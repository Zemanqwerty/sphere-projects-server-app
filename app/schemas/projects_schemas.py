from pydantic import BaseModel

class CreateProject(BaseModel):
    name: str
    description: str
    owner_wallet: str
    coins_count: int
    coins_price: float


class UpdateProject(BaseModel):
    name: str
    description: str
    coins_count: int
    coins_price: float