import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage

@pytest.fixture
def login_page(yandex_page: Page) -> LoginPage:
    return LoginPage(page=yandex_page)


