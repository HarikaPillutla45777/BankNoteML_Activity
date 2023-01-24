# -*- coding: utf-8 -*-
"""BankNote.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WLVRKyRDE2XrbjCw2p_TGxeH775bwPw8
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

df=pd.read_csv("BankNoteML/BankNote_Authentication.csv")

df.shape

df.head()

df.tail()

df.dtypes

X=df.iloc[:,:-1]
y=df.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

classifier = DecisionTreeClassifier()
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)

score

pickle_out = open("BankNote.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

classifier.predict([[3.6216,8.6661,-2.8073,-0.44699]])

