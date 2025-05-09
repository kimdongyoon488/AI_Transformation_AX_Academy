import requests

#res = requests.get("http://127.0.0.1:8000/")
res2 = requests.get("http://127.0.0.1:8000/items/10?q=10")

#res_json = res.json()
res_json2 = res2.json()
#print(res_json)
print(res_json2)