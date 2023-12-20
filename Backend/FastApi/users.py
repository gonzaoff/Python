from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("f")
async def userjson():
    return [{"name" : "Gonza", "surname" : "Escobar", "age": 22 , "url" : "https://www.instagram.com/sibofit"},
            {"name" : "Fede", "surname" : "Escobar", "age": 29 , "url" : "https://www.instagram.com/fyges"},
            {"name" : "Nati", "surname" : "Escobar", "age": 36 , "url" : "https://www.instagram.com/naesc"}]

class User(BaseModel):
    id: int
    name: str
    surname : str
    age: int
    url: str

users_list = [User(id=1, name="Gonzalo", surname="Escobar", age=22, url="/sibofit"),
        User(id=2, name="Federico", surname="Escobar", age=36, url="/fyge"),
        User(id=3, name="Natalia", surname="Escobar", age=28, url="/natiesc")]

# Lista de Usuarios
@app.get("/users/")
async def users():
    return users_list

# Path.
@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)


# Query.
@app.get("/user/")
async def user():
    return search_user(id)

urlquery = "http://127.0.0.1:8000/users?id=1"


@app.post("/user/")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error":"El usuario ya existe."}
    else:
        users_list.append(user)
        return {"success": "Usuario creado exitosamente"}

@app.put("/user/")
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  
            users_list[index] = user
            found = True
            return {"success" : "Usuario modificado exitosamente"}

    if not found:
        return {"error" : "No se ha actualizado el usuario"}


# Funcion resumen
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
    
