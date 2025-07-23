import allure

from curl import *
from locators.logo_locators import LogoLocators
from pages.base_page import BasePage

class LogoPage(BasePage):
    @allure.step("Нажать на логотип Яндекс")
    def click_to_Yandex_logo(self):
        self.click_on_element(LogoLocators.YANDEX_LOGO)

    @allure.step("Нажать на логотип Самокат")
    def click_to_Scooter_logo(self):
        self.click_on_element(LogoLocators.SCOOTER_LOGO)

    @allure.step("Получить URL страницы в новом окне")
    def get_new_window_url(self):
        self.wait_and_switch_to_new_window()
        self.wait_for_url(DZEN_URL)

    @allure.step("Нажать на кнопку Заказать")
    def click_top_order_button(self):
        self.click_on_element(LogoLocators.ORDER_BUTTON)
