# produto_1: str = "Notebook"
# produto_2: str = "Smartphone"
# produto_3: str = "Tablet"
# # Listas
# produtos = []

# # Adicionando os produtos na lista
# produtos.append(
#     produto_1
# )  #   append() é um método que adiciona um elemento ao final da lista
# produtos.append(produto_2)
# produtos.append(produto_3)

# print(produtos)

# numeros = []
# numeros.extend(
#     range(1, 11)
# )  #   extend() é um método que adiciona os elementos de um iterável (como uma lista ou um range) ao final da lista
# print(numeros)

# Json - É o dicionario do Python, transforma objetos literal do java script em dicionários do python

produto_1: dict = {"nome": "Notebook", "preco": 2500.00, "quantidade": 10}
produto_2: dict = {"nome": "Smartphone", "preco": 1500.00, "quantidade": 20}
produto_3: dict = {"nome": "Tablet", "preco": 1000.00, "quantidade": 15}

carrinho = []

carrinho.append(produto_1)
carrinho.append(produto_2)
carrinho.append(produto_3)

for i in carrinho:
    print(
        f"Produto: {i["nome"]} - Preço: R${i["preco"]} - Quantidade: {i["quantidade"]}"
    )
