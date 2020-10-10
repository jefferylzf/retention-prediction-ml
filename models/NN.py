import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("../raw-data/merged_d5-d7_global_0902_raw.csv")

x = df.iloc[:,0:-1].values
y = df.iloc[:,-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

# standardize
sc_x = StandardScaler()
xtrain = sc_x.fit_transform(x_train)
xtest = sc_x.transform(x_test)

y_train = keras.utils.to_categorical(y_train, 2)
y_test = keras.utils.to_categorical(y_test, 2)

model = Sequential()

model.add(Dense(580, input_shape=(len(xtrain[0]),))) # 全连接层

model.add(Activation('relu')) # ReLU

model.add(Dropout(0.2)) # Dropout

model.add(Dense(290)) # 全连接层

model.add(Activation('relu')) # ReLU

model.add(Dropout(0.2)) # Dropout

model.add(Dense(174)) # 全连接层

model.add(Activation('relu')) # ReLU

model.add(Dropout(0.2)) # Dropout

model.add(Dense(2)) # 分类层

model.add(Activation('softmax')) # Softmax

model.summary() # 打印模型

model.compile(loss='categorical_crossentropy',

              optimizer=RMSprop(),

              metrics=['accuracy'])

history = model.fit(xtrain, y_train, batch_size=100, validation_data=(xtest, y_test), epochs=40, verbose=1)