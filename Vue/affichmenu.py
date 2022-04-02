class Affichmenu:
    def __init__(self):
        pass
    def Afficher():
        diction={"1":"Afficher les Utilisateurs",
                "2": "Afficher les Postes",
                "3":"Afficher les commentaires",
                "4":"Afficher les Albums",
                "5":"Afficher les Photos",
                "6":"Afficher les Todos"}
        print("""######################################################################
        |------------------------MENU-----------------------------------------|
        #####################---------------###################################""")
        for k,v in diction.items():
            print("            "+k+")"+v+"                                  ")
        print("######################################################################")
