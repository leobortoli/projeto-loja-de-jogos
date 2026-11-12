import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# String de conexão direta com a sua senha
MONGO_URI = "mongodb+srv://joaoalbertosilvamartins_db_user:2leafbd44@gamesdb.vgegvhv.mongodb.net/?retryWrites=true&w=majority"


if not MONGO_URI:
    raise ValueError("A variável de conexão não foi encontrada!")

# Conexão com o cluster do MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["loja_de_games"]  # Nome do banco de dados

# Teste de conexão
try:
    client.admin.command('ping')
    print("Conexão bem-sucedida com o MongoDB Atlas!")
except Exception as e:
    print("Erro ao conectar ao MongoDB:", e)
    

def cadastrar_produtos_iniciais(db):
    if db["produtos"].count_documents({}) > 0:
        print("\n[INFO] Os produtos já foram cadastrados anteriormente.")
        return

    novo_produto1 = {
        "nome": "PlayStation 5",
        "preco": 4999.90,
        "estoque": 5,
        "categoria": "console",
        "detalhes": {"cor": "Branco", "capacidade": "825GB"}
    }
    
    novo_produto2 = {
        "nome": "Nintendo Switch 2",
        "preco": 2999.90,
        "estoque": 8,
        "categoria": "console",
        "detalhes": {"cor": "Branco", "capacidade": "512GB"}
    }
    
    novo_produto3 = {
        "nome": "Xbox Series X",
        "preco": 5000.00,
        "estoque": 6,
        "categoria": "console",
        "detalhes": {"cor": "Preto", "capacidade": "1TB"}
    }
        
    novo_produto4 = {
        "nome": "Final Fantasy XVI",
        "preco": 249.90,
        "estoque": 12,
        "categoria": "jogo",
        "detalhes": {"plataforma": "PlayStation 5", "genero": "RPG"}
    }
    
    novo_produto5 = {
        "nome": "The Legend of Zelda: Tears of the Kingdom",
        "preco": 299.90,
        "estoque": 13,
        "categoria": "jogo",
        "detalhes": {"plataforma": "Nintendo Switch", "genero": "Ação/Aventura"}
    }
    
    novo_produto6 = {
        "nome": "Halo Infinite",
        "preco": 199.90,
        "estoque": 15,
        "categoria": "jogo",
        "detalhes": {"plataforma": "Xbox Series X", "genero": "FPS"}
    }
    
    novo_produto7 = {
        "nome": "Headset JBL Quantum 800",
        "preco": 199.90,
        "estoque": 22,
        "categoria": "acessorio",
        "detalhes": {"tipo": "Headset", "conectividade": "Sem fio", "marca": "JBL", "cor": "Preto"}
    }
    
    novo_produto8 = {
        "nome": "Teclado Mecânico RGB Redragon",
        "preco": 299.90,
        "estoque": 18,
        "categoria": "acessorio",
        "detalhes": {"tipo": "Teclado", "conectividade": "Com fio", "marca": "Redragon", "cor": "Preto"}
    }
    
    novo_produto9 = {
        "nome": "Mouse Gamer RGB Redragon",
        "preco": 149.90,
        "estoque": 25,
        "categoria": "acessorio",
        "detalhes": {"tipo": "Mouse", "conectividade": "Sem fio", "marca": "Redragon", "cor": "Preto"}
    }
    
    novo_produto10 = {
        "nome": "Solid Snake Action Figure",
        "preco": 300.00,
        "estoque": 5,
        "categoria": "action_figure",
        "detalhes": {"tipo": "Action Figure", "altura": "20cm", "material": "PVC", "personagem": "Solid Snake"}
    }
    
    novo_produto11 = {
        "nome": "Lightning FFXIII Action Figure",
        "preco": 350.00,
        "estoque": 4,
        "categoria": "action_figure",
        "detalhes": {"tipo": "Action Figure", "altura": "20cm", "material": "PVC", "personagem": "Lightning"}
    }
        
    novo_produto12 = {
        "nome": "Hatsune Miku Action Figure",
        "preco": 400.00,
        "estoque": 3,
        "categoria": "action_figure",
        "detalhes": {"tipo": "Action Figure", "altura": "20cm", "material": "PVC", "personagem": "Hatsune Miku"}
    }

    lista_produtos = [
        novo_produto1, novo_produto2, novo_produto3, novo_produto4,
        novo_produto5, novo_produto6, novo_produto7, novo_produto8,
        novo_produto9, novo_produto10, novo_produto11, novo_produto12
    ]

    db.produtos.insert_many(lista_produtos)
    print("\n[SUCESSO] 12 produtos cadastrados com sucesso no MongoDB Atlas!")
            
def buscar_jogos_por_plataforma(db, plataforma_desejada):
    query = {
        "categoria": "jogo",
        "detalhes.plataforma": {"$regex": plataforma_desejada, "$options": "i"}
    }

    print(f"\n--- Jogos para {plataforma_desejada} ---")
    encontrou = False
    for produto in db["produtos"].find(query):
        encontrou = True
        print(f"• {produto['nome']} | R$ {produto['preco']:.2f} | Estoque: {produto['estoque']}")
    if not encontrou:
        print("Nenhum jogo encontrado para esta plataforma.")
        
def buscar_acessorios_por_tipo(db, tipo_desejado):
    query = {
        "categoria": "acessorio",
        "detalhes.tipo": {"$regex": tipo_desejado, "$options": "i"}
    }

    print(f"\n--- Acessórios do tipo {tipo_desejado} ---")
    encontrou = False
    for produto in db["produtos"].find(query):
        encontrou = True
        print(f"• {produto['nome']} | R$ {produto['preco']:.2f} | Estoque: {produto['estoque']}")
    if not encontrou:
        print("Nenhum acessório encontrado.")

def buscar_action_figures_por_personagem(db, personagem_desejado):
    query = {
        "categoria": "action_figure",
        "detalhes.personagem": {"$regex": personagem_desejado, "$options": "i"}
    }

    print(f"\n--- Action Figures do personagem {personagem_desejado} ---")
    encontrou = False
    for produto in db["produtos"].find(query):
        encontrou = True
        print(f"• {produto['nome']} | R$ {produto['preco']:.2f} | Estoque: {produto['estoque']}")
    if not encontrou:
        print("Nenhum action figure encontrado para este personagem.")
        
def atualizar_estoque(db, nome_produto, novo_estoque):
    query = {"nome": {"$regex": nome_produto, "$options": "i"}}
    update = {"$set": {"estoque": novo_estoque}}

    resultado = db["produtos"].update_one(query, update)

    if resultado.modified_count > 0:
        print(f"[SUCESSO] Estoque atualizado para {novo_estoque}.")
    else:
        print(f"[AVISO] Produto '{nome_produto}' não encontrado ou estoque já possui esse valor.")      

def deletar_produto(db, nome_produto):
    query = {"nome": {"$regex": nome_produto, "$options": "i"}}
    resultado = db["produtos"].delete_one(query)

    if resultado.deleted_count > 0:
        print(f"[SUCESSO] Produto '{nome_produto}' deletado com sucesso.")
    else:
        print(f"[AVISO] Produto '{nome_produto}' não encontrado.")

def atualizar_preco(db, nome_produto, novo_preco):
    query = {"nome": {"$regex": nome_produto, "$options": "i"}}
    update = {"$set": {"preco": novo_preco}}

    resultado = db["produtos"].update_one(query, update)

    if resultado.modified_count > 0:
        print(f"[SUCESSO] Preço atualizado para R$ {novo_preco:.2f}.")
    else:
        print(f"[AVISO] Produto '{nome_produto}' não encontrado ou preço já possui esse valor.")

def listar_todos_produtos(db):
    print("\n--- Lista de Todos os Produtos ---")
    encontrou = False
    for produto in db["produtos"].find():
        encontrou = True
        print(f"• {produto['nome']} | Categoria: {produto['categoria']} | R$ {produto['preco']:.2f} | Estoque: {produto['estoque']}")
    if not encontrou:
        print("Nenhum produto encontrado no banco de dados.")


# Bloco principal de execução para testes
if __name__ == "__main__":
    # 1. Cadastra os produtos iniciais (se já não existirem)
    cadastrar_produtos_iniciais(db)

    # 2. Testa as buscas avançadas
    buscar_jogos_por_plataforma(db, "PlayStation 5")
    buscar_action_figures_por_personagem(db, "Solid Snake")

    # 3. Testa a atualização de estoque
    atualizar_estoque(db, "PlayStation 5", 10)

#Menu de opções para o usuário
while True:
    print("\n--- Menu de Opções ---")
    print("1. Listar todos os produtos")
    print("2. Buscar jogos por plataforma")
    print("3. Buscar acessórios por tipo")
    print("4. Buscar action figures por personagem")
    print("5. Atualizar estoque de um produto")
    print("6. Atualizar preço de um produto")
    print("7. Deletar um produto")
    print("8. Sair")

    opcao = input("Escolha uma opção (1-8): ")

    if opcao == "1":
        listar_todos_produtos(db)
    elif opcao == "2":
        plataforma = input("Digite a plataforma desejada: ")
        buscar_jogos_por_plataforma(db, plataforma)
    elif opcao == "3":
        tipo = input("Digite o tipo de acessório desejado: ")
        buscar_acessorios_por_tipo(db, tipo)
    elif opcao == "4":
        personagem = input("Digite o nome do personagem desejado: ")
        buscar_action_figures_por_personagem(db, personagem)
    elif opcao == "5":
        nome_produto = input("Digite o nome do produto para atualizar o estoque: ")
        novo_estoque = int(input("Digite o novo valor de estoque: "))
        atualizar_estoque(db, nome_produto, novo_estoque)
    elif opcao == "6":
        nome_produto = input("Digite o nome do produto para atualizar o preço: ")
        novo_preco = float(input("Digite o novo valor de preço: "))
        atualizar_preco(db, nome_produto, novo_preco)
    elif opcao == "7":
        nome_produto = input("Digite o nome do produto para deletar: ")
        deletar_produto(db, nome_produto)
    elif opcao == "8":
        print("Saindo do programa...")
        break
    else:
        print("[ERRO] Opção inválida! Tente novamente.")
        print(f"Produto '{nome_produto}' deletado com sucesso.")
    else:
        print(f"Produto '{nome_produto}' não encontrado.")
