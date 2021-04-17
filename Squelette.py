from PlusProcheVoisin import *
from Interface import *

class RoboLego():
    def __init__(self,xinit=0,yinit=0,cst=None):
        self.__position=[xinit,yinit]
        self.__listeNoeuds=[]
        self.__constantes=cst
        self.__interface=Application(self.__listeNoeuds,self.__position)

    def recupererNoeuds(self,addresse):
        """Prends en parametre l'adresse du fichier texte contenant les noeuds. Renvoie un liste de noeuds."""
        fichier=open(r'C:\Users\Remis\Documents\GitHub\SAMI\fichier_de_points.txt')
        txt=fichier.read()
        points=txt.split("\n")
        listeNoeuds=[]
        for p in points:
            coordonnee=p.split("\t")
            coordonnee[0],coordonnee[1]=float(coordonnee[0]),float(coordonnee[1])
            listeNoeuds.append(coordonnee)

        return listeNoeuds

    def ordreNoeuds(self,listeNoeuds):
        """Prend en parametre une liste de noeuds. Renvoie la liste des noeuds dans le bon ordre de passage. """
        k=PlusProcheVoisin(listeNoeuds,0,len(listeNoeuds),1000,1000)
        k.listePlusProche()
        self.listeNoeuds=k.nouvelleCoord()

    def partieAuto(self):
        """Prend en parametre une liste de noeuds. Actionne les roues du robot pour le faire se déplacer depuis sa position actuelle vers chaque noeud dans l'ordre de la liste."""


    def cestParti(self,adresse):
        """Lance le robot. Prend en parametre une adresse Utilise ordreNoeuds() et allerVers() pour emmener le robot à destination."""
        listeNoeuds=self.ordreNoeuds(self.recupererNoeuds(adresse))
        self.__interface.Mafenetre.mainloop()
        self.partieAuto()
        print("bob")

###

rob=RoboLego()

rob.cestParti(r'C:\Users\Remis\Documents\GitHub\SAMI\fichier_de_points.txt')
