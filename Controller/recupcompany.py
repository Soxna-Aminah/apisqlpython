import requests
import sys
sys.path.append("..")
from Models import insertion
data=requests.get("https://jsonplaceholder.typicode.com/users")
r="insert into company(name,catchPhrase,bs) values(%s,%s,%s)"
class Recucompany:
    def __init__(self):
        pass
    def recuperation():
        company=[]
        for i in data.json():
            company.append((i['company']['name'],i['company']['catchPhrase'],i['company']['bs']))   
        insecom= insertion.Insert(r,company)
        insecom.connex()
met=Recucompany
met.recuperation()