# Simple project to store the headlines and their respective urls of a news channel inside a CSV file

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

choice = input("\nType.............\n'timesofIndia', 'thehindu' , 'ndtv', 'telegraph' to fetch the articles and their respective URLs to a CSV file: ").lower().strip()

url_dict = {
    "timesofIndia" : "https://timesofindia.indiatimes.com/",
    "thehindu" : "https://www.thehindu.com/",
    "ndtv" : "https://www.ndtv.com/",
    "telegraph" : "https://www.telegraphindia.com/"
        }

if choice == "timesofindia":
    driver.get("https://timesofindia.indiatimes.com/")
    headlines = driver.find_elements("xpath", "//a[contains(@href, 'articleshow')]")

    with open("TOI.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["NO.", "Headline", "URL"])

        for i, headline in enumerate(headlines, start=1):
            href = headline.get_attribute("href")
            article = headline.text.strip()

            if href and article:
                writer.writerow([i, article, href])

elif choice == "thehindu":
    driver.get("https://www.thehindu.com/")
    headlines = driver.find_elements("xpath", "//a[contains(@href, 'article')]")

    with open("HINDU.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["NO.", "Headline", "URL"])

        for i, headline in enumerate(headlines, start=1):
            href = headline.get_attribute("href")
            article = headline.text.strip()

            if href and article:
                writer.writerow([i, article, href])

elif choice == "telegraph":
    driver.get("https://www.telegraphindia.com/")
    headlines = driver.find_elements("xpath", "//a[contains(@href, 'cid')]")

    with open("NDTV.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["NO.", "Headline", "URL"])

        for i, headline in enumerate(headlines, start=1):
            href = headline.get_attribute("href")
            article = headline.text.strip()

            if href and article:
                writer.writerow([i, article, href])

