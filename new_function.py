import os
import random
from nltk.corpus import stopwords
import nltk



def combine_all_text_files(folder_path, number_of_files):
    # Get all file names in the folder

    all_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    # Randomly select the specified number of text files
    selected_files = random.sample(all_files, min(len(all_files), number_of_files))
    
    # Initialize a variable to store the concatenated content
    combined_content = ""
    
    # Loop through each selected file, read its content, and append to the combined_content variable
    for file_name in selected_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Append the file content to the combined_content variable, separated by a space
            combined_content += content + " "
    
    return combined_content

# Example usage
folder_path = os.path.join(os.path.dirname(__file__), 'Sports')
number_of_files = 6000
# combined_content = combine_all_text_files(folder_path, number_of_files)


def filter_words(distinct_words, not_wanted):
    """
    Remove characters in 'not_wanted' from each word in 'distinct_words'.
    
    :param distinct_words: List of words to be filtered.
    :param not_wanted: List of characters to remove from words in distinct_words.
    :return: A list of filtered words with not_wanted characters removed.
    """
    # Filter each word in distinct_words
    filtered_words = []
    for word in distinct_words:
        # Remove not_wanted characters from the current word
        filtered_word = ''.join([char for char in word if char.isalpha()])
        filtered_words.append(filtered_word)
    
    return filtered_words

def merge_files(file_paths, output_path):
    unique_elements = set()

    # Parcourir chaque fichier
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Lire chaque ligne du fichier et ajouter les éléments uniques à l'ensemble
            for line in file:
                element = line.strip()
                if element not in unique_elements:
                    unique_elements.add(element)

    # Écrire les éléments uniques dans le fichier de sortie
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for element in unique_elements:
            output_file.write(element + '\n')

# Exemple d'utilisation
file_paths = ['arabic_stop_words.txt', 'arabicST.txt', 'list.txt']
output_path = 'arabic_sw.txt'
nltk.download('stopwords')
stop_words_arabic = stopwords.words('arabic')
# Afficher les premiers mots vides en arabe
print(len(stop_words_arabic))

    

# Example usage
distinct_words = ['hello.)3', 'world', 'example','(30)']
not_wanted = ['،', '.', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
filtered_words = filter_words(distinct_words, not_wanted)
print(filtered_words)


