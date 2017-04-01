from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import time
import csv
from keras.layers.core import Dense, Activation, Dropout,Merge
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import copy








data_dim = 1
timesteps = 13


# expected input data shape: (batch_size, timesteps, data_dim)
model_A = Sequential()
model_B = Sequential()
model_Combine = Sequential()


# LSTM Part
lstm_hidden_size = [100, 100]
drop_out_rate = [0.5, 0.5]
model_A.add(LSTM(lstm_hidden_size[0], return_sequences=True, input_shape=(timesteps, data_dim)))
model_A.add(Dropout(drop_out_rate[0]))  # return_sequences=True means output cell state C at each LSTM sequence
model_A.add(LSTM(lstm_hidden_size[1], return_sequences=False))
model_A.add(Dropout(drop_out_rate[1]))  # return_sequence=False means output only last cell state C in LSTM sequence
model_A.add(Dense(1, activation='linear'))


# NN Part
in_dimension = 3;
nn_hidden_size = [100, 100]
nn_drop_rate = [0.2, 0.2]
model_B.add(Dense(nn_hidden_size[0], input_dim=in_dimension))
model_B.add(Dropout(nn_drop_rate[0]))
model_B.add(Dense(nn_hidden_size[1]))
model_B.add(Dropout(nn_drop_rate[1]))
model_B.add(Dense(1, activation='linear'))


model_Combine.add(Merge([model_A, model_B], mode='concat'))
model_Combine.add(Dense(1, activation='linear'))


model_Combine.compile(loss="mse", optimizer="rmsprop")




# output the model
from keras.utils.visualize_util import plot, to_graph
graph = to_graph(model_Combine, show_shape=True)
graph.write_png("rnnandnn.png")