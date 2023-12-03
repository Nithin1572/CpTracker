from selenium                       import webdriver
from time                           import sleep
from selenium.webdriver.common.by   import By
from flask                          import Flask, render_template, request
from selenium.common.exceptions     import NoSuchAttributeException
import pandas as pd

#fetching list pf user names from input_list.xlsx (excel file)
df = pd.read_excel(r"C:\Users\Nithin\Desktop\CpTracker\input_list.xlsx")
users = df.values.tolist()

#initialize chrome drive 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
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

        #navigate back to home page
        driver.back()
    except Exception:
        print("Invalid user name")

#convert list to dataframe and export it to outputlist excel
odf = pd.DataFrame(outputList)
odf.to_excel(f"output_list.xlsx",index=False)

#close the drvier 
driver.close()