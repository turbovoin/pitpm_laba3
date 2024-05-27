from enum import Enum
from typing import Set, List, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field



class Brend(str, Enum):
    Name = "Nike"
    name1= "adidas"

brend = Brend

app = FastAPI()


@app.get("/")
async def get_model(name: str | None = "", name1: str | None = ""):
    if name != brend.Name:
        return "not this brend"
    elif name1 != brend.Password:
        return " this brend"
    else:
        return f"brend"