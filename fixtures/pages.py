import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def login_page(yandex_page: Page) -> LoginPage:
    return LoginPage(page=yandex_page)

@pytest.fixture
def registration_page(yandex_page: Page) -> RegistrationPage:
    return RegistrationPage(page=yandex_page)

@pytest.fixture
def dashboard_page(yandex_page: Page) -> DashboardPage:
    return DashboardPage(page=yandex_page)


