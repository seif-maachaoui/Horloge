# Importation des modules
import time

# Je commence par définir ma fonction qui prend en paramètre l'heure, les minutes, les secondes et stop_second
def horloge(hh, mm, ss, stop_second):
    
    #Je place une boucle while qui permet d'afficher l'heure, les minutes et les secondes en continue
    while True:
        #J'affiche l'heure sous le format hh:mm:ss grâce à la méthode format representé par f""
        #02 indique que les valeurs doivent être affiché sur 2 caractères
        #end=\r pour que l'heure reste sur la même ligne
        #flush=true pour forcer l'affichage de la valeur sans attendre le remplissage de la mémoire tampon
        
        print("Heure non modifiable : ", f"{hh:02}:{mm:02}:{ss:02}", end="\r", flush=True)
        
        #J'incrémente de +1 ma variable de seconde avant tout
        ss += 1
        if ss == 60:        #Si on atteint 60 secondes, alors...
            mm += 1         #Ajoute + 1 aux minutes
            ss = 0          #Et je réinitialise mes secondes à 0     
        elif mm == 60:      #Sinon si on atteint 60 minutes, alors...
            hh += 1         #J'ajoute +1 à l'heure
            mm = 0          #Puis réinitialise les minutes à 0
        elif hh == 24:      #Sinon si on atteint 24 heures, alors...
            hh = 0          #On réinitialise la valeur d'heure à 0
        
        # J'attends une seconde avant de rafraîchir l'heure affichée grâce à la fonction sleep
        time.sleep(1)           

        #Je veux à présent que dès que les secondes atteignent stop_second, on sort de la boucle
        if ss == stop_second:
            break
    #Je n'oublie pas de retourner l'heure
    return hh, mm, ss   

#Je stocke ma valeur retournée dans une variable temps
# Qui appellera ma fonction horloge, qui est un tuple avec pour paramètre hh, mm, ss et stop_second
temps = horloge(16, 30, 00, 10)
#Puis j'affiche le temps après 10 secondes
print("Le temps après 10 secondes : ", f"{temps[0]:02d}:{temps[1]:02d}:{temps[2]:02d}")

#Je créer une fonction afficher_heure qui prend en paramètre un tuple heure
def afficher_heure(heure):

    #Je shouaite extraire le contenu de mon tuple, pour manipuler les éléments à l'intérieur
    heures, minutes, secondes = heure
    print("Heure modifiable :", f"{heures:02d}:{minutes:02}:{secondes:02d}")

    #Je créer une variable, pour demander à l'utilisateur si il souhaite changer l'heure
    change_hour = input("Voulez-vous changer l'heure ? (y/n)")
    
    #Si l'utilisateur souhaite changer l'heure, alors...
    if change_hour == "y":
        #La boucle while ici va demander une nouvelle heure jusqu'à qu'elle soit accepté
        while True :
            
            #Je place mes variables pour demander, l'heure, les minutes et les secondes
            heures = input("Veuillez entrer une heure (entre 0 et 23): ")
            minutes = input("Veuillez entrer les minutes (entre 0 et 59): ")
            secondes = input("Veuillez entrer les secondes (entre 0 et 59): ")

            #Je vérifie ici que les valeurs qui ont été entrées soient bien des nombres, des integers
            if heures.isdigit() and minutes.isdigit() and secondes.isdigit():
                heures = int(heures)
                minutes = int(minutes)
                secondes = int(secondes)
                #Je rajoute une condition, qui vérifie si l'heure, les minutes, et les secondes sont bien conforme
                if 0 <= heures <= 23 and 0 <= minutes <= 59 and 0 <= secondes <=59:
                    #Si c'est le cas, j'utilise un break pour sortir de la boucle et passer à la suite
                    break
                else: #Sinon si l'utilisateur entre des valeurs au-dessus de celles autorisées, alors...
                    if heures > 23 and minutes > 59 and secondes > 59:
                        print("Erreur, votre heure n'est pas valide, veuillez réessayer.\n")

    #Enfin, j'affiche la nouvelle heure à l'utilisateur
    print("La nouvelle heure :", f"{heures:02d}:{minutes:02d}:{secondes:02d}")
#J'apelle ma fonction en lui passant en paramètre temps qui va extraire les valeurs des heures, minutes et secondes
#Puis les afficher au format hh:mm:ss
afficher_heure(temps)

#Je déclare une fonction alarme
def time_trigger(sonnerie):

    heures, minutes, secondes = sonnerie

    #Premièrement, je souhaite d'abord afficher l'heure actuelle
    print("Il est actuellement :", time.strftime("%H:%M:%S"))

    #Deuxièment, je souhaite que l'utilisateur puisse régler l'alarme
    alarme = input("Voulez-vous régler une alarme ? (y/n)")

    #Si l'utilisateur souhaite régler l'alarme, alors...
    if alarme == 'y':
        #Boucle while, pour que la boucle continue tant que l'utilisateur n'a pas rentrer les bonnes valeurs
        while True:
            alarme_heure = int(input("Veuillez entrer une heure (entre 0 et 23) : "))
            alarme_minutes = int(input("Veuillez entrer les minutes (entre 0 et 59) : "))
            if 0 < alarme_heure < 24 and 0 < alarme_minutes < 60:
                break
            else:
                print("Erreur, veuillez réessayer")

    while True:
        heure_actuelle = time.localtime().tm_hour
        minute_actuelle = time.localtime().tm_min

        #Si l'heure actuelle et minute actuelle correspond à l'heure de l'alarme, alors..
        if heure_actuelle ==  alarme_heure and minute_actuelle == alarme_minutes:
            print("L'alarme sonne ! Il est :", f"{alarme_heure:02d}:{alarme_minutes:02d}")
            #Si c'est le cas, alors on sort de la boucle
            break
        else:
            #Sinon, on patiente le temps que l'alarme se déclenche
            print("Veuillez patienter...", end='\r')
            
            #On attends toujours une seconde avant de vérifier
            time.sleep(1)

#Appel de ma fonction 
time_trigger((10, 29, 00))
    



