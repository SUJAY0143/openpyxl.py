from selenium import webdriver
from selenium.webdriver.support.select import Select
#write a code to connect chrome driver
driver=webdriver.Chrome(executable_path="c:\\Users\\sujay\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
#code to get connect to webapplication on which a test script is written
driver.get("https://www.globalsqa.com/samplepagetest/")
radiobutton=driver.find_elements_by_name("g2599-education")
for i in radiobutton:
    i.click()
