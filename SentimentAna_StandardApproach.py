# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:49:48 2019

@author: Ankit
"""

import spacy
import pandas as pd 
import re
import numpy as np

#load the affin dataset in dictionary
Affin_wordlist = {}
temp = [Affin_wordlist.update({line.split('\t')[0].strip():int(line.split('\t')[1].strip())}) for line in open("AFINN-111.txt")]

nlp = spacy.load("en_core_web_sm")
text = "problems are hard "
doc = nlp(text)
polarity_score = polarity_compuation(doc)
polarity = ComputePolarity(doc)

def polarity_compuation(doc):
    polarity = 0
    negation_flag = 1
    intensifier = 1
    for token in doc:
        temp_polarity = 0
        if token.text.lower() in ['not','Not','NOT']:
            negation_flag = -1
        if token.text.lower() in ['very','really','extremely']:
            intensifier = 1.5
        if token.text.lower() in Affin_wordlist:
            #print(token.lemma_)
            temp_polarity = Affin_wordlist[token.lemma_]
            temp_polarity = temp_polarity * negation_flag
            temp_polarity = temp_polarity * intensifier
            negation_flag = 1
            intensifier = 1
        polarity = polarity + temp_polarity
    return polarity


