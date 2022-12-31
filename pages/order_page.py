from selenium.webdriver import Keys
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_order_button_up(self):
        self.driver.find_element(*MainPageLocators.ORDER_PAGE_BUTTON_UP).click()

    def click_on_order_button_down(self):
        self.driver.find_element(*MainPageLocators.ORDER_PAGE_BUTTON_DOWN).click()

    def click_on_order_button_in_order(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_IN_ORDER).click()

    def set_name_field(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_sur_name_field(self, sur_name):
        self.driver.find_element(*OrderPageLocators.SUR_NAME_FIELD).send_keys(sur_name)

    def set_address_field(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_metro_station_field(self, station):
        self.driver.find_element(*OrderPageLocators.METRO_STATION).click()
        self.driver.find_element(*OrderPageLocators.METRO_STATION).send_keys(station)
        self.driver.find_element(*OrderPageLocators.METRO_STATION).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def click_on_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def set_order_date(self, order_date):
        self.driver.find_element(*OrderPageLocators.ORDER_DATE_FIELD).click()
        self.driver.find_element(*OrderPageLocators.ORDER_DATE_FIELD).send_keys(order_date)
        self.driver.find_element(*OrderPageLocators.ORDER_DATE_FIELD).send_keys(Keys.ENTER)

    def set_rent_time(self):
        self.driver.find_element(*OrderPageLocators.TIME_RENT).click()
        self.driver.find_element(*OrderPageLocators.QUANTITY_DAY).click()

    def set_colour_sqooter(self):
        self.driver.find_element(*OrderPageLocators.BLACK_COLOUR_FOR_SQOOTER).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    # шаг ввода данных для заказа на стр для кого самокат

    def set_primary_date_for_order(self, Name, Surname, address, station, phone):
        self.set_name_field(Name)
        self.set_sur_name_field(Surname)
        self.set_address_field(address)
        self.set_metro_station_field(station)
        self.set_phone_number(phone)
        self.click_on_next_button()

    def set_secondary_date_for_order(self, order_date, comment):
        self.set_order_date(order_date)
        self.set_rent_time()
        self.set_colour_sqooter()
        self.set_comment(comment)

    def click_on_yes_confirm_button(self):
        self.driver.find_element(*OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

    def get_text_completed_order_info(self):
        text = self.driver.find_element(*OrderPageLocators.ORDER_INFO_TABLE).text
        return text

    def click_on_view_status_order_button(self):
        self.driver.find_element(*OrderPageLocators.VIEW_STATUS_ORDER_BUTTON).click()

    def transfer_to_button_order_down(self):
        element = self.driver.find_element(*MainPageLocators.ORDER_PAGE_BUTTON_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_logo_sqooter(self):
        self.driver.find_element(*OrderPageLocators.SQOOTER_LOGO).click()

    def click_on_logo_yandex(self):
        self.driver.find_element(*OrderPageLocators.YANDEX_LOGO).click()

    def wait_to_visible_sqooter_image_on_main_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.WHO_IS_THE_SCOOTER_FOR_LABEL))

    def wait_to_clickabele_back_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(OrderPageLocators.BACK_BUTTON))

    def wait_to_visible_panel_to_dzen(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.DZEN_LOCATOR))

    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.BUTTON_ACCEPT_COOKIES).click()

    def select_new_windows(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
