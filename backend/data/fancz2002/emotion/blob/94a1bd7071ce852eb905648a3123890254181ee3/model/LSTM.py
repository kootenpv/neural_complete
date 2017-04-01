from keras.models import Sequential
from keras.layers import Masking, Activation, Input,LSTM,Dense
from config import hypers
def myLSTM():
	model = Sequential()
	model.add(Masking(mask_value=0., input_shape=(hypers["timesteps"],hypers["feature_size"])))
	model.add(LSTM(hypers["lstm_hidden"]))
	model.add(Dense(7))
	model.add(Activation('softmax'))
	return model