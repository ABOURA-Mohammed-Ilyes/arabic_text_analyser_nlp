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
    # Get all file names in the folder

        all_files = [f for f in os.listdir(self.folder_path) if f.endswith('.txt')]
        # Randomly select the specified number of text files
        selected_files = random.sample(all_files, min(len(all_files), self.number_of_files))
        print(len(selected_files))
        # Loop through each selected file, read its content, and append to the combined_content variable
        for file_name in selected_files:
            file_path = os.path.join(self.folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Append the file content to the combined_content variable, separated by a space
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
        return self.combined_content.split(separation)

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
        self.combine_all_text_files()
        self.read_sw_file()
        self.distinct_words = self.get_words(self.combined_content)
        self.stop_words = self.get_words(self.sw_content,"\n")
        self.get_remove_number()
        self.get_rid_sw()
        self.distinct_words = [get_display(reshape(word)) for word in self.distinct_words]

SW_Path = "C:/Users/meriem/Documents/vs/tp_m1/nlp/arabic_text_analyser_nlp/list.txt"
folder_path = os.path.join(os.path.dirname(__file__), 'Sports')
number_of_files = 2
test = ArabicTextProcessor(folder_path, SW_Path,number_of_files)
test.processing()
print(test.distinct_words)
print(len(test.distinct_words))