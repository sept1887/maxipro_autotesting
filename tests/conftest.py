import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--env", action="store", default="prod", metavar="NAME", help="only run tests matching the environment NAME.")
    parser.addoption("--url", action="store", default="https://maxipro.ru/", help="This is request url")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )


def pytest_runtest_setup(item):
    envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
    if envnames:
        if item.config.getoption("--env") not in envnames:
            pytest.skip("test requires env is {!r}".format(envnames))


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "91.0",
            "platform": "LINUX",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        browser = webdriver.Remote(
            command_executor="http://192.168.14.19:4444/wd/hub/",
            desired_capabilities=capabilities)

    elif browser_name == "firefox":
        capabilities = {
            "browserName": "firefox",
            "browserVersion": "89.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        browser = webdriver.Remote(
            command_executor="http://192.168.14.19:4444/wd/hub/",
            desired_capabilities=capabilities)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
