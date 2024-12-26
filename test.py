import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver: webdriver.Chrome = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(ChromeDriverManager().install())
)


url_adress = 'https://yandex.ru/maps'


driver.get(url_adress)
time.sleep(5)

delay = 10

# Поиск формы ввода на сайте
elem_search_string = WebDriverWait(driver, delay) \
    .until(ec.presence_of_element_located(
    (By.XPATH, "//input[@class='input__control _bold']")))

# Вписываем данные в форму
elem_search_string.send_keys('Муниципальное автономное , общеобразовательное учреждение гимназия № 16 города Тюмени, г. Тюмень')
# Запускаем поиск
elem_search_string.send_keys(Keys.ENTER)
time.sleep(5)
elem_first_list = WebDriverWait(driver, delay) \
    .until(ec.presence_of_element_located(
    (By.XPATH, "//ul[@class='search-list-view__list']")))
elem_first_list.click()
# name = driver.find_element(By.XPATH, '//a[@class="card-title-view__title-link"]')
element = driver.find_element(By.CLASS_NAME, 'card-title-view__title-link')
print(element.text)
link = element.get_attribute("href")
print(link)
driver.get(link)
phone = driver.find_element(By.XPATH, '//div[@class="orgpage-phones-view__phone-number"]')
print(phone.text)
rating = driver.find_element(By.XPATH, '//span[@class="business-rating-badge-view__rating-text"]')
print(rating.text)