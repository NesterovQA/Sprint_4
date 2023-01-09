import time

from pages.order_page import OrderPage
import allure


class TestOrderPage:

    @allure.title('Тест регистрации через верхнюю кнопку заказа')
    def test_order_sqooter_through_button_up(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.wait_to_visible_sqooter_image_on_main_page()
        order_page.click_on_order_button_up()
        order_page.set_primary_date_for_order('Виталий', 'Нестеров', 'г.Рязань ул. Семашко, 14', 'Рязанский проспект', '+79209526466')
        order_page.wait_to_clickabele_back_button()
        order_page.set_secondary_date_for_order('01.02.2023', 'Пожалуйста, оставьте у подьезда')
        order_page.click_on_order_button_in_order()
        order_page.click_on_yes_confirm_button()
        assert "Заказ оформлен" in order_page.get_text_completed_order_info()

    @allure.title('Тест регистрации через нижнюю кнопку заказа')
    def test_order_sqooter_through_button_down(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.wait_to_visible_sqooter_image_on_main_page()
        order_page.transfer_to_button_order_down()
        order_page.wait_to_clickabele_order_down_button()
        order_page.click_on_order_button_down()
        order_page.set_primary_date_for_order('Иван', 'Иванов', 'г.Москва ул.Загородное шоссе д.17.кв 29',
                                              'Комсомольская', '+792539445566')
        order_page.wait_to_clickabele_back_button()
        order_page.set_secondary_date_for_order('10.02.2023', 'Домофон не работает')
        order_page.click_on_order_button_in_order()
        order_page.click_on_yes_confirm_button()
        assert "Заказ оформлен" in order_page.get_text_completed_order_info()

    @allure.title('Тест перехода на гл страницу самоката через кнопку логотип')
    def test_click_on_logo_sqooter_main_page_transfer_to_main_page(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.wait_to_visible_sqooter_image_on_main_page()
        order_page.transfer_to_button_order_down()
        order_page.wait_to_clickabele_order_down_button()
        order_page.click_on_order_button_down()
        order_page.click_on_logo_sqooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Тест открытия сайта дзена по клику на логотип яндекса')
    def test_click_on_logo_yandex_main_page_transfer_to_yandex(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.wait_to_visible_sqooter_image_on_main_page()
        order_page.transfer_to_button_order_down()
        order_page.wait_to_clickabele_order_down_button()
        order_page.click_on_order_button_down()
        order_page.click_on_logo_yandex()
        order_page.select_new_windows()
        order_page.wait_to_visible_panel_to_dzen()
        assert 'dzen.ru' in driver.current_url


