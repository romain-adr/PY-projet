# =============== 2.1 : La classe Document ===============
class Document:
    # Initialisation des variables de la classe
    def __init__(self, titre="", auteur="", date="", url="", texte=""):
        self.titre = titre 
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte 

# =============== 2.2 : REPRESENTATIONS ===============
    # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(classe)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\t"

    # Fonction qui renvoie le texte à afficher lorsqu'on tape str(classe)
    def __str__(self):
        return f"{self.titre}, par {self.auteur}"
    def getType(self):
        pass

# =============== CLASSE FILLE REddit=================

class RedditDocument(Document):
    def __init__(self, titre="", auteur="", date="", url="", texte="", nbcom=""):
        super().__init__(titre="", auteur="", date="", url="", texte="")
        self.nbcom = nbcom
        
    def __str__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\tnbcom : {self.nbcom}\t"
        
    def getType(self):
        return "Reddit"
    
# =============== CLASSE FILLE Arxiv=================

class ArxivDocument(Document):
    def __init__(self, titre="", auteur="", date="", url="", texte="", co_auth=""):
        super().__init__(titre="", auteur="", date="", url="", texte="")
        self.co_auth = co_auth
        
    def __str__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\tco_auth : {self.co_auth}\t"
        
    def getType(self):
        return "Arxiv"
    