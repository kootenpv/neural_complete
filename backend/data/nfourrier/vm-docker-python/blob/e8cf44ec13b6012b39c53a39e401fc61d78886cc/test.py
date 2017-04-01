import os
import datetime
import numpy as np
from keras.utils import np_utils, generic_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation,Merge
from keras.layers.recurrent import GRU,LSTM
from keras.optimizers import SGD,Adam
from keras.layers import Convolution1D, MaxPooling1D, Flatten
from keras.models import model_from_json
from keras import backend as K


from keras.layers import Input, LSTM, Dense, merge
from keras.models import Model


import keras
import h5py
from collections import defaultdict
import json
import pickle
import os




print('importing keras and tensorflow')