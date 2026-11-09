from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = FastAPI()

MONGO_DETAILS = "mongodb+srv://seu_usuario:sua_senha@cluster.mongodb.net/"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.meu_banco
collection = database.usuarios

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    idade: int

@app.post("/db/usuarios")
async def inserir_usuario(usuario: UsuarioSchema):
    # Insere diretamente no MongoDB
    resultado = await collection.insert_one(usuario.dict())
    if resultado.inserted_id:
        return {"status": "sucesso", "id": str(resultado.inserted_id)}
    raise HTTPException(status_code=500, detail="Falha ao inserir no MongoDB")