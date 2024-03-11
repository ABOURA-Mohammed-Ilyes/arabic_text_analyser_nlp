from concurrent.futures import ProcessPoolExecutor
from farasa.ner import FarasaNamedEntityRecognizer
import os
import json

def ner_word(content):
    named_entity_recognizer = FarasaNamedEntityRecognizer(interactive=True)
    ner_words_unknown = []

    for word in content:
        ner_word = named_entity_recognizer.recognize(word)
        if ner_word.endswith("/O"):
            ner_words_unknown.append(ner_word)
    named_entity_recognizer.terminate()    
    return ner_words_unknown

def load_data():
    json_path = os.path.join(os.path.dirname(__file__), 'unknown_words.json')
    with open(json_path, "r", encoding='utf-8') as j:
        data = json.load(j)
    return data

def chunk_data(data, size):
    return [data[i:i + size] for i in range(0, len(data), size)]

def main():
    data = load_data()
    chunks = chunk_data(data, len(data) // 20)  # Adjust the chunk size as necessary

    with ProcessPoolExecutor() as executor:
        results = executor.map(ner_word, chunks)

    ner_words_unknown = []
    for result in results:
        ner_words_unknown.extend(result)

    # Here you can do something with ner_words_unknown
    print(len(ner_words_unknown))
    with open("ner_words_unknown.json","w",encoding='utf-8') as j:
        json.dump(ner_words_unknown,j,ensure_ascii=False)

if __name__ == "__main__":
    main()
