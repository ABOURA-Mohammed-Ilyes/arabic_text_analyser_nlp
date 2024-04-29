import os
import random
import json

class CountNextWords:
    def __init__(self, allDistinctWords, unknownWords):
        # self.allDistinctWords = list(allDistinctWords.keys())
        self.allWords = allDistinctWords
        self.unknownWords = unknownWords
        self.countedWords = {}


    def evolvedProcessNextWords(self, NUMBER_OF_WORDS):
        allDistinctWords = self.allWords
        count = 0
        for i in range(len(allDistinctWords) - NUMBER_OF_WORDS):
            currentSequence = ' '.join(allDistinctWords[i:i+NUMBER_OF_WORDS])
            nextWord = allDistinctWords[i + NUMBER_OF_WORDS]
            if nextWord not in self.unknownWords:
                if currentSequence not in self.countedWords:
                    count += 1
                    self.countedWords[currentSequence] = {}

                if nextWord in self.countedWords[currentSequence]:
                    self.countedWords[currentSequence][nextWord] += 1
                else:
                    self.countedWords[currentSequence][nextWord] = 1

        print(f"#############################\nnumber of sequence of {NUMBER_OF_WORDS} is {count}\n")
        # Keeping only top 3 most frequent next words for each key
        for key, nextWords in self.countedWords.items():
            sortedNextWords = sorted(nextWords.items(), key=lambda x: x[1], reverse=True)
            topNextWords = sortedNextWords[:3]  # You can adjust the number of top words as needed
            self.countedWords[key] = dict(topNextWords)

        filePath = f"V2\\jsons\\wordsCount_{NUMBER_OF_WORDS}.json"
        with open(filePath,"w",encoding='utf-8') as j:
            json.dump(self.countedWords, j, ensure_ascii=False) 