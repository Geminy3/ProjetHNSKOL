#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:49:23 2021

@author: Aljoscha
"""
import os
import json
from bs4 import BeautifulSoup


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
    
def main():
    data = load_JSON_repo(directory)
#    print(data['JORFDOLE000022666926'].keys())
    
#    export_to_txt(data)
    print(data.keys())
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
