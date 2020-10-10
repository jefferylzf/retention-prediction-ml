import numpy as np
import pandas as pd

churn_file = pd.read_csv('../inter-data/0903/churned_label_0903.csv', header = 0)
retain_file = pd.read_csv('../inter-data/0903/retained_label_0903.csv', header = 0)


res = pd.concat([churn_file,retain_file],axis=0,ignore_index=True)
res.to_csv('../train-data/merged_global_0903_raw.csv')

print('finally')