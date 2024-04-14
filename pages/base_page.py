class BasePage:
    def __init__(self, page):
        self.page = page

    def go_to(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def find_element(self, selector):
        """
        Найти элемент по селектору.

        :param selector: CSS-селектор для поиска элемента
        :return: Элемент (объект типа ElementHandle)
        """
        return self.page.query_selector(selector)

    # Можно добавить метод для поиска всех элементов по селектору
    def find_elements(self, selector):
        """
        Найти все элементы по селектору.

        :param selector: CSS-селектор для поиска элементов
        :return: Список элементов (объекты типа ElementHandle)
        """
        return self.page.query_selector_all(selector)
