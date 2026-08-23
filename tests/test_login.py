import pytest 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from pages.login_page import LoginPage 

@pytest.fixture 
def browser(): 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    driver.maximize_window() 
    yield driver 
    driver.quit() 

def test_valid_login(browser): 
    page = LoginPage(browser) 
    page.open() 
    page.login("tomsmith", "SuperSecretPassword!") 
    message = page.get_success_message() 
    assert "You logged into a secure area!" in message 
    print(f"✅ Success message: {message}") 

def test_wrong_password(browser): 
    page = LoginPage(browser) 
    page.open() 
    page.login("tomsmith", "wrongpassword") 
    message = page.get_error_message() 
    assert "Your password is invalid!" in message 
    print(f"✅ Error message: {message}") 

def test_wrong_username(browser): 
    page = LoginPage(browser) 
    page.open() 
    page.login("wronguser", "SuperSecretPassword!") 
    message = page.get_error_message() 
    assert "Your username is invalid!" in message 
    print(f"✅ Error message: {message}")