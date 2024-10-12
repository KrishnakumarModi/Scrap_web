from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd




service = Service(executable_path = "chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/')
browser.maximize_window()






# NEXT BUTTON

def next_Page():
    next_Button = browser.find_element(By.XPATH,"//li[@class='next']")
    next_Button.click()
    return next_Button




data =[]



for i in range(2):
    next_Page()
    print("scraping page",i+1)
    product_Link = browser.find_elements(By.XPATH, '//div[@class ="sc-66eca60f-0 EYQUt"]')      
    for product in product_Link:
        SKU = product.find_element(By.CLASS_NAME, 'modelNumber').text.strip() 
        name = product.find_element(By.XPATH, '//div[@data-qa="product-name"]').text.strip() 
        brand = product.find_element(By.XPATH, '//div[@class="sc-b74d844-16 cNYrWp"]').text.strip() 
        average = product.find_element(By.XPATH, '//div[@class="sc-2709a77c-2 hUinXQ"]').text.strip()
        rating = product.find_element(By.XPATH, '//span[@class="sc-2709a77c-5 kwLXrK"]').text.strip()
        sponser = product.find_element(By.XPATH, '//div[@class ="sc-66eca60f-23 AkmCS"]').text.strip()
        price = product.find_element(By.XPATH, '//span[@class ="oldPrice"]').text.strip() 
        sales_price = product.find_element(By.XPATH, '//div[@class ="sc-8df39a2e-1 hCDaLm"]').text.strip() 
        express = product.find_element(By.XPATH, '//div[@class ="sc-cf5a3a41-0 eVCkvW"]').text.strip() 
        rank = product.find_element(By.XPATH, '//div[@class="sc-66eca60f-24 fPskJH"]').text.strip() 
        links = product.find_element(By.ID, 'productBox-ZE302022BCDD355B5D1DFZ').text.strip()
        

    data.append({'SKU':SKU,'Name': name, 'Brand':brand, 'Average Rating':average,'Rating Count': rating, 'Sponsered': sponser, 'Price':price,'Sales Price':sales_price, 'Express':express,'Rank':rank, 'link':links})

print(data)
df=pd.DataFrame(data)
df_to_csv(products.csv)





browser.quit()

