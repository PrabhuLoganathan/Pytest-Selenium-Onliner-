The test was a part of automatization test course. The test use Selenuim WebDriver and PyTest.

Test-case:
1) Open page http://onliner.by/
2) Log in
3) Log out
4) Get list of popular themes
5) Click on one random of them
6) Check that it's right page
7) Open main page
8) Use driver.page_source, find all opinions
on main page by regexp. Write them to csv-file.

Test implement PageObject and Singleton pattern.
Work in Chrome and Firefox.
