# Importation des modules
import time

# Je commence par définir ma fonction qui prend en paramètre l'heure, les minutes et les secondes
def horloge(hh, mm, ss):
    
    #Je place une boucle while qui permet d'afficher l'heure, les minutes et les secondes en continue
    while True:
        #J'affiche l'heure sous le format hh:mm:ss grâce à la méthode format representé par f""
        #02 indique que les valeurs doivent être affiché sur 2 caractères
        #end=\r pour que l'heure reste sur la même ligne
        #flush=true pour forcer l'affichage de la valeur sans attendre le remplissage de la mémoire tampon
        
        print(f"{hh:02}:{mm:02}:{ss:02}", end="\r", flush=True)

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
horloge(16, 30, 00)   #J'appelle ma fonction horloge en lui passant comme paramètre 16, 30, 00