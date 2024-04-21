
import os
from generateArabicWordV2 import ArabicTextProcessor

NUMBER_OF_FILES = 6000
stopWordsPath = os.path.join(os.path.dirname(__file__), 'arabicStopWords.txt')
folderPath = os.path.join(os.path.dirname(__file__), 'Sports')
arabicTextProcessor = ArabicTextProcessor(folderPath, stopWordsPath, NUMBER_OF_FILES)
arabicTextProcessor.processing()
