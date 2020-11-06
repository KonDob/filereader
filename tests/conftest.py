# Add functional depend on needs of tests inside
# For global option use pytest.ini

def pytest_report_header(config):
    return "some info about report in console"


def pytest_runtest_setup():
    return 'Some options'
