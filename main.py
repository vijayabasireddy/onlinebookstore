from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import tempfile

# Setup Chrome with headless mode and isolated user profile
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Required for Jenkins
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

# Use a unique temp directory to avoid user data conflicts
user_data_dir = tempfile.mkdtemp()
options.add_argument(f'--user-data-dir={user_data_dir}')

# Setup Chrome WebDriver
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Go to main page
    driver.get("http://192.168.70.41:8080/onlinebookstore/")
    time.sleep(2)

    # Step 2: Click "Login" in the menu
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)

    # Step 3: Click "Login As Admin"
    driver.find_element(By.XPATH, '//a[@href="SellerLogin.html"]').click()
    time.sleep(1)

    # Step 4: Enter credentials
    driver.find_element(By.ID, "userName").send_keys("Admin")
    driver.find_element(By.ID, "Password").send_keys("Admin")

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
finally:
    driver.quit()
