from arramooz.arabicdictionary import ArabicDictionary
from farasa.stemmer import FarasaStemmer
import os
import json
import qalsadi.lemmatizer 
import re

# pip install qalsadi pip  install farasapy

json_path = os.path.join(os.path.dirname(__file__), 'data_train.json')
with open(json_path, "r", encoding='utf-8') as j:
    data = json.load(j)



def filter_no_arabic(content):
    # Expression régulière pour les caractères arabes
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')


    mots_arabes = [word for word,v in content.items() if arabic_pattern.fullmatch(word)]

    return mots_arabes

def dict_test(content):
    
  verbs_dict = ArabicDictionary("verbs")
  nouns_dict = ArabicDictionary("nouns")
  unknown_words = []

  for word in content:
      verbs_list = verbs_dict.lookup(word)
      nouns_list = nouns_dict.lookup(word)

      if len(verbs_list)==0 and len(nouns_list)==0:
          unknown_words.append(word)

  return unknown_words       

def stem_word(content):
    stemmer_interactive = FarasaStemmer(interactive=True)
    stemmed_words_unknown = []

    for word in content:
        stemmed_word = stemmer_interactive.stem(word)
        if stemmed_word == word:
            stemmed_words_unknown.append(word)
    stemmer_interactive.terminate()    
    return stemmed_words_unknown

def type_word(content):
    lemmer = qalsadi.lemmatizer.Lemmatizer()
    lemmas = [lemmer.lemmatize(i, return_pos=True) for i in content ] 
    words_with_all = []

    for word, pos in lemmas:
        if pos == 'all':
            words_with_all.append(word)

    return words_with_all        

           

# Supprimer les mots qui ne sont pas en arabe
data = filter_no_arabic(data) 
stemmed_words_unknown = stem_word(data)
unknown_words = dict_test(stemmed_words_unknown)
words_with_all = type_word(unknown_words)

with open("unknown_words.json","w",encoding='utf-8') as j:
    json.dump(words_with_all,j,ensure_ascii=False)

   
# print(words_with_all)
print(len(stemmed_words_unknown))
print(len(unknown_words))
print(len(words_with_all))

    


