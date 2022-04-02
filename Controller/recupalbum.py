import requests
import sys
sys.path.append("..")
from Models import insertion
data=requests.get("https://jsonplaceholder.typicode.com/todos")
r="insert into ALBUMS(id_album,title,id_user) values(%s,%s,%s)"
class Recupalbum:
    def __init__(self):
        pass
    def recuperation():
        album=[]
        for i in data.json():
            album.append((i['id'],i['title'],i['userId']))   
        inseralbum= insertion.Insert(r,album)
        inseralbum.connex()

met=Recupalbum
met.recuperation()