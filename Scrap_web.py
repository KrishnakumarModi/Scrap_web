from selenium import webdriver
from time import sleep


browser =webdriver.Chrome()
browser.get('https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/')
browser.maximize_window()




product_Sponser ='sc-66eca60f-23 AkmCS'
product_Brand ='sc-66eca60f-24 fPskJH'#[product-name]
product_Amount ='amount'
product_Oldprice ='oldPrice'
product_Name ='sc-66eca60f-24 fPskJH'#[title]
product_Rank =''
product_Express ='sc-cf5a3a41-0 eVCkvW'
product_Avg_rating ='sc-2709a77c-2 hUinXQ'
product_Rating ='sc-2709a77c-5 kwLXrK'
product_Link =''
product_SKU ='modelNumber'
next_Button = browser.find_element("//li[@class='next']")


product = []
for i in range(200):
    product =browser.find_elements_by_class_name(product_Name)
    product.extend(product)







