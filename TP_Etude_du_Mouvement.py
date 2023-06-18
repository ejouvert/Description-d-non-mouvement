import matplotlib.pyplot as plt #importation de la bibliotheque matplotlib

x=[] # Liste des positions de la balle suivant l'axe des x
y=[] # Liste des positions de la balle suivant l'axe des y

dt=0.04 # Pointage des positions d'un objet toutes les 0,04 s

#affichage

plt.ylim(-0.1, 1.85) #indique les limites de l'axe des y
plt.xlabel("Positions x") #je nomme l'axe des X
plt.ylabel("Positions y") #je nomme l'axe des Y
plt.grid(True) #je trace le quadrillage
plt.title("Chute libre sans vitesse initiale") #j'écris le titre du graphique
plt.plot(x, y,'+',color='black') #Tracé des points expérimentaux symbolisé par des +

plt.show() #j'affiche le graphique