from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import tempfile

# === Book Test Data ===
book_quantity = "10"
book_id = "9138f76a-88a2-4224-92c8-51163ed909c6"
book_name = "one indian girl"
author = "chetan bhagat"
price = "399"
quantity = "2"

# === Chrome Headless Setup ===
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument(f'--user-data-dir={tempfile.mkdtemp()}')

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Open bookstore
    driver.get("http://192.168.70.41:8080/onlinebookstore/")
    time.sleep(2)

    # Step 2: Login as Admin
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@href="SellerLogin.html"]').click()
    time.sleep(2)
    driver.find_element(By.ID, "userName").send_keys("admin")
    driver.find_element(By.ID, "Password").send_keys("admin")
    driver.find_element(By.CLASS_NAME, "AdminLogin").click()
    time.sleep(2)

    if "Incorrect" in driver.page_source:
        print("❌ Login failed.")
        driver.quit()
        exit()
    print("✅ Logged in successfully.")

    # Step 3: Update Quantity in Store Books
    driver.find_element(By.ID, "storebooks").click()
    time.sleep(2)
    try:
        update_button = driver.find_element(By.XPATH, "//th[text()='9780132778046']/following-sibling::td/form/button[text()='Update']")
        update_button.click()
        time.sleep(2)
        print("🔄 Clicked 'Update' for book 9780132778046")

        quantity_field = driver.find_element(By.ID, "bookQuantity")
        quantity_field.clear()
        quantity_field.send_keys(book_quantity)
        driver.find_element(By.NAME, "updateFormSubmitted").click()
        print("✅ Book quantity updated.")
    except Exception as e:
        print(f"❌ Update failed: {e}")

    # Step 4: Add New Book
    driver.find_element(By.LINK_TEXT, "Add Books").click()
    time.sleep(2)
    driver.find_element(By.ID, "bookName").send_keys(book_name)
    driver.find_element(By.ID, "bookAuthor").send_keys(author)
    driver.find_element(By.NAME, "price").send_keys(price)
    driver.find_element(By.NAME, "quantity").send_keys(quantity)
    driver.find_element(By.XPATH, '//input[@type="submit" and contains(@value, "Add Book")]').click()
    print(f"📚 Book '{book_name}' added.")
    time.sleep(2)

    # Step 5: Remove Book by ID
    driver.find_element(By.LINK_TEXT, "Remove Books").click()
    time.sleep(2)
    driver.find_element(By.ID, "bookCode").send_keys(book_id)
    driver.find_element(By.XPATH, '//input[@type="submit" and contains(@value, "Remove")]').click()
    print(f"🗑️ Book with ID {book_id} removed.")
    time.sleep(2)

    # Step 6: Navigate to About Us
    driver.find_element(By.ID, "about").click()
    time.sleep(2)
    print("✅ Visited About Us page.")

    # Step 7: Logout
    try:
        driver.find_element(By.ID, "logout").click()
        print("✅ Logged out successfully.")
    except Exception as e:
        print(f"❌ Logout failed: {e}")

finally:
    driver.quit()
    print("🔚 Browser closed. All tests complete.")
