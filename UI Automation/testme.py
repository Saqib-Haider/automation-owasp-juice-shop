import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://juice-shop.herokuapp.com/#/login")
    page.get_by_label("Close Welcome Banner").click()
    page.get_by_label("Text field for the login email").fill("saqibhaider567@gmail.com")
    page.get_by_label("Text field for the login password").fill("abc321@")
    page.get_by_label("Login", exact=True).click()
    page.locator("mat-card").filter(has_text="Apple Juice (1000ml) 1.99¤Add").get_by_label("Add to Basket").click()
    time.sleep(3)
    page.get_by_label("Show the shopping cart").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_label("Add a new address").click()
    page.get_by_placeholder("Please provide a country.").click()
    page.get_by_placeholder("Please provide a country.").fill("bangladesh")
    page.get_by_placeholder("Please provide a name.").fill("tester sh")
    page.locator("div").filter(has_text=re.compile(r"^Mobile Number \*$")).nth(2).click()
    page.get_by_placeholder("Please provide a mobile").fill("01766925564")
    page.get_by_placeholder("Please provide a ZIP code.").fill("1230")
    page.get_by_placeholder("Please provide an address.").fill("dhaka")
    page.locator("div").filter(has_text=re.compile(r"^City \*$")).nth(2).click()
    page.get_by_placeholder("Please provide a city.").fill("dhaka")
    page.get_by_placeholder("Please provide a state.").fill("dhaka")
    page.get_by_role("button", name="send Submit").click()
    #page.get_by_role("cell", name="tester sh").click()

    context.close()
    browser.close()


def runnew(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://juice-shop.herokuapp.com/#/login")
    page.get_by_label("Close Welcome Banner").click()
    page.get_by_label("Text field for the login email").click()
    page.get_by_label("Text field for the login email").fill("saqibhaider567@gmail.com")
    page.get_by_label("Text field for the login password").click()
    page.get_by_label("Text field for the login password").fill("abc321@")
    page.get_by_label("Login", exact=True).click()
    page.get_by_text("search").click()
    page.locator("#mat-input-0").fill("apple")
    time.sleep(3)
    page.locator("#mat-input-0").press("Enter")
    #page.locator("mat-grid-list").click()
    #page.locator("div").filter(has_text="Search Results - apple Apple").nth(1).click()
    #page.get_by_role("link", name="sent back to us").dblclick()
    #page.locator("mat-grid-list div").filter(has_text="Apple Juice (1000ml) 1.99¤Add").nth(1).click()
    page.get_by_text("– 2 of 2").click()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    #run(playwright)
    runnew(playwright)