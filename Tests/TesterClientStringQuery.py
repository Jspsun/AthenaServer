import requests
res = urllib.urlopen('http://localhost:5000/Amessage')
if res.ok:
    print res.json()
