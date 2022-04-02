
from turtle import pen
from Models import readtable
class Lecture:
    def __init__(self):
        pass
    def lectuser():
        r="Select *from USER"
        r1="select *from adresse"
        myread=readtable.Read(r)
        n=myread.lect()
        for i in n:
            ad=readtable.Read(r1)
            m=ad.lect()
            for j in m:
                if j[0]==i[5]:
                    infad=j
            print("############################################################################")
            print("id: ",i[0],"|","Name: ",i[1],"|","Username: " , i[2],"|","website: ", i[3],"|","Phone: ",i[4],"|")
            print("Adresse: id: ",j[0],"street: ",j[1],"suite: ",j[2],"Geo: long:",j[4],"lat: ",j[3])
            print("############################################################################")
    def lectpost():
        r="Select *from POST"
        myread=readtable.Read(r)
        n=myread.lect()
        for i in n:
             print("############################################################################")
             print("id: ",i[0])
             print("tittle:", i[1])
             print("body: ",i[2])
             print("id_user: ",i[3])
             print("############################################################################")
    def lectcomment():
        r="select *from COMMENTS"
        myread=readtable.Read(r)
        n=myread.lect()
        for i in n:
             print("############################################################################")
             print("id: ",i[0])
             print("name: ",i[1])
             print("email: ",i[2])
             print("body: ",i[3])
             print("id_post: ",i[4])
             print("############################################################################")

    def lectalbum():
         r="select *from ALBUMS"
         myread=readtable.Read(r)
         n=myread.lect()
         for i in n:
              print("############################################################################")
              print("id: ",i[0])
              print("tittle:", i[1])
              print("id_user: ",i[2])
              print("############################################################################")
    def lectphotos():
         r="select *from PHOTOS"
         myread=readtable.Read(r)
         n=myread.lect()
         for i in n:
             print("############################################################################")
             print("id: ",i[0])
             print("title: ", i[1])
             print("url: ",i[2])
             print("thumbnailurl: ",i[4])
             print("id_album: ",i[3])
             print("############################################################################")
    def lectodos():
        r="select *from TODOS"
        myread=readtable.Read(r)
        n=myread.lect()
        for i in n:
             print("############################################################################")
             print("id: ",i[0])
             print("title: ", i[1])
             print("id_user: ",i[2])
             print("############################################################################")
 


    

