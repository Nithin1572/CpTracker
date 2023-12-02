from selenium import webdriver

options = webdriver.ChromeOptions()

#after the code is executed the web page opened is detached from code 
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

#set the URL
url = "https://codeforces.com/profile/Nithin_XS"

#get window with specified URL and maximize it 
driver.get(url)
driver.maximize_window()
