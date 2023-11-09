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

    # def is_element_logo(self):
    #     assert self.is_element_present(*locators.BasePageLocators.LOGO), \
    #         "The element logo is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The element logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_input_field(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "The search input field is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "The search button is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_wish_button(self):
        assert self.is_element_present(*locators.BasePageLocators.WISH_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cart_button(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_hity_button(self):
        assert self.is_element_present(*locators.BasePageLocators.HITY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_skidki_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SKIDKI), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_novinki_button(self):
        assert self.is_element_present(*locators.BasePageLocators.NOVINKI), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_samsung_category(self):
        assert self.is_element_present(*locators.BasePageLocators.HEAD_CAT_SAMSUNG), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_samsung_j701(self):
        assert self.hover_action(*locators.BasePageLocators.HEAD_CAT_SAMSUNG), \
            "The element is not present"
        assert self.is_element_present(*locators.BasePageLocators.SUBCATEGORY_SAMSUNG_HEADER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_slider(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_SLIDER), \
            "The element 'main_slider' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cat_zaryadki(self):
        assert self.is_element_present(*locators.MainPageLocators.CAT_ZARYADKI), \
            "The element 'cat_zaryadki' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_subcat(self):
        assert self.hover_action(*locators.MainPageLocators.CAT_ZARYADKI), \
            "Element 'cat_zaryadki' is not present"
        assert self.is_element_present(*locators.MainPageLocators.MAIN_SUBCAT), \
            "Element 'main subcategory' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_refund(self):
        assert self.is_element_present(*locators.MainPageLocators.REFUND), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_delivery(self):
        assert self.is_element_present(*locators.MainPageLocators.FREE_SHIPPING), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_otsrochka(self):
        assert self.is_element_present(*locators.MainPageLocators.PAYMENT_DELAY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_support(self):
        assert self.is_element_present(*locators.MainPageLocators.TECHNICAL_SUPPORT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_SHOW_ALL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_prev_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_LEFT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_next_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_RIGHT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_PANEL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_new_product_8(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_SMARTEX_XIAOMI_REDMI_NOTE_5_A_PRIME), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BEST_SELLERS_SHOW_ALL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BEST_SELLERS_LEFT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BEST_SELLERS_RIGHT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BEST_SELLERS_PANEL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_trends(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDS_2023_PREVIOUS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_trends(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDS_2023_NEXT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_footer_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "The element footer logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def subscribe_action(self, email):
        assert self.input_data(*locators.BasePageLocators.INPUT_SUBSCRIBE, email), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBE), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_alert_success_after_subscribe(self):
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")



