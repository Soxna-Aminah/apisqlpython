import requests
import sys
sys.path.append("..")
from Models import insertion
data=requests.get("https://jsonplaceholder.typicode.com/photos")
r="insert into PHOTOS(id_photo,title,url,id_album,thumbnailUrl) values(%s,%s,%s,%s,%s)"
class Recuptof:
    def __init__(self):
        pass
    def recuperation():
        tof=[]
        for i in data.json():
            tof.append((i['id'],i['title'],i['url'],i['albumId'],i['thumbnailUrl']))   
        inserttof= insertion.Insert(r,tof)
        inserttof.connex()

met=Recuptof
met.recuperation()