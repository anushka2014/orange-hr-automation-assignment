import time

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.personal_info_management import PIMPage

def test_orangehrm_flow(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    login.login("Admin", "admin123")
    time.sleep(3)

    pim = PIMPage(driver)
    pim.go_to_pim()

    employees = [("Chris", "Evans"),("Marget","Robbie")]
    for fname, lname in employees:
        pim.add_employee(fname, lname)

    pim.verify_employee("Chris")

    dashboard = DashboardPage(driver)
    dashboard.logout()
    time.sleep(2)
    # driver.quit()