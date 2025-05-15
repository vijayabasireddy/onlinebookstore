from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime

# Setup screenshot directory
os.makedirs('selenium_screenshots', exist_ok=True)

def take_screenshot(driver, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"selenium_screenshots/{step_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"📸 Screenshot saved: {filename}")

# Chrome Options for GUI
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1280,1024')

try:
    # Initialize WebDriver
    service = Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    
    # Test Data
    book_quantity = 30
    book_id = "8bd5fe50-9725-41da-bad8-476d577894f1"
    book_name = "one arranged murder"
    author = "chetan bhagat"
    price = "499"
    quantity = "5"

    # Test steps
    print("🌐 Navigating to application...")
    driver.get("http://192.168.70.41:8080/onlinebookstore/")
    take_screenshot(driver, "01_homepage")
    time.sleep(2)

    print("🔑 Logging in...")
    driver.find_element(By.LINK_TEXT, "Login").click()
    take_screenshot(driver, "02_login_page")
    time.sleep(2)
    
    driver.find_element(By.XPATH, '//a[@href="SellerLogin.html"]').click()
    take_screenshot(driver, "03_seller_login")
    time.sleep(2)
    
    driver.find_element(By.ID, "userName").send_keys("admin")
    driver.find_element(By.ID, "Password").send_keys("admin")
    take_screenshot(driver, "04_credentials_entered")
    time.sleep(1)
    
    driver.find_element(By.CLASS_NAME, "AdminLogin").click()
    take_screenshot(driver, "05_post_login")
    time.sleep(2)
    
    if "Incorrect" in driver.page_source:
        print("❌ Login failed: Incorrect credentials.")
    elif "Welcome" in driver.page_source or "Dashboard" in driver.title:
        print("✅ Login successful!")
    else:
        print("⚠️ Login result uncertain")

    print("📚 Accessing store books...")
    driver.find_element(By.ID, "storebooks").click()
    take_screenshot(driver, "06_store_books")
    time.sleep(2)

    try:
        print("🔄 Updating book quantity...")
        update_button = driver.find_element(By.XPATH, "//th[text()='9780132778046']/following-sibling::td/form/button[text()='Update']")
        update_button.click()
        take_screenshot(driver, "07_update_clicked")
        time.sleep(2)

        quantity_field = driver.find_element(By.ID, "bookQuantity")
        quantity_field.clear()
        quantity_field.send_keys(book_quantity)
        take_screenshot(driver, "08_quantity_updated")
        time.sleep(2)

        update_submit_btn = driver.find_element(By.XPATH, "//input[@type='submit' and @value=' Update Book ']")
        update_submit_btn.click()
        take_screenshot(driver, "09_quantity_submitted")
        time.sleep(2)
        print("✅ Book quantity updated successfully")
    except Exception as e:
        print(f"⚠️ Book update skipped: {str(e)}")

    print("➕ Adding new book...")
    driver.find_element(By.LINK_TEXT, "Add Books").click()
    take_screenshot(driver, "10_add_books_page")
    time.sleep(2)

    driver.find_element(By.ID, "bookName").send_keys(book_name)
    time.sleep(0.5)
    driver.find_element(By.ID, "bookAuthor").send_keys(author)
    time.sleep(0.5)
    driver.find_element(By.NAME, "price").send_keys(price)
    time.sleep(0.5)
    driver.find_element(By.NAME, "quantity").send_keys(quantity)
    take_screenshot(driver, "11_book_details_entered")
    time.sleep(0.5)
    
    driver.find_element(By.XPATH, '//input[@type="submit" and contains(@value, "Add Book")]').click()
    take_screenshot(driver, "12_book_added")
    time.sleep(0.5)
    print(f"📚 Book '{book_name}' added successfully")

    print("➖ Removing book...")
    driver.find_element(By.LINK_TEXT, "Remove Books").click()
    take_screenshot(driver, "13_remove_books_page")
    time.sleep(2)

    driver.find_element(By.ID, "bookCode").send_keys(book_id)
    take_screenshot(driver, "14_book_id_entered")
    driver.find_element(By.XPATH, '//input[@type="submit" and contains(@value, "Remove")]').click()
    take_screenshot(driver, "15_remove_submitted")
    time.sleep(3)
    print(f"🗑️ Book with ID {book_id} removed successfully")

    print("ℹ️ Viewing about page...")
    driver.find_element(By.ID, "about").click()
    take_screenshot(driver, "16_about_page")
    time.sleep(2)
    print("✅ About page viewed successfully")

    print("🚪 Logging out...")
    driver.find_element(By.ID, "logout").click()
    take_screenshot(driver, "17_logged_out")
    time.sleep(2)
    print("✅ Logged out successfully")

except Exception as e:
    print(f"❌ Test failed: {str(e)}")
    raise

finally:
    print("🔚 Cleaning up...")
    if 'driver' in locals():
        driver.quit()
    print("✅ Browser closed")
