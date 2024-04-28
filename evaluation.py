import random

class Evaluation():


    def __init__(self, data_train,data_test, NUMBER_OF_WORDS):
        self.distinct_words = data_train
        self.test_words = data_test
        self.NUMBER_OF_WORDS = NUMBER_OF_WORDS

    def evaluate_accuracy(self):

        '''a function to evaluate the accuracy of the model'''
        last_list = []
        test_words = self.test_words
        total_words = len(test_words)
        correct_predictions = 0
        last_list.append(test_words[0])
        for i in range(len(test_words) - self.NUMBER_OF_WORDS):
            currentKey = ' '.join(test_words[i:i+self.NUMBER_OF_WORDS])
            next_word_actual = test_words[i + self.NUMBER_OF_WORDS]

  
            if currentKey in self.distinct_words:
                predicted_next_words = list(self.distinct_words[currentKey].keys())
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
        

