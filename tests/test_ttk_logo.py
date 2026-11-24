from playwright.sync_api import sync_playwright, expect

binary_yandex_driver_file = r'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe'

def test_ttk_logo():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=binary_yandex_driver_file, headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://itsm-stage.ttk.ru/login")

        login_input = page.locator("//input[@name='login']")
        login_input.fill('matveynovikov')

        password_input = page.locator("//input[@name='password']")
        password_input.fill("0bi2f0rti4Novik?")

        login_button = page.locator("//button[@name='login']")
        login_button.click()

        сategory_card = page.locator("(//div[@name='category-view-category-card'])[1]")
        сategory_card.click()
        page.wait_for_timeout(2000)
        ttk_logo = page.locator("//img[@alt='ttk-full-logo']")

        expect(ttk_logo).not_to_be_visible()