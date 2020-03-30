import requests

URL = "http://127.0.0.1:8000/crit/fish/"

g = input("Enter Fish you want")
print(g)

URL = URL+g+'/'
print(URL)
r = requests.get(url=URL)
r = r.json()

print(r)