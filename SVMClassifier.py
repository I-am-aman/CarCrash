import csv
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt


with open("feature_vector.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter=' ')
    feature_vector = list(reader)

X = [list(map(float, lst)) for lst in feature_vector]

# Reading label_vector.csv
with open("label_vector.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter=' ')
    label_vector = list(reader)

y_temp_list = [list(map(int, lst)) for lst in label_vector]
y = [j for sub in y_temp_list for j in sub]

# Standardization
X_scaled = preprocessing.scale(X)

# Normalization
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)

# Training and Testing the model
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.20)

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Accuracy is {0}".format(accuracy_score(y_test, y_pred)))

fpr, tpr, thresholds = roc_curve(y_test, y_pred)
print("True Positive Rate: {0}".format(tpr))
print("False Positive Rate: {0}".format(fpr))
auc = roc_auc_score(y_test, y_pred)
print('AUC RF:%.3f' % auc)

plt.plot(fpr, tpr, 'r-', label='SVM AUC: %.3f' % auc)
plt.plot([0, 1], [0, 1], 'k-', label='random')
plt.plot([0, 0, 1, 1], [0, 1, 1, 1], 'g-', label='perfect')
plt.legend()
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
