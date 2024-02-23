from arabic_reshaper import reshape
from bidi.algorithm import get_display

#first inqtall pip install arabic-reshaper ,pip install python-bidi

class ArabicTextProcessor:
    def __init__(self, text_path, SW_Path):
        self.text_path = text_path
        self.SW_Path = SW_Path
        self.text_content = ""
        self.sw_content = ""
        self.distinct_words = []
        self.stop_words = []

    def read_files(self):
        try:
            with open(self.text_path, 'r', encoding='utf-8') as file:
                self.text_content = file.read()
            with open(self.SW_Path, 'r', encoding='utf-8') as file:
                self.sw_content = file.read()
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred: ", e)

    
    def get_words(self,content,separation = " "):
        '''a function for splitting files to list'''
        return self.text_content.split(separation)

    def get_rid_sw(self):
        '''a function delete stop words'''
        for word in self.distinct_words : 
            if word in self.stop_words :
                self.distinct_words.remove(word)

    def get_remove_number(self):
        for word in self.distinct_words : 
            if word.isdigit() :
                self.distinct_words.remove(word) 

    def get_remove_parantheces(self):
        pass

    def processing(self):
        self.read_files()
        self.distinct_words = self.get_words(self.text_content)
        self.stop_words = self.get_words(self.sw_content,"\n")
        self.get_remove_number()
        self.get_rid_sw()
        self.distinct_words = [get_display(reshape(word)) for word in self.distinct_words]


text_path = "C:/Users/meriem/Documents/vs/tp_m1/nlp/Sports/0000.txt"
SW_Path = "C:/Users/meriem/Documents/vs/tp_m1/nlp/arabic_text_analyser_nlp/list.txt"
test = ArabicTextProcessor(text_path, SW_Path)
test.read_files()
test.processing()
print(test.distinct_words)