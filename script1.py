import csv
from bs4 import BeautifulSoup
import requests

url = "https://lahore.comsats.edu.pk/cs/Faculty.aspx"
results = requests.get(url).text
doc = BeautifulSoup(results, "html.parser")


data = []

table = doc.find('table')  

if table:
    
    trs = table.find_all('tr')
    
    if trs:
        for tr in trs:
            
            new_table = tr.find('table')
            if new_table:

                td = new_table.find_all('td')
                
                
                if len(td) > 2:
                    inside_td = td[2]
                    
                    a = inside_td.find_all('a')
                    name = a[0].string if a and a[0].string else "N/A"
                    
                    span = inside_td.find_all('span')
                    extra_info = [s.string for s in span if s.string]  
                    
                
                    record = [name] + extra_info
                    data.append(record)  
    else:
        print("No rows found in the table.")
else:
    print("Table not found.")

with open('SP22-BSE-080.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Name", "Position", "Department", "Research Interests", "Other Info"])
    
    writer.writerows(data)

print("Data has been written to comsats_cs_faculty_data.csv.")
