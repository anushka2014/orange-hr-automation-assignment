from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_pim(self):
        self.driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']").click()
        time.sleep(2)

    def add_employee(self, fname, lname):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, 'firstName').send_keys(fname)
        self.driver.find_element(By.NAME, 'lastName').send_keys(lname)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def verify_employee(self, fname):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee List']"))).click()

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card")))

        rows = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card")

        for row in rows:
            try:
                cols = row.find_elements(By.CSS_SELECTOR, "div.oxd-table-cell")
                first_middle_name = cols[2].text.strip()

                if first_middle_name.lower() == fname.lower():
                    cols[2].click()
                    time.sleep(5)
                    print("Name:",fname,"Verified")
                    return True

            except Exception as e:
                print("Error while verifying:", e)
                continue

        print("Employee not found")
        return False
