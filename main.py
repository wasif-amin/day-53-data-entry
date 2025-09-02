from bs4 import  BeautifulSoup
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import  requests

RESPONDER_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdLSgBHfG9xencVdlDsX5EwC6c_LaxD8ry8CL3diY_AJghc0w/viewform?usp=sharing&ouid=103228249568220945808"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(ZILLOW_LINK)
web = response.text
#
soup = BeautifulSoup(web, "html.parser")
listing_containers = soup.select(".StyledPropertyCard-c11n-8-84")
#
#
#
# #print(all_prices)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
# # driver.get(RESPONDER_LINK)
#
#
#
# # Initialize your lists outside the loop.
all_links = []
all_addresses = []
all_prices = []

# Loop through each individual listing container found.
for container in listing_containers:
        link_element = container.select_one("a.StyledPropertyCardDataArea-anchor")
        address_element = container.select_one("address[data-test='property-card-addr']")
        price_element = container.select_one("span.PropertyCardWrapper__StyledPriceLine")


        if link_element and address_element and price_element:
            all_links.append(link_element.get("href"))
            all_addresses.append(address_element.get_text().strip())

            # Clean the price string before appending.
            clean_price = price_element.get_text().replace("/mo", "").split("+")[0].strip()
            all_prices.append(clean_price)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver,10)
for n in range(len(all_links)):
    driver.get(RESPONDER_LINK)
    address_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address_field.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link_field.send_keys(all_links[n])
    submit_button.click()

