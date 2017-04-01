# build the model: a single LSTM
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.models import Sequential
from keras.optimizers import RMSprop


from text_model import *


print('Build model...')
model = Sequential()
model.add(LSTM(512, batch_input_shape=(batch_size,maxlen, len(chars)), return_sequences=True, stateful=True))
model.add(LSTM(512 , stateful=True))
model.add(Dense(len(chars)))
print (len(chars))
model.add(Activation('softmax'))




optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


model.save('model_dump.h5py')
#