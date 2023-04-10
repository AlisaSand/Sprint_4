from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ImportantQuestionSection:
    BUTTON_TO_ACCEPT_COOKIES = [By.XPATH, './/button[text()="да все привыкли"]']
    QUESTION_ABOUT_PAYMENT = [By.ID, 'accordion__heading-0']
    QUESTION_ABOUT_QUANTITY_OF_SCOOTER = [By.ID, 'accordion__heading-1']
    QUESTION_ABOUT_TIME_OF_USING = [By.ID, 'accordion__heading-2']
    QUESTION_ABOUT_ORDER_TODAY = [By.ID, 'accordion__heading-3']
    QUESTION_ABOUT_RETURNING_OF_SCOOTER = [By.ID, 'accordion__heading-4']
    QUESTION_ABOUT_SCOOTER_CHARGING = [By.ID, 'accordion__heading-5']
    QUESTION_ABOUT_ORDER_CANCELLATION = [By.ID, 'accordion__heading-6']
    QUESTION_ABOUT_LONG_DISTANCE_SHIPMENT = [By.ID, 'accordion__heading-7']
    ANSWER_ABOUT_PAYMENT = [By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]']
    ANSWER_ABOUT_QUANTITY_OF_SCOOTERS = [By.XPATH, './/p[text()="Пока что у нас так: один заказ — один самокат. '
                                                   'Если хотите покататься с друзьями, можете просто сделать '
                                                   'несколько заказов — один за другим."]']
    ANSWER_ABOUT_TIME_OF_USING = [By.XPATH, './/p[text()="Допустим, вы оформляете заказ на 8 мая.'
                                            ' Мы привозим самокат 8 мая в течение дня.'
                                            ' Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру.'
                                            ' Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]']
    ANSWER_ABOUT_ORDER_TODAY = [By.XPATH, './/p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]']
    ANSWER_ABOUT_RETURNING_OF_SCOOTER = [By.XPATH, './/p[text()="Пока что нет! '
                                                   'Но если что-то срочное — всегда можно позвонить в поддержку по '
                                                   'красивому номеру 1010."]']
    ANSWER_ABOUT_SCOOTER_CHARGING = [By.XPATH, './/p[text()="Самокат приезжает к вам с полной зарядкой. '
                                               'Этого хватает на восемь суток — даже если будете кататься без'
                                               ' передышек и во сне. Зарядка не понадобится."]']
    ANSWER_ABOUT_ORDER_CANCELLATION = [By.XPATH, './/p[text()="Да, пока самокат не привезли. Штрафа не будет, '
                                                 'объяснительной записки тоже не попросим. Все же свои."]']
    ANSWER_ABOUT_LONG_DISTANCE_SHIPMENT = [By.XPATH, './/p[text()="Да, обязательно. Всем самокатов!'
                                                     ' И Москве, и Московской области."]']

    def __init__(self, driver):
        self.driver = driver

    def get_on_questions_section(self):
        self.click_accept_cookies()
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_PAYMENT)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_accept_cookies(self):
        self.driver.find_element(*self.BUTTON_TO_ACCEPT_COOKIES).click()

    def click_on_question_about_payment(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_PAYMENT))).click()

    def click_on_question_about_quantity_of_scooters(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_QUANTITY_OF_SCOOTER))).click()

    def click_on_question_about_time_of_using(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_TIME_OF_USING))).click()

    def click_on_question_about_order_today(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_ORDER_TODAY))).click()

    def click_on_question_about_returning_of_scooter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_RETURNING_OF_SCOOTER))).click()

    def click_on_question_about_scooter_charging(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_SCOOTER_CHARGING))).click()

    def click_on_question_about_order_cancellation(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_ORDER_CANCELLATION))).click()

    def click_on_question_about_long_distance_shipment(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((
            self.QUESTION_ABOUT_LONG_DISTANCE_SHIPMENT))).click()

    def check_answer_on_payment_question(self):
        self.get_on_questions_section()
        self.click_on_question_about_payment()
        actual_result = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ANSWER_ABOUT_PAYMENT))).text
        expected_result = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actual_result == expected_result, 'There should be an answer on a question'

    def check_answer_on_question_about_quantity_of_scooters(self):
        self.get_on_questions_section()
        self.click_on_question_about_quantity_of_scooters()
        actual_result = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ANSWER_ABOUT_QUANTITY_OF_SCOOTERS))).text
        expected_result = 'Пока что у нас так: один заказ — один самокат.' \
                          ' Если хотите покататься с друзьями, ' \
                          'можете просто сделать несколько заказов — один за другим.'
        assert actual_result == expected_result, 'There should be an answer on a question'

    def check_answer_on_question_about_time_of_using(self):
        self.get_on_questions_section()
        self.click_on_question_about_time_of_using()
        actual_result = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ANSWER_ABOUT_TIME_OF_USING))).text
        expected_result = 'Допустим, вы оформляете заказ на 8 мая.'\
                            ' Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды'\
                            ' начинается с момента, когда вы оплатите заказ курьеру.'\
                            ' Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert actual_result == expected_result, 'There should be an answer on a question'

    def check_answer_about_order_today(self):
        self.get_on_questions_section()
        self.click_on_question_about_order_today()
        actual_result = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ANSWER_ABOUT_ORDER_TODAY))).text
        expected_result = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert actual_result == expected_result, 'There should be an answer on a question'

    def check_answer_about_returning_of_scooter(self):
        self.get_on_questions_section()
        self.click_on_question_about_returning_of_scooter()
        actual_result = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ANSWER_ABOUT_RETURNING_OF_SCOOTER))).text
        expected_result = 'Пока что нет! '\
                            'Но если что-то срочное — всегда можно позвонить в поддержку по '\
                            'красивому номеру 1010.'
        assert actual_result == expected_result, 'There should be an answer on a question'

    def check_answer_about_scooter_charging(self):
        self.get_on_questions_section()
        self.click_on_question_about_scooter_charging()
        actual_result = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ANSWER_ABOUT_SCOOTER_CHARGING))).text
        expected_result = 'Самокат приезжает к вам с полной зарядкой. '\
                            'Этого хватает на восемь суток — даже если будете кататься без'\
                            ' передышек и во сне. Зарядка не понадобится.'
        assert actual_result == expected_result, 'There should be an answer on a question'

    def check_answer_about_order_cancellation(self):
        self.get_on_questions_section()
        self.click_on_question_about_order_cancellation()
        actual_result = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ANSWER_ABOUT_ORDER_CANCELLATION))).text
        expected_result = 'Да, пока самокат не привезли. Штрафа не будет, '\
                            'объяснительной записки тоже не попросим. Все же свои.'
        assert actual_result == expected_result, 'There should be an answer on a question'

    def check_answer_about_long_distance_shipment(self):
        self.get_on_questions_section()
        self.click_on_question_about_long_distance_shipment()
        actual_result = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
            self.ANSWER_ABOUT_LONG_DISTANCE_SHIPMENT))).text
        expected_result = 'Да, обязательно. Всем самокатов!'\
                            ' И Москве, и Московской области.'
        assert actual_result == expected_result, 'There should be an answer on a question'
