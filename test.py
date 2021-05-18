import requests
import json

url = 'http://0.0.0.0:80/seqvec'
sequence = 'MAVDSPDERLQRRIAQL'


r = requests.post(url, json={'seq': sequence})
print(json.loads(r.text)['seqvec'])
