# Project to fetch all the links from a given webpage of different websites using headless browser method.....

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
choice = input("\nType 'youtube', 'nitdgp', 'gemini', 'amazon', 'flipkart' , 'irctc', 'svmcm' to fetch all links in their respective website: ").lower()

url_dict = {
       "youtube" : "https://www.youtube.com/",
       "nitdgp" : "https://nitdgp.ac.in/",
       "gemini" : "https://gemini.google.com/app?is_sa=1&is_sa=1&android-min-version=301356232&ios-min-version=322.0&campaign_id=bkws&utm_source=sem&utm_source=google&utm_medium=paid-media&utm_medium=cpc&utm_campaign=bkws&utm_campaign=2024enIN_gemfeb&pt=9008&mt=8&ct=p-growth-sem-bkws&gclsrc=aw.ds&gad_source=1&gad_campaignid=20357620749&gbraid=0AAAAApk5BhkWVYoUCYOD50ZTeYRuHCjla&gclid=Cj0KCQiAsNPKBhCqARIsACm01fRDj5GIVkpR6K9HrR5FF66bNcP43M-qGP1TDC1mxazWngKLTaYQO38aAsBVEALw_wcB",
       "amazon" : "https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=3320728229584589670&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9180056&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1",
       "flipkart" : "https://www.flipkart.com/",
       "irctc" : "https://www.irctc.co.in/nget/train-search",
       "svmcm" : "https://svmcm.wb.gov.in/"
}

if choice in url_dict:
    driver.get(url_dict[choice])

link = driver.find_elements("xpath", "//a")
for i, links in enumerate(link, start=1):
    href = links.get_attribute("href")
    if href:
        print(i,href)

input("\nThe browser is open! To close it press ENTER")

driver.quit()
