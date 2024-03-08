from arramooz.arabicdictionary import ArabicDictionary
from farasa.stemmer import FarasaStemmer
from farasa.ner import FarasaNamedEntityRecognizer
import os
import json


json_path = os.path.join(os.path.dirname(__file__), 'data_train.json')
with open(json_path, "r", encoding='utf-8') as j:
    data = json.load(j)

def dict_test(content):
    
  verbs_dict = ArabicDictionary("verbs")
  nouns_dict = ArabicDictionary("nouns")
  unknown_words = []

  for word in content:
      verbs_list = verbs_dict.lookup(word)
      nouns_list = nouns_dict.lookup(word)

      if len(verbs_list)==0 and len(nouns_list)==0:
          unknown_words.append(word)

      # else:
      #   if verbs_list:
      #       for word_tuple in verbs_list:
      #           word_info = dict(word_tuple)
      #           print(f"Root (verb): {word_info['root']}")
      #   if nouns_list:
      #       for word_tuple in nouns_list:
      #           word_info = dict(word_tuple)
      #           print(f"Root (noun): {word_info['root']}")    

  return unknown_words       

def stem_word(content):
    stemmer_interactive = FarasaStemmer(interactive=True)
    stemmed_words_unknown = []

    for word, k in content.items():
        stemmed_word = stemmer_interactive.stem(word)
        if stemmed_word == word:
            stemmed_words_unknown.append(word)
    return stemmed_words_unknown


def ner_word(content):
    named_entity_recognizer_interactive = FarasaNamedEntityRecognizer(interactive=True)
    ner_words_unknown = []

    for word in content:
        print(word)
        ner_word = named_entity_recognizer_interactive.recognize(word)
        if "O" in ner_word:
            ner_words_unknown.append(word)
    return ner_words_unknown

           

stemmed_words_unknown = stem_word(data)
unknown_words = dict_test(stemmed_words_unknown)
# ner_words_unknown = ner_word(unknown_words)
# print(ner_words_unknown)
print(unknown_words)
print(len(stemmed_words_unknown))
print(len(unknown_words))

# print(len(ner_words_unknown))
            