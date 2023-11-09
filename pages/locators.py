from selenium.webdriver.common.by import By


class BasePageLocators:  # Локатори елементів, які не змінюються. Все що в хедері і в футері.
    LOGIN_SIGNUP = (By.XPATH,
                    "//div[@class='top_bar_user']/a[@href='user/login']")  # краще все брати: зовнішньо в подвійних лапках, а внутрішні одинарні.
    DETAILS = (By.XPATH, "//a[text()='Детали сотрудничества']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
    PHONE = (By.XPATH, "//*[text()='+38 098 911 95 22']")  # в XPATH-і можна "*" і "div"
    CURRENCY = (By.XPATH, "//select[@id='currency']")
    CURRENCY_UAH = (By.XPATH, "//option[text()='UAH']")
    CURRENCY_USD = (By.XPATH, "//option[text()='USD']")
    CURRENCY_EUR = (By.XPATH, "//option[text()='EUR']")
    LOGO = (By.XPATH, "//img[@src='images/logo.png']")
    SEARCH_INPUT = (By.XPATH, "//input[@class='header_search_input tt-input']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='header_search_button trans_300']")
    WISH_BUTTON = (By.XPATH, "//img[@src='images/heart.png']")  # WISH_BUTTON = (By.XPATH, '//a[@href="wish/show"]')
    CART_BUTTON = (By.XPATH, "//img[@src='images/cart.png']")  # CART_BUTTON = (By.XPATH, '//a[@href="cart/show"]')
    HITY = (By.XPATH, "//span[text()='Хиты']")
    SKIDKI = (By.XPATH, "//span[text()='Скидки']")
    NOVINKI = (By.XPATH, "//span[text()='Новинки']")
    HEAD_CAT_SAMSUNG = (By.XPATH,
                        "//div[text()='Samsung']")  # HEAD_CAT_SAMSUNG = (By.XPATH, "//div[@class='search-by-level-1' and text()='Samsung']")
    SUBCATEGORY_SAMSUNG_HEADER = (By.XPATH,
                                  "//a[text()='Samsung J701']")  # В консолі Chrome робимо заморозку: setTimeout(function(){debugger;}, 5000) - на 5 сек.
    SUBSCRIBE = (By.XPATH,
                 "//button[text()='Подписаться!']")  # //button[@class="newsletter_button"] # SUBSCRIBE = (By.XPATH, "//button[text() = 'Подписаться!']")
    INPUT_SUBSCRIBE = (By.XPATH, "//input[@name='submail']")
    LOGO_FOOTER = (By.XPATH, "//img[@src='images/logo-footer.png']")
    ALERT_SUCCESS = (By.XPATH,
                     "//div[@id = 'alert-success']")  # Локатор меню що спливає після підписання на розсилку. Ви успішно підписалися.
    ALERT_ERROR = (By.XPATH, "//div[@id = 'alert-error']")  # Негативне повідомлення


class MainPageLocators:  # Локатори елементів, які змінюються. Все що є на головній сторінці.
    MAIN_SLIDER = (By.XPATH, "//div[@class = 'screen_slider']")
    CAT_ZARYADKI = (By.XPATH, "//a[@href='category/zaryadki']")
    MAIN_SUBCAT = (By.XPATH, "//a[@href='category/Besprovodnye-BZU']")
    REFUND = (By.XPATH, "//div[@class='characteristics']//div[text()='Возврат средств']/parent::*/parent::*/parent::*")
    FREE_SHIPPING = (
        By.XPATH, "//div[@class='characteristics']//div[text()='Бесплатная доставка']/parent::*/parent::*/parent::*")
    PAYMENT_DELAY = (
        By.XPATH, "//div[@class='characteristics']//div[text()='Отсрочка оплаты']/parent::*/parent::*/parent::*")
    TECHNICAL_SUPPORT = (
        By.XPATH, "//div[@class='characteristics']//div[text()='Тех.поддержка']/parent::*/parent::*/parent::*")
    NEW_ARRIVALS_SHOW_ALL = (By.XPATH, "//div[@class='arrivals_nav_container']/a[@class='view-all']")
    NEW_ARRIVALS_LEFT = (By.XPATH, "//div[@class='arrivals_nav arrivals_prev']/i[@class='fas fa-chevron-left']")
    NEW_ARRIVALS_RIGHT = (By.XPATH, "//div[@class='arrivals_nav arrivals_next']/i[@class='fas fa-chevron-right']")
    NEW_ARRIVALS_PANEL = (By.XPATH, "//div[@class='row']/div[@class='col-lg-12']")
    NEW_ARRIVALS_SMARTEX_XIAOMI_REDMI_NOTE_5_A_PRIME = (By.XPATH,
                                                        "//a[text()='Гидрогелевая бронепленка пленка Smartex Xiaomi Redmi Note 5A Prime']/parent::*/parent::*/parent::*/parent::*/parent::*/parent::*")

    BEST_SELLERS_SHOW_ALL = (By.XPATH, "//div[@class='best_nav_container']/a[@class='view-all']")
    BEST_SELLERS_LEFT = (By.XPATH, "//div[@class='best_prev best_nav']/i[@class='fas fa-chevron-left']")
    BEST_SELLERS_RIGHT = (By.XPATH, "//div[@class='best_next best_nav']/i[@class='fas fa-chevron-right']")
    BEST_SELLERS_PANEL = (By.XPATH, "//div[@class='bestsellers_panel panel active']")
    BEST_SELLERS_HOCO_DI04_BT_WIRELESS_MOUSE_BLACK = (By.XPATH,
                                                      "//div[@class='slick-slide slick-active']//a[text()='Компьютерная мышка HOCO DI04 BT Wireless Mouse Black']/parent::*/parent::*/parent::*/parent::*/parent::*")

    TRENDS_2023_PREVIOUS = (By.XPATH, "//div[@class='trends_prev trends_nav slick-arrow']")
    TRENDS_2023_NEXT = (By.XPATH, "//div[@class='trends_next trends_nav slick-arrow']")
    TRENDS_2023_HOCO_ES20_PLUS_AIRPODS2_BLUETOOTH_WHITE = (By.XPATH,
                                                           "//div[@data-slick-index='7']//a[text()='Наушники HOCO ES20 PLUS AirPods2 Bluetooth/ White']/parent::*/parent::*/parent::*/parent::*/parent::*")

# # //div[@class="characteristics"]//div[text()="Возврат средств"]
# # //div[text()="Возврат средств"]/parent::*/parent::*/parent::*
# //div[@class="characteristics"]//div[text()="Возврат средств"]/parent::*/parent::*/parent::*
# # //div[@class="characteristics"]//div[text()="Бесплатная доставка"]
# # //div[text()="Бесплатная доставка"]/parent::*/parent::*/parent::*
# //div[@class="characteristics"]//div[text()="Бесплатная доставка"]/parent::*/parent::*/parent::*
# # //div[@class="characteristics"]//div[text()="Отсрочка оплаты"]
# # //div[text()="Отсрочка оплаты"]/parent::*/parent::*/parent::*
# //div[@class="characteristics"]//div[text()="Отсрочка оплаты"]/parent::*/parent::*/parent::*
# # //div[@class="characteristics"]//div[text()="Тех.поддержка"]
# # //div[text()="Тех.поддержка"]/parent::*/parent::*/parent::*
# //div[@class="characteristics"]//div[text()="Тех.поддержка"]/parent::*/parent::*/parent::*
#
# //div[@class="arrivals_nav_container"]/a[@class="view-all"]
# //div[@class="arrivals_nav arrivals_prev"]/i[@class="fas fa-chevron-left"]
# //div[@class="arrivals_nav arrivals_next"]/i[@class="fas fa-chevron-right"]
# //div[@class="row"]/div[@class="col-lg-12"]
# #//a[text()="Гидрогелевая бронепленка пленка Smartex Xiaomi Redmi Note 5A Prime"]
# //a[text()="Гидрогелевая бронепленка пленка Smartex Xiaomi Redmi Note 5A Prime"]/parent::*/parent::*/parent::*/parent::*/parent::*/parent::*
#
# //div[@class="best_nav_container"]/a[@class="view-all"]
# //div[@class="best_prev best_nav"]/i[@class="fas fa-chevron-left"]
# //div[@class="best_next best_nav"]/i[@class="fas fa-chevron-right"]
# //div[@class="bestsellers_panel panel active"]
# //div[@class="slick-slide slick-active"]//a[text()="Компьютерная мышка HOCO DI04 BT Wireless Mouse Black"]/parent::*/parent::*/parent::*/parent::*/parent::*
#
# //div[@class="trends_prev trends_nav slick-arrow"]
# //div[@class="trends_next trends_nav slick-arrow"]
#
# //div[@data-slick-index="7"]//a[text()="Наушники HOCO ES20 PLUS AirPods2 Bluetooth/ White"]/parent::*/parent::*/parent::*/parent::*/parent::*
# //div[@class="trends_slider_container"]//div[@data-slick-index="7"]
