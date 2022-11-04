import zeep 

wsdl_url = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

number = input("Digite um número: ")

result = client.service.NumberToWords(
	ubiNum=number
)

print(f"Você digitou o numero: {number} e ele em ingles é: ")
print(result)