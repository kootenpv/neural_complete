# neural_complete

neural_complete is autocomplete, trained on python source code, using a neural network. Ironically, it is trained on files containing [keras](https://keras.io/) imports. A neural network trained to help writing neural network code.

Rather than completing a word, it will suggest finishing a whole line. It uses information from previous lines to make a suggestion.

One could eventually imagine that everyone will have a neural network to automagically complete their whole scripts :-)

But not yet with this code.

### Components

This repository contains the backend for neural_complete. It uses flask to expose a LSTM Recurrent Neural Network. This is where you can experiment with your models and your own data.

The [frontend repository](https://github.com/kootenpv/ng2_neural_complete) is a very thin layer communicating with the backend to receive autocomplete suggestions, written in [Angular 2](https://angular.io/).

Hopefully the modular structure will be inspiring. It is setup so that it could soon also be used for training QA.

## Do It Yourself

### Scraping data

Unfortunately the Github API does not allow to search by filename, so I wrote a scraping script to gather python data specifically trained on keras source code. You can change the search query to gather your own data. Do not overdo it as to "annoy" github; in my case I only ran it for a few minutes, roughly 200 scripts. You would need a lot more for a better result.

### Training the model

### Using the model

### Credits

It uses a lot of the ideas of the standard keras [LSTM text generation example](https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py).
