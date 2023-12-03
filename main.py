from selenium                       import webdriver
from time                           import sleep
from selenium.webdriver.common.by   import By
from flask                          import Flask, render_template, request
from selenium.common.exceptions     import NoSuchAttributeException
import pandas as pd

#fetching list of user names from input_list.xlsx (excel file)
#and convert it to python list
df = pd.read_excel(r"C:\Users\Nithin\Desktop\CpTracker\input_list.xlsx")
users = df.values.tolist()

#initialize chrome drive 
#add_argument prevent browsesr from opening again and again
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

#set codeforces url in chrome driver 
url = "https://codeforces.com"
driver.get(url)

#iterate for individual user and fetch there rating 
outputList = [[]]
for user in users:
    individualUser = []

    #getting search box and enter button using XPATH
    search_box   = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div[5]/form/div[1]/label/input')
    enter_button = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div[5]/form/div[2]/input')

    #clearing the search box
    search_box.clear()

    #enter user name and click enter
    search_box.send_keys(user)
    enter_button.click()
    try:
        rating = driver.find_element(By.XPATH, '//*[@id="pageContent"]/div[2]/div/div[2]/ul/li[1]/span[1]')

        #storing name and rating in a python list
        individualUser.append(user)
        individualUser.append(rating.text)
        outputList.append(individualUser)
        print("user name :%s rating: %s" %(user,rating.text))
        
        #navigate back to home page
        driver.back()
    except Exception:
        individualUser.append(user)
        individualUser.append("INVALID USER")
        outputList.append(individualUser)
        print("Invalid user name")

#convert list to dataframe and export it to outputlist excel
odf = pd.DataFrame(outputList)
odf.to_excel(f"output_list.xlsx",index=False)

#close the drvier 
driver.close()