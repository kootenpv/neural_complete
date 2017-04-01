import { Ng2AutoCompleteKerasPage } from './app.po';

describe('ng2-auto-complete-keras App', function() {
  let page: Ng2AutoCompleteKerasPage;

  beforeEach(() => {
    page = new Ng2AutoCompleteKerasPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
