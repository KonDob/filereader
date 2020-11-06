import pytest

# Add functional depend on needs of tests inside
# For global option use pytest.ini


@pytest.fixture(scope="session", autouse=True)
def setup():
    """This is setup fixutre"""
    pass


@pytest.fixture(scope="session", autouse=True)
def help_method():
    print('Here should be some functionality before tests')
    yield
    print('Here should be some functionality after tests')


def pytest_report_header(config):
    return "some info about report in console"


def pytest_runtest_setup():
    return 'Some options'
