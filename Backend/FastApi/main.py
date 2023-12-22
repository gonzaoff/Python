from fastapi import FastAPI
from routers import products,users

app = FastAPI()

# Routers

app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hola FastApi!"

'''
Para inicializar servidor uvircorn:
uvicorn nombreDelFile:variableFastAPI --reload
'''

@app.get("/url/")
async def url():
    return { "url_ig":"https://instagram.com/sibofit" }

# Documentacion con Swagger: http://127.0.0.1:8000/docs
# Documentacion con Redocly: http://127.0.0.1:8000/redoc

# Operaciones para el servidor con decorador
# @app.post() "Creador"
# @app.get() "Lector"
# @app.put() "Actualizador"
# @app.delete() "Eliminador"