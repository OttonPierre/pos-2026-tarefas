from xml.dom.minidom import parse
import json

dom = parse('tarefa09/imobiliaria.xml') 

imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')

lista = []

for imovel in imoveis:
    # descrição
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue
    # endereço
    endereco = imovel.getElementsByTagName("endereco")[0].firstChild.nodeValue
    rua = imovel.getElementsByTagName("rua")[0].firstChild.nodeValue
    if imovel.getElementsByTagName("número"):
        numero = imovel.getElementsByTagName("número")[0].firstChild.nodeValue
    else: 
        numero = None
    bairro = imovel.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = imovel.getElementsByTagName("cidade")[0].firstChild.nodeValue
    # proprietário
    proprietario = imovel.getElementsByTagName("proprietario")[0].firstChild.nodeValue
    nome = imovel.getElementsByTagName("nome")[0].firstChild.nodeValue
    if imovel.getElementsByTagName("telefone"):
        telefone = imovel.getElementsByTagName("telefone")[0].firstChild.nodeValue
    if imovel.getElementsByTagName("email"):
        email = imovel.getElementsByTagName("email")[0].firstChild.nodeValue
    # características
    caracteristicas = imovel.getElementsByTagName("caracteristicas")[0].firstChild.nodeValue
    tamanho = imovel.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    numQuartos = imovel.getElementsByTagName("numQuartos")[0].firstChild.nodeValue
    numBanheiros = imovel.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue
    valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue

    lista.append(
        {
            "descricao": descricao,
            "endereco": {
                "rua": rua,
                "numero": numero,
                "bairro": bairro,
                "cidade": cidade
            },
            "proprietario": {
                "nome": nome,
                "telefone": telefone,
                "email": email,
            },
            "caracteristicas": {
                "tamanho": tamanho,
                "numQuartos": numQuartos,
                "numBanheiros": numBanheiros
            },
            "valor": valor
        }
    )

dados = {
    "imobiliaria": {
        "imoveis": lista
    }
}

with open('imobiliaria.json', 'w', encoding="utf-8") as json_file:
    json.dump(dados, json_file)