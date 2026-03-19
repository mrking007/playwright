import pytest


@pytest.fixture(scope="function")
def fixtures():
    print("Example for Fixtures")
    return "Pass"
@pytest.fixture(scope="function")
def Secondfixtures():
    print("Example for SecondFixtures")
    yield
    print("Thank You!")

@pytest.mark.skip
def test_initialCheck(fixtures,Secondfixtures):
    print("Hello-World!")
    assert fixtures == "Pass"
@pytest.mark.smoke
def test_SecondCheck(fixtures,Secondfixtures):
     print("Welcome MathanKumar")