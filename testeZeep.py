import zeep 

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

country_code = "BR"

result = client.service.CountryIntPhoneCode(
	sCountryISOCode=country_code
)
print(f"O código de telefone do {country_code} é {result}")

country_code = "US"

result = client.service.CountryIntPhoneCode(
	sCountryISOCode=country_code
)

print(f"O código de telefone do {country_code} é {result}")