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

def test_com_de_presse(data):
        
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
            


                


def main():
#    data = load_JSON_repo(directory)
#    print(data['JORFDOLE000017758144']['arborescence'])

#    xpo_motif = export_to_txt(data)

#    find_a_word(xpo_motif, "service")

#    nuage(xpo_motif)

    data = load_JSON_repo(directory)
    export_to_csv(data)


    



    

                
#    print(stock)
    
#    print(data.keys())
#    what_to_do(data)

#    print(len(str(export_to_txt(data))))

main()