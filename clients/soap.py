import zeep

wsdl_countries = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
wsdl_number_to_words = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

countries_client = zeep.Client(wsdl=wsdl_countries)
numbers_client = zeep.Client(wsdl=wsdl_number_to_words)

def norway_capital():
	country_code = "NO" # Noruega
	result = countries_client.service.CapitalCity(sCountryISOCode=country_code)
	return result


while(True):
	print("")
	print("="*10 + " ZEEP - SOAP CLIENT " + "="*10 +"\n")
	print("1. Qual a Capital da Noruega? ")
	print("2. Número por Extenso")
	print("0. Encerrar")
	option = input("\nEscolha uma opção: ")
	print("")

	if option == "0":
		break

	if option == "1":
		print("="*10 + " NORUEGA " + "="*10)
		print(f"\nA capital da Noruega é {norway_capital()}")

	if option == "2":
		print("="*10 + " NÚMERO POR EXTENSO " + "="*10)
		number = int(input("Digite um número: "))
		response = numbers_client.service.NumberToWords(ubiNum=number)
		print(f"\n{response}")
