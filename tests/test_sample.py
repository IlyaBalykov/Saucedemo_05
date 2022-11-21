from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_sample():
    browser_options = webdriver.ChromeOptions()
    browser_options.headless = True
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=browser_options
    )
    driver.get('https://www.saucedemo.com/')

    assert driver.title == 'Swag Labs'

    driver.quit()
