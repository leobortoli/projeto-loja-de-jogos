from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("A variável MONGO_URI não foi encontrada no arquivo .env!")

client = MongoClient(MONGO_URI)

try:
    db_names = client.list_database_names()
    print("Conexão bem-sucedida! Bancos disponíveis:", db_names)
except Exception as e:
    print("Erro ao conectar ao MongoDB:", e)
    
def cadastrar_produto(db):
    
    novo_produto1 = {
        "nome": "PlayStation 5",
        "preco": 4999.90,
        "estoque": 5,
        "categoria": "console",
        "detalhes": {
            "cor": "Branco",
            "capacidade": "825GB"
        }
    }
    
    novo_produto2 = {
        "nome": "Nintendo Switch 2",
        "preco": 2999.90,
        "estoque": 8,
        "categoria": "console",
        "detalhes": {
            "cor": "Branco",
            "capacidade": "512GB"
        }
    }
    
    novo_produto3 = {
        "nome": "Xbox Series X",
        "preco": 5000.00,
        "estoque": 6,
        "categoria": "console",
        "detalhes": {
            "cor": "Preto",
            "capacidade": "1TB"
        }
    }
        
    novo_produto4 = {
        "nome": "Final Fantasy XVI",
        "preco": 249.90,
        "estoque": 12,
        "categoria": "jogo",
        "detalhes": {
            "plataforma": "Playstation 5",
            "genero": "RPG"
        }
    }
    
    novo_produto5 = {
        "nome": "The Legend of Zelda: Tears of the Kingdom",
        "preco": 299.90,
        "estoque": 13,
        "categoria": "jogo",
        "detalhes": {
            "plataforma": "Nintendo Switch",
            "genero": "Ação/Aventura"
        }
    }
    
    novo_produto6 = {
        "nome": "Halo Infinite",
        "preco": 199.90,
        "estoque": 15,
        "categoria": "jogo",
        "detalhes": {
            "plataforma": "Xbox Series X",
            "genero": "FPS"
        }
    }
    
    novo_produto7 = {
        "nome": "Headset JBL Quantum 800",
        "preco": 199.90,
        "estoque": 22,
        "categoria": "acessório",
        "detalhes": {
            "tipo": "Headset",
            "conectividade": "Sem fio",
            "Marca": "JBL",
            "cor": "Preto"
        }
    }
    
    novo_produto8 = {
        "nome": "Teclado Mecânico RGB Redragon",
        "preco": 299.90,
        "estoque": 18,
        "categoria": "acessório",
        "detalhes": {
            "tipo": "Teclado",
            "conectividade": "Com fio",
            "Marca": "Redragon",
            "cor": "Preto"
        } 
    }
    
    novo_produto9 = {
        "nome": "Mouse Gamer RGB Redragon",
        "preco": 149.90,
        "estoque": 25,
        "categoria": "acessório",
        "detalhes": {
            "tipo": "Mouse",
            "conectividade": "Sem fio",
            "Marca": "Redragon",
            "cor": "Preto"
        }
    }
    
    novo_produto10 = {
        "nome": "Solid Snake Action Figure",
        "preco": 300.00,
        "estoque": 5,
        "categoria": "Action Figure",
        "detalhes": {
            "tipo": "Action Figure",
            "altura": "20cm",
            "material": "PVC",
            "personagem": "Solid Snake"}
    }
    
    novo_produto11 = {
        "nome": "Lightning FFXIII Action Figure",
        "preco": 350.00,
        "estoque": 4,
        "categoria": "Action Figure",
        "detalhes": {
            "tipo": "Action Figure",
            "altura": "20cm",
            "material": "PVC",
            "personagem": "Lightning"
        }
    }
        
    novo_produto12 = {
        "nome": "Hatsune Miku Action Figure",
        "preco": 400.00,
        "estoque": 3,
        "categoria": "Action Figure",
        "detalhes": {
            "tipo": "Action Figure",
            "altura": "20cm",
            "material": "PVC",
            "personagem": "Hatsune Miku"
        }
    }

    resultado = db.produtos.insert_many([novo_produto1, novo_produto2, novo_produto3, novo_produto4, novo_produto5, novo_produto6, novo_produto7, novo_produto8, novo_produto9, novo_produto10, novo_produto11, novo_produto12])
            
def buscar_jogos_por_plataforma(db, plataforma_desejada):
    query = {
        "categoria": "jogo",
        "detalhes.plataforma": plataforma_desejada
    }

    print(f"\n--- Jogos para {plataforma_desejada} ---")
    for produto in db["produtos"].find(query):
        print(f"- {produto['nome']} | R$ {produto['preco']} | Estoque: {produto['estoque']}")
        
def buscar_acessorios_por_tipo(db, tipo_desejado):
    query = {
        "categoria": "acessório",
        "detalhes.tipo": tipo_desejado
    }

    print(f"\n--- Acessórios do tipo {tipo_desejado} ---")
    for produto in db["produtos"].find(query):
        print(f"- {produto['nome']} | R$ {produto['preco']} | Estoque: {produto['estoque']}")

def buscar_action_figures_por_personagem(db, personagem_desejado):
    query = {
        "categoria": "Action Figure",
        "detalhes.personagem": personagem_desejado
    }

    print(f"\n--- Action Figures do personagem {personagem_desejado} ---")
    for produto in db["produtos"].find(query):
        print(f"- {produto['nome']} | R$ {produto['preco']} | Estoque: {produto['estoque']}")
        
def atualizar_estoque(db, nome_produto, novo_estoque):
    query = {"nome": nome_produto}
    update = {"$set": {"estoque": novo_estoque}}

    resultado = db["produtos"].update_one(query, update)

    if resultado.modified_count > 0:
        print(f"Estoque do produto '{nome_produto}' atualizado para {novo_estoque}.")
    else:
        print(f"Produto '{nome_produto}' não encontrado ou estoque já está atualizado.")       

def deletar_produto(db, nome_produto):
    query = {"nome": nome_produto}
    resultado = db["produtos"].delete_one(query)

    if resultado.deleted_count > 0:
        print(f"Produto '{nome_produto}' deletado com sucesso.")
    else:
        print(f"Produto '{nome_produto}' não encontrado.")