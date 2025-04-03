import allure

from helper import create_user_credentials, generate_random_address, generate_random_metro_station, create_data
from pages.order_page import OrderPage
from data import Credentials




class TestOrderByTopButton:
    @allure.title("Тест успешного оформления заказа по верхней кнопке Заказать")
    def test_successful_order_top_btn(self, driver):

        order_page = OrderPage(driver)


        order_page.click_top_order_button()
        order_page.fill_first_order_form(Credentials.FIRST_NAME, Credentials.LAST_NAME, Credentials.ADDRESS, Credentials.DROPDOWN_STANTION, Credentials.PHONE_NUMBER)
        order_page.click_next()
        order_page.fill_second_order_form(Credentials.DATA,Credentials.DROPDOWN_DAYS, Credentials.COMMENT)
        order_page.click_order()
        popup_text = order_page.get_order_popup_text()

        assert "Заказ оформлен" in popup_text

    @allure.title("Тест успешного оформления заказа по нижней кнопке Заказать")
    def test_successful_order_bottom_btn(self, driver):
        first_name, last_name, phone_number = create_user_credentials()
        address = generate_random_address()
        metro_station = generate_random_metro_station()
        data = create_data()
        order_page = OrderPage(driver)

        order_page.click_bottom_order_button()
        order_page.fill_first_order_form(first_name, last_name, address, metro_station, phone_number)
        order_page.click_next()
        order_page.fill_second_order_form_random(data, Credentials.COMMENT)
        order_page.click_order()
        popup_text = order_page.get_order_popup_text()

        assert "Заказ оформлен" in popup_text