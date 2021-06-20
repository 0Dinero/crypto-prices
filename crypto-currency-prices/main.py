import requests
def btcprice():
    url = requests.get("https://blockchain.info/ticker")
    x = url.json()
    print(x["USD"]["buy"], "$")
def ethprice():
    url = requests.get("https://apiv2.bitcoinaverage.com/indices/crypto/ticker/ETHUSDC")
    x = url.json()
    print(x["last"])
print("What price do you wanna check?")
print("BTC = bitcoin")
i = 1
while i == 1:
    x = input(">>> ")
    xx = x.upper()
    if xx == "BTC":
        btcprice()
    else:
        i = 0