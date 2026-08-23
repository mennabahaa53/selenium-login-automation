from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage: 
    URL = "https://the-internet.herokuapp.com/login" 

    def __init__(self, driver): 
        self.driver = driver 

    def open(self): 
        self.driver.get(self.URL) 

    def enter_username(self, username): 
        self.driver.find_element(By.ID, "username").send_keys(username) 

    def enter_password(self, password): 
        self.driver.find_element(By.ID, "password").send_keys(password) 

    def click_login(self): 
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click() 

    def get_success_message(self): 
        return self.driver.find_element(By.CSS_SELECTOR, ".flash.success").text 

    def get_error_message(self): 
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash"))
        )
        return element.text

    def login(self, username, password): 
        self.enter_username(username) 
        self.enter_password(password) 
        self.click_login()