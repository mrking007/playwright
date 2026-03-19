import pytest


@pytest.fixture(scope="session")
def setupfixtures():
    print("Conf_test Fixture")