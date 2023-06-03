from pydantic import BaseModel

class SamplePostRequest(BaseModel):
    a: int
    b: str
    c: list[int]