import zeep

wsdl_url = "http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

numero = input("Digite um número inteiro: ")
result = client.service.NumberToWords(
	ubiNum=numero
)

print(f"O número {numero} em extenso é: {result}")