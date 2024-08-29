import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

headers = {'Content-Type': 'text/xml; charset=utf-8'}

def soap_function(func, func_value, value):
	# envia uma solicitação SOAP para uma API e retorna o resultado
	payload = f"""<?xml version="1.0" encoding="utf-8"?>
	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
		<soap:Body>
			<{func} xmlns="http://www.oorsprong.org/websamples.countryinfo">
				<{func_value}>{value}</{func_value}>
			</{func}>
		</soap:Body>
	</soap:Envelope>
	"""

	result_element = func+"Result"
	response = requests.request("POST", url, headers=headers, data=payload)
	result = parseString(response.text).getElementsByTagName(f"m:{result_element}")[0].firstChild.nodeValue

	return result


def new_zealand_capital():
	nz_capital = soap_function("CapitalCity", "sCountryISOCode", "NZ")
	return nz_capital


while(True):
	print("")
	print("="*10 + " API SOAP - COUNTRIES " + "="*10 +"\n")
	print("1. Qual a Capital da Nova Zelândia? ")
	print("2. Código ISO do país")
	print("3. Código ISO da idioma")
	print("4. Nome do país")
	print("0. Encerrar")

	terminal = input("\n Escolha uma opção: ")
	print("")

	if terminal == "0":
		break

	elif terminal == "1":
		print("="*10 + " NOVA ZELÂNDIA " + "="*10)
		print(f"\nCapital da Nova Zelândia é {new_zealand_capital()}")

	elif terminal == "2":
		print("="*10 + " CÓDIGO ISO DO PAÍS " + "="*10)
		value = input("Digite o nome de um país (em inglês): ")
		country_code = soap_function("CountryISOCode", "sCountryName", value)
		print(f"\nO codigo ISO de {value} é {country_code}")

	elif terminal == "3":
		print("="*10 + " CÓDIGO ISO DO IDIOMA " + "="*10)
		value = input("Digite o nome de um idioma (em inglês): ")
		lang_code = soap_function("LanguageISOCode", "sLanguageName", value)
		print(f"\nO codigo ISO de {value} é {lang_code}")

	elif terminal == "4":
		print("="*10 + " NOME DO PAÍS " + "="*10)
		value = input("Digite o código ISO do país: ")
		country_name = soap_function("CountryName", "sCountryISOCode", value)
		print(f"\nO país do código {value} é {country_name}")

