import numpy as np 
import pandas as pd 
import pickle 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import svm #Import svm model
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import confusion_matrix

df = pd.read_csv("dataset/heartdis.csv")
df.head()
df.info()
x = df.drop('target',axis = 1) 
print(x)
y = df.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=109) # 70% training and 30% test
ml = svm.SVC(kernel='linear',probability=True) # Linear Kernel

ml.fit(x_train, y_train)

#Predict the response for test dataset
y_pred = ml.predict(x_test)

ml.score(x_test,y_test)

confusion_matrix(y_test,y_pred)
pickle_out = open("classifier.pkl", "wb") 
pickle.dump(ml, pickle_out) 
pickle_out.close()