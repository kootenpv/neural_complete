import { Injectable } from '@angular/core';
import {Http, Headers} from '@angular/http';

@Injectable()
export class LocalService {

  URL: string = "http://localhost:9078/"

  constructor(private http: Http) {
  }

  createJsonHeader(headers: Headers) {
    headers.append('Content-Type', 'application/json');
  }


  post(data: any, path: string) {
    let headers = new Headers();
    this.createJsonHeader(headers)
    return this.http.post(this.URL + path, JSON.stringify(data), {headers: headers})
  }

  predict(data: any) {
    return this.post(data, "predict")
  }

  getModels() {
    return this.post({}, "get_models")
  }

}
