import json
import pytest
from pages.eco_impact_page import EcoImpactPage

# URL страницы с счетчиками экологического вклада
ECO_IMPACT_URL = "https://www.avito.ru/avito-care/eco-impact"

# Тест для снимка скриншота счетчика CO2
import allure


# Оформляем тесты с помощью декораторов feature и story от Allure
@allure.feature('Страница экологического воздействия')
@allure.story('Скриншот счетчика CO2')
def test_co2_counter_screenshot(page):
    with allure.step("Переход на страницу экологического воздействия"):
        eco_page = EcoImpactPage(page)
        eco_page.go_to(ECO_IMPACT_URL)
    with allure.step("Получение счетчика CO2"):
        co2_counter = eco_page.get_co2_counter()
        assert co2_counter, "Элемент счетчика CO2 не найден на странице."
    with allure.step("Создание скриншота счетчика CO2"):
        co2_counter.screenshot(path="output/TC_01_co2_counter.png")


# Повторите подобные шаблоны для других функций тестирования


# Тест для снимка скриншота счетчика воды
def test_water_counter_screenshot(page):
    eco_page = EcoImpactPage(page)
    eco_page.go_to(ECO_IMPACT_URL)
    water_counter = eco_page.get_water_counter()
    assert water_counter, "The water counter element was not found on the page."
    water_counter.screenshot(path="output/TC_02_water_counter.png")


# Тест для снимка скриншота счетчика энергии
def test_energy_counter_screenshot(page):
    eco_page = EcoImpactPage(page)
    eco_page.go_to(ECO_IMPACT_URL)
    energy_counter = eco_page.get_energy_counter()
    assert energy_counter, "The energy counter element was not found on the page."
    energy_counter.screenshot(path="output/TC_03_energy_counter.png")


# Функция для чтения данных для мокирования из файла
def load_mock_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# Тест для проверки с мокированными данными
@pytest.mark.parametrize(
    "test_data_file, counter_selector, output_filename",
    [
        (
                "data_requests/test_data_01.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_04.png",
        ),
        (
                "data_requests/test_data_02.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_05.png",
        ),
        (
                "data_requests/test_data_03.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_06.png",
        ),
        (
                "data_requests/test_data_04.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_07.png",
        ),
        (
                "data_requests/test_data_05.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_08.png",
        ),
        (
                "data_requests/test_data_06.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_09.png",
        ),
        (
                "data_requests/test_data_07.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_10.png",
        ),
        (
                "data_requests/test_data_08.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_11.png",
        ),
        (
                "data_requests/test_data_09.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_12.png",
        ),
        (
                "data_requests/test_data_10.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_13.png",
        ),
        (
                "data_requests/test_data_11.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_14.png",
        ),
        (
                "data_requests/test_data_12.json",
                EcoImpactPage.IMPACT_ITEMS_BLOCK,
                "TC_15.png",
        ),
    ],
)
def test_mocked_data_counter(page, test_data_file, counter_selector, output_filename):
    mock_data = load_mock_data(test_data_file)
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(
            status=200,
            body=json.dumps(mock_data),
            headers={"Content-Type": "application/json"},
        ),
    )
    eco_page = EcoImpactPage(page)
    eco_page.go_to(ECO_IMPACT_URL)
    eco_page.take_screenshot_of_counter(counter_selector, output_filename)
    counter_element = eco_page.find_element(counter_selector)
    assert (
        counter_element
    ), f"The counter element was not found on the page. Selector: {counter_selector}"
