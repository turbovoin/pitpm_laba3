from enum import Enum
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

class Profile(str, Enum):
    user = "user"
    password = "user"

class Item(BaseModel):
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(...)):
    results = {"item_id": item_id, "item": item}
    return results