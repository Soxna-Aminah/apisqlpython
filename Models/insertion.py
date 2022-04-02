import mysql.connector
class Insert:
    def __init__(self,r,para):
        self.r=r
        self.para=para
    def connex(self):
        r=self.r
        para=self.para
        par={
        "host":"localhost",
        "user":"Aminah",
        "password":'Ami@h1998',
        "database":"projetapirset"}
        with mysql.connector.connect(**par) as db:
            with db.cursor() as c:
                c.executemany(r,para)
            db.commit()


