import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pytest_bdd import scenarios, given, when, then, parsers
from pages.LoginPage import LoginPage

scenarios('../login.feature')

page = None

@given('I open the login page')
def open_login_page(browser):
    global page
    page = LoginPage(browser)
    page.open()

@when(parsers.parse('I enter username "{username}" and password "{password}"'))
def enter_credentials(username, password):
    page.enter_username(username)
    page.enter_password(password)

@when("I click login")
def click_login():
    page.click_login()

@then("I should see dashboard")
def verify_dashboard(browser):
    assert "inventory" in browser.current_url