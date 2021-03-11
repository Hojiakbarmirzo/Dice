import requests
import json
from pprint import pprint


token='1696683157:AAH3NeNVQfFeIwBQtBCAokCOb2hp9_773SQ'
def sendDice(indx):
    url=f'https://api.telegram.org/bot{token}/sendDice'
    payload={
        'chat_id':indx,
        'value':0
    }
    r=requests.get(url,params=payload)
    return r.json()

url=f'https://api.telegram.org/bot{token}/getUpdates'
r=requests.get(url)
data=r.json()
updates=data['result']
id_user=updates[-1]['message']['from']['id']
print(id_user)
sendDice(id_user)