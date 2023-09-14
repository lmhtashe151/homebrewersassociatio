from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
class MapBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def scrape_and_save(self):
        self.driver.get('https://www.homebrewersassociation.org/homebrew-recipe/freyas-locks-blonde-ale/')  # Replace 'YOUR_URL' with the URL of the page you want to scrape

        # Locate and extract the desired information
        title = self.driver.find_element(By.CLASS_NAME, 'entry-title').text
        specs = self.driver.find_element(By.CLASS_NAME, 'specs').text
        description = self.driver.find_element(By.CLASS_NAME, 'recipe-description').text
        ingredients = self.driver.find_element(By.CLASS_NAME, 'ingredients').text
        directions = self.driver.find_element(By.CLASS_NAME, 'directions').text

        # Create a text file and write the information to it
        with open('recipe_info.txt', 'w', encoding='utf-8') as txt_file:
            txt_file.write(f"Title: {title}\n\n")
            txt_file.write(f"Specs: {specs}\n\n")
            txt_file.write(f"Description: {description}\n\n")
            txt_file.write(f"Ingredients:\n{ingredients}\n\n")
            txt_file.write(f"Directions:\n{directions}\n\n")

        # Close the WebDriver
        self.driver.quit()

bot = MapBot()
bot.scrape_and_save()
# python -i recipes.py
# bot.driver.find_element(By.CLASS_NAME, 'entry-title')
# 'Freya’s Locks Blonde Ale'
# bot.driver.find_element(By.CLASS_NAME, 'specs')
# 'ABV: 4.5%\nIBU: 21\nSRM: 6-7\nOG: 1.044 (11°P)\nFG: 1.010 (2.6°P)'
# bot.driver.find_element(By.CLASS_NAME, 'recipe-description').text
# bot.driver.find_element(By.CLASS_NAME, 'ingredients').text
# bot.driver.find_element(By.CLASS_NAME, 'directions').text
# //*[@id="post-77430"]/header/h1