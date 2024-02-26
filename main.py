from generateArabicWord import ArabicTextProcessor
import os

""" SW_Path = os.path.join(os.path.dirname(__file__), 'arabic_sw.txt')
folder_path = os.path.join(os.path.dirname(__file__), 'Sports')
number_of_files = 6000
test = ArabicTextProcessor(folder_path, SW_Path,number_of_files)
test.processing() """


import json

# Ouvrir le fichier JSON en mode lecture
json_path = os.path.join(os.path.dirname(__file__), 'data_train.json')
with open(json_path, "r", encoding='utf-8') as j:
    # Charger le contenu JSON en tant que dictionnaire
    data = json.load(j)

value = "جولبيس"
# Maintenant, 'data' est un dictionnaire contenant le contenu du fichier JSON
print(data[value])
