# selenium-login-automation
Automated login testing framework using Selenium WebDriver, Python, and Pytest with Page Object Model design pattern.
# 🤖 Selenium Login Automation Framework 
Automated browser testing framework built with Python, Selenium WebDriver, and Pytest. 
## 🛠️ Tech Stack 
- Python 3.11
- Selenium WebDriver
- Pytest
- Page Object Model Pattern
## ✅ What It Tests 
- Valid login with correct credentials
- Invalid login with wrong password
- Invalid login with wrong username
## 📁 Project Structure
selenium-project/

pages/
       login_page.py   ← Page Object
    
tests/
      test_login.py   ← Test Cases
    

## ▶️ How To Run
    ```bash
    pip install selenium pytest webdriver-manager
    pytest tests/test_login.py -v -s

## 📊 Test Results

-   test\_valid\_login ✅ PASSED
-   test\_wrong\_password ✅ PASSED
-   test\_wrong\_username ✅ PASSED

      
