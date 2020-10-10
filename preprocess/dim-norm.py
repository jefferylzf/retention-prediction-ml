import pandas as pd

df = pd.read_csv(("../raw-data/{}").format('merged_users_0902.csv'), header = 0)

df = df.drop(['Unnamed: 0', 'gaid', 'country'], axis=1)

df.to_csv(('../inter-data/{}').format('data.csv'))
print('finally')