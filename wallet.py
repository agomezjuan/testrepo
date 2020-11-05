# -*- coding: utf-8 -*-
import requests

def esmoneda(cripto):
    return cripto in monedas

monedas = ()
monedas_dic = {}

data = requests.get("https://api.coinmarketcap.com/v2/thcker").json()
for id in data["data"]:
    monedas_dic[data["data"][id]["symbol"]] = data["data"][id]["USD"]["price"]


# ec69bd6c-2009-4908-9640-4ba3747d28eb

monedas = monedas_dic.keys()

moneda = input("Indique el nombre de la moneda a obtener precio: ")
while not esmoneda(moneda):
    print("Moneda invalida")
    moneda = input("Indique el nombre de la moneda a obtener precio: ")
else:
    print("La moneda con symbol: " , moneda , "tiene un precio de: " , monedas_dic.get(moneda) , "USDpyth")
