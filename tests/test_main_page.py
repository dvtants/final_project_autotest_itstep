import pytest
from ..pages.base_page import BasePage  # дві крапки перед pages.base_page - абсолютний шлях до файлу
# from pages.main_page import MainPage
from ..settings import sets  # дві крапки перед settings - абсолютний шлях до файлу


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    # def test_login_logout(self, browser):
    #    link_to_site = browser.current_url

# pytest -s -v test_main_page.py - не працює, треба вказувати точну адресу, а саме: tests/test_main_page.py
# pytest -s -v tests/test_main_page.py
# pytest -s -v -m "main_page"
# pytest -s -v
# pytest
