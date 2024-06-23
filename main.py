import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()

#Click on make appointment
driver.find_element(By.ID,"btn-make-appointment").click()

#Enter username and password
driver.find_element(By.ID,"txt-username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
driver.find_element(By.XPATH,"//button[@id='btn-login']").click()


#Fill Form
driver.find_element(By.NAME,"facility").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/form/div[1]/div/select/option[2]").click()
driver.find_element(By.NAME,"hospital_readmission").click()
driver.find_element(By.ID,"radio_program_medicaid").click()
driver.find_element(By.ID,"txt_visit_date").send_keys("27/08/2030")
driver.find_element(By.ID,"txt_comment").send_keys("Please check appointment")
driver.find_element(By.ID,"btn-book-appointment").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Go to Homepage']").click()

#lOGOUT
driver.find_element(By.ID,"menu-toggle").click()
driver.find_element(By.XPATH,"/html/body/nav/ul/li[5]/a").click()

driver.quit()
