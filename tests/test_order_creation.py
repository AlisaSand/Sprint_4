from faker import Faker
from datetime import datetime, timedelta
from pages.create_order_page import CreateOrderPage

fake = Faker("ru_RU")


class TestOrderCreation:
    def test_create_order_by_order_creation_button_in_header(self, driver):
        name = fake.first_name()
        surname = fake.last_name()
        address = fake.street_name()
        phone_number = fake.phone_number()
        replaced_symbols = ['(', ')', '-', ' ']
        for s in replaced_symbols:
            phone_number = phone_number.replace(s, '')
        day = (datetime.now() + timedelta(days=2)).day
        month = datetime.month
        year = datetime.year
        date = str(day) + "." + str(month) + "." + str(year)
        carrier_comment = fake.first_name()
        create_order_page = CreateOrderPage(driver)
        create_order_page.check_creation_order_by_clicking_on_order_button_in_header(
            name, surname, address, phone_number, date, carrier_comment
        )

    def test_create_order_by_order_creation_button_bottom(self, driver):
        name = fake.first_name()
        surname = fake.last_name()
        address = fake.street_name()
        phone_number = fake.phone_number()
        replaced_symbols = ['(', ')', '-', ' ']
        for s in replaced_symbols:
            phone_number = phone_number.replace(s, '')
        day = (datetime.now() + timedelta(days=4)).day
        month = datetime.month
        year = datetime.year
        date = str(day) + "." + str(month) + "." + str(year)
        carrier_comment = fake.first_name()
        create_order_page = CreateOrderPage(driver)
        create_order_page.check_creation_order_by_clicking_on_bottom_order_button(
            name, surname, address, phone_number, date, carrier_comment
        )

    def test_main_scooter_page_is_open_by_clicking_on_scooter_logo(self, driver):
        create_order_page = CreateOrderPage(driver)
        create_order_page.check_main_scooter_page_appeared_after_clicking_on_scooter_logo()

    def test_yandex_page_is_open_by_clocking_on_yandex_logo(self, driver):
        create_order_page = CreateOrderPage(driver)
        create_order_page.check_main_yandex_page_appeared_after_clicking_on_yandex_logo()
