from tensorflow import keras
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import classification_report
# param
test_model_name = 'MLP-fulltrain'
data_name = ''

# load model
test_mlp = keras.models.load_model('./models_file/{}'.format(test_model_name))

# load data
df=pd.read_csv("../train-data/withNewFeatures/merged_27-28.csv")

x = df.iloc[:,2:-1].values
y = df.iloc[:,-1].values

sc_x = StandardScaler()
x = sc_x.fit_transform(x)
# y = keras.utils.to_categorical(y, 2)

y_pred = test_mlp.predict(x, batch_size=100, verbose=1)
y_pred_bool = np.argmax(y_pred, axis=1)


print(classification_report(y, y_pred_bool))



