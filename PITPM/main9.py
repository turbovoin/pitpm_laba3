from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None



@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Sasha",
                    "description": "A very nice person",
                    "age": 24,
                    
                },
                {
                    "name": "Dima"
                    
                },
                {
                    "name": "Nikita"
                    
                },
            ],
        ),
    ],
):
    results = {"name1": item_id, "namename": item}
    return results