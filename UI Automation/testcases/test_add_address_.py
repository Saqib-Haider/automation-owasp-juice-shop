from pages.LoginPage import LoginPage
from pages.BasketPage import BasketPage
from pages.AddressPage import AddressPage
from pages.ProductListPage import ProductListPage
from user import information
from playwright.sync_api import Playwright, sync_playwright, expect, Page
import allure

def test_add_items_to_basket(set_up_teardown)-> None:
    page = set_up_teardown
    email = information.email
    password = information.password
    country = information.country
    name = information.name
    number = information.number
    zip_code = information.zip_code
    address = information.address
    city = information.city
    state = information.state
    login_page = LoginPage(page)
    login_page.login(email,password)
    product_page = ProductListPage(page)
    product_page.click_add_item()
    product_page.click_shopping_cart()
    basket_page = BasketPage(page)
    basket_page.click_checkout()
    address_page = AddressPage(page)
    address_page.click_add_new_address()
    address_page.fill_up_form(country, name, number, zip_code, address, city, state)

#Check after adding address and submitting
    expect(address_page.check_address()).to_be_visible()

