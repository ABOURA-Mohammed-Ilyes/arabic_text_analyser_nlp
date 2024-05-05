# pip install qalsadi pip  install farasapy

from arramooz.arabicdictionary import ArabicDictionary
from farasa.stemmer import FarasaStemmer
import os
import json
import qalsadi.lemmatizer 
import re


class ArabicTextAnalyzer:
    def __init__(self, trainingData):
        self.trainingData = trainingData

    
    def noArabicWordsFilter(self, data):
        arabicPattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
        arabicWord = [word for word, _ in data.items() if arabicPattern.fullmatch(word)]
        return arabicWord


    def stemFilter(self, data):
        stemmerInteractive = FarasaStemmer(interactive=True)
        unknownWords = []
        for word in data:
            stemmedWord = stemmerInteractive.stem(word)
            if stemmedWord == word:
                unknownWords.append(word)
        stemmerInteractive.terminate()
        return unknownWords


    def dictionnaryFilter(self, data):
        
        verbs = ArabicDictionary("verbs")
        nouns = ArabicDictionary("nouns")
        unknownWords = []

        for word in data:
            verbsList = verbs.lookup(word)
            nounsList = nouns.lookup(word)

            if len(verbsList)==0 and len(nounsList)==0:
                unknownWords.append(word)

        return unknownWords   


    def wordTypeFilter(self, data):
        lemmer = qalsadi.lemmatizer.Lemmatizer()
        lemmas = [lemmer.lemmatize(i, return_pos=True) for i in data] 
        unknowWords = []

        for word, pos in lemmas:
            if pos == 'all':
                unknowWords.append(word)

        return unknowWords


    def Analyze(self):
        print("------------------------------------")
        print("Start Analyzing")
        trainingData = self.noArabicWordsFilter(self.trainingData)
        print("-> filtering none arabic words done")
        remainingUnknownWords = self.stemFilter(trainingData)
        print("-> stem filter done")
        remainingUnknownWords = self.dictionnaryFilter(remainingUnknownWords)
        print("-> dictionnary filter done")
        remainingUnknownWords = self.wordTypeFilter(remainingUnknownWords)
        print("-> word type filter done")

        with open("V2\\jsons\\unknownWords.json","w",encoding='utf-8') as j:
            json.dump(remainingUnknownWords, j, ensure_ascii=False)

        print("-> Remaining unknwon Words registered")