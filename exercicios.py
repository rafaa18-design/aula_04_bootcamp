# 1 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# lista: list = list(range(1, 11))

# for i in lista:
#     print(f"{i} elevado ao quadrado = {i**2}")

# 2 - Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# lista: list = ["Python", "Java", "C++", "JavaScript"]
# removido = lista.remove(
#     "C++"
# )  # remove() é um método que remove a primeira ocorrência de um elemento na lista
# adicionado = lista.append("Ruby")

# print("Item removido: C++")
# print("Item adicionado: Ruby")
# print(lista)

# 3 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano
#  de publicação. Imprima cada informação.

# from typing import Dict

# livro: Dict[str, any] = {
#     "livro_01": {
#         "titulo": "O Senhor dos Anéis",
#         "autor": "J.R.R. Tolkien",
#         "ano": 1954,
#     },
#     "livro_02": {
#         "titulo": "Arte da guerra",
#         "autor": "Sun Tzu",
#         "ano": 500,
#     },
#     "livro_03": {
#         "titulo": "O Hobbit",
#         "autor": "J.R.R. Tolkien",
#         "ano": 1951,
#     },
# }

# lista_livro: list = []
# lista_livro.append(livro)

# for i in lista_livro:
#     print(
#         f"Livro: {i["livro_01"]["titulo"]} \n-- Autor: {i["livro_01"]["autor"]} \n-- Ano: {i["livro_01"]["ano"]}\n"
#     )
#     print(
#         f"Livro: {i["livro_02"]["titulo"]} \n-- Autor: {i["livro_02"]["autor"]} \n-- Ano: {i["livro_02"]["ano"]}\n"
#     )
#     print(
#         f"Livro: {i["livro_03"]["titulo"]} \n-- Autor: {i["livro_03"]["autor"]} \n-- Ano: {i["livro_03"]["ano"]}\n"
#     )


# 4 - Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um
#  dicionário.

# string: str = "banana"
# ocorrencias: dict = {}

# for caracteres in string:
#     if caracteres in ocorrencias:
#         ocorrencias[caracteres] += 1
#     else:
#         ocorrencias[caracteres] = 1

# print(ocorrencias)

# palavra: str = "macaco piruleta"
# ocorrencia: dict = {}

# for carac in palavra:
#     if carac in ocorrencia:
#         ocorrencia[carac] += 1
#     else:
#         ocorrencia[carac] = 1
# print(ocorrencia)


# 5 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário
# {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# frutas: list = ["maçã", "banana", "cereja"]
# precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# for i in frutas:
#     if i in precos:
#         print(f"Fruta: {i} - Preço: R${precos[i]}")
#         precos[i] += precos[i]
#     else:
#         print(f"Fruta: {i} não encontrada")
# print(f"Preço total: R${precos[i]}")
