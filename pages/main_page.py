from ..pages import base_page, locators
import inspect  # потрібен щоби написати прінт


class MainPage(base_page.BasePage):
    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button login is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_feedback(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button feedback is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button delivery is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_warranty(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "Button warranty is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_number_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Number phone is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_currency(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_currency_uah(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element currency is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_UAH), \
            "The element currency_uah is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_currency_usd(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element currency is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_USD), \
            "The element currency_usd is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_currency_eur(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element currency is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_EUR), \
            "The element currency_eur is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The element logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


