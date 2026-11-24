from time import sleep
from playwright.sync_api import sync_playwright, expect

binary_yandex_driver_file = r'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe'

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(executable_path=binary_yandex_driver_file, headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    #page.goto("https://itsm-stage.ttk.ru/login")

    email_input = page.locator("//div[@data-testid='login-form-email-input']//div//input")
    email_input.fill("user.name@gmail.com")

    password_input = page.locator("//div[@data-testid='login-form-password-input']//div//input")
    password_input.fill("password")

    login_button = page.locator("//button[@data-testid='login-page-login-button']")
    login_button.click()

    error_alert = page.locator("//div[@data-testid='login-page-wrong-email-or-password-alert']")
    expect(error_alert).to_be_visible()

