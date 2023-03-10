#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier

def main():
    # gets the training data
    trainingData = pd.read_csv('csc-350-fall-2022-final-project/Phishing_Legitimate_Training.csv')
    trainingData = np.array(trainingData)
    outputClasses, atributes = splitOutputClass(trainingData)
    
    # gets the kaggle submission data
    testingData = pd.read_csv('csc-350-fall-2022-final-project/Phishing_Legitimate_TestWithoutClass.csv')
    testingData = np.array(testingData)
    testIds = testingData[:, 0]
    testAtributes = testingData[:, 1:len(testingData)-1]
    
   
    
    # creat the model using catboost
    model = CatBoostClassifier(iterations=3000,
                           learning_rate=1,
                           depth=3)
    # fit the model
    model.fit(atributes, outputClasses)
    
    # make predictions and makes the submition file
    predicitions = model.predict(testAtributes)
    fileName = '300.csv'
    submition(testIds, predicitions, fileName)
    
    

    


# splits the data into the atributes and the output class
def splitOutputClass(data):
    outputclasses = data[:, len(data[0])-1]
    atributes = data[:, 1:len(data[0])-1]
    
    return (outputclasses, atributes)
    
# makes the extra random tree ensamble
def makeExtraRanEnsamble(atributes, outputClasses, numOfModels):
    voters = []
    for i in range(numOfModels):
        name = 'ert' + str(i)
        model = ExtraTreesClassifier()
        voters.append((name, model))
        
    ensamble = VotingClassifier(voters, voting='hard')
    ensamble.fit(atributes, outputClasses)
    return ensamble
    

# writes tha kaggle submition csv file
def submition(ids, results, fileName):
    s = 'id,CLASS_LABEL' + '\n'
    for i in range(len(results)):
        s += str(ids[i]) + ',' + str(int(results[i])) + '\n'
    
    file = open(fileName, 'w')
    file.write(s)
    file.close()
    
          


  
        
main()
