import allure
import pytest

import data
from pages.quest_page import QuestPage


class TestAnswerQoest:
    @allure.title("Тест на соответсвие вопросов и ответов в разделе Вопросы о важном")
    @pytest.mark.parametrize('quest_number, expected_text', data.QuestText.quest_text)
    def test_card_names(self, driver, quest_number, expected_text):

        quest_page = QuestPage(driver)

        quest_page.click_on_qust(quest_number)


        assert quest_page.check_answ_text(expected_text,quest_number)
