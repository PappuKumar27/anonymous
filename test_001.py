import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
option = Options()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

@pytest.mark.usefixtures("setup")
class Test_pk:
    def test_001(self):
        driver.get("https://www.flipkart.com/")

    def test_002(self):
        driver.get("https://www.imdb.com/")