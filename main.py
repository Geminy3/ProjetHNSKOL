#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:03:06 2021

@author: Aljoscha
"""

from Loading_Json import * 
import re
import time

directory = './LegifranceJSON'




def main():
#    data = load_JSON_repo(directory)
#    print(data['JORFDOLE000017758144']['arborescence'])

#    xpo_motif = export_to_txt(data)

#    find_a_word(xpo_motif, "service")

#    nuage(xpo_motif)

    data = load_JSON_repo(directory)

    i = 1

    with open("export_var.csv", 'w', encoding="utf-8") as f:
        f.writelines([str(i)+ ";" + "date" + ';' + "id" + ";" + "titre" + ';' + "legislature"
                      + ";" +  "exposé des motifs" + ';' +"Communiqué de presse" 
                      + ";" + "Catégorie" +'\n'])
        for var in data:
            date = (data[var]['dateCreation'] / 1000)
            date = time.ctime(date)
            xpo = BeautifulSoup(data[var]['exposeMotif'], 'html.parser')
            xpo = xpo.get_text() + '\n'
            f.writelines([str(i) + ";"+ str(date) + ";" 
                          + data[var]['id']+ ";"+ data[var]['titre'] + ";" 
                          + data[var]['legislature']['libelle'] + ";"+ xpo])
            i += 1
        
    temp2 = []
    
    for var in data:
        if data[var]['exposeMotif'] == "" | data[var]['exposeMotif'] != "[]":
            temp2 = temp2 + [data[var]['id']]
    

    
    temp = []
    
        
    
    for var in data:
        if data[var]['exposeMotif'] == "":
            data2 = data[var]['arborescence']['liens']
            for var2 in data2:
                for var3 in var2:
                    if "Communiqué de presse" in var2[var3]:
                        temp = temp + [data[var]['id'] + " : " + var2['lien'] + var2['libelle']]
    
#        for ids in temp:
#            if ids in data:
#                data2 = data[var]['arborescence']['liens']
#                for var2 in data2:
#                    for var3 in var2:
#                        if "Communiqué de presse" in var2[var3]:
#                            print(var2['lien'])
    
    temp = set(temp)
    
    temp3 = []
    
    for var in temp:
        if var in temp2:
            continue
        else:
            temp3 = temp3 + [var]
    
    print(len(temp))
    print(len(temp2))
    print(len(temp3))
            
                
#    print(stock)
    
#    print(data.keys())
#    what_to_do(data)

#    print(len(str(export_to_txt(data))))

main()