#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:03:06 2021

@author: Aljoscha
"""

from Loading_Json import * 
import re
import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

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
            

def top_feats(row, features, top_n=25):
    ''' Get top n tfidf values in row and return them with their corresponding feature names.'''
    topn_ids = np.argsort(row)[::-1][:top_n]
    top_feats = [(features[i], row[i]) for i in topn_ids if row[i]>0]
    df = pd.DataFrame(top_feats)
    if len(top_feats) > 0:
        df.columns = ['feature', 'score']
    print(df)
#    print(pd.crosstab(df.feature, df.score))
#    plt = df.plot.barh(x='feature',rot=0, color="green")
    return(df)

def top_feats_in_doc(Xtr, features, row_id, top_n=25):
    ''' Top features in specific document (matrix row) '''
    row = np.squeeze(Xtr[row_id].toarray())
    return top_feats(row, features, top_n)

       
      


def main():
#    data = load_JSON_repo(directory)
#    print(data['JORFDOLE000017758144']['arborescence'])

#    xpo_motif = export_to_txt(data)

#    find_a_word(xpo_motif, "service")

#    nuage(xpo_motif)

##### Load les datas depuis les dossiers

#    data_id = load_JSON_repo(directory)
#    df = to_df(data_id)
#    df.to_excel("export_excel.xlsx")

##### Load les datas à partir du fichier excel

    df = pd.read_excel("export_excel.xlsx", index_col='id')
#    del df["Unnamed: 0"]
#    df.to_excel("export_excel.xlsx")

#    df.year.value_counts().plot.bar()
#    df_xpo = df.dropna(subset = ["Exposé des motifs"])
#    df_xpo.year.value_counts().plot.bar()


#### Print le graph des années + %

#    temp = df.groupby('year').titre.count()
#    temp2 = df.groupby(['year'])["Exposé des motifs"].count()
#    
#    temp = pd.concat([temp, temp2], axis=1)
#    temp.columns = ['nb_loi', "nb_xpo"]
#    temp3 = temp.nb_xpo / temp.nb_loi * 100
#    temp = pd.concat([temp, temp3], axis = 1)
#    print(temp)
    
#    plt.plot(temp)


##### Voir les lois sans xpo

    df_na = df.loc[df["Exposé des motifs"].isna()]
    titre_na = []
    for titre in df_na.titre:
        titre = re.sub("\d*", "", titre)
        titre_na.append(titre)
        
    stopwords = []
    with open("./stopword.txt", 'r', encoding="utf-8") as f:
        for word in f.readlines():
            stopwords.append(word.rstrip('\n').lower())

    with open("./Stop-words-french.txt", 'r', encoding="utf-8") as f:
        for word in f.readlines():
            stopwords.append(word.rstrip('\n').lower())


    
    stopwords = stopwords + ["relative", "relatives", "tendant", "visant", 
                             "rectificative",'diverses', 'er']
    stopwords = set(stopwords)

    vectorizer = CountVectorizer(stop_words = stopwords, max_features=50)
    vectorizer.fit(titre_na)
#    print(vectorizer.get_feature_names())
    
    X = vectorizer.transform(titre_na).toarray()
    features = vectorizer.get_feature_names()
#    print(X.toarray())
    

    n_docs, n_terms = X.shape

    tf_sum = np.sum(X, axis=0)
    top_feats(tf_sum, features, 30)
    
    
    
#    print(stock)
    
#    print(data.keys())
#    what_to_do(data)

#    print(len(str(export_to_txt(data))))

main()


#data= load_JSON_title(directory)
#print(data['LOI n° 2010-1657 du 29 décembre 2010 de finances pour 2011']['arborescence'])