from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

algorithm = "HS256"



class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "sibofit" : {
        "username": "sibofit",
        "full_name" : "Gonzalo Escobar",
        "email": "gonza-09-10@gmail.com",
        "disabled": False,
        "password" : "gonzasib",
    },
    "GonzaEsc23" : {
        "username": "GonzaEsc23",
        "full_name" : "Dario Sibolich",
        "email": "gonzaescobar26@gmail.com",
        "disabled": False,
        "password" : "654321",
    },
    "JMay" : {
        "username": "JMay",
        "full_name" : "Jose Maydana",
        "email": "joseMay@gmail.com",
        "disabled": True,
        "password" : "gon123",
    },
}

# LogIn
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    
    # Si el usuario no existe...
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario incorrecto")
    
    user = search_user_db(form.username)
    
    # Si la contrase;a es incorrecta
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contrase;a incorrecta")
    
    return {"access_token": user.username, 
            "token_type": "bearer"}

