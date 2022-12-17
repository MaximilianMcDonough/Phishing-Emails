#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import VotingClassifier
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
    
    '''
    treeModel = tree.DecisionTreeClassifier()
    treeModel.fit(atributes, outputClasses)
    
    ranForestModel = RandomForestClassifier(n_estimators=250)
    ranForestModel.fit(atributes, outputClasses)
    
    adiBoost = AdaBoostClassifier(n_estimators=500)
    adiBoost.fit(atributes, outputClasses)
    
    extraRandom = ExtraTreesClassifier()
    extraRandom.fit(atributes, outputClasses)
    
    
    treeResults = treeModel.predict(testAtributes)
    RanForestResults = ranForestModel.predict(testAtributes)
    adiBoostResults = adiBoost.predict(testAtributes)
    extraRandomResuts = extraRandom.predict(testAtributes)
    '''
    # creat the model
    model = CatBoostClassifier(iterations=3000,
                           learning_rate=1,
                           depth=3)
    # fit the model
    model.fit(atributes, outputClasses)
    
    # make predictions and makes the submition file
    predicitions = model.predict(testAtributes)
    fileName = '300.csv'
    submition(testIds, predicitions, fileName)
    
    
    '''
    for i in range(10):
        #trains model
        #model = makeExtraRanEnsamble(atributes, outputClasses, 5)
        model = RandomForestClassifier(n_estimators=250)
        model.fit(atributes, outputClasses)
        
        # gets predicitns
        predicitions = model.predict(testAtributes)
        
        # formats and writes submission file
        fileName = 'RandomForest' + str(i) + '.csv'
        submition(testIds, predicitions, fileName)
    '''


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
