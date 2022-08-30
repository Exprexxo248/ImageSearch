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
waiter = WebDriverWait(driver=driver, timeout=2)

page_url = "https://bitis.com.vn/collections/nam"
driver.get(url=page_url)

i = 0
links = []

button = driver.find_element(by=By.CSS_SELECTOR, value=".btn-loadmore")

div_xpath = '//*[@id="collection-body"]/div[3]/div/div[2]/div[2]/div[1]/div[{}]'
image_xpath = './/*[@class="product-boxImg-flex"]/a/*/picture/img'

while True:
    i += 1
    div = None
    try:
        div = WebDriverWait(driver=driver, timeout=2).until(
            EC.presence_of_element_located((By.XPATH, div_xpath.format(i)))
        )
        driver.execute_script("arguments[0].scrollIntoView();", div)
        location = driver.execute_script("return window.pageYOffset;")
        img = WebDriverWait(driver=div, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, image_xpath))
        )

        href = img.get_attribute("src")
        links.append(href)
    except:
        try:
            button = driver.find_element(
                by=By.CSS_SELECTOR, value=".btn-loadmore"
            ).click()
            i -= 1
        except:
            print("Cannot find more")
            break

print("Image Crawled: ", len(links))


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
