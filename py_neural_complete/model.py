import os
import just
import numpy as np
from keras.layers import Activation, Dense, LSTM
from keras.models import Sequential, load_model
from keras.optimizers import RMSprop


class LSTMBase(object):

    def __init__(self, model_name, encoder_decoder=None, hidden_units=128, base_path="models/"):
        self.model_name = model_name
        self.h5_path = base_path + model_name + ".h5"
        self.pkl_path = base_path + model_name + ".pkl"
        self.model = None
        self.hidden_units = hidden_units
        if encoder_decoder is None:
            self.encoder_decoder = just.read(self.pkl_path)
        else:
            self.encoder_decoder = encoder_decoder

    def sample(self, preds, temperature=1.0):
        # helper function to sample an index from a probability array
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)
        return np.argmax(probas)

    def build_model(self):
        if os.path.isfile(self.h5_path):
            model = self.load()
        else:
            # build the model: a single LSTM
            print('Building model...')
            num_unique_q_tokens = len(self.encoder_decoder.ex)
            num_unique_a_tokens = len(self.encoder_decoder.ey)
            model = Sequential()
            input_s = (None, num_unique_q_tokens)
            model.add(LSTM(self.hidden_units, input_shape=input_s))
            model.add(Dense(num_unique_a_tokens))
            model.add(Activation('softmax'))
            optimizer = RMSprop(lr=0.01)
            model.compile(loss='categorical_crossentropy', optimizer=optimizer)
        return model

    def train(self, test_cases=None, iterations=10, batch_size=256, num_epochs=3, **kwargs):
        if self.model is None:
            self.model = self.build_model()
        if not hasattr(self.encoder_decoder, "X"):
            X, y = self.encoder_decoder.get_xy()
            self.encoder_decoder.X, self.encoder_decoder.y = X, y
        for iteration in range(iterations):
            print()
            print('-' * 50)
            print('Iteration', iteration)
            self.model.fit(self.encoder_decoder.X, self.encoder_decoder.y,
                           batch_size=batch_size, nb_epoch=num_epochs,
                           **kwargs)
            self._show_test_cases(test_cases)

    def predict(self, text, diversity, max_prediction_steps, break_at_token=None):
        if self.model is None:
            self.model = self.build_model()
        outputs = []
        for _ in range(max_prediction_steps):
            X = self.encoder_decoder.encode_question(text)
            preds = self.model.predict(X, verbose=0)[0]
            answer_token = self.sample(preds, diversity)
            new_text_token = self.encoder_decoder.decode_y(answer_token)
            outputs.append(new_text_token)
            text += new_text_token
            if break_at_token is not None and break_at_token == new_text_token:
                break
        return self.encoder_decoder.untokenize(outputs)

    def save(self):
        if hasattr(self.encoder_decoder, "X"):
            del self.encoder_decoder.X
        if hasattr(self.encoder_decoder, "y"):
            del self.encoder_decoder.y
        just.write(self.encoder_decoder, self.pkl_path)
        self.model.save(self.h5_path)

    def load(self):
        return load_model(self.h5_path)

    def _show_test_cases(self, test_cases):
        if test_cases is None:
            return
        for test_case in test_cases:
            print('----- Generating with seed: \n\n', test_case)
            print("\n\n--PREDICTION--\n\n")
            for diversity in [0.2, 0.5, 1]:
                print("--------- diversity {} ------- ".format(diversity))
                print(self.predict(test_case, diversity, self.encoder_decoder.maxlen))
