import numpy as np
import keras
from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import SimpleRNN
from keras.layers import Dense, Dropout, Embedding, LSTM, Input, Bidirectional
from keras.initializations import normal, identity
from keras.optimizers import RMSprop
from keras.utils import np_utils
from keras import backend as K
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
from keras.models import save_model, load_model


def display_lstm_weights(model,data_x):
	lstm = model.layers[0]
	f = K.function([K.learning_phase(), lstm.input], [lstm.output])
	x = [data_x[0][0]]
	y = f([0,[x]])
	print('------------input gate---------------')
	print(K.get_value(lstm.W_i))
	print(K.get_value(lstm.U_i))
	print(K.get_value(lstm.b_i))
	print('------------input data gate---------------')
	print(K.get_value(lstm.W_c))
	print(K.get_value(lstm.U_c))
	print(K.get_value(lstm.b_c))
	print('------------forget gate---------------')
	print(K.get_value(lstm.W_f))
	print(K.get_value(lstm.U_f))
	print(K.get_value(lstm.b_f))
	print('------------output gate---------------')
	print(K.get_value(lstm.W_o))
	print(K.get_value(lstm.U_o))
	print(K.get_value(lstm.b_o))


	print('------------x---------------')
	print(x)
	print('------------y---------------')
	print(y)
	sys.exit(0)