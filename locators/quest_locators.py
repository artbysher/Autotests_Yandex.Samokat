from selenium.webdriver.common.by import By


class QuestLocators:
    ALL_QUESTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    @staticmethod
    def quest_number(quest):
        return By.XPATH, f"//div[@id='accordion__heading-{quest}']"

    @staticmethod
    def answ_number(quest):
        return By.XPATH, f"//div[@id='accordion__panel-{quest}']//p"