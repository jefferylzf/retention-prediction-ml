import pandas as pd

df1 = pd.read_csv("../train-data/withNewFeatures/merged_global_0927_clear.csv")
df2 = pd.read_csv("../train-data/withNewFeatures/merged_global_0928_clear.csv")
df3 = pd.read_csv("../train-data/withNewFeatures/merged_global_0904_raw.csv")
df4 = pd.read_csv("../train-data/withNewFeatures/merged_global_0905_raw.csv")
df5 = pd.read_csv("../train-data/withNewFeatures/merged_global_0906_raw.csv")
df6 = pd.read_csv("../train-data/withNewFeatures/merged_global_0907_raw.csv")
df7 = pd.read_csv("../train-data/withNewFeatures/merged_global_0908_raw.csv")

res = pd.concat([df1,df2], axis=0, ignore_index=False)
res.drop(res.columns[0],axis=1,inplace=True)
res.to_csv("../train-data/withNewFeatures/merged_27-28.csv")