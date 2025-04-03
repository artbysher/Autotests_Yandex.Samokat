import random

from selenium.webdriver.common.by import By
from data import DaysOptions


class OrderLocators:
    TOP_ORDER_BUTTON = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
#Локаторы для формы Для кого самокат
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STANTION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    STANTION = (By.XPATH, "//input[@value='Комсомольская']")
    LIST_STANTION = (By.XPATH, ".//li[@class='select-search__row']")
    PHON_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    THEN_BUTTON = (By.XPATH, "//button[text()='Далее']")

# Локаторы для формы Про аренду
    CALENDAR = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    THREE_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    CHECKBOX_BLACK = (By.ID, "black")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    FORM_ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    YES_BTN = (By.XPATH, "//button[text()='Да']")

    ORDER_POPUP = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
#Рандомный локатор для колличества суток
def get_random_days_locator():
    random_day = random.choice(DaysOptions.DAYS_OPTIONS)
    return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{random_day}']")
