from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()

url = "https://books.rakuten.co.jp/rb/17638823/?bkts=1&scid=mi_ssm_upc1571"
username = "nguyenngocquang28@icloud.com"
password = "Qqq28281299@"
dob = '19920828'
while True:

    driver.get(url)
    try:
        try:
            add_to_cart_button = driver.find_element(By.CSS_SELECTOR,'button.new_addToCart')
        except NoSuchElementException:
            print("Not found yet")  
        add_to_cart_button.click()
        print("Found")
        time.sleep(3)
        button = driver.find_element(By.ID, "js-cartBtn")
        button.click()
        user_id_input = driver.find_element(By.NAME, "u")
        password_input = driver.find_element(By.NAME, "p")

        user_id_input.send_keys(username)
        password_input.send_keys(password)

        driver.find_element(By.NAME, "submit").click()
        time.sleep(10)
  
        username_input = driver.find_element(By.ID,'loginInner_u')
        username_input.clear()
        username_input.send_keys('nguyenngocquang28@icloud.com')

        password_input = driver.find_element(By.ID,'loginInner_p')
        password_input.clear()
        password_input.send_keys('Qqq28281299@') 
        dob_input = driver.find_element(By.ID,'loginInner_birthday')
        dob_input.clear()
        dob_input.send_keys(dob)         
        submit_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/form/div/p[1]/input')
        submit_button.click()
        time.sleep(10)        
        confirm_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/form/div[2]/div/div/button')
        confirm_button.click()  
        time.sleep(10)        
        cancel_confirm_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/div/div[1]/a')
        cancel_confirm_button.click()
        print("Done--- Order Placed")
        time.sleep(5)
        driver.quit()
    except:
        continue
    time.sleep(3)
    
