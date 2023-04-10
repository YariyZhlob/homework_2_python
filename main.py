
import time
from selene import be, have
from selene.support.shared import browser
import pytest


@pytest.fixture
def open_browser():
    browser.open('https://www.google.com/')
    browser.element('[id="L2AGLb"]').click()


@pytest.fixture
def maximize_browser():
    browser.browserSize = "1920x1080"

@pytest.fixture
def close_browser():
    browser.close()


def test_elements(open_browser, maximize_browser):
    browser.element('[class="gLFyf"]').should(be.blank).type('https://demoqa.com/automation-practice-form').press_enter()


def test_elements_no_available_items(open_browser):
    browser.element('[class="gLFyf"]').should(be.blank).type('abufufufuffjlsld;').press_enter()
    browser.element('[id="result-stats"]').should(have.text("Результатов: примерно 0"))
