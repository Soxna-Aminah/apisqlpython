from select import select
import requests
import sys
sys.path.append("..")
from Models import insertion
from Models import readtable
data=requests.get("https://jsonplaceholder.typicode.com/users")
r="insert into USER(id_user,name,username,phone,id_adresse,id_company,email,website) values(%s,%s,%s,%s,%s,%s,%s,%s)"
r1="select *from adresse"
r2="select *from company"
class Recupuser:
    def __init__(self):
        pass
    def recuperation():
        user=[]
        id_ad=0
        id_com=0
        for i in data.json():
            street=i['address']['street']
            company=i['company']['name']
            objad=readtable.Read(r1).lect()
            objcomp=readtable.Read(r2).lect()
            for k in objad:
                if k[1]==street:
                    id_ad=k[0]
            for l in objcomp:
                if l[1]==company:
                    id_com=l[0]   
            user.append((i['id'],i['name'],i['username'],i['phone'],id_ad,id_com,i['email'],i['website']))         
        inseuser= insertion.Insert(r,user)
        inseuser.connex()

us=Recupuser
us.recuperation()
#print(data.json())

#         
#         insecom.connex()
# met=Recucompany
# met.recuperation()