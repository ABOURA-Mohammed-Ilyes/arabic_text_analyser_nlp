
import os
import json
from generateArabicWordV2 import ArabicTextProcessor
from ArabicTextAnalyzer import ArabicTextAnalyzer
from interface import Interface
from evaluation import Evaluation


NUMBER_OF_FILES = 6000
NUMBER_OF_WORDS = 2
stopWordsPath = os.path.join(os.path.dirname(__file__), 'arabicStopWords.txt')
folderPath = os.path.join(os.path.dirname(__file__), 'Sports')
arabicTextProcessor = ArabicTextProcessor(folderPath, stopWordsPath, NUMBER_OF_FILES, NUMBER_OF_WORDS)
arabicTextProcessor.processing()


trainingDataPath = os.path.join(os.path.dirname(__file__), 'jsons\\dinstinctWords.json')
with open(trainingDataPath, "r", encoding='utf-8') as j:
    trainingData = json.load(j)


testDataPath = os.path.join(os.path.dirname(__file__), 'jsons\\testWords.json')
with open(testDataPath, "r", encoding='utf-8') as t:
    testData = json.load(t)


arabicTextAnalyzer = ArabicTextAnalyzer(trainingData)
#arabicTextAnalyzer.Analyze()

#go to nerv2 and run it after analyze

interface = Interface(trainingData)
#interface.show_interface()


ev = Evaluation(trainingData, testData, NUMBER_OF_WORDS)
ev.evaluate_accuracy()