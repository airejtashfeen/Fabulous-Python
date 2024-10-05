import requests
from bs4 import BeautifulSoup
import csv

url = 'https://lahore.comsats.edu.pk/cs/faculty.aspx'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    with open('scraped_links.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Link Text', 'URL'])

        for link in links:
            text = link.text.strip()  
            href = link.get('href')  
            if href:  
                writer.writerow([text, href])

    print("Data saved to 'scraped_links.csv'.")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
