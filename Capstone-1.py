"""
Test case ID:TC_login_01

Test objective:
  Successful employee login to OrangeHRM Portal
Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
 1.In the login panel,enter the user name(Test data: “Admin”)
2.Enter the password for ESS User account in the password field (Test data:”admin123”)
3.Click”login”button

 Expected result:
The user is logged successfully
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located(self.username_locator))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located(self.password_locator))
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button_locator))
        login_button.click()
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.dashboard_header_locator = (By.XPATH, "//h6[text()='Dashboard']")

    def is_dashboard_visible(self):
        dashboard_header = self.wait.until(EC.presence_of_element_located(self.dashboard_header_locator))
        return dashboard_header.is_displayed()

from selenium import webdriver

# Test case ID and objective
test_case_id = "TC_login_01"
test_objective = "Successful employee login to OrangeHRM Portal"

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Launch the OrangeHRM site
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Initialize the page objects
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    # Perform login
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()

    # Verify login
    if dashboard_page.is_dashboard_visible():
        print(f"{test_case_id}: {test_objective} - Passed")
    else:
        print(f"{test_case_id}: {test_objective} - Failed: Dashboard not visible")

except Exception as e:
    # Capture and display any errors
    print(f"{test_case_id}: {test_objective} - Failed. Error: {str(e)}")
finally:
    # Close the browser
    driver.quit()

"""
Test case ID:TC_login_02

Test objective:
Invalid employee login to orangeHRM portal

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
 1.In the login panel,enter the user name(Test data: “Admin”)
2.Enter the password for ESS User account in the password field (Test data:”admin123”)
3.Click”login”button

 Expected result:
A valid error message displayed for invalid credentials is displayed.

TestCases dealing with the PIM:
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")
        self.error_message_locator = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located(self.username_locator))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located(self.password_locator))
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button_locator))
        login_button.click()

    def get_error_message(self):
        error_message = self.wait.until(EC.visibility_of_element_located(self.error_message_locator))
        return error_message.text

# Test Script
from selenium import webdriver

# Define test case ID and objective
test_case_id = "TC_login_02"
test_objective = "Invalid employee login to OrangeHRM portal"

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Launch the OrangeHRM site and maximize the window
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Initialize the page object
    login_page = LoginPage(driver)

    # Step 2: Enter the username
    login_page.enter_username("Admin")

    # Step 3: Enter an incorrect password
    login_page.enter_password("wrongpassword")

    # Step 4: Click the login button
    login_page.click_login_button()

    # Step 5: Verify the error message is displayed
    error_message = login_page.get_error_message()

    # Step 6: Assert the error message matches the expected text
    assert "Invalid credentials" in error_message, "Error message does not match expected text"

    # Test passed
    print(f"{test_case_id}: {test_objective} - Passed")

except AssertionError as ae:
    # Handle assertion errors separately
    print(f"{test_case_id}: {test_objective} - Failed. Assertion Error: {str(ae)}")
except Exception as e:
    # Handle any other exceptions
    print(f"{test_case_id}: {test_objective} - Failed. Error: {str(e)}")
finally:
    # Close the browser
    driver.quit()

"""
Test case ID:TC_PIM_01

Test objective:
Add a new employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser
Steps:
1.Go to PIM Module from the left pane in the web page.
2.Click on Add and add new employee details in the page
3.Fill in all the personal details of the employee and click save

Expected Result:
The user should be able to add new employee in the PIM and should see a message successful employee addition.

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver

class LoginPage:
    """Page Object Model for OrangeHRM Login Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self, url):
        """Opens the login page."""
        self.driver.get(url)

    def login(self, username, password):
        """Logs in to the application."""
        username_field = self.wait.until(EC.presence_of_element_located(self.username_field))
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.wait.until(EC.presence_of_element_located(self.password_field))
        password_field.clear()
        password_field.send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()


class PIMPage:
    """Page Object Model for the PIM Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.pim_module_link = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
        self.add_employee_button = (By.XPATH, "//button[contains(text(),'Add Employee')]")
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[contains(text(),'Save')]")
        self.success_message = (By.XPATH, "//div[contains(@class,'oxd-alert-content')]")

    def navigate_to_pim(self):
        """Navigates to the PIM module."""
        self.wait.until(EC.element_to_be_clickable(self.pim_module_link)).click()
        self.wait.until(EC.presence_of_element_located(self.add_employee_button))

    def add_employee(self, first_name, last_name):
        """Adds a new employee."""
        self.wait.until(EC.element_to_be_clickable(self.add_employee_button)).click()
        first_name_field = self.wait.until(EC.presence_of_element_located(self.first_name_field))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        last_name_field = self.wait.until(EC.presence_of_element_located(self.last_name_field))
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def is_success_message_displayed(self):
        """Checks if the success message is displayed."""
        try:
            message = self.wait.until(EC.presence_of_element_located(self.success_message))
            return message.is_displayed()
        except Exception as e:
            print(f"Error locating success message: {e}")
            return False


@pytest.fixture(scope="function")
def driver():
    """Initializes the WebDriver."""
    driver = webdriver.Chrome()  # You can replace this with Firefox, Edge, etc.
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_employee(driver):
    """Test case ID: TC_PIM_01 - Add a new employee in the PIM Module."""
    # Test Setup
    login_page = LoginPage(driver)
    pim_page = PIMPage(driver)
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Precondition: Login
    login_page.open(url)
    login_page.login("Admin", "admin123")

    # Step 1: Navigate to PIM Module
    pim_page.navigate_to_pim()

    # Step 2: Add new employee
    pim_page.add_employee("John", "Doe")

    # Step 3: Verify success message
    assert pim_page.is_success_message_displayed(), "Employee addition failed. Success message not displayed."

    print("Test passed: New employee successfully added to PIM module.")


"""
Test case ID:TC_PIM_02

Test objective:
Edit an existing employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser
Steps:
1.Go to PIM Module from the left pane in the web page.
2.From the existing list of Employees in the PIM Module.
edit the employee information of the employee and save it.

Expected Result:
The user should be able to edit an existing employee information in the PIM and should see a message successful employee details addition.


"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    """Page Object Model for the PIM Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.pim_module_link = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
        self.employee_list = (By.XPATH, "//table[@id='employeeListTable']")
        self.edit_button_template = (By.XPATH, "//table[@id='employeeListTable']//td[text()='{first_name} {last_name}']/following-sibling::td//a")  # Dynamic edit button
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[contains(text(),'Save')]")
        self.success_message = (By.XPATH, "//div[contains(@class,'oxd-alert-content')]")

    def navigate_to_pim(self):
        """Navigates to the PIM module."""
        self.wait.until(EC.element_to_be_clickable(self.pim_module_link)).click()
        self.wait.until(EC.presence_of_element_located(self.employee_list))

    def edit_employee(self, first_name, last_name):
        """Edits an existing employee."""
        edit_button_xpath = self.edit_button_template[1].format(first_name=first_name, last_name=last_name)
        edit_button = (By.XPATH, edit_button_xpath)
        self.wait.until(EC.element_to_be_clickable(edit_button)).click()
        first_name_field = self.wait.until(EC.presence_of_element_located(self.first_name_field))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        last_name_field = self.wait.until(EC.presence_of_element_located(self.last_name_field))
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def is_success_message_displayed(self):
        """Checks if the success message is displayed."""
        try:
            message = self.wait.until(EC.presence_of_element_located(self.success_message))
            return message.is_displayed()
        except Exception as e:
            print(f"Error locating success message: {e}")
            return False

    def verify_employee_updated(self, first_name, last_name):
        """Verifies if the employee details are updated."""
        employee_name_xpath = f"//table[@id='employeeListTable']//td[text()='{first_name} {last_name}']"
        try:
            updated_employee = self.wait.until(EC.presence_of_element_located((By.XPATH, employee_name_xpath)))
            return updated_employee.is_displayed()
        except Exception as e:
            print(f"Error locating updated employee: {e}")
            return False
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object Model for OrangeHRM Login Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self, url):
        """Opens the login page."""
        self.driver.get(url)

    def login(self, username, password):
        """Logs in to the application."""
        username_field = self.wait.until(EC.presence_of_element_located(self.username_field))
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.wait.until(EC.presence_of_element_located(self.password_field))
        password_field.clear()
        password_field.send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
import pytest
from selenium import webdriver
from pim_page import PIMPage
from login_page import LoginPage  # Import LoginPage class

@pytest.fixture(scope="function")
def driver():
    """Initializes the WebDriver."""
    driver = webdriver.Chrome()  # You can replace this with Firefox, Edge, etc.
    driver.maximize_window()
    yield driver
    driver.quit()

def test_edit_employee(driver):
    """Test case ID: TC_PIM_02 - Edit an existing employee in the PIM Module."""

    # Test Setup
    login_page = LoginPage(driver)
    pim_page = PIMPage(driver)
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Precondition: Login
    login_page.open(url)
    login_page.login("Admin", "admin123")

    # Step 1: Navigate to PIM Module
    pim_page.navigate_to_pim()

    # Step 2: Edit an existing employee (Modify details)
    pim_page.edit_employee("John", "Updated")  # Updating employee name

    # Step 3: Verify success message
    success_message_displayed = pim_page.is_success_message_displayed()
    assert success_message_displayed, "Employee editing failed. Success message not displayed."

    # Step 4: Verify employee details are updated
    employee_updated = pim_page.verify_employee_updated("John", "Updated")
    assert employee_updated, "Employee details for 'John Updated' were not found or updated correctly."

    print("Test passed: Employee successfully edited in PIM module.")

"""

Test case ID:TC_PIM_03

Test objective:
Delete an existing employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
1.Go to PIM Module from the left pane in the web page.
2.From the existing list of Employees in the PIM Module.delete an existing employee.

Expected Result:
The user should be able to delete an existing employee information in the PIM and should see a message successful deletion.


"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PIMPage:
    """Page Object Model for the PIM Module."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.employee_card = (By.XPATH, "(//div[@class='oxd-table-card'])[1]")
        self.delete_button = (By.XPATH, "//button[normalize-space()='Delete']")
        self.confirm_delete_button = (By.XPATH, "//button[contains(text(), 'Yes, Delete')]")
        self.success_message = (By.XPATH, "//div[contains(text(), 'Successfully Deleted')]")

    def select_employee(self):
        """Selects the first employee in the list."""
        employee_card = self.wait.until(EC.presence_of_element_located(self.employee_card))
        employee_name = employee_card.text  # Capture the employee name for verification
        employee_card.click()
        return employee_name

    def delete_employee(self):
        """Deletes the selected employee."""
        self.wait.until(EC.element_to_be_clickable(self.delete_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.confirm_delete_button)).click()

    def is_success_message_visible(self):
        """Checks if the success message is displayed."""
        try:
            return self.wait.until(EC.presence_of_element_located(self.success_message)).is_displayed()
        except TimeoutException:
            return False

    def is_employee_deleted(self, employee_name):
        """Verifies that the employee is no longer visible in the list."""
        try:
            self.wait.until(
                EC.invisibility_of_element_located((By.XPATH, f"//div[contains(text(), '{employee_name}')]"))
            )
            return True
        except TimeoutException:
            return False
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.pim_page import PIMPage


@pytest.fixture(scope="function")
def driver():
    """Initializes the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_delete_employee(driver):
    """
    Test Case: Delete an employee from the PIM module.
    """

    # Test data
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    # Initialize Page Objects
    login_page = LoginPage(driver)
    pim_page = PIMPage(driver)

    # Step 1: Open the login page
    login_page.open(url)

    # Step 2: Log in
    login_page.login(username, password)
    assert login_page.is_pim_module_visible(), "Login failed or PIM module not visible"

    # Step 3: Navigate to the PIM module
    driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']").click()

    # Step 4: Select an employee
    employee_name = pim_page.select_employee()

    # Step 5: Delete the selected employee
    pim_page.delete_employee()

    # Step 6: Verify the success message
    success_message_visible = pim_page.is_success_message_visible()
    assert success_message_visible, "Employee deletion success message not visible."
    print("Test Passed: Employee deletion success message displayed.")

    # Step 7: Verify that the employee is deleted from the list
    employee_deleted = pim_page.is_employee_deleted(employee_name)
    assert employee_deleted, f"Employee '{employee_name}' still exists in the list."
    print("Test Passed: Employee was deleted successfully.")
