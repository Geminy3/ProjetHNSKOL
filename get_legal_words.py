#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:58:59 2021

@author: Aljoscha
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import re

url = "https://www.assemblee-nationale.fr/connaissance/lexique.asp#P21_51"

var = BeautifulSoup(urlopen(url), 'html.parser')
# = var.prettify()

legal_words = []

for div in var.find_all('div'):
    if div.get('class') == ['article-content-sub', 'fiche-synthese']:
        for td in div.find_all('td'):
            for a in td.find_all('a'):
#    if classe == ['article-content-sub', 'fiche-synthese']:
                if "\r\n\t\t\t\t\t" not in a.string : 
                    legal_words.append(a.string.lower())
                
    
#print(legal_words)

with open("stopword.txt", 'a', encoding="utf-8") as f:
    for word in legal_words:
        print(word)
        f.write(word + '\n')
        

