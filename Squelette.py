Go pour le squelette :
from PlusProcheVoisin import *

class RoboLego():
    def __init__(xinit=0,yinit=0):
        self.position=[xinit,yinit]
        self.listeNoeuds=[]

    def recupererNoeuds(self,addresse):
        """Prends en parametre l'adresse du fichier texte contenant les noeuds. Renvoie un liste de noeuds."""
        fichier=open(r'C:\Users\Remis\Documents\GitHub\SAMI\fichier_de_points.txt')
        txt=fichier.read()
        points=txt.split("\n")
        listeNoeuds=[]
        for p in points:
            coordonnee=p.split("\t")
            coordonee[0],coordonnee[1]=float(coo[0]),float(coo[1])
            listeNoeuds.append(coordonnee)

        return listeNoeuds

    def ordreNoeuds(self,listeNoeuds):
        """Prend en parametre une liste de noeuds. Renvoie la liste des noeuds dans le bon ordre de passage. """
        k=PlusProcheVoisint(listeNoeuds,0,len(listeNoeuds),3,3)
        listeOrdonnee=PlusProcheVoisin.distanceParcourt(k.nouvelleCoord())
        return listeOrdonnee

    def allerVers(self,noeud):
        """Prend en parametre un noeud. Actionne les roues du robot pour le faire se déplacer depuis sa position actuelle vers un noeud objectif."""


    def cestPartie(self,adresse):
        listeNoeuds=ordreNoeuds(recupererAdresse(adresse))
    """Lance le robot. Utilise ordreNoeuds() et allerVers() pour emmener le robot à destination."""