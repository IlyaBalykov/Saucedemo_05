
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_sample():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.saucedemo.com/')

    assert driver.title == 'Swag Labs'

    driver.quit()

# Create pytest.ini for parameters
