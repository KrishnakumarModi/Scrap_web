from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd




service = Service(executable_path = "chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/')
browser.maximize_window()




"""
product_Sponser ='sc-66eca60f-23 AkmCS'
product_Brand ='pdp-brand-ZECB29782C8C4BD506B8EZ'
product_Amount ='amount'
product_Oldprice ='oldPrice'
product_Name ='//div[@class="sc-66eca60f-24 fPskJH"]'
product_Rank =''
product_Express ='sc-cf5a3a41-0 eVCkvW'
product_Avg_rating ='sc-2709a77c-2 hUinXQ'
product_Rating ='sc-2709a77c-5 kwLXrK'
product_Link ='sc-19767e73-0 bwele'
product_SKU ='modelNumber'"""

# NEXT BUTTON

def next_Page():
    next_Button = browser.find_element(By.XPATH,"//li[@class='next']")
    next_Button.click()
    return next_Button



"""product = {"SKU" : [product_SKU],
           "Name" : [product_Name],
           "Brand" : [product_Brand],
           "Average Rating" : [product_Avg_rating],
           "Rating Count" : [product_Rating],
           "Sponsered" : [product_Sponser],
           "Price" : [product_Oldprice],
           "Sales Price" : [product_Amount],
           "Express" : [product_Express],
           "Rank" : [product_Rank],
           "Link" : [product_Link]

}"""

for i in range(5):
    print("scraping page",i+1)
    product_Box = browser.find_elements(By.XPATH, '//div[@class="sc-19767e73-1 fCFkgQ grid"]')
    next_Page()

data =[]


for product in product_Box:     
    #SKU = product.find_element(By.XPATH, '//div[@class="modelNumber"]').text.strip() #
   # name = product.find_element(By.XPATH, '//div[@class="sc-66eca60f-24 fPskJH"]').text.strip() #
    #brand = product.find_element(By.XPATH, '//div[@data-qa="product-name"]').text.strip() #
    average = product.find_element(By.XPATH, '//div[@class="sc-2709a77c-2 hUinXQ"]').text.strip() #
    rating = product.find_element(By.XPATH, '//span[@class="sc-2709a77c-5 kwLXrK"]').text.strip() #
    sponser = product.find_element(By.XPATH, '//div[@class ="sc-66eca60f-23 AkmCS"]').text.strip() #
    price = product.find_element(By.XPATH, '//span[@class ="oldPrice"]').text.strip() #
    sales_price = product.find_element(By.XPATH, '//div[@class ="sc-8df39a2e-1 hCDaLm"]').text.strip() #
    express = product.find_element(By.XPATH, '//div[@class ="sc-cf5a3a41-0 eVCkvW"]').text.strip() #
    rank = product.find_element(By.XPATH, '//div[@class="sc-66eca60f-24 fPskJH"]').text.strip() 
    links = product.find_element(By.XPATH, '//div[@class="sc-66eca60f-24 fPskJH"]').text.strip() 
        

    data.append({"""'SKU':SKU,"""'Name': name, 'Brand':brand, 'Average Rating':average,'Rating Count': rating, 'Sponsered': sponser, 'Price':price,'Sales Price':sales_price, 'Express':express,'Rank':rank, 'link':links})

print(data)
# df=pd.DataFrame(data)





browser.quit()

