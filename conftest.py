from playwright.sync_api import sync_playwright
import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def create_output_directory():
    # Путь к директории для скриншотов
    output_dir = os.path.join(os.path.dirname(__file__), "output")

    # Создание директории, если она еще не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)  # Запуск браузера
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
