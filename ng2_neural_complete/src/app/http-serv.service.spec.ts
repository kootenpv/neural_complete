/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { HttpServService } from './http-serv.service';

describe('HttpServService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [HttpServService]
    });
  });

  it('should ...', inject([HttpServService], (service: HttpServService) => {
    expect(service).toBeTruthy();
  }));
});
