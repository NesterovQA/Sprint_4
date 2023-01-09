from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


# Класс главной страницы
class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_first_question(self):
        self.driver.find_element(*MainPageLocators.QUESTION_1).click()

    def get_text_first_answer(self):
        text = self.driver.find_element(*MainPageLocators.ANSWER_1).text
        return text

    def click_on_second_question(self):
        self.driver.find_element(*MainPageLocators.QUESTION_2).click()

    def get_text_second_answer(self):
        text = self.driver.find_element(*MainPageLocators.ANSWER_2).text
        return text

    def click_on_third_question(self):
        self.driver.find_element(*MainPageLocators.QUESTION_3).click()

    def get_text_third_answer(self):
        text = self.driver.find_element(*MainPageLocators.ANSWER_3).text
        return text

    def click_on_fourth_question(self):
        self.driver.find_element(*MainPageLocators.QUESTION_4).click()

    def get_text_fourth_answer(self):
        text = self.driver.find_element(*MainPageLocators.ANSWER_4).text
        return text

    def click_on_fifth_question(self):
        self.driver.find_element(*MainPageLocators.QUESTION_5).click()

    def get_text_fifth_answer(self):
        text = self.driver.find_element(*MainPageLocators.ANSWER_5).text
        return text

    def click_on_sixth_question(self):
        self.driver.find_element(*MainPageLocators.QUESTION_6).click()

    def get_text_sixth_answer(self):
        text = self.driver.find_element(*MainPageLocators.ANSWER_6).text
        return text

    def click_on_seventh_question(self):
        self.driver.find_element(*MainPageLocators.QUESTION_7).click()

    def get_text_seventh_answer(self):
        text = self.driver.find_element(*MainPageLocators.ANSWER_7).text
        return text

    def click_on_eighth_question(self):
        self.driver.find_element(*MainPageLocators.QUESTION_8).click()

    def get_text_eighth_answer(self):
        text = self.driver.find_element(*MainPageLocators.ANSWER_8).text
        return text

    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.BUTTON_ACCEPT_COOKIES).click()

    def transfer_to_questions(self):
        element = self.driver.find_element(*MainPageLocators.ACCORDION_MENU)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_to_visible_sqoter_image_on_main_page(self):
        WebDriverWait(self.driver, 8).until(expected_conditions.visibility_of_element_located(MainPageLocators.SQOOTER_IMAGE))