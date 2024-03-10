import random

class Evaluation():


    def __init__(self, data_train,data_test):
        self.distinct_words = data_train
        self.test_words = data_test

    def evaluate_accuracy(self):

        '''a function to evaluate the accuracy of the model'''
        last_list = []
        test_words = self.test_words
        total_words = len(test_words)
        correct_predictions = 0
        last_list.append(test_words[0])
        for i in range(len(test_words) - 1):
            current_word = test_words[i]
            next_word_actual = test_words[i + 1]

  
            if current_word in self.distinct_words:
                predicted_next_words = list(self.distinct_words[current_word].keys())
                random_next_word = random.choice(predicted_next_words)
                last_list.append(random_next_word)
            else:
                random_next_word = None


            if random_next_word == next_word_actual:
                correct_predictions += 1

        accuracy = (correct_predictions / total_words) * 100
        print("original : ",self.test_words[:5])
        print('test : ',last_list[:5])
        print(f"Accuracy: {accuracy:.2f}%")
        

