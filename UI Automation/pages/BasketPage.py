class BasketPage:
    def __init__(self, page):
        self.page = page
        self.checkout_btn = page.get_by_role("button", name="Checkout")
        self.add_new_address_btn = page.get_by_label("Add a new address")
    
    
    def click_checkout(self):
        self.checkout_btn.click()