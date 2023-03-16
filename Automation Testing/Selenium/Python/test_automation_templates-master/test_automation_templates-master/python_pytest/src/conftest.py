import pytest
from src.common.test_data_handler import TestDataHandler
from src.common.webdriver_handler import WebDriverHandler
from src.common.api_manager import ApiManager


@pytest.fixture(scope="session")
def api_manager():
    return ApiManager()

@pytest.fixture(scope="session")
def test_data_handler():
    return TestDataHandler()

@pytest.fixture(scope="function")
def webdriver_handler():
    """
    function scope - fixture is destroyed after each test
    :return:
    """
    webdriver=WebDriverHandler()
    webdriver.setup()
    yield webdriver # test is executed here
    webdriver.quit()
