import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    my_driver = None
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        my_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute test (chrome or firefox)")
