from pages.important_question_page import ImportantQuestionSection


class TestAnswerOfImportantQuestion:
    def test_question_about_payment(self, driver):
        questions = ImportantQuestionSection(driver)
        questions.check_answer_on_payment_question()

    def test_question_about_quantity_of_scooters(self, driver):
        questions = ImportantQuestionSection(driver)
        questions.check_answer_on_question_about_quantity_of_scooters()

    def test_question_about_time_of_using(self, driver):
        questions = ImportantQuestionSection(driver)
        questions.check_answer_on_question_about_time_of_using()

    def test_question_about_order_today(self, driver):
        questions = ImportantQuestionSection(driver)
        questions.check_answer_about_order_today()

    def test_question_about_returning_of_scooter(self, driver):
        questions = ImportantQuestionSection(driver)
        questions.check_answer_about_returning_of_scooter()

    def test_question_about_scooter_charging(self, driver):
        questions = ImportantQuestionSection(driver)
        questions.check_answer_about_scooter_charging()

    def test_question_about_order_cancellation(self, driver):
        questions = ImportantQuestionSection(driver)
        questions.check_answer_about_order_cancellation()

    def test_question_about_long_distance_shipment(self, driver):
        questions = ImportantQuestionSection(driver)
        questions.check_answer_about_long_distance_shipment()
