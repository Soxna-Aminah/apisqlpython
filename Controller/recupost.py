import requests
import sys
sys.path.append("..")
from Models import insertion
data=requests.get("https://jsonplaceholder.typicode.com/posts")
r="insert into POST(id_post,title,body,id_user) values(%s,%s,%s,%s)"
class Recupost:
    def __init__(self):
        pass
    def recuperation():
        todo=[]
        for i in data.json():
            todo.append((i['id'],i['title'],i['body'],i['userId']))   
        inserpst= insertion.Insert(r,todo).connex()

met=Recupost
met.recuperation()