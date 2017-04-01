from pandas import DataFrame
from util import *
import datetime
import time
from extract import get_labevents_extractors
from keras.models import Sequential
from keras.layers.core import Activation, Dense, Masking, Merge
from keras.layers.wrappers import TimeDistributed
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM, SimpleRNN
from keras.layers import Input, merge
from keras.models import Model, load_model
from keras.callbacks import EarlyStopping
from keras.regularizers import l2, activity_l2
from keras.optimizers import SGD


ninput = Input(shape = (3, 2))
mask = Masking(mask_value=0, name = "MASKING")(ninput)
lstm = LSTM(3)(mask)
model = Model(input = ninput, output = lstm)
model.compile(optimizer = "sgd", loss = 'binary_crossentropy')
data1 = [[1,2],  [0,0],[5,6]]
data2 = [[1,2], [5,6],[0,0]]
print model.get_config()
# print mask.get_output_shape_for(1)
print model.predict(np.array([data1,data2]))