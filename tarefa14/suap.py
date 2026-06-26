import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

token = ""
headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)
ano = input("Digite o ano:")
periodo = input("Digite o período:")
url = api_url+f"ensino/meu-boletim/{ano}/{periodo}/"
print(url)
response = requests.get(url, headers=headers)

disciplinas = response.json()["results"]
for disciplina in disciplinas:
    print(f"{disciplina['disciplina']:<70} - {disciplina['nota_etapa_1']['nota']} - {disciplina['nota_etapa_2']['nota']} - {disciplina['nota_etapa_3']['nota']} - {disciplina['nota_etapa_4']['nota']}")

print(response)