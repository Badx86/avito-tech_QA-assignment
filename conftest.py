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
def browser():
    print('\nstart browser...')
    with sync_playwright() as p:
        # Выбираем тип браузера, например, можно использовать p.firefox или p.webkit
        browser = p.chromium.launch(
            headless=False if 'CI' not in os.environ else True, # Если CI в окружении, запускаем в headless режиме
            args=['--no-sandbox', '--disable-dev-shm-usage'] if 'CI' in os.environ else []
        )
        yield browser
        print('\nquit browser...')
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
