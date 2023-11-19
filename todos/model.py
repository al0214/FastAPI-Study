from pydantic import BaseModel

# class Item(BaseModel):
#     id : int
#     status : str
    
class Todo(BaseModel):
    id: int
    item : str
    
    class Config:
        json_schema_extra = {
            "example" : {
                "id" : 2,
                "item" : "Example Schema!"
            }
        }

class TodoItem(BaseModel):
    item : str
    
    class Config:
        json_schema_extra = {
            "example" : {
                "item" : "Read the next chapter of the book."
            }
        }