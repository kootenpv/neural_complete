"""
Selects recurrent neural network based on the name.

Author: Mateusz Malinowski
Email: mmalinow@mpi-inf.mpg.de
"""


from keras.layers.recurrent import GRU
from keras.layers.recurrent import LSTM
from keras.layers.recurrent import SimpleRNN
#from keras.layers.recurrent import JZS1
#from keras.layers.recurrent import JZS2
#from keras.layers.recurrent import JZS3




select = {
        'lstm':LSTM,
        'gru':GRU,
        'simpleRNN':SimpleRNN,
        #'mut1':JZS1,
        #'mut2':JZS2,
        #'mut3':JZS3,
        #'jzs1':JZS1,
        #'jzs2':JZS2,
        #'jzs3':JZS3
        }

