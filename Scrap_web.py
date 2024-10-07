from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd




service = Service(executable_path = "chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/')
browser.maximize_window()





product_Sponser ='sc-66eca60f-23 AkmCS'
product_Brand ='pdp-brand-ZECB29782C8C4BD506B8EZ'
product_Amount ='amount'
product_Oldprice ='oldPrice'
product_Name ="sc-66eca60f-24 fPskJH"
product_Rank =''
product_Express ='sc-cf5a3a41-0 eVCkvW'
product_Avg_rating ='sc-2709a77c-2 hUinXQ'
product_Rating ='sc-2709a77c-5 kwLXrK'
product_Link ='sc-19767e73-0 bwele'
product_SKU ='modelNumber'

# NEXT BUTTON

def next_Page():
    next_Button = browser.find_element(By.XPATH,"//li[@class='next']")
    next_Button.click()
    return next_Button



product = {"SKU" : [product_SKU],
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

}


for i in range(10):
    print('Scraping page',i+1)
    products = browser.find_elements(By.CLASS_NAME , "product_Name")
    for p in products:
        product.append(p.text)
    next_Page()
    time.sleep(1)
    
   

df = pd.DataFrame(product)
df.to_csv('product.csv')



browser.quit()

