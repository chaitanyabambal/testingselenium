import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def setup():
    global  name,driver
    name = input("enter name :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(7)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com")
    driver.find_element_by_name("name").send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[4]").click()
    time.sleep(1)
    driver.find_element_by_name("fcheckbox").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
