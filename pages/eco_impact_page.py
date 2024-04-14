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

    def take_screenshot_of_counter(self, counter_selector, screenshot_name):
        # Делаем скриншот выбранного счетчика и сохраняем его
        self.page.locator(counter_selector).screenshot(
            path=f"output/{screenshot_name}.png"
        )

    def get_co2_counter(self):
        return self.page.locator(self.CO2_COUNTER)

    def get_water_counter(self):
        return self.page.locator(self.WATER_COUNTER)

    def get_energy_counter(self):
        return self.page.locator(self.ENERGY_COUNTER)
