import booking.constants as const 
import os 
from selenium import webdriver 

#constructuor of the booking class 
class Booking(webdriver.Chrome): 

    def __init__(self, driver_path=r"C:/Users/User/selenium_drivers", teardown=False): 
        self.driver_path = driver_path 
        self.teardown = teardown 
        os.environ['PATH'] += self.driver_path 
        # super is used to instantiate the webdriver.Chrome class 
        super(Booking, self).__init__() 
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, *args) -> None:
        if self.teardown: 
            return super().__exit__(*args)

    def land_first_page(self): 
        self.get(const.BASE_URL)

    def change_currency(self, currency=None): 
        
        currency_element = self.find_element_by_css_selector( 
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click() 

        selected_currency_element = self.find_element_by_css_selector(
            'a[data-modal-header-async-url-param*="selected_currency=USD"]'
        )
        selected_currency_element.click()

    def select_place(self, place_to_go): 
        search_field = self.find_element_by_id('ss')
        # clears the text 
        search_field.clear() 
        search_field.send_keys(place_to_go)

        self.find_element_by_css_selector(
            'li[data-i="0"]'
        ).click() 

    def select_dates(self, check_in_date, check_out_date): 

        # self.implicitly_wait(15)
        self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        ).click() 

        # self.implicitly_wait(15)
        self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        ).click() 

    
    def select_adults(self, count=0): 
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()
        temp = count 

        while True: 
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click() 
            adults_value_element = self.find_element_by_id('group_adults')
            # should give back the adults count 
            value = adults_value_element.get_attribute('value')

            # exit loop once the value attrib equals to one 
            if int(value) == 1: 
                break

        while temp > 1: 
            increase_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Increase number of Adults"]'
            )
            increase_adults_element.click() 
            temp = temp - 1 


       
    def submit_query(self): 
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click() 
        

      
            
            

