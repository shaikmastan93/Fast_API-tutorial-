from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()
# <<<<<<<<<<----------------------Handling Request and Response Bodies-------------------------------------->>>>
class User(BaseModel):
    name:str = Field(...,min_length=1,description="should be minmum length")
    age:int = Field(...,le=120,gt=0,description="age between 1 and 120")

@app.post("/user/")
async def create_user(user:User):
    return{"name":user.name,"age":user.age}