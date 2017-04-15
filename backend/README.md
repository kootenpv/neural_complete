# Neural Complete (backend)

This repository contains the backend for [Neural Complete](../). It uses Flask to expose a LSTM Recurrent Neural Network. This is where you can experiment with your models and your own data.

### Installation

    pip3.5 install -r requirements.txt

### Training the model

Not such a nice setup, but at least possible to reproduce:

    python3.5 neural_complete.py char
    python3.5 neural_complete.py token

### Using created models

    python3.5 serve.py
