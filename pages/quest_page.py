import allure
from pages.base_page import BasePage
from locators.quest_locators import QuestLocators


class QuestPage(BasePage):
    @allure.step("Открыть вопрос")
    def click_on_qust(self, quest_number):
        quest_locator = QuestLocators.quest_number(quest_number)
        self.scroll_to_element(QuestLocators.ALL_QUESTION)
        self.wait_for_element(quest_locator)
        self.scroll_to_element(quest_locator)
        self.click_on_element(quest_locator)


    @allure.step("Сравни текст ответа")
    def check_answ_text(self, expected_text, answ_number):
        answ_locator = QuestLocators.answ_number(answ_number)
        self.wait_for_element(answ_locator)

        actual_text = self.get_text_on_element(answ_locator)
        return actual_text == expected_text
