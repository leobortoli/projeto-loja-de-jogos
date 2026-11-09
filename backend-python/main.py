from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import Dict, Any, List, Optional
import os

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client["loja_games"]
collection_produtos = db["produtos"]

# Auxiliar para converter o ObjectId do Mongo para string no JSON
def produto_helper(produto) -> dict:
    return {
        "id": str(produto["_id"]),
        "nome": produto["nome"],
        "preco": produto["preco"],
        "estoque": produto["estoque"],
        "categoria": produto["categoria"],
        "detalhes": produto.get("detalhes", {})
    }

class ProdutoModel(BaseModel):
    nome: str
    preco: float = Field(..., gt=0)
    estoque: int = Field(..., ge=0)
    categoria: str
    detalhes: Dict[str, Any] = {}

# 1. INCLUIR
@app.post("/api/produtos")
async def incluir_produto(produto: ProdutoModel):
    resultado = await collection_produtos.insert_one(produto.dict())
    return {"status": "sucesso", "id": str(resultado.inserted_id)}

# 2. LISTAR TODOS
@app.get("/api/produtos")
async def listar_produtos():
    produtos = []
    async for prod in collection_produtos.find():
        produtos.append(produto_helper(prod))
    return produtos

# 3. OBTER POR ID
@app.get("/api/produtos/{id}")
async def obter_produto(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    
    produto = await collection_produtos.find_one({"_id": ObjectId(id)})
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto_helper(produto)

# 4. ALTERAR
@app.put("/api/produtos/{id}")
async def alterar_produto(id: str, produto: ProdutoModel):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    
    resultado = await collection_produtos.update_one(
        {"_id": ObjectId(id)}, 
        {"$set": produto.dict()}
    )
    
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return {"status": "sucesso", "mensagem": "Produto atualizado com sucesso"}

# 5. EXCLUIR
@app.delete("/api/produtos/{id}")
async def excluir_produto(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    
    resultado = await collection_produtos.delete_one({"_id": ObjectId(id)})
    
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
        
    return {"status": "sucesso", "mensagem": "Produto excluído com sucesso"}