class ProductListPage:
    def __init__(self, page):
        self.page = page
        self.add_item_btn = page.locator("mat-card").filter(has_text="Apple Juice (1000ml) 1.99¤Add").get_by_label("Add to Basket")
        self.shopping_cart_btn = page.get_by_label("Show the shopping cart")
    
    
    def click_add_item(self):
        self.add_item_btn.click()

    def click_shopping_cart(self):
        self.page.wait_for_timeout(5000)
        self.shopping_cart_btn.click()