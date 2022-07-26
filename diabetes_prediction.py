# -*- coding: utf-8 -*-
"""Diabetes Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19amZgtG26SgWCN2EECVj3-IkOkeRkyuS

Importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis
PIMA Diabetes Dataset
"""

# loading the diabetes dataset to pandas Dataframe
diabetes_dataset= pd.read_csv('/content/diabetes.csv')

# printing the first 5 row of dataset
diabetes_dataset.head()

#number of rows and colums
diabetes_dataset.shape

#getting the statistical measure of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0--> Non-Diabetes
1--> Diabetes
"""

diabetes_dataset.groupby('Outcome').mean()

#seperating data and labels
X = diabetes_dataset.drop(columns = 'Outcome',axis=1)
Y = diabetes_dataset['Outcome']

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

"""Train Test Split"""

X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""Training the Model"""

classifier = svm.SVC(kernel ='linear')

#training the support vestor Machine Classifier
classifier.fit(X_train,Y_train)

"""Model Evaluation Accuracy Score"""

#accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('Accuracy score of the training data: ',training_data_accuracy)

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print('Accuracy score of the test data: ',test_data_accuracy)

"""Making Predictive System"""

input_data = (10,168,74,0,0,38,0.537,34)

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshaped)
print(std_data)
prediction = classifier.predict(std_data)
print(prediction)
if (prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

