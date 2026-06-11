import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"


op = input("Digite 1 para ListOfCountryNamesByCode, 2 para ListOfCountryNamesByName e 3 para ListOfCountryNamesGroupedByContinent: ")

codigo = input("Digite o código do país:")

if op == '1':
    operation = "ListOfCountryNamesByCode"
elif op == '2':
    operation = "ListOfCountryNamesByName"
elif op == '3':
    operation = "ListOfCountryNamesGroupedByContinent"
else:
    print('número inválido!')

payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{operation} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{codigo}</sCountryISOCode>
					</{operation}>
				</soap:Body>
			</soap:Envelope>"""

headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    if op == "1":
        response = parseString(response.text).documentElement.getElementsByTagName("m:ListOfCountryNamesByCode")[0].firstChild.nodeValue
    elif op == "2":
        response = parseString(response.text).documentElement.getElementsByTagName("m:ListOfCountryNamesByName")[0].firstChild.nodeValue
    elif op == "3":
        response = parseString(response.text).documentElement.getElementsByTagName("m:ListOfCountryNamesGroupedByContinent")[0].firstChild.nodeValue
    print (response)