import json
from urllib.request import urlopen
import pandas as pd

with urlopen("http://www.floatrates.com/daily/usd.json") as response:
    source = response.read()
#data = json.load(urlopen("http://www.floatrates.com/daily/usd.json"))
#print(data)
data= json.loads(source)
#print(json.dumps(data, indent=2)

#print(len(data[dict]))
#print(type(data['eur']))
#print['data']['eur']

brics = pd.DataFrame(data)
print(brics)

 #   for nitem in item:
  #      print(nitem.get('alphaCode'))


   # for item in data['people']:
    #    print("division number is:")
    #print((item['div_no']))



#usd_rates = dict()

#print([data])

#for key, value in data.items():
 #   print(key, value)
   # print(eur['code'])

#for item in data:
 #   print (data)

#with open('new_codes.json', 'w') as f:
 #   json.dump(data, f, indent=2)

#
#for item in data['list']['resources']:
 #   name = item['resource']['fields']['name']
  #  price = item['resource']['fields']['price']
   # usd_rates[name] = price


#print(50 * float(usd_rates['USD/INR']))