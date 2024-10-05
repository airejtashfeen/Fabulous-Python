from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

# Path to ChromeDriver and the Chrome version you want to use
driver_path = "/Users/airejtashfeen/Downloads/chromedriver-mac-x64/chromedriver"
chrome_binary_path = "/Users/airejtashfeen/Downloads/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"

# Set Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

# Start the Chrome service
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to scrape
url = "https://www.prioritytire.com/catalogsearch/result/?q=yokohama&brand=Yokohama"
driver.get(url)

time.sleep(50)

# Find products on the page
products = driver.find_elements(By.CLASS_NAME, "product-info-wrapper")

# Prepare data for CSV
data = []
for product in products:
    title = product.find_element(By.CLASS_NAME, "product-attributes").text
    price = product.find_element(By.CLASS_NAME, "price-box price-final_price").text
    availability = product.find_element(By.CLASS_NAME, "product-stock").text
    data.append([title, price, availability])

# Save to CSV
with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Availability'])  # Header
    writer.writerows(data)

print("Data scraped and saved to products.csv")

# Close the driver
driver.quit()
