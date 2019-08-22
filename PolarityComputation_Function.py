# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:35:28 2019

@author: Ankit
"""

def ComputePolarity(text):
    polarity = 0
    for token in doc:
        negation_multiplier = 1
        temp_polarity = 0
        if token.pos_ =="NOUN" or token.pos_ =="PROPN":
            if token.text.lower() in Affin_wordlist:
                temp_polarity = Affin_wordlist[token.text.lower()]
            for child in token.children:
                if child.pos == "ADJ":
                    if child.text.lower() in Affin_wordlist:
                        temp_polarity = temp_polarity + Affin_wordlist[child.text.lower()]
                        for left_child in child.lefts:
                            if left_child.pos_ == "ADV" and left_child.dep_ =="neg":
                                temp_polarity = temp_polarity *-1
                            if left_child.pos_ == "ADV" and left_child.dep_ !="neg":
                                temp_polarity = temp_polarity*1.5
                if child.text in ['Not','not','NOT']:
                    negation_multiplier = -1
        if token.pos_ == "VERB":
            if token.is_stop == False:
                if token.text.lower() in Affin_wordlist:
                    temp_polarity = Affin_wordlist[token.text.lower()]
                for child in token.children:
                    if child.pos_ == "ADJ":
                        if child.text.lower() in Affin_wordlist:
                            temp_polarity = temp_polarity + Affin_wordlist[child.text.lower()]
                        for left_child in child.lefts:
                            if left_child.pos == "ADV" and left_child.dep_ == "neg":
                                temp_polarity = temp_polarity*-1
                            if left_child.pos == "ADV" and left_child.dep_ != "neg":
                                temp_polarity = temp_polarity * 1.5
                    
                    if child.pos == "ADV" and child.dep == "neg":
                        temp_polarity = temp_polarity*-1
                    if child.pos_ == "ADV" and child.dep_ != "neg":
                        if child.text.lower() in Affin_wordlist:
                            temp_polarity = temp_polarity + Affin_wordlist[child.text.lower()]
                            for left_child in child.lefts:
                                #if adverb is modifying an adverb - very beautifully painted
                                if left_child.pos_ == "ADV":
                                    temp_polarity = temp_polarity*1.5
                        if child.text.lower() not in Affin_wordlist:
                            temp_polarity = temp_polarity * 1.5
            if token.is_stop == True:
                for child in token.children:
                    if child.pos_ == "ADJ":
                        if child.text.lower() in Affin_wordlist:
                            temp_polarity = Affin_wordlist[child.text.lower()]
                        for left_child in child.lefts:
                            if left_child.pos_ =="ADV" and left_child.dep_ =="neg":
                                temp_polarity = temp_polarity*-1
                            if left_child.pos_ == "ADV" and left_child.dep_ !="neg":
                                temp_polarity = temp_polarity*1.5
                    if child.text in ['Not','not','NOT']:
                        negation_multiplier = -1
                        
        temp_polarity = negation_multiplier * temp_polarity
        polarity = polarity + temp_polarity
    return polarity
                                
                                
                                
                                
                            
                    
                            
                    