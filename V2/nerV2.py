from concurrent.futures import ProcessPoolExecutor
from farasa.ner import FarasaNamedEntityRecognizer
import os
import json

def nerWord(content):
    namedEntityRecognizer = FarasaNamedEntityRecognizer(interactive=True)
    unkownWordsAfterNer = []

    for word in content:
        nerWord = namedEntityRecognizer.recognize(word)
        if nerWord.endswith("/O"):
            unkownWordsAfterNer.append(nerWord)
    namedEntityRecognizer.terminate()    
    return unkownWordsAfterNer

def loadData():
    jsonPath = os.path.join(os.path.dirname(__file__), 'jsons\\unknownWords.json')
    with open(jsonPath, "r", encoding='utf-8') as j:
        data = json.load(j)
    return data

def chunkData(data, size):
    return [data[i:i + size] for i in range(0, len(data), size)]

def main():
    data = loadData()
    chunks = chunkData(data, len(data) // 10)  # Adjust the chunk size as necessary ( number of threads )

    with ProcessPoolExecutor() as executor:
        results = executor.map(nerWord, chunks)

    unkownWordsAfterNer = []
    for result in results:
        unkownWordsAfterNer.extend(result)

    unkownWordsAfterNer = [word.replace('/', '') for word in unkownWordsAfterNer]
    unkownWordsAfterNer = [word.replace('O', '') for word in unkownWordsAfterNer]
    
    # Here you can do something with ner_words_unknown
    with open("V2\\jsons\\unknownWords.json","w",encoding='utf-8') as j:
        json.dump(unkownWordsAfterNer, j, ensure_ascii=False)

if __name__ == "__main__":
    main()
