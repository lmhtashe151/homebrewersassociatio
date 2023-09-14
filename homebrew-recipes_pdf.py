import os
import json  # Thêm import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

class MapBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def scrape_and_save_as_pdf(self, url):
        self.driver.get(url)  # Sử dụng URL được truyền vào

        # Locate and extract the desired information
        title = self.driver.find_element(By.CLASS_NAME, 'entry-title').text
        specs = self.driver.find_element(By.CLASS_NAME, 'specs').text
        description = self.driver.find_element(By.CLASS_NAME, 'recipe-description').text
        ingredients = self.driver.find_element(By.CLASS_NAME, 'ingredients').text
        directions = self.driver.find_element(By.CLASS_NAME, 'directions').text

        # Create a PDF file with the title as the filename
        pdf_filename = f"{title}.pdf"  # Sửa tên file PDF
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

        # Define styles for the content
        styles = getSampleStyleSheet()
        style_normal = styles['Normal']
        style_title = styles['Title']

        # Create a list to hold the PDF content
        pdf_content = []
        pdf_content.append(Paragraph(f"<u>Title:</u> {title}", style_title))
        pdf_content.append(Spacer(1, 12))
        pdf_content.append(Paragraph(f"<u>Specs:</u> {specs}", style_normal))
        pdf_content.append(Spacer(1, 12))
        pdf_content.append(Paragraph(f"<u>Description:</u> {description}", style_normal))
        pdf_content.append(Spacer(1, 12))
        pdf_content.append(Paragraph(f"<u>Ingredients:</u>", style_normal))
        ingredient_lines = ingredients.split('\n')
        for line in ingredient_lines:
            pdf_content.append(Paragraph(line, style_normal))
        pdf_content.append(Spacer(1, 12))
        pdf_content.append(Paragraph(f"<u>Directions:</u>", style_normal))
        direction_lines = directions.split('\n')
        for line in direction_lines:
            pdf_content.append(Paragraph(line, style_normal))
        pdf_content.append(Spacer(1, 12))
        # Build the PDF document
        doc.build(pdf_content)

    def scrape_and_save_multiple_as_pdf(self, urls):  # Hàm để scrap và lưu nhiều URL
        for url in urls:
            self.scrape_and_save_as_pdf(url)


if __name__ == "__main__":
    with open('your_file.json', 'r') as json_file:  # Đọc tệp JSON
        data = json.load(json_file)
        urls = data["url"]  # Lấy danh sách URL từ tệp JSON
    bot = MapBot()
    bot.scrape_and_save_multiple_as_pdf(urls)  # Gọi hàm để scrap và lưu nhiều URL
