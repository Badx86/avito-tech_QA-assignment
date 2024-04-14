import allure

from .base_page import BasePage


class EcoImpactPage(BasePage):
    # Класс для блока со всеми счетчиками
    IMPACT_ITEMS_BLOCK = ".desktop-impact-items-F7T6E"

    # Класс для каждого элемента счетчика
    COUNTER_CLASS = ".desktop-impact-item-eeQO3"

    # Селекторы для каждого счетчика по порядку
    CO2_COUNTER = f"{COUNTER_CLASS}:nth-of-type(2)"
    WATER_COUNTER = f"{COUNTER_CLASS}:nth-of-type(4)"
    ENERGY_COUNTER = f"{COUNTER_CLASS}:nth-of-type(6)"

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Скриншот счетчика: {screenshot_name}")
    def take_screenshot_of_counter(self, counter_selector, screenshot_name):
        self.page.locator(counter_selector).screenshot(
            path=f"output/{screenshot_name}.png"
        )

    @allure.step("Получение счетчика CO2")
    def get_co2_counter(self):
        return self.page.locator(self.CO2_COUNTER)

    @allure.step("Получение счетчика воды")
    def get_water_counter(self):
        return self.page.locator(self.WATER_COUNTER)

    @allure.step("Получение счетчика энергии")
    def get_energy_counter(self):
        return self.page.locator(self.ENERGY_COUNTER)