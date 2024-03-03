from generateArabicWord import ArabicTextProcessor
from interface import Interface
import os
import json

json_path = os.path.join(os.path.dirname(__file__), 'data_train.json')
with open(json_path, "r", encoding='utf-8') as j:
    data = json.load(j)

""" SW_Path = os.path.join(os.path.dirname(__file__), 'arabic_sw.txt')
folder_path = os.path.join(os.path.dirname(__file__), 'Sports')
number_of_files = 6000
test = ArabicTextProcessor(folder_path, SW_Path,number_of_files)
test.processing() """




interface = Interface(data)
interface.show_interface()