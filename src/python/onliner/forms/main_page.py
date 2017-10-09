import csv
import os
import random
import re

from src.python.framework.base_page import BasePage
from src.resources import locators


class MainPage(BasePage):
    # Try to find all popular themes and go to the one of them randomly
    def find_and_click_theme(self):
        themes = self.driver.find_elements(*locators.MainPageLocators.themes)
        while True:
            choice = random.choice(themes)
            if choice.is_displayed():
                break
        choice_text = choice.text
        choice.click()
        return choice_text

    def find_opinions(self):
        opinion_text_pattern = re.compile(r'text">(.+?)</div>', re.MULTILINE)
        opinion_author_pattern = re.compile(r'author">(.+?)</nobr>', re.MULTILINE)
        op_text = opinion_text_pattern.findall(self.driver.page_source)
        op_author = opinion_author_pattern.findall(self.driver.page_source)

        opinions = []
        for l in range(len(op_text)):
            author = re.split(r' <nobr>', op_author.pop())
            opinions.append((author[0] + ' ' + author[1], op_text.pop()))

        with open(os.path.abspath('../../../reports/opinions.cvs'), 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(opinions)