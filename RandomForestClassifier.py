from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
import csv
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

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

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

fpr, tpr, thresholds = roc_curve(y_test, y_pred)
print("True Positive Rate: {0}".format(tpr))
print("False Positive Rate: {0}".format(fpr))
auc = roc_auc_score(y_test, y_pred)
print('AUC RF:%.3f' % auc)

plt.plot(fpr, tpr, 'b-', label='RandomForest AUC: %.3f' % auc)
plt.plot([0, 1], [0, 1], 'k-', label='random')
plt.plot([0, 0, 1, 1], [0, 1, 1, 1], 'g-', label='perfect')
plt.legend()
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
