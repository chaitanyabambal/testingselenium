import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture()
def setUp():
    global movie_name, driver, year, director_name, distributor, producer
    movie_name = input("Enter name of movie : ")
    year = input("Enter year of release : ")
    director_name = input("Enter name of director: ")
    distributor = input("Enter name of distributor")
    producer = input("Enter name of producer: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("Test case started")
    driver.maximize_window()
    yield
    time.sleep(8)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("name").send_keys(movie_name)
    time.sleep(1)
    driver.find_element_by_name("year").send_keys(year)
    time.sleep(1)
    driver.find_element_by_name("director").send_keys(director_name)
    time.sleep(1)
    driver.find_element_by_name("dist").send_keys(distributor)
    time.sleep(1)
    driver.find_element_by_name("producer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(1)
