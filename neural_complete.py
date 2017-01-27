import tokenize as tk
from io import BytesIO

import just

from encoder_decoder import TextEncoderDecoder
from model import LSTMBase


CHAR_MODEL_NAME = "neural_complete_char"
TOKEN_MODEL_NAME = "neural_complete_token"

TRAINING_TEST_CASES = ["from keras.layers import"]


def text_tokenize(txt):
    """ specific tokenizer suitable for extracting 'python tokens' """
    toks = []
    try:
        for x in tk.tokenize(BytesIO(txt.encode('utf-8')).readline):
            toks.append(x)
    except tk.TokenError:
        pass
    tokkies = []
    old = (0, 0)
    for t in toks:
        if not t.string:
            continue
        if t.start[0] == old[0] and t.start[1] > old[1]:
            tokkies.append(" " * (t.start[1] - old[1]))
        tokkies.append(t.string)
        old = t.end
    if txt.endswith(" "):
        tokkies.append(" ")
    toks = [x for x in tokkies if not x.startswith("#")]
    return toks[1:]


def get_data():
    return list(just.multi_read("data/**/*.py").values())


def train(ted, model_name):
    lb = LSTMBase(model_name, ted)
    lb.train(test_cases=TRAINING_TEST_CASES)
    lb.save()


def train_char(model_name):
    data = get_data()
    ted = TextEncoderDecoder(data, tokenize=list, untokenize="".join, padding=" ",
                             min_count=1, maxlen=40)
    train(ted, model_name)


def train_token(model_name):
    data = get_data()
    ted = TextEncoderDecoder(data, tokenize=text_tokenize, untokenize="".join, padding=" ",
                             min_count=1, maxlen=20)
    train(ted, model_name)


def get_char_model():
    return LSTMBase(CHAR_MODEL_NAME)


def get_token_model():
    return LSTMBase(TOKEN_MODEL_NAME)


def neural_complete(model, text, diversities):
    predictions = [model.predict(text, diversity=d, max_prediction_steps=80,
                                 break_at_token="\n")
                   for d in diversities]
    # returning the latest sentence, + prediction
    suggestions = [text.split("\n")[-1] + x.rstrip("\n") for x in predictions]
    return suggestions
