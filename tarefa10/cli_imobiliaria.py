import json

with open("tarefa10/imobiliaria.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

imoveis = dados["imobiliaria"]["imoveis"]

for i in range(len(imoveis)):
    print(i + 1, imoveis[i]["descricao"])

opcao = int(input("Digite o id do imóvel para saber mais: "))

imovel = imoveis[opcao - 1]

print("\nDescrição:", imovel["descricao"])
print("Proprietário:")
print("Nome:", imovel["proprietario"].get("nome"))
print("Telefone:", imovel["proprietario"].get("telefone"))
print("Email:", imovel["proprietario"].get("email"))
print("Endereço:")
print("Rua:", imovel["endereco"].get("rua"))
print("Número:", imovel["endereco"].get("numero"))
print("Bairro:", imovel["endereco"].get("bairro"))
print("Cidade:", imovel["endereco"].get("cidade"))
print("Características:")
print("Tamanho:", imovel["caracteristicas"].get("tamanho"))
print("Quartos:", imovel["caracteristicas"].get("numQuartos"))
print("Banheiros:", imovel["caracteristicas"].get("numBanheiros"))
print("Valor:", imovel["valor"])