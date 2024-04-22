import random

class Evaluation():


    def __init__(self, trainingData, testData):
        self.trainingData = trainingData
        self.testData = testData

    def evaluate_accuracy(self):

        '''a function to evaluate the accuracy of the model'''
        lastList = []
        testWords = self.testData
        comparisonCount = 0
        correctPredictions = 0
        lastList.append(testWords[0])
        for i in range(len(testWords) - 1):
            currentWord = testWords[i]
            NextWord = testWords[i + 1]

  
            if currentWord in self.trainingData:
                predictedNextWords = list(self.trainingData[currentWord].keys())
                randomNextWord = random.choice(predictedNextWords)
                lastList.append(randomNextWord)
                comparisonCount+=1
            else:
                randomNextWord = None


            if NextWord == randomNextWord:
                correctPredictions += 1

        accuracy = (correctPredictions / comparisonCount) * 100
        # print("original : ",self.testData[:5])
        # print('test : ',lastList[:5])
        print(f"Accuracy: {accuracy:.2f}%")
        

