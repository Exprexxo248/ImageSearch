from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import json
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

page_url = "https://bitis.com.vn/collections/nam"
driver.get(url=page_url)

i = 0
links = []

button = driver.find_element(by=By.CSS_SELECTOR, value=".btn-loadmore")

while True:
    driver.execute_script(
        "window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'})"
    )
    driver.implicitly_wait(0.1)
    try:
        button = driver.find_element(by=By.CSS_SELECTOR, value=".btn-loadmore").click()
    except:
        print("Cannot find more")
        break

driver.execute_script("window.scrollTo(0, 0)")


element_xpath = '//*/div[@class="row listProduct-row listProduct-resize listProduct-filter loaded"]/div[{}]'
image_xpath = './/*[@class="prod-img first-image"]/picture/img'

while True:
    driver.execute_script(
        "window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'})"
    )
    i += 1
    try:
        element = driver.find_element(by=By.XPATH, value=element_xpath.format(i))
        temp = element.find_element(by=By.XPATH, value=image_xpath)
        driver.implicitly_wait(0.2)
        href = temp.get_attribute("src")
        print(href)
        links.append(href)

    except:
        break


print(len(links))


_id = 0
data = dict()
mapping = dict()
for link in links:
    _id += 1
    shoe_object = dict()
    shoe_object["_id"] = _id
    shoe_object["name"] = f"Hunter X {_id}"
    shoe_object["image_url"] = link
    data[str(_id)] = shoe_object
    mapping[link] = _id

json_objects = json.dumps(data)
json_mapping = json.dumps(mapping)

with open("objects.json", "w") as outfile:
    json.dump(json_objects, outfile)
with open("mapping.json", "w") as outfile:
    json.dump(json_mapping, outfile)

driver.quit()
