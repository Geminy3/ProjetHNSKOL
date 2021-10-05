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
import spacy


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



## To load the full directory by titles
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



## To load the full directory by year
def JSON_to_JSON_year(directory):
    
    data = {}
    
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as read_file:
                temp = json.load(read_file)
                data[temp['dossierLegislatif']['id']] = temp['dossierLegislatif']
            continue
        else:
            continue

    i = 2007
    years = {}

    
    while i <= 2021:
        temp = {}
        for ids in data:
            if str(i) in data[ids]['titre']:
                temp[ids] = data[ids]
#                print(temp[ids].keys(), str(i))
            else:
                continue
        years[str(i)] = temp
        i = i + 1

#    print(years.keys())        
    return(years)


##To load the full directory by legislature
def JSON_to_JSON_Legis(directory):
    
##à faire : 
    #trier legis pour supprimer les redondances
    #Re-importer les fichiers JSON par legisislature : faire entre les dossiers dans leurs valeurs legislature respectives
    # Type : if legis[...] == data[titre][legislature] do: legis2 = legis2 + {data...} where legis2 est un dict ({})
    
    data = {}
        
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as read_file:
                temp = json.load(read_file)
                data[temp['dossierLegislatif']['id']] = temp['dossierLegislatif']
                continue
        else:
            continue

    legis = []

    for title in data:
        for i in legis:
            if legis[i] != [data[title]['legislature']['libelle']]:
                legis = legis + [data[title]['legislature']['libelle']]
            else:
                continue

    print(legis)
    return(legis)


##To Load data
def Load_JSON(directory):
    
    data = {}
    
    json = input("Choisissez un type d'importation du JSON parmi : " + '\n'
                 "[id] " + " [title] " + " [year] " + " [legislature] " + '\n')
    if json == 'id':
        data = load_JSON_repo(directory)
        what_to_do(data)
    elif json == 'title':
        data = load_JSON_title(directory)
        what_to_do(data)
    elif json == 'year':
        data = JSON_to_JSON_year(directory)
        what_to_do_sup(data)
#    elif json == 'legislature':
#        data = JSON_to_JSON_Legis(directory)
#        what_to_do_sup(data)
    else:
        print("Ce type d'importation n'existe pas, veuillez réesayer" + '\n')
        Load_JSON(directory)

    return(data)


#### Traitement des données

##Export de l'expo des motifs, avec l'ID du dossier legislatif
# Fonctionne à partir de repo / titles

        
def export_to_txt(data):

    Txt_propre = []    
    
    for xpo in data:
        Expo_des_motifs = BeautifulSoup(data[xpo]['exposeMotif'], 'html.parser')
        Txt_propre = Txt_propre + [data[xpo]['id'] + " : " + Expo_des_motifs.get_text() + '\n']
    
    with open("xpo_export.txt", "w", encoding='utf8') as f:
        for line in Txt_propre:
            f.write(line + "\n")
    
    return(Txt_propre)


def export_to_txt_year(data):
    
    Txt_propre = []
    
    for var in data:
        Txt_propre = Txt_propre + ["Lois" + var]
        for var2 in data[var]:
            Expo_des_motifs = BeautifulSoup(data[var][var2]['exposeMotif'], 'html.parser')
            Txt_propre = Txt_propre + [Expo_des_motifs.get_text() + '\n']
    
        
    with open("xpo_export_by_year.txt", "w", encoding='utf8') as f:
        for line in Txt_propre:
                f.write(line + "\n")
    print("printed")
    
    return(Txt_propre)



# Fonctionne à partir de texte donné en entré

#def grey_color(word, font_size, position, orientation, random_state=None, **kwargs):
#    return 'hsl(0, 0%%, %d%%)' % random.randint(50, 100)


##Nuage de mots, stopwords dans stopword.txt
def nuage_base(cor_pus):
    texte = ""
    texte = texte.join(xpo.rstrip('\n') + " " for xpo in cor_pus)

    stopwords2 = []
    
    f = open("stopword.txt", 'r', encoding="utf-8")
    for lines in f:
        stopwords2.append(lines.rstrip('\n'))

    from nltk.corpus import stopwords
    sw_french = stopwords.words("french")
    sw_french = sw_french + stopwords2


    limit = 50

    fontcolor='#fa0000' # couleur des caractères
    bgcolor = '#000000' # couleur de fond

    
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
    
        
    plt.imshow(wordcloud.recolor(random_state=3))
    
    plt.axis('off')
    plt.show()



def nuage_plus(cor_pus, regex):

    stopwords2 = []
    
    f = open("stopword.txt", 'r', encoding="utf-8")
    for lines in f:
        stopwords2.append(lines.rstrip('\n'))

    from nltk.corpus import stopwords
    sw_french = stopwords.words("french")
    sw_french = sw_french + stopwords2

    limit = 50


    texte = ""    
    for word in cor_pus:
        texte = texte + word.rstrip('\n') + " "
    
    pattern = re.compile(regex, re.IGNORECASE)
    pos = pattern.finditer(texte)
    start_pattern = [m.start() for m in pos]

    
    n = 1
    
    for s in start_pattern:
        if n < len(start_pattern):
            strt = s
            end = len(texte) - (len(texte) - start_pattern[n])
            txt = texte[strt:end]
        else:
            strt = s
            end = len(texte)
            txt = texte[strt:end]

        fontcolor='#fa0000' # couleur des caractères
        bgcolor = '#000000' # couleur de fond
        wordcloud = WordCloud(
            max_words=limit,
            stopwords= sw_french, # liste de mots-outils
            #mask=imread('img/mask.png'),  # avec ou sans masque, à essayer ! (attention, nécessite un fichier de masque en noir et blanc)
            background_color=bgcolor,
            #    font_path=font   # si on veut changer la police de caractères
            ).generate(txt.lower()) # tolower() permet de mettre tout le texte en minuscule

        fig = plt.figure()
        plt.subplot(int(len(start_pattern)/2+1), 2, n)
        
        print(texte[strt:strt+len(regex)])
        n = n + 1

#        print(texte[strt:strt + 8])
## taille de la figure
        fig.set_figwidth(14)
        fig.set_figheight(18)
    
        plt.imshow(wordcloud.recolor(random_state=3))
    
        plt.axis('off')
        
        
    plt.show()
   


def find_a_word(corpus, word):
    
    texte = ""
    texte = texte.join(xpo.rstrip('\n') + " " for xpo in corpus)
    
    
    pattern = re.compile(word, re.IGNORECASE)
    res = pattern.finditer(texte)
    start_pattern = [m.start() for m in res]
    
    print("occurence de " + word + " : " + str(len(start_pattern)) + '\n')
    return(start_pattern)


def what_to_do(data):
    
    wtd = input("Que souhaitez vous faire avec ces données ? :" + '\n' +
                "[nuage] " + " [export] " + " [occurence]" + 
                " [back]"+ '\n')
    if wtd == 'nuage':
        nuage_base(export_to_txt(data))
    elif wtd == 'export':
        export_to_txt(data)
    elif wtd == 'occurence':
        word = input ("Quel mot cherchez-vous ? : " + '\n')
        find_a_word(export_to_txt(data), word)
    elif wtd== "back":
        Load_JSON(directory)
    else:
        print("Ce type d'opération n'existe pas, veuillez réesseayer : " + '\n')
        what_to_do(data)

def what_to_do_sup(data):
    
    wtd = input("Que souhaitez vous faire avec ces données ? :" + '\n' +
                "[nuage] " + " [export] " + " [occurence]" + 
                " [multi_nuage] " + " [back]" + '\n')
    if wtd == 'nuage':
        nuage_base(export_to_txt_year(data))
    elif wtd == 'multi_nuage':
        nuage_plus(export_to_txt_year(data), "Lois\d\d\d\d")
    elif wtd == 'export':
        export_to_txt_year(data)
    elif wtd == 'occurence':
        word = input ("Quel mot cherchez-vous ? : " + '\n')
        find_a_word(export_to_txt_year(data), word)
    elif wtd == "back":
        Load_JSON(directory)
    else:
        print("Ce type d'opération n'existe pas, veuillez réesseayer : " + '\n')
        what_to_do_sup(data)             

def test_spacy(txt):
    
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(txt)
    for token in doc:
        print(token.text, token.pos_, token.dep_)
    
    
    
#def main():
    
#    data = load_JSON_repo(directory)
 
#    years = JSON_to_JSON_year(directory)
    
#    print(data['JORFDOLE000017758144']['arborescence'])

#    xpo_motif = export_to_txt(data)

#    find_a_word(xpo_motif, "service")

#    nuage(xpo_motif)
  
#    print(data.keys())



## Exposé des motifs

#Expo_des_motifs = data['dossierLegislatif']['exposeMotif']
#Expo_des_motifs = BeautifulSoup(data['dossierLegislatif']['exposeMotif'], 'html.parser')

#Txt_propre = Expo_des_motifs.get_text()
