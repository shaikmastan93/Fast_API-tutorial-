
# Creating and Managing Routes: GET, POST, PUT, DELETE 
from fastapi import FastAPI

app = FastAPI()
#<<<<<<<<<<<----------------------CRUD OPERATION BASICS---------------------------------->>>>>>>>>
# @app.get("/")
# def root_api():
#     return{"Helleo","World"}

# @app.post("/items/")
# def create_item(name:str,price:float):
#     return{"name":name,"price":price}

# @app.put("/item/{item_id}")
# def update_item(item_id:int,name:str,price:float):
#     return{"item_id":item_id,"name":name,"price":price}

# @app.delete("/item/{item_id}")
# def delete_item(item_id:int):
#     return{"message":f"the {item_id} deelete successfully"}
#<<<<<<<<<<<----------------------CRUD OPERATION BASICS---------------------------------->>>>>>>>>

#<<<<<<<<<--------------------------Path Parameters ---------------------------->>>>>>>>>>>>
# @app.get("/users/{user_id}")
# def get_user_id(user_id:int):
#     return {"user":user_id}

# @app.get("/users/{user_name}")
# def user_name(user_name:str):
#     return{"user":user_name}

#<<<<<<<<<--------------------------Path Parameters---------------------------->>>>>>>>>>>>
#<<<<<<<<<--------------------------Query Parameters---------------------------->>>>>>>>>>>>
# @app.get("/users/")
# def user_details(user_id:int,user_name:str):
#     return{"user_id":user_id,"user_name":user_name}

# @app.get("/users/")
# def user_details(user_id:int,name:str=None):
#     return{"user_id":user_id,"name":name}
#<<<<<<<<<--------------------------Query Parameters---------------------------->>>>>>>>>>>>
#<<<<<<<<<--------------------------Combine Query & Path Parameters---------------------------->>>>>>>>>>>>
# @app.get("/users/{user_id}/details")
# def read_user_details(user_id:int,include_email:bool=False):
#     if include_email:
#         return {"user_id":user_id,"include_email":"email included"}
#     else:
#         return{"user_id":user_id,"include_email":"Email not included"}
#<<<<<<<<<--------------------------Combine Query & Path Parameters---------------------------->>>>>>>>>>>>
#<<<<<<<<<--------------------------Handling Request and Response Bodies---------------------------->>>>>>>>>>>>

#<<<<<<<<<--------------------------Handling Request and Response Bodies---------------------------->>>>>>>>>>>>