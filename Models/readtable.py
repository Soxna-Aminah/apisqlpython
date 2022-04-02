import mysql.connector
class Read:
    def __init__(self,r):
        self.r=r
        r=self.r
    def lect(self):
        r=self.r
        par={
        "host":"localhost",
        "user":"Aminah",
        "password":'Ami@h1998',
        "database":"projetapirset"}
        with mysql.connector.connect(**par) as db:
            with db.cursor() as c:
                c.execute(r)
                n=c.fetchall()
                return n