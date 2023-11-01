from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH,
                    "//div[@class='top_bar_user']/a[@href='user/login']")  # краще все брати: зовнішньо в подвійних лапках, а внутрішні одинарні.
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
    PHONE = (By.XPATH, "//*[text()='+38 098 911 95 22']")  # в XPATH-і можна "*" і "div"
    CURRENCY = (By.XPATH, "//select[@id='currency']")
    CURRENCY_UAH = (By.XPATH, "//option[text()='UAH']")
    CURRENCY_USD = (By.XPATH, "//option[text()='USD']")
    CURRENCY_EUR = (By.XPATH, "//option[text()='EUR']")
    LOGO = (By.XPATH, "//img[@src='images/logo.png']")
    SEARCH = (By.XPATH, "//input[@class='header_search_input tt-input']")
    BUTTON_SUBMIT = (By.XPATH, "//button[@class='header_search_button trans_300']")
    WISH_SHOW = (By.XPATH, "//img[@src='images/heart.png']")
    CART_SHOW = (By.XPATH, "//img[@src='images/cart.png']")




