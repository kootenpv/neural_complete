import { Component } from '@angular/core';
import { Observable } from 'rxjs/Observable';

import {Http, Headers} from '@angular/http';

import {LocalService} from "./http-serv.service";

import 'rxjs/add/observable/of';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [LocalService]
})
export class AppComponent {

  constructor(public localService: LocalService) {
    this.getModels();
  }

  title = 'neural complete!';
  data: Observable<string[]>;
  myData: string;

  codeArray: Array<string> = [];
  lstmModels: Array<string> = [];
  activeModel: string = "neural_token";

  mySource = (keyword: any) => {
    var data = {"keyword": this.codeArray.join("\n") + "\n" + keyword,
                "model": this.activeModel};
    return this.localService.predict(data).map((data) => { return data.json() })
  }

  append() {
    if (this.myData) {
      console.log("appended")

      this.codeArray.push(this.myData + "\n")
      this.myData = ""
    }
  }

  getModels() {
    return this.localService.getModels()
      .subscribe(data => this.lstmModels = data.json()['data']['results'],
                 err => console.log("ere", err))
  }

}
