import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
from subprocess import call
from IPython.display import Image
from sklearn.metrics import roc_curve, roc_auc_score, auc
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

from joblib import load
df=pd.read_csv("../train-data/withNewFeatures/merged_27-28.csv")
rf = load('./models_file/randomforest-fulltrain.joblib')

x_new = df.iloc[:,2:-1].values
y_new = df.iloc[:,-1].values
y_newpred = rf.predict(x_new)
target_names = ['retain', 'churn']

print('----------test for another---------')
print(classification_report(y_new, y_newpred, target_names=target_names))