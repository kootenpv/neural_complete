"""Recurrent neural network model."""
from ...model import KerasModel
from ..window_model import FrameModel




class RecurrentModel(KerasModel, FrameModel):
    """RNN."""
    def _create_model(self, input_shape, num_categories):
        from keras.layers.core import Activation, Dense, Dropout, Reshape
        from keras.models import Sequential
        from keras.layers.recurrent import LSTM
        model = Sequential()
        model.add(
            LSTM(
                32,
                input_shape=input_shape,
                return_sequences=True
            )
        )
        model.add(
            LSTM(
                32,
                return_sequences=True,
                go_backwards=True
            )
        )
        model.add(LSTM(32, return_sequences=False))
        model.add(Dense(num_categories))
        model.add(Activation('softmax'))
        return model