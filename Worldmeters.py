
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from datetime import datetime

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
browser = webdriver.Chrome(service=service, options=options)

Link = 'https://www.worldometers.info/world-population/'
browser.get(Link)

filename = 'D:/world_population_data.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        "Timestamp", "Current_World_Population", "Births_Today", "Deaths_Today",
        "Population_Growth_Today", "Births_This_Year", "Deaths_This_Year", "Population_Growth_This_Year"
    ])


    for _ in range(60):
        browser.refresh()  
        time.sleep(3)  

        counters = browser.find_elements(By.CLASS_NAME, 'rts-counter')
        if len(counters) >= 7:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data_row = [
                now,
                counters[0].text,  # Current
                counters[1].text,  # Births today
                counters[2].text,  # Deaths today
                counters[3].text,  # Growth today
                counters[4].text,  # Births this year
                counters[5].text,  # Deaths this year
                counters[6].text   # Growth this year
            ]
            writer.writerow(data_row)
            print("Saved at", now)
        else:
            print("Not completed yet")

        time.sleep(60)  

browser.quit()
print("Completed Successfuly")
