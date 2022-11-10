import requests
from getpass import getpass
import pandas as pd
import json

api_url = "https://suap.ifrn.edu.br/api/"

user = '20191181110029'
password = getpass()

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()["access"]


headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

response = requests.get(api_url+"v2/minhas-informacoes/boletim/2022/1/", headers=headers)



data = json.loads(response.text)
  
df = pd.DataFrame(data)

print(df)



print(response)