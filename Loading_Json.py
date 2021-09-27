#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:49:23 2021

@author: Aljoscha
"""
import os
import json
from bs4 import BeautifulSoup
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from imageio import imread
import re
import pandas as pd


directory = './LegifranceJSON'


data = {}


## To load the full directory by id's
def load_JSON_repo(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as read_file:
                temp = json.load(read_file)
                data[temp['dossierLegislatif']['id']] = temp['dossierLegislatif']
            continue
        else:
            continue
    return(data)



## TO load the full directory by titles
def load_JSON_title(directory):
    
    data = {}
    
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as read_file:
                temp = json.load(read_file)
                data[temp['dossierLegislatif']['titre']] = temp['dossierLegislatif']
            continue
        else:
            continue
    return(data)

## To load the full directory by legislatures
def load_JSON_by_legis(directory):  
    ##à faire : 
    #trier legis pour supprimer les redondances
    #Re-importer les fichiers JSON par legisislature : faire entre les dossiers dans leurs valeurs legislature respectives
    # Type : if legis[...] == data[titre][legislature] do: legis2 = legis2 + {data...} where legis2 est un dict ({})
   
    legis = []
    data = {}
    
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as read_file:
                temp = json.load(read_file)
                data[temp['dossierLegislatif']['titre']] = temp['dossierLegislatif']
            continue
        else:
            continue

    for title in data:
        for i in legis:
            if legis[i] != [data[title]['legislature']['libelle']]:
                legis = legis + [data[title]['legislature']['libelle']]
            else:
                continue

    print(legis)
    return(legis)


def export_to_txt(data):

    Txt_propre = []    
    
    for xpo in data:
        Expo_des_motifs = BeautifulSoup(data[xpo]['exposeMotif'], 'html.parser')
        Txt_propre = Txt_propre + [data[xpo]['id'] + " : " + Expo_des_motifs.get_text() + '\n']
    
    with open("xpo_export.txt", "w", encoding='utf8') as f:
        for line in Txt_propre:
            f.write(line + "\n")
    
    return(Txt_propre)

#with open("./LegifranceJSON/JORFDOLE000017758132.json", 'r') as read_file:
#    data = json.load(read_file)
    

def grey_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return 'hsl(0, 0%%, %d%%)' % random.randint(50, 100)

def nuage(xpo_motif):
    texte = ""
    texte = texte.join(xpo.rstrip('\n') + " " for xpo in xpo_motif)


    from nltk.corpus import stopwords
    sw_french = stopwords.words("french")
    sw_french = sw_french + ["l'article", 'code', 'loi', 'également', 'leurs', 'entre',
                             'cette', 'dont', 'autre', 'plu', 'article', 'plus',
                             'permettre', 'droit', 'disposition', 'mise', 'a',
                             'articles', 'cette', 'notamment', 'nécessaire', 'cas',
                             'enfin', 'modalités', 'cet', 'ainsi', 'comme', 'afin',
                             "d'un", 'tout', 'prévoit',"d'une", 'effet', 'permet',
                             'dispositions', 'mesure', 'droits', ]


    limit = 50

#fontcolor='#fafafa'
    fontcolor='#fa0000' # couleur des caractères
    bgcolor = '#000000' # couleur de fond
#bgcolor = '#ffffff'
#bgcolor = '#aa0000'
    
    wordcloud = WordCloud(
        max_words=limit,
        stopwords= sw_french, # liste de mots-outils
        #mask=imread('img/mask.png'),  # avec ou sans masque, à essayer ! (attention, nécessite un fichier de masque en noir et blanc)
        background_color=bgcolor,
        #    font_path=font   # si on veut changer la police de caractères
        ).generate(texte.lower()) # tolower() permet de mettre tout le texte en minuscule


    fig = plt.figure()

## taille de la figure
    fig.set_figwidth(14)
    fig.set_figheight(18)
    
        
    plt.imshow(wordcloud.recolor(color_func=grey_color, random_state=3))
    
    plt.axis('off')
    plt.show()


def find_a_word(xpo_motif, word):
    
    texte = ""
    texte = texte.join(xpo.rstrip('\n') + " " for xpo in xpo_motif)
    
    pattern = re.compile(word, re.IGNORECASE)
    
    res = pattern.finditer(texte)
    start_pattern = [m.start() for m in res]
    
    print(len(start_pattern))


def main():
    data = load_JSON_repo(directory)
#    print(data['JORFDOLE000017758144']['arborescence'])

    xpo_motif = export_to_txt(data)

    find_a_word(xpo_motif, "sécurité publique")
#    nuage(xpo_motif)
  
#    print(data.keys())
main()



#print(data['executionTime'])


## Tout le dossier législatif

#print(data['dossierLegislatif'].keys())

#for i in data['dossierLegislatif']:
#    print(i, " : ")
#    print(data['dossierLegislatif'][i], "\n")


##Dossier de loi

#print(data['dossierLegislatif']['dossiers'][1].keys())

#for j in data['dossierLegislatif']['dossiers'][1]:
#    print(j, " : ")
#    print(data['dossierLegislatif']['dossiers'][1][j], "\n")

## Exposé des motifs

#Expo_des_motifs = data['dossierLegislatif']['exposeMotif']
#Expo_des_motifs = BeautifulSoup(data['dossierLegislatif']['exposeMotif'], 'html.parser')

#Txt_propre = Expo_des_motifs.get_text()
