# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:17:37 2022

@author: Romain
"""
class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0 # nombre de documents publies
        self.production = [] #dictionnaire des documents  ́ecrits par l’auteur
# =============== 2.5 : ADD ===============
    def add(self, production):
        self.ndoc += 1
        self.production.append(production)
    def __str__(self):
        return f"Auteur : {self.name}\t# productions : {self.ndoc}"