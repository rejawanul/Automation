'''#Importing packages from SELENIUM, we will work with "Chrome Browser"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

#Open Chrome Browser

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com')
lin2 test
sdvsdv
rfujdofliu
'''

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://getintopc.com/softwares/audio-processing/syrinxsamples-cs15d-kontakt-free-download/')
driver.find_element(By.CLASS_NAME, 'btn').click()
