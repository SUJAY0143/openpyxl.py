from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
#write a code to connect chrome driver
driver=webdriver.Chrome(executable_path="c:\\Users\\sujay\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
#code to get connect to webapplication on which a test script is written
driver.get("https://www.globalsqa.com/samplepagetest/")
#checkboxes=driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/form[1]/div[5]/label[2]/input[1]")
checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
sleep(2)
for i in  checkboxes:
    i.click()
    print(i)

