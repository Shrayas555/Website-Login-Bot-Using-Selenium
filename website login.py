from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path='/Users/shrayasraju/Desktop/chromedriver')
driver.get('http://secure-retreat-92358.herokuapp.com/')
fname=driver.find_element(By.XPATH,'/html/body/form/input[1]')
lname=driver.find_element(By.XPATH,'/html/body/form/input[2]')
email=driver.find_element(By.XPATH,'/html/body/form/input[3]')
signup=driver.find_element(By.XPATH,'/html/body/form/button')
action=ActionChains(driver)
action.click(fname)
action.send_keys('Shrayas')
action.click(lname)
action.send_keys('Raju')
action.click(email)
action.send_keys('Shrayas5555@gmail.com')
action.click(signup)
action.perform()

