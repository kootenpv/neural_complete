# ng2_neural_complete

Either serve the `dist/` folder directly, or use angular 2 CLI to serve the client where it refreshes on code changes.

It depends on `ng2-auto-complete` for autocomplete functionality

### Angular 2 CLI

1. Install [angular 2 cli](https://github.com/angular/angular-cli) (and its prerequisites)

2. Run `ng serve`

3. Observe the frontend at http://localhost:4200

### Serve the dist folder

    cd dist/

Using python:

    python -m SimpleHTTPServer 4200     # python 2
    python3 -m http.server 4200         # python 3

Or node:

    npm install http-server -g
    http-server -p 4200

### Improvements

Note that it might be an idea to refactor this to use angular2/material for looks and autocomplete.
