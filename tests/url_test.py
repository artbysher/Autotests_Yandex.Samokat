import allure
from curl import *
from pages.url_page import LogoPage


class TestYandexLogo:
    @allure.title("Тест на открытие главной страницы Дзена через логотип Яндекс")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_to_Yandex_logo()
        logo_page.get_new_window_url()

        assert  logo_page.check_url(DZEN_URL)

    @allure.title("Тест на открытие главной страницы сайта через логотип Самокат")
    def test_scooter_logo_redirects_to_dzen(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_top_order_button()
        logo_page.click_to_Scooter_logo()

        assert logo_page.check_url(MAIN_SITE)

