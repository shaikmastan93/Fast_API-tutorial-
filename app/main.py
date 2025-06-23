from fastapi import FastAPI,Form,UploadFile,File
from pydantic import BaseModel,EmailStr,Field
from typing import List

app = FastAPI()

# <<<<<<<<<--------------------------Data Validation in FastAPI with Pydantic------------------------>>>>>>>
# class User(BaseModel):
#     username:str
#     email:str
#     age:int


# @app.post("/register/")
# async def reg_user(user:User):
#     return user
# <<<<<<<<<--------------------------Data Validation in FastAPI with Pydantic------------------------>>>>>>>
#Regular expressions
#Custom validators

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

# class User(BaseModel):
#     username: str = Field(..., pattern=r'^[a-zA-Z0-9_.-]+$')
#     email: EmailStr
#     age: int = Field(..., gt=0,lt=120)

# @app.post("/register/")
# async def user_reg(user: User):
#     return user

#<<<<------------  Handling Form Data and File Uploads in FastAPI---------------------->
# -----------
# @app.post("/login")
# async def login(username:str=Form(...),password:str=Form(...)):
#     return {"username":username,"message":"Login Successfull"}
#<<<--------------- UploadFile------------------------>>
# @app.post("/uploadfile/")
# async def create_upload_file(file:UploadFile=File(...)):
#     return {"filename":file.filename}

#<<<<<<<<<<<<------------save uploaded file---------------->

# @app.post("/uploadfile/")
# async def upload_file(file:UploadFile=File(...)):
  
#     with open(f'uploads/{file.filename}', "wb") as f:

#         f.write(await file.read())
#     return{"message":f"{file.filename} saved successfully"}

#<--------------------------------------Upload Multiple files------------------------->

@app.post('/uploadfiles/')
async def upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}
    