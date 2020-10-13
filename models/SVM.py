import sklearn
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

df=pd.read_csv("../train-data/withNewFeatures/merged_02-08.csv")

x = df.iloc[:,4:-1].values
y = df.iloc[:,-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5, random_state = 0)

# standardize
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

param_grid = {'C': [1e-3, 1e-2, 1e-1, 1, 10, 100, 1000], 'gamma': [0.001, 0.0001, 0.5]}
clf = sklearn.svm.SVC(kernel='rbf', probability=True)
grid_search = GridSearchCV(clf, param_grid, verbose=1)
clf.fit(x_train, y_train)
from sklearn.metrics import classification_report

print(clf.score(x_test, y_test))
y_pred = clf.predict(x_test)
target_names = ['retain', 'churn']
print(classification_report(y_test, y_pred, target_names=target_names))