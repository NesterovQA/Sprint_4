from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class TestMainPage:

    @allure.title('Проверка отображения вопроса 1')
    def test_question_1(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.wait_to_visible_sqoter_image_on_main_page()
        main_page.accept_cookies()
        main_page.transfer_to_questions()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.QUESTION_1))
        main_page.click_on_first_question()
        assert main_page.get_text_first_answer() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка отображения вопроса 2')
    def test_question_2(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.wait_to_visible_sqoter_image_on_main_page()
        main_page.accept_cookies()
        main_page.transfer_to_questions()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.QUESTION_2))
        main_page.click_on_second_question()
        assert main_page.get_text_second_answer() == 'Пока что у нас так: один заказ — один самокат. Если хотите ' \
                                                     'покататься с друзьями, можете просто сделать несколько заказов ' \
                                                     '— один за другим.'

    @allure.title('Проверка отображения вопроса 3')
    def test_question_3(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.wait_to_visible_sqoter_image_on_main_page()
        main_page.accept_cookies()
        main_page.transfer_to_questions()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.QUESTION_3))
        main_page.click_on_third_question()
        assert main_page.get_text_third_answer() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая ' \
                                                    'в течение дня. Отсчёт времени аренды начинается с момента, ' \
                                                    'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в ' \
                                                    '20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка отображения вопроса 4')
    def test_question_4(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.wait_to_visible_sqoter_image_on_main_page()
        main_page.accept_cookies()
        main_page.transfer_to_questions()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.QUESTION_4))
        main_page.click_on_fourth_question()
        assert main_page.get_text_fourth_answer() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка отображения вопроса 5')
    def test_question_5(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.wait_to_visible_sqoter_image_on_main_page()
        main_page.accept_cookies()
        main_page.transfer_to_questions()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.QUESTION_5))
        main_page.click_on_fifth_question()
        assert main_page.get_text_fifth_answer() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в ' \
                                                    'поддержку по красивому номеру 1010.'

    @allure.title('Проверка отображения вопроса 6')
    def test_question_6(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.wait_to_visible_sqoter_image_on_main_page()
        main_page.accept_cookies()
        main_page.transfer_to_questions()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.QUESTION_6))
        main_page.click_on_sixth_question()
        assert main_page.get_text_sixth_answer() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на ' \
                                                    'восемь суток — даже если будете кататься без передышек и во сне.' \
                                                    ' Зарядка не понадобится.'

    @allure.title('Проверка отображения вопроса 7')
    def test_question_7(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.wait_to_visible_sqoter_image_on_main_page()
        main_page.accept_cookies()
        main_page.transfer_to_questions()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.QUESTION_7))
        main_page.click_on_seventh_question()
        assert main_page.get_text_seventh_answer() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной ' \
                                                       'записки тоже не попросим. Все же свои.'

    @allure.title('Проверка отображения вопроса 8')
    def test_question_8(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.wait_to_visible_sqoter_image_on_main_page()
        main_page.accept_cookies()
        main_page.transfer_to_questions()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.QUESTION_8))
        main_page.click_on_eighth_question()
        assert main_page.get_text_eighth_answer() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
