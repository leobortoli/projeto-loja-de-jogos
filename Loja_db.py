import os
from pymongo import MongoClient


def load_dotenv():
    """Carrega um arquivo .env simples sem depender de python-dotenv."""
    caminho = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.isfile(caminho):
        return

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha and not linha.startswith("#") and "=" in linha:
                chave, valor = linha.split("=", 1)
                os.environ.setdefault(chave.strip(), valor.strip().strip("'\""))


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("A variável de conexão não foi encontrada!")

client = MongoClient(MONGO_URI)
db = client["loja-de-games"]

try:
    client.admin.command("ping")
    print("Conexão bem-sucedida com o MongoDB Atlas!")
except Exception as e:
    print("Erro ao conectar ao MongoDB:", e)


def cadastrar_produto(database):
    produtos = [
        {"nome": "PlayStation 5", "preco": 4999.90, "estoque": 5, "categoria": "console", "detalhes": {"cor": "Branco", "capacidade": "1TB"}},
        {"nome": "Nintendo Switch 2", "preco": 2999.90, "estoque": 8, "categoria": "console", "detalhes": {"cor": "Branco", "capacidade": "512GB"}},
        {"nome": "Xbox Series X", "preco": 5000.00, "estoque": 6, "categoria": "console", "detalhes": {"cor": "Preto", "capacidade": "1TB"}},
        {"nome": "Final Fantasy XVI", "preco": 249.90, "estoque": 12, "categoria": "jogo", "detalhes": {"plataforma": "PlayStation 5", "genero": "RPG"}},
        {"nome": "The Legend of Zelda: Tears of the Kingdom", "preco": 299.90, "estoque": 13, "categoria": "jogo", "detalhes": {"plataforma": "Nintendo Switch", "genero": "Ação/Aventura"}},
        {"nome": "Halo Infinite", "preco": 199.90, "estoque": 15, "categoria": "jogo", "detalhes": {"plataforma": "Xbox Series X", "genero": "FPS"}},
        {"nome": "Headset JBL Quantum 800", "preco": 199.90, "estoque": 22, "categoria": "acessorio", "detalhes": {"tipo": "Headset", "conectividade": "Sem fio", "Marca": "JBL", "cor": "Preto"}},
        {"nome": "Teclado Mecânico RGB Redragon", "preco": 299.90, "estoque": 18, "categoria": "acessorio", "detalhes": {"tipo": "Teclado", "conectividade": "Com fio", "Marca": "Redragon", "cor": "Preto"}},
        {"nome": "Mouse Gamer RGB Redragon", "preco": 149.90, "estoque": 25, "categoria": "acessorio", "detalhes": {"tipo": "Mouse", "conectividade": "Sem fio", "Marca": "Redragon", "cor": "Preto"}},
        {"nome": "Solid Snake Action Figure", "preco": 300.00, "estoque": 5, "categoria": "action_figure", "detalhes": {"tipo": "Action Figure", "altura": "20cm", "material": "PVC", "personagem": "Solid Snake"}},
        {"nome": "Lightning FFXIII Action Figure", "preco": 350.00, "estoque": 4, "categoria": "action_figure", "detalhes": {"tipo": "Action Figure", "altura": "20cm", "material": "PVC", "personagem": "Lightning"}},
        {"nome": "Hatsune Miku Action Figure", "preco": 400.00, "estoque": 3, "categoria": "action_figure", "detalhes": {"tipo": "Action Figure", "altura": "20cm", "material": "PVC", "personagem": "Hatsune Miku"}},
    ]

    for produto in produtos:
        database["produtos"].update_one(
            {"nome": produto["nome"]},
            {"$set": produto},
            upsert=True,
        )


def cadastrar_novo_produto(database):
    print("\n--- Cadastro de novo produto ---")

    nome = input("Digite o nome do produto: ").strip()
    try:
        preco = float(input("Digite o preço do produto: R$ ").strip())
        estoque = int(input("Digite a quantidade em estoque: ").strip())
    except ValueError:
        print("Erro: Preço e estoque devem ser números válidos.")
        return

    print("Escolha a categoria do produto: [jogo, console, acessorio, action_figure]")
    categoria = input("Digite a categoria do produto: ").strip().lower()

    novo_produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
        "categoria": categoria,
        "detalhes": {},
    }

    if categoria == "jogo":
        novo_produto["detalhes"] = {
            "plataforma": input("Digite a plataforma do jogo: ").strip(),
            "genero": input("Digite o gênero do jogo: ").strip(),
        }
    elif categoria == "console":
        novo_produto["detalhes"] = {
            "cor": input("Digite a cor do console: ").strip(),
            "capacidade": input("Digite a capacidade do console: ").strip(),
        }
    elif categoria == "acessorio":
        novo_produto["detalhes"] = {
            "tipo": input("Digite o tipo do acessório: ").strip(),
            "conectividade": input("Digite a conectividade do acessório: ").strip(),
        }
    elif categoria == "action_figure":
        novo_produto["detalhes"] = {
            "tipo": input("Digite o tipo da action figure: ").strip(),
            "altura": input("Digite a altura da action figure: ").strip(),
            "material": input("Digite o material da action figure: ").strip(),
            "personagem": input("Digite o personagem da action figure: ").strip(),
        }

    if not nome:
        print("Erro: o nome do produto não pode estar vazio.")
        return

    resultado = database["produtos"].insert_one(novo_produto)
    print(f"Produto cadastrado com sucesso. ID: {resultado.inserted_id}")


def buscar_jogos_por_plataforma(database, plataforma_desejada):
    query = {"categoria": "jogo", "detalhes.plataforma": plataforma_desejada}
    print(f"\n--- Jogos para {plataforma_desejada} ---")
    for produto in database["produtos"].find(query):
        print(f"- {produto['nome']} | R$ {produto['preco']} | Estoque: {produto['estoque']}")


def buscar_acessorios_por_tipo(database, tipo_desejado):
    query = {"categoria": "acessorio", "detalhes.tipo": tipo_desejado}
    print(f"\n--- Acessórios do tipo {tipo_desejado} ---")
    for produto in database["produtos"].find(query):
        print(f"- {produto['nome']} | R$ {produto['preco']} | Estoque: {produto['estoque']}")


def buscar_action_figures_por_personagem(database, personagem_desejado):
    query = {"categoria": "action_figure", "detalhes.personagem": personagem_desejado}
    print(f"\n--- Action Figures do personagem {personagem_desejado} ---")
    for produto in database["produtos"].find(query):
        print(f"- {produto['nome']} | R$ {produto['preco']} | Estoque: {produto['estoque']}")


def atualizar_estoque(database, nome_produto, novo_estoque):
    resultado = database["produtos"].update_one(
        {"nome": nome_produto},
        {"$set": {"estoque": novo_estoque}},
    )
    if resultado.modified_count > 0:
        print(f"Estoque do produto '{nome_produto}' atualizado para {novo_estoque}.")
    else:
        print(f"Produto '{nome_produto}' não encontrado ou estoque já está atualizado.")


def deletar_produto(database, nome_produto):
    resultado = database["produtos"].delete_one({"nome": nome_produto})
    if resultado.deleted_count > 0:
        print(f"Produto '{nome_produto}' deletado com sucesso.")
    else:
        print(f"Produto '{nome_produto}' não encontrado.")


def listar_todos_produtos(database):
    print("\n=== CATÁLOGO COMPLETO DE PRODUTOS ===")
    produtos = list(database["produtos"].find())

    if not produtos:
        print("O inventário está vazio.")
        return

    for i, produto in enumerate(produtos, 1):
        print(f"{i}. [{produto['categoria'].upper()}] {produto['nome']} - R$ {produto['preco']:.2f} | Estoque: {produto['estoque']}")
        print(f"   Detalhes: {produto['detalhes']}")


def atualizar_preco(database, nome_produto, novo_preco):
    resultado = database["produtos"].update_one(
        {"nome": {"$regex": nome_produto, "$options": "i"}},
        {"$set": {"preco": novo_preco}},
    )
    if resultado.modified_count > 0:
        print(f"[SUCESSO] Preço do produto '{nome_produto}' atualizado para R$ {novo_preco:.2f}.")
    else:
        print(f"[AVISO] Produto '{nome_produto}' não encontrado ou preço já possui esse valor.")


def menu():
    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1. Cadastrar novo produto")
        print("2. Buscar jogos por plataforma")
        print("3. Buscar acessórios por tipo")
        print("4. Buscar action figures por personagem")
        print("5. Atualizar estoque de um produto")
        print("6. Deletar um produto")
        print("7. Listar todos os produtos")
        print("8. Atualizar preço de um produto")
        print("9. Sair")

        opcao = input("Escolha uma opção (1-9): ")

        if opcao == "1":
            cadastrar_novo_produto(db)
        elif opcao == "2":
            plataforma = input("Digite a plataforma desejada (ex: PlayStation 5, Nintendo Switch, Xbox Series X): ")
            buscar_jogos_por_plataforma(db, plataforma)
        elif opcao == "3":
            tipo = input("Digite o tipo de acessório desejado (ex: Headset, Teclado, Mouse): ")
            buscar_acessorios_por_tipo(db, tipo)
        elif opcao == "4":
            personagem = input("Digite o nome do personagem desejado (ex: Solid Snake, Lightning, Hatsune Miku): ")
            buscar_action_figures_por_personagem(db, personagem)
        elif opcao == "5":
            nome_produto = input("Digite o nome do produto para atualizar o estoque: ")
            novo_estoque = int(input("Digite o novo valor de estoque: "))
            atualizar_estoque(db, nome_produto, novo_estoque)
        elif opcao == "6":
            nome_produto = input("Digite o nome do produto para deletar: ")
            deletar_produto(db, nome_produto)
        elif opcao == "7":
            listar_todos_produtos(db)
        elif opcao == "8":
            nome_produto = input("Digite o nome do produto para atualizar o preço: ")
            novo_preco = float(input("Digite o novo preço: "))
            atualizar_preco(db, nome_produto, novo_preco)
        elif opcao == "9":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 9.")

if __name__ == "__main__":
    cadastrar_produto(db)
    menu()

