from fastapi import FastAPI
from routes import user
app = FastAPI()

app.include_router(user.router)
@app.get("/")
async def read_root():
    return {"message": "Welcome to the NomNom List API!"}