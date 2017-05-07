# Neural Complete (frontend)

Either serve the `dist/` folder directly, or use angular 2 CLI to serve the client where it refreshes on code changes.

It depends on `ng2-auto-complete` for autocomplete functionality

### Angular 2 CLI

1. Install [angular 2 cli](https://github.com/angular/angular-cli) (and its prerequisites)

2. Run `npm install`

3. Run `ng serve`

4. Observe the frontend at http://localhost:4200

### Serve the dist folder

    cd dist/

Using python:

    python -m SimpleHTTPServer 4200     # python 2
    python3 -m http.server 4200         # python 3

Or node:

    npm install http-server -g
    http-server -p 4200

### Changes

To make changes to the code, first install nodejs/npm/angcli, then:

    npm install
    ng serve --port 8080
