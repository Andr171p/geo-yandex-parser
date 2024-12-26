from pydantic import BaseModel


class ResultSchema(BaseModel):
    name: str
    phone: str
    address: str
    link: str
    rating: float
