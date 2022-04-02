import requests
# import sys
# sys.path.append("..")
from Models.insertion import Insert
userjson=requests.get("https://jsonplaceholder.typicode.com/users")
r="insert into adresse(street,suite,geolat,geolong) values(%s,%s,%s,%s)"

class recupadress:
    def __init__(self):
        pass
    def recuperation():
        adresse=[]
        for i in userjson.json():
            adresse.append((i['address']['street'],i['address']['suite'],i['address']['geo']['lat'],i['address']['geo']['lng']))
        
        inseadr= Insert(r,adresse)
        inseadr.connex()
# n=recupadress
# n.recuperation()