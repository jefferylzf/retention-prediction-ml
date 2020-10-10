from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.datasets.samples_generator import make_blobs
import pandas as pd
from sklearn.svm import SVC

# '''创建训练的数据集'''
datatarget = pd.read_csv("../raw-data/merged_d5-d7_global_0902_raw.csv")

X = datatarget.iloc[:, 0:-1].values
y = datatarget.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# '''模型融合中使用到的各个单模型'''
estimators = [
    ('RF', RandomForestClassifier(max_depth=20, min_samples_leaf=5, n_estimators=200,
                       random_state =0)),
    ('GB', GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_features=2, max_depth=2, random_state=0)),
    ('SVM',SVC(kernel='rbf', C=1, gamma=0.5, probability=True))]

from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
clf = StackingClassifier(
   estimators=estimators, final_estimator=LogisticRegression())

print(clf.fit(X_train, y_train).score(X_test, y_test))

