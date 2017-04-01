

import cnn
import blstm
import split_view_cnn


import numpy as np


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import LSTM, Merge
from keras.optimizers import SGD


def build_empty_model(X_shape, up_shape, down_shape, Y_shape) :
    # This can be the combination of the splitview cnn and the blstm