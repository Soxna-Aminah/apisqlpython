import affichmenu
from Controller import lecture

menu=affichmenu.Affichmenu
choix=5
while choix != 0:
    menu.Afficher()
    lect=lecture.Lecture
    choix=input("Faites votre choix ou 0 pour quitter:")
    if choix=="1":
        lect.lectuser()
    elif choix=="2":
        lect.lectpost()
    elif choix=="3":
        lect.lectcomment()
    elif choix=="4":
        lect.lectalbum()
    elif choix=="5":
        lect.lectphotos()
    elif choix=="6":
        lect.lectodos()
    else :
        print("Choix indisponible")
