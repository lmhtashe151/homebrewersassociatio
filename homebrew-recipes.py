from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
class MapBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def search_f(self, num_pages):
        extracted_product_names = []
        for page in range(1, num_pages + 1):
            page_url = f"https://www.homebrewersassociation.org/homebrew-recipes/page/{page}/"
            self.driver.get(page_url)
            time.sleep(1)
            elements = bot.driver.find_elements(By.CLASS_NAME, 'entry-header')
            for element in elements:
                # product_name = element.text
                # extracted_product_names.append(product_name)
                a_elements = element.find_elements(By.TAG_NAME, 'a')
                for a_element in a_elements:
                    url = a_element.get_attribute("href")
                    extracted_product_names.append(url)
        return extracted_product_names
    

bot = MapBot()
num_pages_to_scrape = 160  # You can set the number of pages you want to scrape
extracted_product_names = bot.search_f(num_pages_to_scrape)
data = {"url": extracted_product_names}
json_file_path = "homebrew-recipes-URL.json"
with open(json_file_path,"w") as json_file:
    json.dump(data, json_file, indent=4)