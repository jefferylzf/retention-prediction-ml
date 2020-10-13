import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# param
model_name = 'MLP-fulltrain'
df=pd.read_csv("../train-data/withNewFeatures/merged_02-08.csv")

x = df.iloc[:,4:-1].values
y = df.iloc[:,-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.05, random_state = 0)

# standardize
sc_x = StandardScaler()
xtrain = sc_x.fit_transform(x_train)
xtest = sc_x.transform(x_test)

y_train = keras.utils.to_categorical(y_train, 2)
y_test = keras.utils.to_categorical(y_test, 2)

model = Sequential()

model.add(Dense(512, input_shape=(len(xtrain[0]),))) # 全连接层

model.add(Activation('relu')) # ReLU

model.add(Dropout(0.2)) # Dropout

model.add(Dense(256)) # 全连接层

model.add(Activation('relu')) # ReLU

model.add(Dropout(0.2)) # Dropout

model.add(Dense(73)) # 全连接层

model.add(Activation('relu')) # ReLU

model.add(Dropout(0.2)) # Dropout

model.add(Dense(2)) # 分类层

model.add(Activation('softmax')) # Softmax

model.summary() # 打印模型

model.compile(loss='categorical_crossentropy',

              optimizer=RMSprop(),

              metrics=['accuracy'])

history = model.fit(xtrain, y_train, batch_size=100, validation_data=(xtest, y_test), epochs=20, verbose=1)

model.save('./models_file/{}'.format(model_name))
from sklearn.metrics import classification_report
import numpy as np
y_pred = model.predict(xtest, batch_size=64, verbose=1)
y_pred_bool = np.argmax(y_pred, axis=1)
y_test_bool = np.argmax(y_test, axis = 1)
print(classification_report(y_test_bool, y_pred_bool))