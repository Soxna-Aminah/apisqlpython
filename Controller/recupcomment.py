import requests
import sys
sys.path.append("..")
from Models import insertion
data=requests.get("https://jsonplaceholder.typicode.com/comments")
r="insert into COMMENTS(id_comment,name,email,body,id_post) values(%s,%s,%s,%s,%s)"
class Recupcom:
    def __init__(self):
        pass
    def recuperation():
        com=[]
        for i in data.json():
            com.append((i['id'],i['name'],i['email'],i['body'],i['postId']))   
        insertcom= insertion.Insert(r,com).connex()

met=Recupcom
met.recuperation()