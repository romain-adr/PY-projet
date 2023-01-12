import re
import pandas as pd
from Author import Author

# =============== 2.7 : CLASSE CORPUS ===============
class Corpus:
    def __init__(self, nom):
        self.nom = nom 
        self.authors = {} #le dictionnaire des auteurs
        self.aut2id = {} #
        self.id2doc = {} # dictionnaire des documents
        self.ndoc = 0 #comptage des documents
        self.naut = 0 # comptage des autheurs

    def add(self, doc):
        if doc.auteur not in self.aut2id:
            self.naut += 1
            self.authors[self.naut] = Author(doc.auteur)
            self.aut2id[doc.auteur] = self.naut
        self.authors[self.aut2id[doc.auteur]].add(doc.texte)

        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

# =============== 2.8 : REPRESENTATION ===============
    def show(self, n_docs=-1, tri="abc"):
        docs = list(self.id2doc.values())
        if tri == "abc":  # Tri alphabétique
            docs = list(sorted(docs, key=lambda x: x.titre.lower()))[:n_docs]
        elif tri == "123":  # Tri temporel
            docs = list(sorted(docs, key=lambda x: x.date))[:n_docs]

        print("\n".join(list(map(repr, docs))))

    def __repr__(self):
        docs = list(self.id2doc.values())
        docs = list(sorted(docs, key=lambda x: x.titre.lower()))

        return "\n".join(list(map(str, docs)))
#---------------------#  

    def search(self, word=''): #retourne les phrases contenant le mot-clef entre en paramettre
        texte = str(list(self.id2doc.values()))
        passages = []
        word_re = re.compile(word, re.IGNORECASE)
        sentences = re.split(r'[.!?]', texte)
        for sentence in sentences:
            if re.search(word_re, sentence):
                passages.append(sentence.strip())
        return passages 
        
    def concorde(self, word='',posg='20',posd='20'):
        passages = []
        start_df = [] 
        end_df = []
        texte = str(list(self.id2doc.values()))
        word_re = re.compile(word, re.IGNORECASE)
        sentences = re.split(r'[.!?]', texte)
        for sentence in sentences:
            if re.search(word_re, sentence):
                passages.append(sentence.strip())
        for sentence in passages:
            start_index = sentence.find(word)
            end_index = sentence.find(word) + len(word)
            context_start = sentence[start_index-int(posg):start_index]
            context_end = sentence[end_index:end_index+int(posd)]
            start_df.append(context_start)
            end_df.append(context_end)
        data = {'start': start_df, 'word': word, 'end': end_df}
        df = pd.DataFrame(data)
        return df
        
        




