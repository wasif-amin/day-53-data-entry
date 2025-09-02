from bs4 import  BeautifulSoup
from  selenium import webdriver
from selenium.webdriver.common.by import By
import  requests
from selenium.webdriver.support.wait import WebDriverWait

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
RESPONDER_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdLSgBHfG9xencVdlDsX5EwC6c_LaxD8ry8CL3diY_AJghc0w/viewform?usp=sharing&ouid=103228249568220945808"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(ZILLOW_LINK, headers=header)
web = response.text

soup = BeautifulSoup(web, "html.parser")
link_elements = soup.find_all(name="a")
links = []
for item in link_elements:
    link = item.get("href")
    if "san-francisco" in link:
        links.append(link)

PRICE_ELEMENTS = soup.select(".PropertyCardWrapper span")
all_prices = []
for price in PRICE_ELEMENTS:
    if "$" in price.text:
        clean_price = price.get_text().replace("/mo", "").split("+")[0]
        all_prices.append(clean_price)
ADDRESS_ELEMENTS = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = []
for address in ADDRESS_ELEMENTS:
    clean_address = address.get_text().replace("|", "").strip()
    all_addresses.append(clean_address)
all_addresses.pop(0)
links.pop(0)
links.pop(1)
links.pop(2)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver,10)
for n in range(len(links)):
    driver.get(RESPONDER_LINK)
    address_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_field.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(links[n])
    submit_button.click()
#









