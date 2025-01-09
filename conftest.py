import pytest

@pytest.fixture(scope="class")
def setup():
    print("driver is opened")
    yield
    print("closed browser")