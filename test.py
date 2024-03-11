from arramooz.arabicdictionary import ArabicDictionary
from farasa.stemmer import FarasaStemmer
from farasa.ner import FarasaNamedEntityRecognizer
import os
import json
import qalsadi.lemmatizer 
import re


# import threading

# def ner_word_wrapper(content, results):
#     named_entity_recognizer_interactive = FarasaNamedEntityRecognizer()
#     ner_words_unknown = []
#     for word in content:
#         ner_word = named_entity_recognizer_interactive.recognize(word)
#         if "O" in ner_word:
#             ner_words_unknown.append(word)
#     named_entity_recognizer_interactive.terminate()
#     with results.lock:
#         results.value.extend(ner_words_unknown)


# chunksize = 100
# chunks = [unknown_words[i:i + chunksize] for i in range(0, len(unknown_words), chunksize)]

# results = threading.local()
# results.value = []
# threads = []
# for chunk in chunks:
#     thread = threading.Thread(target=ner_word_wrapper, args=(chunk, results))
#     thread.start()
#     threads.append(thread)

# for thread in threads:
#     thread.join()

# with open("unknown_words.json","w",encoding='utf-8') as j:
#     json.dump(unknown_words,j,ensure_ascii=False)        


from multiprocessing import Pool



def ner_word(content):
    print("hey")
    named_entity_recognizer_interactive = FarasaNamedEntityRecognizer()
    ner_words_unknown = []
    print("2")
    for word in content:
        print(word)
        ner_word = named_entity_recognizer_interactive.recognize(word)
        print(ner_word)
        if "O" in ner_word:
            ner_words_unknown.append(word)
    print("3")
    named_entity_recognizer_interactive.terminate()
    return ner_words_unknown



json_path = os.path.join(os.path.dirname(__file__), 'words_with_all.json')
with open(json_path, "r", encoding='utf-8') as j:
    data = json.load(j) 



def diviser_liste(liste, n):
    if n <= 0:
        raise ValueError("Le nombre de divisions doit être supérieur à 0")
    taille = len(liste)
    sous_listes = [[] for _ in range(n)]
    for i in range(taille):
        sous_listes[i % n].append(liste[i])
    return sous_listes



nombre_de_divisions = 4
listes_divisees = diviser_liste(data, nombre_de_divisions)
print(len(listes_divisees[0]))




with Pool(processes=1) as pool:
    results = pool.map(ner_word, listes_divisees)