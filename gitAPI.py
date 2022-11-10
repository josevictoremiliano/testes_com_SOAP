import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass


password = "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"
username = 'josevictoremiliano'
  
url = "https://api.github.com/user/following/" + username
print(url)


response = requests.get(url,
            auth = HTTPBasicAuth('josevictoremiliano', password))

print(response.json())

