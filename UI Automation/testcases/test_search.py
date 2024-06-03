from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from user import information
from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_add_items_to_basket(set_up_teardown)-> None:
    page = set_up_teardown
    email = information.email
    password = information.password
    search = information.search
    enter = information.enter
    login_page = LoginPage(page)
    login_page.login(email,password)
    product_page = ProductListPage(page)
    product_page.search_items(search, enter)

#Check for 2 apple items in search results
    expect(page.get_by_text("– 2 of 2")).to_be_visible()
    search_results = page.query_selector_all("app-search-result .mat-grid-tile")
    assert len(search_results) == 2

#Check for no banana in search items
    banana_items = [result for result in search_results if "banana" in result.inner_text().lower()]
    assert len(banana_items) == 0