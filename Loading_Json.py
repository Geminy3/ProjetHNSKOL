#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:49:23 2021

@author: Aljoscha
"""
import os
import json
from bs4 import BeautifulSoup


import os
directory = './LegifranceJSON'


data = {}

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename), 'r') as read_file:
            temp = json.load(read_file)
            data[temp['dossierLegislatif']['titre']] = temp
        continue
    else:
        continue

#with open("./LegifranceJSON/JORFDOLE000017758132.json", 'r') as read_file:
#    data = json.load(read_file)
    
    
print(len(data))
print(data.keys())

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
