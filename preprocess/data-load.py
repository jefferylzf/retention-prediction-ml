import numpy as np
import pandas as pd
churned_user = pd.read_csv("../raw-data/churned_dataset_0902.csv", header = 0)
churned_user['label'] = 0
churned_user.to_csv('../raw-data/churned_user_0902.csv')
print('finally')