import csv
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


service = Service(SERVICE_PATH)

browser_options = Options()
browser_options.add_argument('--headless')

driver = webdriver.Edge(service=service, options=browser_options)

driver.get('https://www.metacritic.com/game/')

articles = driver.find_elements(By.CLASS_NAME, 'c-articleSummary')

news = []
for article in articles:
    try:
        title = article.find_element(By.CLASS_NAME, "c-articleSummary_title").text.strip()
        description = article.find_element(By.CLASS_NAME, "c-articleSummary_description").text.strip()
        link = article.find_element(By.CLASS_NAME, 'c-articleSummary_container').get_attribute('href')
        if title.strip() and description.strip():
            news.append({'Title': title, 'Description': description, 'Link': link})
        else:
            print(f'Re-scraping article with missing title and description.')
            title = WebDriverWait(article, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "c-articleSummary_title"))).text.strip()
            description = WebDriverWait(article, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "c-articleSummary_description"))).text.strip()
    except Exception as error:
        print(f'An error occurred: {error}.')

driver.quit()

current_date = datetime.now().strftime('%d-%m-%Y')
save_path = SAVE_PATH
os.makedirs(save_path, exist_ok=True)
csv_file = os.path.join(save_path, f'news_{current_date}.csv')
if news:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Description', 'Link'])
        writer.writeheader()
        writer.writerows(news)
    print(f'Data saved to {csv_file}.')
else:
    print('No articles found. The output file was not created.')
