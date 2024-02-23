from arabic_reshaper import reshape
from bidi.algorithm import get_display
import os
import random

#first inqtall pip install arabic-reshaper ,pip install python-bidi

class ArabicTextProcessor:
    def __init__(self, folder_path, SW_Path,number_of_files):
        self.folder_path = folder_path
        self.SW_Path = SW_Path
        self.number_of_files = number_of_files
        self.combined_content = ""
        self.sw_content = ""
        self.distinct_words = []
        self.stop_words = []
        


    def combine_all_text_files(self):
        '''a function that will combine all files randomly'''

        all_files = [f for f in os.listdir(self.folder_path) if f.endswith('.txt')]
        selected_files = random.sample(all_files, min(len(all_files), self.number_of_files))
        print(len(selected_files))
        for file_name in selected_files:
            file_path = os.path.join(self.folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.combined_content += content + " "


    def read_sw_file(self):
        try:
            with open(self.SW_Path, 'r', encoding='utf-8') as file:
                self.sw_content = file.read()
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred: ", e)

    
    def get_words(self,content,separation = " "):
        '''a function for splitting files to list'''
        return content.split(separation)

    def get_rid_sw(self):
        '''a function delete stop words'''
        self.distinct_words = [word for word in self.distinct_words if word not in self.stop_words]

    def filter_words(self):
        """
        Remove characters in 'not_wanted' from each word in 'distinct_words'.
        
        :param distinct_words: List of words to be filtered.
        :param not_wanted: List of characters to remove from words in distinct_words.
        :return: A list of filtered words with not_wanted characters removed.
        """
        filtered_words = []
        for word in self.distinct_words:
            # Remove not_wanted characters from the current word
            filtered_word = ''.join([char for char in word if char.isalpha()])
            filtered_words.append(filtered_word)
        
        return filtered_words
    
    def filter_space(self):
        self.distinct_words = [word for word in self.distinct_words if word != '']
                    
    def processing(self):
        self.combine_all_text_files()
        self.read_sw_file()
        self.distinct_words = self.get_words(self.combined_content)
        print(len(self.distinct_words))
        self.stop_words = self.get_words(self.sw_content,"\n")
        self.get_rid_sw()
        self.distinct_words = self.filter_words()
        self.filter_space()
        self.distinct_words = [get_display(reshape(word)) for word in self.distinct_words]
        print(self.distinct_words)
        print(len(self.distinct_words))

SW_Path = "C:/Users/meriem/Documents/vs/tp_m1/nlp/arabic_text_analyser_nlp/list.txt"
folder_path = os.path.join(os.path.dirname(__file__), 'Sports')
number_of_files = 1
test = ArabicTextProcessor(folder_path, SW_Path,number_of_files)
test.processing()
