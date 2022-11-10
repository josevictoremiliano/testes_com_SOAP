import json
import pandas as pd
from urllib.request import urlopen
# store the URL in url as 
# parameter for urlopen
url = "https://www.testjsonapi.com/users/"
  
# store the response of URL
response = urlopen(url)
# Opening JSON file
#f = open(response.read())
  
# returns JSON object as 
# a dictionary
data = json.loads(response.read())
  
df = pd.DataFrame(data)

print(df)
 
# Closing file
response.close()