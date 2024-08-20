from pydantic import BaseModel

# Define a Pydantic model for input
class TextInput(BaseModel):
    text: str