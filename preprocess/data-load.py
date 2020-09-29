import numpy as np
import pandas as pd

param = {'input-data-name':'churned_dataset_0902.csv',
         'output-data-name':'churned_users_0902.csv',
         'bool_retained': 0
         }


csv_file = pd.read_csv(("../raw-data/{}").format(param['input-data-name']), header = 0)
csv_file['pvp-unlock'] = 0
csv_file['hunt-unlock'] = 0
csv_file['exp-unlock'] = 0
csv_file['label'] = param['bool_retained']

for idx in range(len(csv_file)):
    lv = csv_file.loc[idx, 'level_cnt']
    if lv >= 70:
        csv_file.loc[idx, 'pvp-unlock'] = 1
        csv_file.loc[idx, 'hunt-unlock'] = 1
        csv_file.loc[idx, 'exp-unlock'] = 1
    if lv >= 30:
        csv_file.loc[idx, 'hunt-unlock'] = 1
        csv_file.loc[idx, 'pvp-unlock'] = 1
    if lv >= 15:
        csv_file.loc[idx, 'hunt-unlock'] = 1

csv_file.to_csv(('../raw-data/{}').format(param['output-data-name']))


print('finally')