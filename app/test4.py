from fastapi import FastAPI,Form,UploadFile,File
from pydantic import BaseModel,EmailStr,Field


app = FastAPI()

@app.post("/uploading_file/")
async def uploads_file(file:UploadFile=File(...)):
    with open(f'uploads/{file.filename}', "wb")as f:
        f.write(await file.read())
    return {"message":f'{file.filename} saved successfully'}


@app.post("/upload_multi_files/")
async def upload_multi_files(files:list[UploadFile]=File(...)):
    return {"filenames":[file.filename for file in files]}