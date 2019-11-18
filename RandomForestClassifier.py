from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import csv

# Reading feature_vector.csv
readlist = []
with open("feature_vector.csv",'r') as myfile:
    reader = csv.reader(myfile,delimiter=' ')
    readlist = list(reader)

X = [list(map(float,lst)) for lst in readlist]

# Reading label_vector.csv
readlist.clear()
with open("label_vector.csv", 'r') as myfile:
    reader = csv.reader(myfile, delimiter=' ')
    readlist = list(reader)

ylist = [list(map(int,lst)) for lst in readlist]
y = [j for sub in ylist for j in sub]

# Training and Testing the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
clf = RandomForestClassifier(n_estimators=110, min_samples_leaf=1, min_samples_split=2)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
