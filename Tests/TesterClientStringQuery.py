import requests
res = urllib.urlopen('http://localhost:5000/api/add_message/1234')
if res.ok:
    print res.json()
