from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM


def get_model(props):
    return basic_model(props)


def basic_model(props):
    maxlen, chars = props['maxlen'], props['chars']
    model = Sequential()
    model.add(LSTM(512, return_sequences=True, input_shape=(maxlen, len(chars))))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(len(chars)))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    return model