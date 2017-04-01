from keras.layers import LSTM, Activation
from keras.models import Sequential
from keras.optimizers import RMSprop
import numpy as np


model = Sequential()
# 1 output, 2 timesteps, 1 component per timestep
model.add(LSTM(2, input_shape=(2, 1)))
model.add(Activation('softmax'))


optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


X = np.zeros((1, 2, 1))
X[0, 0, 0] = 1
X[0, 1, 0] = 0
model.fit(X, np.matrix([[1.0, 0.0]]), nb_epoch=20)


print(model.predict(X))