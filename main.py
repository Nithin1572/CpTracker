from selenium                     import webdriver
from time                         import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

#after the code is executed the web page opened is detached from code 
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

#set the URL
url = "https://codeforces.com"

#get window with specified URL and maximize it 
driver.get(url)
# driver.maximize_window()

search_box   = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div[5]/form/div[1]/label/input')
enter_button = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div[5]/form/div[2]/input')

user = 'Nithin_XS'

search_box.send_keys(user)
enter_button.click()

rating = driver.find_element(By.XPATH, '//*[@id="pageContent"]/div[2]/div/div[2]/ul/li[1]/span[1]')
print(rating.text)

driver.close()