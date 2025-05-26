from pydantic import BaseModel


class TextRequestSchema(BaseModel):
    text: str