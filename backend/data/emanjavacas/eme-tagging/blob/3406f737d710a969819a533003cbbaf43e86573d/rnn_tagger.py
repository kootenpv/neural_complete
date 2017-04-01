

from keras.models import Model
from keras.layers import Input, Dense, Flatten
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import Bidirectional, TimeDistributed




def bilstm_layer(input_layer, lstm_dims, rnn_layers, dropout):
    lstm = None
    if isinstance(lstm_dims, (list, tuple)):
        lstm_dims = lstm_dims
    else:
        assert isinstance(lstm_dims, int)
        lstm_dims = [lstm_dims] * rnn_layers
    for i in range(rnn_layers):
        if i == 0:
            nested = input_layer
        else:
            nested = lstm
        wrapped = LSTM(
            output_dim=lstm_dims[i], activation='tanh', return_sequences=True,
            dropout_W=dropout, dropout_U=dropout, name='bistm_%d' % i)
        lstm = Bidirectional(wrapped, merge_mode='sum')(nested)
    return lstm




def bilstm_tagger(ft_model, n_tags, maxlen,
                  lstm_dims=150, hidden_dim=100, rnn_layers=3, dropout=0.2):
    input_layer = Input(shape=(maxlen, ft_model.dim), name='input')
    lstm = bilstm_layer(input_layer, lstm_dims, rnn_layers, dropout)
    output_layer = TimeDistributed(Dense(n_tags, activation='softmax'))(lstm)
    model = Model(input=input_layer, output=output_layer)
    return model

