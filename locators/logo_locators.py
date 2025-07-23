from selenium.webdriver.common.by import By


class LogoLocators:
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']/img[@alt='Yandex']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']/img[@alt='Scooter']")