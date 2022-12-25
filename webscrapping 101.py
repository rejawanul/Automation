import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

#BLOCK Notification

prefs = {"profile.default_content_setting_values.notifications":2}
chrome_options.add_experimental_option("prefs",prefs)

#For this project , I am using BBC SPORTS SITE

website = "https://www.thesun.co.uk/sport/football/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)


#Finding the text , title and subtitle by xpath

#this Xpath contain only the title and subtitle
#//div[@class="teaser__copy-container"]

#find.element works for collecting only one data
#find.elements works for list of data 
#for this project, we want all data with this this xpath 

containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')

# making a list of Titles, subtitles & links

titles = []
subtitles= []
links = []






#this Xpath contain only the title 
#//div[@class="teaser__copy-container"]/a/h3

for container in containers:
    title= container.find_element(by="xpath",value='./a/h3').text

#this xpath contain only the subtitle
#//div[@class="teaser__copy-container"]/a/p

    subtitle = container.find_element(by="xpath",value='./a/p').text

#this xpath contain only link
#get_attribute can collect the class name
#//div[@class="teaser__copy-container"]/a

    link = container.find_element(by="xpath",value='./a').get_attribute("href")


    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


#making a dictonary

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}

#making a dataframe with pandas by my_dict

df_headlines = pd.DataFrame(my_dict)

#Export that dataframe to CSV file
df_headlines.to_csv('headline.csv')
#df_headlines.to_excel('headline.excel')

driver.quit()