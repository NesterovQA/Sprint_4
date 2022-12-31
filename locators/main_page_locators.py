import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPageLocators:
    QUESTION_1 = (By.ID, "accordion__heading-0")
    # QUESTION_1_2 = (By.XPATH, ".//div[@id='accordion__heading-0']")
    # ACCORDION_PANEL_1 = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    ANSWER_1 = (By.XPATH, ".//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    # ANSWER_2 = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    ANSWER_2 = (By.XPATH, ".//p[contains(text(), 'Пока что у нас так: один заказ — один самокат. Если')]")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    ANSWER_3 = (By.XPATH, ".//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая')]")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    ANSWER_4 = (By.XPATH, ".//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    ANSWER_5 = (By.XPATH, ".//p[contains(text(), 'Пока что нет! Но если что-то срочное')]")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    ANSWER_6 = (By.XPATH, ".//p[contains(text(), 'Самокат приезжает к вам с полной зарядкой')]")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    ANSWER_7 = (By.XPATH, ".//p[contains(text(), 'Да, пока самокат не привезли. Штрафа не будет,')]")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    ANSWER_8 = (By.XPATH, ".//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")
    ACCORDION_MENU = (By.XPATH, ".//*[@class='accordion']")
    # ORDER_PAGE_BUTTON_DOWN =(By.XPATH, '(//*[contains(@class, "text input__textfield")])[1]')
    BUTTON_ACCEPT_COOKIES = (By.XPATH, ".//*[@id='rcc-confirm-button']")
    SQOOTER_IMAGE = (By.XPATH, ".//img[@alt='Scooter blueprint']")
    ORDER_PAGE_BUTTON_UP = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_PAGE_BUTTON_DOWN = (By.XPATH, ".//*[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
