#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:03:06 2021

@author: Aljoscha
"""

from Loading_Json import *

directory = './LegifranceJSON'

def main():
#    data = load_JSON_repo(directory)
#    print(data['JORFDOLE000017758144']['arborescence'])

#    xpo_motif = export_to_txt(data)

#    find_a_word(xpo_motif, "service")

#    nuage(xpo_motif)
  
#    print(data.keys())
    data = Load_JSON(directory)
    print(data.keys())
    what_to_do(data)

main()