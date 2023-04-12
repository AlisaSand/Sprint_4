from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CreateOrderLocator:
    CREATE_ORDER_BUTTON_IN_HEADER = [By.XPATH, './/button[text()="Заказать"]']
    CREATE_ORDER_BUTTON_ON_BOTTOM = [By.XPATH, './/button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]']
    CREATE_ORDER_HEADER = [By.XPATH, './/div[text()="Для кого самокат"]']
    NAME_FIELD = [By.XPATH, './/div[@class="Order_Form__17u6u"]//input[@placeholder="* Имя"]']
    SURNAME_FIELD = [By.XPATH, './/div[@class="Order_Form__17u6u"]//input[@placeholder="* Фамилия"]']
    ADDRESS_FIELD = [By.XPATH, './/div[@class="Order_Form__17u6u"]//input[@placeholder="* Адрес: куда привезти заказ"]']
    METRO_SELECT = [By.XPATH, './/div[@class="Order_Form__17u6u"]//input[@placeholder="* Станция метро"]']
    METRO_SELECT_CHERKIZOVSKAYA = [By.XPATH,
                                  './/div[@class="Order_Form__17u6u"]/div[4]//button/div[text()="Черкизовская"]']
    METRO_SELECT_SOKOLNIKI = [By.XPATH,
                                   './/div[@class="Order_Form__17u6u"]/div[4]//button/div[text()="Сокольники"]']
    PHONE_NUMBER_FIELD = [By.XPATH, './/div[@class="Order_Form__17u6u"]/div[5]/input']
    FUTHER_BUTTON = [By.XPATH, './/button[text()="Далее"]']
    ABOUT_RENT_HEADER = [By.XPATH, './/div[text()="Про аренду"]']
    SHIPPING_DATE = [By.XPATH, './/div[@class="Order_Form__17u6u"]//input[1]']
    SELECT_DAYS = [By.XPATH, './/span[@class="Dropdown-arrow"]']
    DAYS_FOR_RENT_FOR_BLACK_SCOOTER_SELECT = [By.XPATH, './/div[@class="Dropdown-menu"]/div[text()="двое суток"]']
    DAYS_FOR_RENT_FOR_GREY_SCOOTER_SELECT = [By.XPATH, './/div[@class="Dropdown-menu"]/div[text()="трое суток"]']
    SCOOTER_COLOR_BLACK_SELECT = [By.ID, 'black']
    SCOOTER_COLOR_GREY_SELECT = [By.ID, 'grey']
    COMMENT = [By.XPATH, './/div[@class="Order_Form__17u6u"]//input[@placeholder="Комментарий для курьера"]']
    PUBLISH_ORDER_BUTTON = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    CONFIRMATION_BUTTON = [By.XPATH, './/button[text()="Да"]']
    ORDER_CREATED_HEADER = [By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ"]']
    ORDER_NUMBER = [By.XPATH, './/div[@class="Order_Text__2broi"]']
    SCOOTER_LOGO = [By.XPATH, './/img[@alt="Scooter"]']
    YANDEX_LOGO = [By.XPATH, './/img[@alt="Yandex"]']
    MAIN_HEADER = [By.XPATH, './/div[@class="Home_Header__iJKdX"]']
    YANDEX_BUTTON = [By.XPATH, './/button[text()="Найти"]']


class CreateOrderAction(BasePage):
    def click_on_create_order_button_in_header(self):
        self.click_on_element(CreateOrderLocator.CREATE_ORDER_BUTTON_IN_HEADER)

    def click_on_create_order_button_on_bottom(self):
        self.click_on_element(CreateOrderLocator.CREATE_ORDER_BUTTON_ON_BOTTOM)

    def fill_name_field(self, name):
        self.find_element(CreateOrderLocator.NAME_FIELD).send_keys(name)

    def fill_surname_field(self, surname):
        self.find_element(CreateOrderLocator.SURNAME_FIELD).send_keys(surname)

    def fill_address_field(self, address):
        self.find_element(CreateOrderLocator.ADDRESS_FIELD).send_keys(address)

    def fill_metro_station_cherkizovskaya_field(self):
        self.click_on_element(CreateOrderLocator.METRO_SELECT)
        self.click_on_element(CreateOrderLocator.METRO_SELECT_CHERKIZOVSKAYA)

    def fill_metro_station_sokolniki_field(self):
        self.click_on_element(CreateOrderLocator.METRO_SELECT)
        self.click_on_element(CreateOrderLocator.METRO_SELECT_SOKOLNIKI)

    def fill_phone_number(self, phone_number):
        self.find_element(CreateOrderLocator.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def click_on_futher_button(self):
        self.click_on_element(CreateOrderLocator.FUTHER_BUTTON)

    def click_on_scooter_logo(self):
        self.click_on_element(CreateOrderLocator.SCOOTER_LOGO)

    def click_on_yandex_logo(self):
        self.click_on_element(CreateOrderLocator.YANDEX_LOGO)

    def get_to_bottom_order_creation_button(self):
        element = self.find_element(CreateOrderLocator.CREATE_ORDER_BUTTON_ON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def fill_about_rent_form_black_scooter(self, date, comment):
        self.find_element(CreateOrderLocator.ABOUT_RENT_HEADER)
        self.click_on_element(CreateOrderLocator.SHIPPING_DATE)
        self.find_element(CreateOrderLocator.SHIPPING_DATE).send_keys(date)
        self.click_on_element(CreateOrderLocator.SELECT_DAYS)
        self.click_on_element(CreateOrderLocator.DAYS_FOR_RENT_FOR_BLACK_SCOOTER_SELECT)
        self.click_on_element(CreateOrderLocator.SCOOTER_COLOR_BLACK_SELECT)
        self.find_element(CreateOrderLocator.COMMENT).send_keys(comment)
        self.click_on_element(CreateOrderLocator.PUBLISH_ORDER_BUTTON)
        self.click_on_element(CreateOrderLocator.CONFIRMATION_BUTTON)

    def fill_about_rent_form_grey_scooter(self, date, comment):
        self.find_element(CreateOrderLocator.ABOUT_RENT_HEADER)
        self.click_on_element(CreateOrderLocator.SHIPPING_DATE)
        self.find_element(CreateOrderLocator.SHIPPING_DATE).send_keys(date)
        self.click_on_element(CreateOrderLocator.SELECT_DAYS)
        self.click_on_element(CreateOrderLocator.DAYS_FOR_RENT_FOR_GREY_SCOOTER_SELECT)
        self.click_on_element(CreateOrderLocator.SCOOTER_COLOR_GREY_SELECT)
        self.find_element(CreateOrderLocator.COMMENT).send_keys(comment)
        self.click_on_element(CreateOrderLocator.PUBLISH_ORDER_BUTTON)
        self.click_on_element(CreateOrderLocator.CONFIRMATION_BUTTON)

    def check_creation_order_by_clicking_on_order_button_in_header(
            self, name, surname, address, phone_number, date, carrier_comment
    ):
        self.click_on_create_order_button_in_header()
        self.fill_name_field(name)
        self.fill_surname_field(surname)
        self.fill_address_field(address)
        self.fill_metro_station_cherkizovskaya_field()
        self.fill_phone_number(phone_number)
        self.click_on_futher_button()
        self.fill_about_rent_form_black_scooter(date, carrier_comment)

        assert self.find_element(CreateOrderLocator.ORDER_CREATED_HEADER).is_displayed(),\
            "There should be a header with success message"

    def check_creation_order_by_clicking_on_bottom_order_button(
            self, name, surname, address, phone_number, date, carrier_comment
    ):
        self.get_to_bottom_order_creation_button()
        self.click_on_create_order_button_on_bottom()
        self.fill_name_field(name)
        self.fill_surname_field(surname)
        self.fill_address_field(address)
        self.fill_metro_station_sokolniki_field()
        self.fill_phone_number(phone_number)
        self.click_on_futher_button()
        self.fill_about_rent_form_grey_scooter(date, carrier_comment)

        assert self.find_element(CreateOrderLocator.ORDER_CREATED_HEADER).is_displayed(),\
            "There should be a header with success message"

    def check_main_scooter_page_appeared_after_clicking_on_scooter_logo(self):
        self.click_on_create_order_button_in_header()
        self.click_on_scooter_logo()
        assert self.find_element(CreateOrderLocator.MAIN_HEADER).is_displayed(), 'Scooter main page should be opened'

    def check_main_yandex_page_appeared_after_clicking_on_yandex_logo(self):
        self.click_on_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.find_element(CreateOrderLocator.YANDEX_BUTTON)
        current_url = self.driver.current_url
        assert current_url == 'https://dzen.ru/?yredirect=true', 'yandex main page should be opened'
