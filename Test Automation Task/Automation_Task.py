from socket import timeout
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(executable_path=r"C:\selenium\geckodriver.exe")
driver = webdriver.Firefox(service=s)
driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app")
# Registration
driver.find_element(By.XPATH,"/html/body/div/div/main/div/div/p[2]/button").click()
driver.find_element(By.XPATH,"/html/body/div/div/main/div/div/div[1]/div/input").send_keys("Harshad")
driver.find_element(By.XPATH,"/html/body/div/div/main/div/div/div[2]/div/input").send_keys("Harshad")
driver.find_element(By.XPATH,"/html/body/div/div/main/div/div/button").click()
driver.quit()

# LOGIN
driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app")
driver.find_element(By.XPATH,"/html/body/div/div/main/div/div/div[1]/div/input").send_keys("harsh")
driver.find_element(By.XPATH,"/html/body/div/div/main/div/div/div[2]/div/input").send_keys("12345")
driver.find_element(By.XPATH,"/html/body/div/div/main/div/div/button").click()

