from generateArabicWord import ArabicTextProcessor
from evaluation import Evaluation
from interface import Interface
import os
import json


SW_Path = os.path.join(os.path.dirname(__file__), 'arabic_sw.txt')
folder_path = os.path.join(os.path.dirname(__file__), 'archive\\Sports')
number_of_files = 6000
test = ArabicTextProcessor(folder_path, SW_Path,number_of_files)
test.processing()

json_path = os.path.join(os.path.dirname(__file__), 'data_train.json')
with open(json_path, "r", encoding='utf-8') as j:
    data = json.load(j)

# interface = Interface(data)
# interface.show_interface()


json_path_test = os.path.join(os.path.dirname(__file__), 'data_test.json')
with open(json_path_test, "r", encoding='utf-8') as t:
    data_test = json.load(t)


ev = Evaluation(data,data_test)
ev.evaluate_accuracy()  

