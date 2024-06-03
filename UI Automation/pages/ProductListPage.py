class ProductListPage:
    def __init__(self, page):
        self.page = page
        self.add_item_btn = page.locator("mat-card").filter(has_text="Apple Juice (1000ml) 1.99¤Add").get_by_label("Add to Basket")
        self.shopping_cart_btn = page.get_by_label("Show the shopping cart")
        self.search_btn = page.get_by_text("search")
        self.search = page.locator("#mat-input-0")
    
    
    def click_add_item(self):
        self.add_item_btn.click()

    def click_shopping_cart(self):
        self.page.wait_for_timeout(5000)
        self.shopping_cart_btn.click()


    def click_search(self):
        self.search_btn.click()

    def enter_search(self, search):
        self.search.fill(search)

    def keystroke_enter(self, enter):
        self.search_btn.press(enter)


    def search_items(self, search, enter):
        self.click_search()
        self.enter_search(search)
        self.page.wait_for_timeout(2000)
        self.keystroke_enter(enter)