# Project : Extracting the links from a given website and sending it through whatsapp

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pywhatkit
from datetime import datetime

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver.get("https://svmcm.wb.gov.in/")

choice = input("\nType\n'youtube', 'gemini' , 'amazon' , 'flipkart' , 'svmcm' to send the links to whatsapp: ")
url_dict = {
    "youtube" : "https://www.youtube.com/",
    "gemini" : "https://gemini.google.com/app",
    "amazon" : "https://www.amazon.in/",
    "flipkart" : "https://www.flipkart.com/",
    "svmcm" : "https://svmcm.wb.gov.in/",
}

if choice in url_dict:
    driver.get(url_dict[choice])

url = []

link = driver.find_elements("xpath", "//a")
for i, links in enumerate(link, start=1):
    href = links.get_attribute("href")
    if href:
        url.append(href)

url = url[:10]
msg = "Important links from SVMCM website"
for i, link in enumerate(url, 1):
    msg +=f"{i}. {link}\n"       # Coverting the 'urls' to a string so that the "pywhatkit" module can access the 'urls'

phone_no = input("\nEnter the phone no. at which you want to send the links: ")
now = datetime.now()
hour = now.hour
minute = now.minute + 2

cls_time = int(input("\nEnter the time in seconds after which you want to close whatsapp: "))
pywhatkit.sendwhatmsg(phone_no, msg, hour, minute, wait_time=40, tab_close=True, close_time=cls_time)

driver.quit()
# End of the code