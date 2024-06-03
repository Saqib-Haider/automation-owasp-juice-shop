class AddressPage:
    def __init__(self, page):
        self.page = page
        self.add_new_address_btn = page.get_by_label("Add a new address")
        self.country = page.get_by_placeholder("Please provide a country.")
        self.name = page.get_by_placeholder("Please provide a name.")
        self.number = page.get_by_placeholder("Please provide a mobile")
        self.zip_code = page.get_by_placeholder("Please provide a ZIP code.")
        self.address = page.get_by_placeholder("Please provide an address.")
        self.city = page.get_by_placeholder("Please provide a city.")
        self.state = page.get_by_placeholder("Please provide a state.")
        self.submit_btn = page.get_by_role("button", name="send Submit")
        self.address_visibility = page.get_by_role ("table")
    
    
    def click_add_new_address(self):
        self.add_new_address_btn.click()

    def enter_country(self, country):
        self.country.fill(country)

    def enter_name(self, name):
        self.name.fill(name)
    
    def enter_number(self, number):
        self.number.fill(number)
    
    def enter_zip_code(self, zip_code):
        self.zip_code.fill(zip_code)
    
    def enter_address(self, address):
        self.address.fill(address)
    
    def enter_city(self, city):
        self.city.fill(city)
    
    def enter_state(self, state):
        self.state.fill(state)
    
    def click_submit(self):
        self.submit_btn.click()

    def fill_up_form(self, country, name, number, zip_code, address, city, state):
        self.enter_country(country)
        self.enter_name(name)
        self.enter_number(number)
        self.enter_zip_code(zip_code)
        self.enter_address(address)
        self.enter_city(city)
        self.enter_state(state)
        self.click_submit()

    def check_address(self):
        return self.address_visibility