from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Step 1: Go to main page
driver.get("http://192.168.70.41:8080/onlinebookstore/")
time.sleep(2)

# Step 2: Click "Login" in the menu
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(2)

# # Step 3: Click "Login As Admin"
# driver.find_element(By.LINK_TEXT, "Login As Admin").click()
# time.sleep(2)
driver.find_element(By.XPATH, '//a[@href="SellerLogin.html"]').click()
time.sleep(1)

# Step 4: Enter credentials
driver.find_element(By.ID, "userName").send_keys("Admin")
driver.find_element(By.ID, "Password").send_keys("Admin")  # Replace with actual password

# Step 5: Click the login button
driver.find_element(By.CLASS_NAME, "AdminLogin").click()
time.sleep(3)

# Step 6: Check login result
if "Incorrect" in driver.page_source:
    print("❌ Login failed: Incorrect credentials.")
elif "Welcome" in driver.page_source or "Dashboard" in driver.title:
    print("✅ Login successful!")
else:
    print("⚠️ Login result uncertain – check manually.")

# Step 7: Close browser
driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
 
# service = Service(executable_path="/home/bvijayalakshmi/selenium/chromedriver")
# driver = webdriver.Chrome(service=service)
 
# driver.get("http://10.201.0.3:8080/onlinebookstore/")
 
# driver.find_element(By.XPATH, '//a[@href="CustomerLogin.html"]').click()
# time.sleep(1)
 
# driver.find_element(By.XPATH, '//a[@href="SellerLogin.html"]').click()
# time.sleep(1)
 
# driver.find_element(By.ID, "userName").send_keys("admin")
# time.sleep(1)
 
# driver.find_element(By.ID, "Password").send_keys("admin")
# time.sleep(1)
 
# driver.find_element(By.CLASS_NAME, "AdminLogin").click()
# time.sleep(1)
 
# time.sleep(5)
