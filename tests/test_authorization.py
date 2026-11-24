import pytest
from time import sleep
from playwright.sync_api import expect, Page

@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(yandex_page: Page):
        yandex_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = yandex_page.locator("//div[@data-testid='login-form-email-input']//div//input")
        email_input.fill("user.name@gmail.com")

        password_input = yandex_page.locator("//div[@data-testid='login-form-password-input']//div//input")
        password_input.fill("password")

        login_button = yandex_page.locator("//button[@data-testid='login-page-login-button']")
        login_button.click()

        error_alert = yandex_page.locator("//div[@data-testid='login-page-wrong-email-or-password-alert']")
        expect(error_alert).to_be_visible()
        expect(error_alert).to_have_text("Wrong email or password")
