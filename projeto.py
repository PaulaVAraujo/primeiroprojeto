import json


with open('api.json', 'r', encoding='utf-8') as codigo:
    dados = json.load(codigo) 

linha_escolhida = input("Digite o código da linha: ")

def buscar_linhas():
      for linha in dados:
           if linha['codigo'] == linha_escolhida:
                print(f"Linha: {linha['codigo']}")
                print(f"Horarios: {linha['horarios']}")
                break
      else:
           print("Linha não encontrada!")

buscar_linhas()
