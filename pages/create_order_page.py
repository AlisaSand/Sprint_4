from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CreateOrderPage:
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

    def __init__(self, driver):
        self.driver = driver

    def click_on_create_order_button_in_header(self):
        self.driver.find_element(*self.CREATE_ORDER_BUTTON_IN_HEADER).click()

    def click_on_create_order_button_on_bottom(self):
        self.driver.find_element(*self.CREATE_ORDER_BUTTON_ON_BOTTOM).click()

    def fill_name_field(self, name):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.NAME_FIELD))).send_keys(name)

    def fill_surname_field(self, surname):
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)

    def fill_address_field(self, address):
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def fill_metro_station_cherkizovskaya_field(self):
        self.driver.find_element(*self.METRO_SELECT).click()
        self.driver.find_element(*self.METRO_SELECT_CHERKIZOVSKAYA).click()

    def fill_metro_station_sokolniki_field(self):
        self.driver.find_element(*self.METRO_SELECT).click()
        self.driver.find_element(*self.METRO_SELECT_SOKOLNIKI).click()

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def click_on_futher_button(self):
        self.driver.find_element(*self.FUTHER_BUTTON).click()

    def click_on_scooter_logo(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.SCOOTER_LOGO))).click()

    def click_on_yandex_logo(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.YANDEX_LOGO))).click()

    def get_to_bottom_order_creation_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.CREATE_ORDER_BUTTON_ON_BOTTOM)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def fill_about_rent_form_black_scooter(self, date, comment):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ABOUT_RENT_HEADER)))
        self.driver.find_element(*self.SHIPPING_DATE).click()
        self.driver.find_element(*self.SHIPPING_DATE).send_keys(date)
        self.driver.find_element(*self.SELECT_DAYS).click()
        self.driver.find_element(*self.DAYS_FOR_RENT_FOR_BLACK_SCOOTER_SELECT).click()
        self.driver.find_element(*self.SCOOTER_COLOR_BLACK_SELECT).click()
        self.driver.find_element(*self.COMMENT).send_keys(comment)
        self.driver.find_element(*self.PUBLISH_ORDER_BUTTON).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.CONFIRMATION_BUTTON))).click()

    def fill_about_rent_form_grey_scooter(self, date, comment):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ABOUT_RENT_HEADER)))
        self.driver.find_element(*self.SHIPPING_DATE).click()
        self.driver.find_element(*self.SHIPPING_DATE).send_keys(date)
        self.driver.find_element(*self.SELECT_DAYS).click()
        self.driver.find_element(*self.DAYS_FOR_RENT_FOR_GREY_SCOOTER_SELECT).click()
        self.driver.find_element(*self.SCOOTER_COLOR_GREY_SELECT).click()
        self.driver.find_element(*self.COMMENT).send_keys(comment)
        self.driver.find_element(*self.PUBLISH_ORDER_BUTTON).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.CONFIRMATION_BUTTON))).click()

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

        assert WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ORDER_CREATED_HEADER))).is_displayed(), "There should be a header with success message"

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

        assert WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ORDER_CREATED_HEADER))).is_displayed(), "There should be a header with success message"

    def check_main_scooter_page_appeared_after_clicking_on_scooter_logo(self):
        self.click_on_create_order_button_in_header()
        self.click_on_scooter_logo()
        assert WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.MAIN_HEADER))).is_displayed(), 'Scooter main page should be opened'

    def check_main_yandex_page_appeared_after_clicking_on_yandex_logo(self):
        self.click_on_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.YANDEX_BUTTON)))
        current_url = self.driver.current_url
        assert current_url == 'https://dzen.ru/?yredirect=true', 'yandex main page should be opened'
