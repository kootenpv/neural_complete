import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { MaterialModule } from '@angular/material';
import { AppComponent } from './app.component';
import { Ng2AutoCompleteModule } from 'ng2-auto-complete';

import { HighlightJsModule, HighlightJsService } from '../../node_modules/angular2-highlight-js';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    MaterialModule.forRoot(),
    HighlightJsModule,
    Ng2AutoCompleteModule
  ],
  providers: [
    HighlightJsService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
