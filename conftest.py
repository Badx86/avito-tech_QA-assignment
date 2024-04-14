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
    browser = playwright.chromium.launch(headless=False)  # Запуск браузера
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

    # Add this import to use allure specific features
    import allure

    # Импортируем allure для использования его функций
    import allure

    # Используем хук Allure для добавления информации, такой как скриншоты и логи
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        outcome = yield
        report = outcome.get_result()
        if report.when == "call" and report.failed:
            mode = "a" if os.path.exists("failure_logs.txt") else "w"
            try:
                with open("failure_logs.txt", mode) as f:
                    if "page" in item.fixturenames:
                        web_page = item.funcargs["page"]
                        screenshot_path = f"output/{report.nodeid.replace('::', '_')}_failed.png"
                        web_page.screenshot(path=screenshot_path)
                        f.write(f"Скриншот: {screenshot_path}\n")
                        allure.attach.file(screenshot_path, name="Скриншот при ошибке",
                                           attachment_type=allure.attachment_type.PNG)
                    f.write(f"{report.nodeid} :: {report.longrepr}\n")
            except Exception as e:
                print(f"Ошибка при записи логов ошибок: {str(e)}")

