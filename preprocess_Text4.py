# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 08:00:09 2020

@author: Novin
"""
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.stem import PorterStemmer 
from nltk.stem import WordNetLemmatizer 
import re


def cleanText(sen):
    #lowercase
    sen = sen.lower()
    #remove tag 
    sentence =  re.sub(r'<[^>]+>', ' ' , sen)
    # remove url from sentence
    sentence = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%|-)*\b', 
                                                              '', sen )
    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)
    return sentence


def preprocess(text):
	# NLTK sentence tockenizer
	a=float(1.2)
	if type(text)==type(a): return ''
	sen_tokens = sent_tokenize(text) 
	# text cleaning with map cleanText on sentences
	processSen = list(map(cleanText,sen_tokens))
	# NLTK word tockenizer 
	word_tokens = []
	for sen in processSen:
		word_tokens.extend(word_tokenize(sen))
	#NLTK english stopwords    
	stop_words = set(stopwords.words('english')) 
	# remove stopwords  
	processWords = [w.rstrip('\']').lstrip('[\'') for w in word_tokens if not w in stop_words] 
	return processWords





