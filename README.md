<div align="center">
    <table>
        <tr>
        <td align="center"><a href="https://github.com/Badx86/avito-tech_QA-assignment/actions/workflows/CI.yml">
            <img alt="Avito-tech" src="https://github.com/Badx86/avito-tech_QA-assignment/actions/workflows/CI.yml/badge.svg">
        </a></td>  
        <td align="center"><a href="https://github.com/Badx86/avito-tech_QA-assignment/actions/workflows/python-app.yml">
            <img alt="Avito-tech-scheduled" src="https://github.com/Badx86/avito-tech_QA-assignment/actions/workflows/python-app.yml/badge.svg">
        </a></td>  
        <td align="center"><a href="https://badx86.github.io/avito-tech_QA-assignment/">
            <img alt="Allure-report" src="https://img.shields.io/badge/Allure%20Report-deployed-green">
        </a></td>
    <tr>
        <td align="center"><a href="https://www.python.org/doc/versions/">
            <img alt="Python Version" src="https://img.shields.io/badge/python-3.11-blue">
        </a></td>
        <td align="center"><a href="https://pypi.org/project/playwright/">
            <img alt="dependency - playwright" src="https://img.shields.io/badge/dependency-playwright-blue?logo=playwright&logoColor=white">
        </a></td>
        <td align="center"><a href="https://pypi.org/project/pytest">
            <img alt="dependency - pytest" src="https://img.shields.io/badge/dependency-pytest-blue?logo=pytest&logoColor=white">
        </a></td>
</tr>
<tr>
        <td align="center"><a href="https://pypi.org/project/pytest-xdist/">
            <img alt="dependency - pytest" src="https://img.shields.io/badge/dependency-pytest_xdist-blue?logo=pytest_xdist&logoColor=white">
        </a></td>
        <td align="center"><a href="https://pypi.org/project/pytest-sugar/">
            <img alt="dependency - pytest" src="https://img.shields.io/badge/dependency-pytest_sugar-blue?logo=pytest_sugar&logoColor=white">
        </a></td>
        <td align="center"><a href="https://github.com/psf/black">
            <img alt="dependency - pytest" src="https://camo.githubusercontent.com/7d770c433d6198d89f8c1e2f187b904a9721d176259d0e97157337741cc8e837/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667">
        </a></td>
    </tr>
    </table>
</div>

# Avito Tech QA Assignment
Этот репозиторий содержит тесты для проверки отображения данных в экологических счетчиках на сайте Avito.

- В файле `task_1` находится ответ на `Задание 1`, где необходимо изучить скриншот и перечислить все имеющиеся баги и 
    указать их приоритет;
- Файл `TESTCASES.md` содержит описания тест-кейсов, которые проверяют различные аспекты отображения счетчиков;
- Файл `BUGS.md` перечисляет все найденные баги во время тестирования и их приоритеты;

## Установка
Для работы с проектом вам потребуется Python 3 и пакетный менеджер pip. Установите их, если они ещё не установлены на вашей машине.

### Клонирование репозитория
Клонируйте репозиторий с помощью git: `git clone https://github.com/Badx86/avito-tech_QA-assignment`

Перейдите в каталог проекта: `cd avito-tech_QA-assignment`

### Установка зависимостей
Установите зависимости проекта, используя pip: `pip install -r requirements.txt`

### Запуск тестов
Для запуска тестов используйте pytest: `pytest` 
Для параллельного выполнения тестов:   `pytest -n auto`

## Результаты тестирования
После выполнения тестов вы можете найти результаты в папке `output`. Каждый скриншот снабжен метками, 
    соответствующими номеру тест-кейса и времени проведения теста. Это облегчает процесс проверки и анализа результатов.

## Отчётность
Для анализа результатов тестирования и дальнейших действий по устранению багов, используйте файл `BUGS.md`, 
    который содержит детализированный список проблем, их влияние на работу продукта и предложения по исправлениям.
