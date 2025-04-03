import allure


from pages.base_page import BasePage
from locators.order_locators import OrderLocators, get_random_days_locator


class OrderPage(BasePage):
    @allure.step("Нажать на кнопку заказа вверху страницы")
    def click_top_order_button(self):
        self.click_on_element(OrderLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажать на кнопку заказа внизу страницы")
    def click_bottom_order_button(self):
        self.scroll_to_element(OrderLocators.BOTTOM_ORDER_BUTTON)
        self.click_on_element(OrderLocators.BOTTOM_ORDER_BUTTON)


    @allure.step("Заполнить первую форму заказа- Для кого самокат")
    def fill_first_order_form(self, first_name, last_name,address,dropdown_stantion, phone_number):
        self.send_keys_to_input(OrderLocators.FIRST_NAME, first_name)
        self.send_keys_to_input(OrderLocators.LAST_NAME, last_name)
        self.send_keys_to_input(OrderLocators.ADDRESS, address)
        self.click_on_element(OrderLocators.METRO_STANTION)
        self.send_keys_to_input(OrderLocators.METRO_STANTION, dropdown_stantion)
        self.click_on_element(OrderLocators.LIST_STANTION)
        self.send_keys_to_input(OrderLocators. PHON_NUMBER, phone_number)

    @allure.step("Нажать кнопку далее")
    def click_next(self):
        self.click_on_element(OrderLocators.THEN_BUTTON)

    @allure.step("Заполнить вторую форму заказа- Про аренду")
    def fill_second_order_form(self, data, dropdown_days, comment):
        self.send_keys_to_input(OrderLocators.CALENDAR, data)
        self.click_on_element(OrderLocators.CHECKBOX_BLACK)
        self.click_on_element(OrderLocators.RENTAL_PERIOD)
        self.click_on_element(OrderLocators.THREE_DAYS)
        self.send_keys_to_input(OrderLocators.COMMENT, comment)

    @allure.step("Заполнить рандомно вторую форму заказа- Про аренду")
    def fill_second_order_form_random(self, data, comment):
        days = get_random_days_locator()
        self.send_keys_to_input(OrderLocators.CALENDAR, data)
        self.click_on_element(OrderLocators.CHECKBOX_BLACK)
        self.click_on_element(OrderLocators.RENTAL_PERIOD)
        self.click_on_element(days)
        self.send_keys_to_input(OrderLocators.COMMENT, comment)

    @allure.step("Нажать кнопку Заказать и кнопку Да")
    def click_order(self):
        self.click_on_element(OrderLocators.FORM_ORDER_BUTTON)
        self.click_on_element(OrderLocators.YES_BTN)

    @allure.step("Получить текст всплывающего сообщения")
    def get_order_popup_text(self):
        return self.get_text_on_element(OrderLocators.ORDER_POPUP)