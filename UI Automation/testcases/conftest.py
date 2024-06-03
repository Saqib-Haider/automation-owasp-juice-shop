from playwright.sync_api import Playwright
import pytest

@pytest.fixture()
def set_up_teardown(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://juice-shop.herokuapp.com/#/login")
    yield page
    context.close()
    browser.close()