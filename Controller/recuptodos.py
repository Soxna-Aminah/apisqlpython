import requests
import sys
sys.path.append("..")
from Models import insertion
data=requests.get("https://jsonplaceholder.typicode.com/todos")
r="insert into TODOS(id_todo,title,id_user) values(%s,%s,%s)"
class Recuptodo:
    def __init__(self):
        pass
    def recuperation():
        todo=[]
        for i in data.json():
            todo.append((i['id'],i['title'],i['userId']))   
        insertodo= insertion.Insert(r,todo)
        insertodo.connex()

met=Recuptodo
met.recuperation()