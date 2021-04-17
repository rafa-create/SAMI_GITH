Go pour le squelette :
from PlusProcheVoisin import *

class RoboLego():
    def __init__(x=0,y=0):
        position=[x,y]

    def recupererNoeuds(self,addresse):
        """Prends en parametre l'adresse du fichier texte contenant les noeuds. Renvoie un liste de noeuds."""
        listeNoeuds=[]
        return listeNoeuds

    def ordreNoeuds(self,listeNoeuds):
        """Prend en parametre une liste de noeuds. Renvoie la liste des noeuds dans le bon ordre de passage. """
        k=PlusProcheVoisint(listeNoeuds,0,len(listeNoeuds),3,3)
        listeOrdonnee=PlusProcheVoisin.distanceParcourt(k.nouvelleCoord())
        return listeOrdonnee

    def allerVers(self,noeud):
        """Prend en parametre un noeud. Actionne les roues du robot pour le faire se déplacer depuis sa position actuelle vers un noeud objectif."""


    def cestPartie(self):
    """Lance le robot. Utilise ordreNoeuds() et allerVers() pour emmener le robot à destination."""