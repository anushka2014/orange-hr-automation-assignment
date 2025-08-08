from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        wait = WebDriverWait(self.driver, 10)
        user_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name")))
        user_dropdown.click()
        logout_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
        logout_option.click()