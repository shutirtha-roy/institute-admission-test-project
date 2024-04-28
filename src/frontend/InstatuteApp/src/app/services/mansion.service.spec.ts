import { TestBed } from '@angular/core/testing';

import { MansionService } from './mansion.service';

describe('MansionServiceService', () => {
  let service: MansionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MansionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
