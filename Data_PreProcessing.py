# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:36:46 2019

@author: Ankit
"""

import pandas as pd
import re
import numpy as np

#load the affin dataset in dictionary
Affin_wordlist = {}
temp = [Affin_wordlist.update({line.split('\t')[0].strip():int(line.split('\t')[1].strip())}) for line in open("AFINN-111.txt")]

#import packages for dependency parsing
import spacy
nlp = spacy.load("en_core_web_sm")
text = "not like I am interested but I work on NLP"
doc = nlp(text)
polarity = ComputePolarity(doc)

#analyzing the chunks
for token in doc:
    print(token.text,token.dep_,token.head.text,token.pos_,token.is_stop,
          [child for child in token.children])
