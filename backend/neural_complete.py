
import just

from encoder_decoder import TextEncoderDecoder, text_tokenize
from model import LSTMBase

TRAINING_TEST_CASES = ["from keras.layers import"]


def get_data():
    return list(just.multi_read("data/**/*.py").values())


def train(ted, model_name):
    lb = LSTMBase(model_name, ted)
    try:
        lb.train(test_cases=TRAINING_TEST_CASES)
    except KeyboardInterrupt:
        pass
    print("saving")
    lb.save()


def train_char(model_name):
    data = get_data()
    # list makes a str "str" into a list ["s","t","r"]
    ted = TextEncoderDecoder(data, tokenize=list, untokenize="".join, padding=" ",
                             min_count=1, maxlen=40)
    train(ted, model_name)


def train_token(model_name):
    data = get_data()
    # text tokenize splits source code into python tokens
    ted = TextEncoderDecoder(data, tokenize=text_tokenize, untokenize="".join, padding=" ",
                             min_count=1, maxlen=20)
    train(ted, model_name)


def get_model(model_name):
    return LSTMBase(model_name)


def neural_complete(model, text, diversities):
    predictions = [model.predict(text, diversity=d, max_prediction_steps=80,
                                 break_at_token="\n")
                   for d in diversities]
    # returning the latest sentence, + prediction
    suggestions = [text.split("\n")[-1] + x.rstrip("\n") for x in predictions]
    return suggestions


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        raise Exception(
            "expecting model name, such as 'neural' and type (either 'char' or 'token'")
    model_name = "_".join(sys.argv[1:])
    if sys.argv[2] == "char":
        train_char(model_name)
    elif sys.argv[2] == "token":
        train_token(model_name)
    else:
        msg = "The second argument cannot be {}, but should be either 'char' or 'token'"
        raise Exception(msg.format(sys.argv[2]))
