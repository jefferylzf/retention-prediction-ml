import numpy as np
import pandas as pd

param = {'input-data-name':'retained_0903.csv',
         'output-data-name':'retained_label_0903.csv',
         'bool_churn': 0
         }


csv_file = pd.read_csv(("../raw-data/0903/{}").format(param['input-data-name']), header = 0)
csv_file['pvp-unlock'] = 0
csv_file['hunt-unlock'] = 0
csv_file['exp-unlock'] = 0
csv_file['label'] = param['bool_churn']

for idx in range(len(csv_file)):
    lv = csv_file.loc[idx, 'level_cnt1'] + csv_file.loc[idx, 'level_cnt2'] + csv_file.loc[idx, 'level_cnt3']
    if lv >= 70:
        csv_file.loc[idx, 'pvp-unlock'] = 1
        csv_file.loc[idx, 'hunt-unlock'] = 1
        csv_file.loc[idx, 'exp-unlock'] = 1
    if lv >= 30:
        csv_file.loc[idx, 'hunt-unlock'] = 1
        csv_file.loc[idx, 'pvp-unlock'] = 1
    if lv >= 15:
        csv_file.loc[idx, 'hunt-unlock'] = 1

csv_file.to_csv(('../inter-data/0903/{}').format(param['output-data-name']))


print('finally')