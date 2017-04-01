from keras.layers import Dense
from keras.layers import Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential




def create():
    model = Sequential()


    model.add(LSTM(10, input_dim=6))
    model.add(Dropout(0.25))
    model.add(Dense(1))


    model.compile(loss='msle', optimizer='rmsprop')


    return model