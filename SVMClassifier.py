import pandas as pd
import numpy as np
import csv
import random
import matplotlib.pyplot as plt
from sklearn.metrics import  accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

with open("feature_vector.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter=' ')
    feature_vector = list(reader)

X = [list(map(float, lst)) for lst in feature_vector]
print(X)

with open("label_vector.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter=' ')
    label_vector = list(reader)

y_temp_list = [list(map(int, lst)) for lst in label_vector]
y = [j for sub in y_temp_list for j in sub]
print(y)

shuffle_vector = list(zip(X, y))
random.shuffle(shuffle_vector)
X, y = zip(*shuffle_vector)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Accuracy is {0}".format(accuracy_score(y_test, y_pred)))
