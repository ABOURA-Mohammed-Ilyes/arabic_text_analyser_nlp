
import os
import json
from CountNextWords import CountNextWords
from generateArabicWordV2 import ArabicTextProcessor
from ArabicTextAnalyzer import ArabicTextAnalyzer
from interface import Interface
from evaluation import Evaluation


NUMBER_OF_FILES = 6000
NUMBER_OF_WORDS = 1
stopWordsPath = os.path.join(os.path.dirname(__file__), 'arabicStopWords.txt')
folderPath = os.path.join(os.path.dirname(__file__), 'Sports')
arabicTextProcessor = ArabicTextProcessor(folderPath, stopWordsPath, NUMBER_OF_FILES)
# arabicTextProcessor.processing()


distinctWordsPath = os.path.join(os.path.dirname(__file__), 'jsons\\dinstinctWords.json')
with open(distinctWordsPath, "r", encoding='utf-8') as j:
    distinctWords = json.load(j)


testDataPath = os.path.join(os.path.dirname(__file__), 'jsons\\testWords.json')
with open(testDataPath, "r", encoding='utf-8') as t:
    testData = json.load(t)


arabicTextAnalyzer = ArabicTextAnalyzer(distinctWords)
# arabicTextAnalyzer.Analyze()

#go to nerv2 and run it after analyze

unknownWordData = os.path.join(os.path.dirname(__file__), 'jsons\\unknownWords.json')
with open(unknownWordData, "r", encoding='utf-8') as t:
    unknownWordData = json.load(t)

allWordsData = os.path.join(os.path.dirname(__file__), 'jsons\\AllWords.json')
with open(allWordsData, "r", encoding='utf-8') as t:
    allWordsData = json.load(t)

countnextWords = CountNextWords(allWordsData, unknownWordData)
countnextWords.evolvedProcessNextWords(NUMBER_OF_WORDS)

filePath = f"jsons\\wordsCount_{NUMBER_OF_WORDS}.json"

trainingData = os.path.join(os.path.dirname(__file__), filePath)
with open(trainingData, "r", encoding='utf-8') as t:
    trainingData = json.load(t)

# interface = Interface(trainingData)
# interface.show_interface()


ev = Evaluation(trainingData, testData, NUMBER_OF_WORDS)
ev.evaluate_accuracy()