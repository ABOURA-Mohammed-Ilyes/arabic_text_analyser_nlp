# from arabic_reshaper import reshape
# from bidi.algorithm import get_display
import os
import random
import json

#first inqtall pip install arabic-reshaper ,pip install python-bidi

class ArabicTextProcessor:
    def __init__(self, folder_path, SW_Path,number_of_files):
        self.folder_path = folder_path
        self.SW_Path = SW_Path
        self.number_of_files = number_of_files
        self.combined_content = ""
        self.sw_content = ""
        self.file_words = []
        self.distinct_words = {}
        self.stop_words = []
        

    #begin file precesiing
    def combine_all_text_files(self):
        '''a function that will combine all files randomly'''

        all_files = [f for f in os.listdir(self.folder_path) if f.endswith('.txt')]
        selected_files = random.sample(all_files, min(len(all_files), self.number_of_files))
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

    
    def get_text_to_list(self,content,separation = " "):
        '''a function for splitting files to list'''
        return content.split(separation)
    
    #end file precesiing

    #begin filters 

    def filter_sw(self):
        '''a function delete stop words'''
        self.distinct_words = {word: {} for word in self.distinct_words if word not in self.stop_words}
        self.file_words = [word for word in self.file_words if word not in self.stop_words]

    def filter_not_alpha_characters(self,content,dictionnary=True):
        """
        a function for Removing characters not alpha from each word in 'distinct_words'.
        """
        if dictionnary :
            filtered_words = {}
        else :
            filtered_words = []

        for word in content:
            # remove noalpha characters from the cvrrent word
            filtered_word = ''.join([char for char in word if char.isalpha() and char != '_'])
            if dictionnary:
                filtered_words[filtered_word] = {}
            else :
                filtered_words.append(filtered_word)

        return filtered_words
    
    def filter_void(self):
        self.distinct_words = {word: {} for word in self.distinct_words if word != ''}
        self.file_words = [word for word in self.file_words if word != '']

    #end filters  

    #begin next words processing       

    def process_next_words(self):
        '''a function that find next wrds for every distinct words'''
        words = self.file_words
        for i in range(len(words)):
            if i < len(words) - 1:
                next_cle = words[i + 1]
                if next_cle in self.distinct_words[words[i]]:
                    self.distinct_words[words[i]][next_cle] += 1
                else:
                    self.distinct_words[words[i]][next_cle] = 1

        for word, next_words in self.distinct_words.items():
           
            # x[1] is he value
            sorted_next_words = sorted(next_words.items(), key=lambda x: x[1], reverse=True)
            top_5_next_words = sorted_next_words[:3]
            self.distinct_words[word] = dict(top_5_next_words)            


    #end next words processing 
                                   
    def processing(self):
        '''function that process our model'''
        #read files
        self.combine_all_text_files()
        self.read_sw_file()
        # make them a list
        self.distinct_words = self.get_text_to_list(self.combined_content)
        self.file_words = self.get_text_to_list(self.combined_content)
        self.stop_words = self.get_text_to_list(self.sw_content,"\n")
        print(len(self.stop_words))
        print("Before processing : ",len(self.distinct_words))
        #functions for filters 
        self.distinct_words = self.filter_not_alpha_characters(self.distinct_words)
        self.file_words = self.filter_not_alpha_characters(self.file_words,False)
        self.filter_sw()
        self.filter_void()
        #next word processing
        self.process_next_words()

        # mirror the arabic words
        #self.distinct_words = {
        #     get_display(reshape(word)): {
        #         get_display(reshape(w)): v for w, v in value.items()
        #     } for word, value in self.distinct_words.items()
        # }

        #print result 
        #print("the matrixe : ",self.distinct_words)

        with open("data_train.json","w",encoding='utf-8') as j:
            json.dump(self.distinct_words,j,ensure_ascii=False) 

        print("After processing : ",len(self.distinct_words))


