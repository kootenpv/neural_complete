from cors import crossdomain
from flask import Flask, jsonify, request

from encoder_decoder import TextEncoderDecoder
from neural_complete import text_tokenize 
from neural_complete import neural_complete
from neural_complete import get_char_model
from neural_complete import get_token_model

if __name__ == "__main__":

    app = Flask(__name__)

    models = {}
    models['char'] = get_char_model()
    models['token'] = get_token_model()

    @app.route("/predict", methods=["GET", "POST", "OPTIONS"])
    @crossdomain(origin='*', headers="Content-Type")
    def predict():
        if request.method == 'POST':
            parameters = request.json
        sentence = parameters.get("keyword", "from ")
        model_name = parameters.get("model", "char")
        suggestions = neural_complete(models[model_name], sentence, [0.2, 0.5, 1])
        return jsonify({"data": {"results": suggestions}})

    app.run(host="0.0.0.0", port=9078)
