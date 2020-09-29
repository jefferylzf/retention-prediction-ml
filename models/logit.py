import sklearn
import pandas as pd


param = {'data-name':'churaned_dataset_0902'}
csv_file = pd.read_csv("../raw-data/%s".format(param['data-name']), header = 0)