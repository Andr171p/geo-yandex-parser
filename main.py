import time

from bs4 import BeautifulSoup

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


base_url: str = "https://2gis.ru/tyumen"


driver.get(base_url)
# time.sleep(5)

form = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.TAG_NAME, 'form'))
)
input_field = form.find_element(By.XPATH, './/input[@type="text"]')
input_field.clear()
input_field.send_keys("Гимназия 83")
input_field.send_keys(Keys.ENTER)
time.sleep(3)

'''schools = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.CLASS_NAME, '_awwm2v'))
)'''

divs = driver.find_element(By.XPATH, '//div[@class="_z72pvu"]')
print(divs.text)

gymnasia_name = divs.find_element(By.XPATH, '//span[@class="_1a82cfg"]//span').text

# Находим категорию
category = divs.find_element(By.XPATH, '//span[@class="_oqoid"]').text

# Находим рейтинг
rating_stars = len(divs.find_elements(By.CSS_SELECTOR, '._1fkin5c svg'))
total_ratings = driver.find_element(By.XPATH, '//div[@class="_jspzdm"]').text.split()[0]

# Находим адрес
address = divs.find_element(By.XPATH, '//span[@class="_1w9o2igt"]').text

# Находим количество филиалов
branches_count = int(divs.find_element(By.XPATH, '//a[@href="/tyumen/branches/1830124219539445"]').text.split()[0])

# Находим статус работы
status = divs.find_element(By.XPATH, '//div[@style="color: rgb(254, 80, 0);"]').text

# Находим ссылку
link = driver.current_url

print(f'''
        Название: {gymnasia_name}
        Категория: {category}
        Рейтинг: {rating_stars} звезд, {total_ratings} оценок
        Адрес: {address}
        Филиалы: {branches_count}
        Статус: {status}
        Ссылка: {link}
''')