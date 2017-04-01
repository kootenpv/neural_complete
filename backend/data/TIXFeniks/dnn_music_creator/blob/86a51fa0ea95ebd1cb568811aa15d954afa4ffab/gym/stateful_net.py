from keras.layers import Dense, Activation
from keras.layers import LSTM, TimeDistributed
from keras.models import Sequential
from keras.optimizers import RMSprop




def get_st_model():
    print('Build model...')
    model = Sequential()
    model.add(LSTM(512, batch_input_shape=(1, 1, 29), return_sequences=True, stateful=True))
    model.add(LSTM(512, stateful=True))
    model.add(Dense(29))
    print (29)
    model.add(Activation('softmax'))




    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)


    model.load_weights('text_model_saved.h5py')


    return model