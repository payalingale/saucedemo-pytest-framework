
import pytest
import base64
import pytest_html
from pages.login_page import LoginPage
from playwright.sync_api import Page
from pytest_metadata.plugin import metadata_key
from dotenv import load_dotenv
load_dotenv()

ENVIRONMENTS = {
    "prod": "https://www.saucedemo.com",
    "staging": "https://staging.saucedemo.example",
}


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    report = yield
    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page')
        if page is not None:
            png = page.screenshot(full_page=True)
            report.extras = getattr(report, 'extras', []) + [
                pytest_html.extras.png(base64.b64encode(
                    png).decode(), name='screenshot')
            ]
    return report


def pytest_configure(config):
    config.stash[metadata_key]["Env"] = config.getoption("--env")
    config.stash[metadata_key]["Browser"] = ", ".join(
        config.getoption("--browser") or ["chromium"])
    config.stash[metadata_key]["Base URL"] = ENVIRONMENTS[config.getoption(
        "--env")]


def pytest_html_report_title(report):
    report.title = "SauceDemo Automation Report"


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        default='prod',
        choices=list(ENVIRONMENTS),
        help='Environment to run against'
    )


@pytest.fixture(scope='session')
def base_url(request):
    return ENVIRONMENTS[request.config.getoption("--env")]


@pytest.fixture(scope='session', autouse=True)
def configure_test_id(playwright):
    playwright.selectors.set_test_id_attribute('data-test')


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.open()
    return lp
