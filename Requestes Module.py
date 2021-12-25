import requests

r = requests.get("https://financialmodelingprep.com/api/v3/quote/AAPL,FB")
print(r.text)
print(r.status_code)

#url = "www.something.com"
#data={"p1":4,"p2":6}

#r2 = requests.post(url=url,data=data)
#print(r.text)
