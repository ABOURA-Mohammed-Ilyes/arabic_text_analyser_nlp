import os
import random
import json
import re

class ArabicTextProcessor:
    def __init__(self, folderPath, stopWordsPath, NUMBER_OF_FILES):
        self.folderPath = folderPath
        self.stopWordsPath = stopWordsPath
        self.NUMBER_OF_FILES = NUMBER_OF_FILES
        # self.NUMBER_OF_WORDS = NUMBER_OF_WORDS
        self.combinedContent = "" #Contient tous les fichiers text pour le training séparé avec un " "
        self.remaingContent = "" #Contient tous les fichiers text pour le test séparé avec un " "
        self.stopWordsContent = "" 
        self.distinctWords = {} #Contient une liste de tous les mots pour faire le training
        self.testWords = [] #Contient une liste de tous les mots pour faire le test
        self.fileWords = [] #Une copie du tableau distinctWords en tableau au lieu d'une liste
        self.stopWords = []
        

    def combineAllTextFiles(self):
        '''a function that will combine all files randomly'''

        allFiles = [file for file in os.listdir(self.folderPath) if file.endswith('.txt')]
        selectedFiles = random.sample(allFiles, min(len(allFiles), self.NUMBER_OF_FILES))
        for fileName in selectedFiles:
            filePath = os.path.join(self.folderPath, fileName)
            with open(filePath, 'r', encoding='utf-8') as file:
                content = file.read()
                self.combinedContent += content + " "

        # Combine the remaining files
        remainingFiles = [file for file in allFiles if file not in selectedFiles]
        for fileName in remainingFiles:
            filePath = os.path.join(self.folderPath, fileName)
            with open(filePath, 'r', encoding='utf-8') as file:
                content = file.read()
                self.remaingContent += content + " "


    def readStopWordsFile(self):
        try:
            with open(self.stopWordsPath, 'r', encoding='utf-8') as file:
                self.stopWordsContent = file.read()
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred: ", e)


    def getTextToList(self, content, separation = " "):
        '''a function for splitting files to list'''
        return content.split(separation)


    def getTextToListV2(self, content, separators=" ,.\n"):
        return re.split(f"[{re.escape(separators)}]", content)


    def filterNotAlphaCharacters(self, content, dictionnary=True):
        """
        a function for Removing characters not alpha from each word in 'distinctWords'.
        """
        if dictionnary :
            filteredWords = {}
        else :
            filteredWords = []

        for word in content:
            filteredWord = ''.join([char for char in word if char.isalpha() and char != '_'])
            if dictionnary:
                filteredWords[filteredWord] = {}
            else :
                filteredWords.append(filteredWord)

        return filteredWords
    
    def filterNotAlphaCharactersV2(self, content, dictionnary=True):
        if dictionnary:
            filteredWords = {}
        else:
            filteredWords = []

        for word in content:
            # Keep only alphabetic characters, periods, and commas
            filteredWord = ''.join([char for char in word if (char.isalpha() and char!= '_') or char in {'.', ','}])
            if dictionnary:
                filteredWords[filteredWord] = {}
            else:
                filteredWords.append(filteredWord)

        return filteredWords
    

    def filterStopWordsAndVoid(self):
        '''a function delete stop words'''
        self.distinctWords = {word: {} for word in self.distinctWords if word not in self.stopWords}
        self.distinctWords = {word: {} for word in self.distinctWords if word != ''}
        self.fileWords = [word for word in self.fileWords if word not in self.stopWords]
        self.fileWords = [word for word in self.fileWords if word != '']
        self.testWords = [word for word in self.testWords if word not in self.stopWords]
        self.testWords = [word for word in self.testWords if word != '']

    def filterStopWordsAndVoidV2(self):
        '''a function delete stop words'''
        temp_stopWords = [word for word in self.stopWords if word not in {'.', ','}]
        self.distinctWords = {word: {} for word in self.distinctWords if word not in temp_stopWords}
        self.distinctWords = {word: {} for word in self.distinctWords if word != ''}
        self.fileWords = [word for word in self.fileWords if word not in temp_stopWords]
        self.fileWords = [word for word in self.fileWords if word != '']
        self.testWords = [word for word in self.testWords if word not in temp_stopWords]
        self.testWords = [word for word in self.testWords if word != '']



    def processNextWords(self):
        '''a function that find next words for every distinct words'''
        words = self.fileWords
        for i in range(len(words)):
            if i < len(words) - 1:
                nextCle = words[i + 1]
                if nextCle in self.distinctWords[words[i]]:
                    self.distinctWords[words[i]][nextCle] += 1
                else:
                    self.distinctWords[words[i]][nextCle] = 1

        for word, nextWords in self.distinctWords.items():
            sortedNextWords = sorted(nextWords.items(), key=lambda x: x[1], reverse=True)
            top3NextWords = sortedNextWords[:3]
            self.distinctWords[word] = dict(top3NextWords)


    def processing(self):
        '''function that process our model'''
        
        #read files
        self.combineAllTextFiles()
        self.readStopWordsFile()
        
        # make them a list
        # self.distinctWords = self.getTextToList(self.combinedContent)
        # self.testWords = self.getTextToList(self.remaingContent)
        # self.fileWords = self.getTextToList(self.combinedContent)
        # self.stopWords = self.getTextToList(self.stopWordsContent,"\n")

        self.distinctWords = self.getTextToListV2(self.combinedContent)
        self.testWords = self.getTextToListV2(self.remaingContent)
        self.fileWords = self.getTextToListV2(self.combinedContent)
        self.stopWords = self.getTextToListV2(self.stopWordsContent)
        
        print("###################################\nBefore processing : ", len(self.distinctWords), "\n###################################")

        #functions for filters 
        # self.distinctWords = self.filterNotAlphaCharacters(self.distinctWords)
        # self.fileWords = self.filterNotAlphaCharacters(self.fileWords, False)
        # self.testWords = self.filterNotAlphaCharacters(self.testWords, False)

        self.distinctWords = self.filterNotAlphaCharactersV2(self.distinctWords)
        self.fileWords = self.filterNotAlphaCharactersV2(self.fileWords, False)
        self.testWords = self.filterNotAlphaCharactersV2(self.testWords, False)

        # self.filterStopWordsAndVoid()

        self.filterNotAlphaCharactersV2()

        with open("V2\\jsons\\dinstinctWords.json","w",encoding='utf-8') as j:
            json.dump(self.distinctWords, j, ensure_ascii=False) 

        with open("V2\\jsons\\AllWords.json","w",encoding='utf-8') as j:
            json.dump(self.fileWords, j, ensure_ascii=False) 

        with open("V2\\jsons\\testWords.json","w",encoding='utf-8') as j:
            json.dump(self.testWords, j, ensure_ascii=False)

        print("After processing : ", len(self.distinctWords), "\n###################################")