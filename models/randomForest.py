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

df=pd.read_csv("../train-data/merged_72h_global_0902_raw.csv")

testdf = pd.read_csv("../train-data/merged_global_0903_raw.csv")
x = df.iloc[:,0:-1].values
y = df.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

rf=RandomForestClassifier(max_depth=20, min_samples_leaf=18, n_estimators=200,
                       random_state =0)
rf.fit(X_train,y_train)

from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

x_0903 = testdf.iloc[:,0:-1].values
y_0903 = testdf.iloc[:,-1].values

y_pred = rf.predict(x_0903)
target_names = ['retain', 'churn']

print(classification_report(y_0903, y_pred, target_names=target_names))

# print('f1 score:')
# print(f1_score(y_test, y_pred, average='macro'))
#
# print('accuracy:')
# print(rf.score(X_test, y_test))

importances = rf.feature_importances_
std = np.std([tree.feature_importances_ for tree in rf.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]
feature_name = ['level_cnt','ads_cnt','pvp_cnt','pvp_won_cnt','gem_spend','coin_spend',
                'gem_earn',	'ads_reward_cnt',	'org_hero_cnt', 'level_e_try_cnt',
                'level_e_cnt','idle_cnt',	'purchase_times',	'login_cnt',	'level_h_cnt',
                'log_num',	'd1_duration',	'd2_duration',	'd3_duration',	'willpay',	'daily_task_cnt',
                'pvp-unlock',	'hunt-unlock',	'exp-unlock']
# Print the feature ranking
# print("Feature ranking:")
#
# for f in range(X_train.shape[1]):
#     print("%d. feature %s (%f)" % (f + 1, indices[f], importances[indices[f]]))

# Plot the impurity-based feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X_train.shape[1]), importances[indices],
        color="r", yerr=std[indices], align="center")
plt.xticks(range(X_train.shape[1]), indices)
plt.xlim([-1, X_train.shape[1]])
plt.show()