import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_report_dir = "allure-results"