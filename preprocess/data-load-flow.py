import numpy as np
import pandas as pd
date = '0904'
retain_param = {'input-data-name':('retained_{}.csv').format(date),
         'output-data-name':('retained_label_{}.csv').format(date),
         'bool_churn': 0
         }

churn_param = {'input-data-name':('churned_{}.csv').format(date),
         'output-data-name':('churned_label_{}.csv').format(date),
         'bool_churn': 1
         }

# Retain user data load and process
retain_df = pd.read_csv(("../raw-data/{0}/{1}").format(date, retain_param['input-data-name']), header = 0)
retain_df['pvp-unlock'] = 0
retain_df['hunt-unlock'] = 0
retain_df['exp-unlock'] = 0
retain_df['label'] = retain_param['bool_churn']

for idx in range(len(retain_df)):
    lv = retain_df.loc[idx, 'level_cnt1'] + retain_df.loc[idx, 'level_cnt2'] + retain_df.loc[idx, 'level_cnt3']
    if lv >= 70:
        retain_df.loc[idx, 'pvp-unlock'] = 1
        retain_df.loc[idx, 'hunt-unlock'] = 1
        retain_df.loc[idx, 'exp-unlock'] = 1
    if lv >= 30:
        retain_df.loc[idx, 'hunt-unlock'] = 1
        retain_df.loc[idx, 'pvp-unlock'] = 1
    if lv >= 15:
        retain_df.loc[idx, 'hunt-unlock'] = 1

# churn user data load and process
churn_df = pd.read_csv(("../raw-data/0903/{}").format(churn_param['input-data-name']), header = 0)
churn_df['pvp-unlock'] = 0
churn_df['hunt-unlock'] = 0
churn_df['exp-unlock'] = 0
churn_df['label'] = churn_param['bool_churn']

for idx in range(len(churn_df)):
    lv = churn_df.loc[idx, 'level_cnt1'] + churn_df.loc[idx, 'level_cnt2'] + churn_df.loc[idx, 'level_cnt3']
    if lv >= 70:
        churn_df.loc[idx, 'pvp-unlock'] = 1
        churn_df.loc[idx, 'hunt-unlock'] = 1
        churn_df.loc[idx, 'exp-unlock'] = 1
    if lv >= 30:
        churn_df.loc[idx, 'hunt-unlock'] = 1
        churn_df.loc[idx, 'pvp-unlock'] = 1
    if lv >= 15:
        churn_df.loc[idx, 'hunt-unlock'] = 1


res = pd.concat([churn_df,retain_df],axis=0,ignore_index=True)
res.replace(np.nan,0, inplace=True)
res.to_csv(('../train-data/merged_global_{}_raw.csv').format(date))

# csv_file.to_csv(('../inter-data/0903/{}').format(param['output-data-name']))
# csv_file.to_csv(('../inter-data/0903/{}').format(param['output-data-name']))

print('finally')
