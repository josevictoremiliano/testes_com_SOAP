import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass


password = "TOKEN DO GITHUB https://github.com/settings/tokens?type=beta"
username = input("Digite seu username: ")
  
url = "https://api.github.com/user/following/" + username

response = requests.put(url,
            auth = HTTPBasicAuth('josevictoremiliano', password))


print(response.status_code)

if response.status_code == 204:
    print("Success")
else:
    print("Failed")