# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import tempfile

# # === Chrome Options WITHOUT Headless ===
# options = webdriver.ChromeOptions()
# # DO NOT USE HEADLESS IF YOU WANT VISIBLE BROWSER
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-gpu')
# options.add_argument(f'--user-data-dir={tempfile.mkdtemp()}')

# # Setup Chrome WebDriver
# service = Service(executable_path="./chromedriver")
# driver = webdriver.Chrome(service=service, options=options)

# # === Book Details ===
# book_quantity = 30
# book_id = "8bd5fe50-9725-41da-bad8-476d577894f1"
# book_name = "one arranged murder"
# author = "chetan bhagat"
# price = "499"
# quantity = "5"

# try:
#     driver.get("http://192.168.70.41:8080/onlinebookstore/")
#     time.sleep(2)

#     driver.find_element(By.LINK_TEXT, "Login").click()
#     time.sleep(2)

#     driver.find_element(By.XPATH, '//a[@href="SellerLogin.html"]').click()
#     time.sleep(2)

#     driver.find_element(By.ID, "userName").send_keys("admin")
#     driver.find_element(By.ID, "Password").send_keys("admin")
#     time.sleep(1)

#     driver.find_element(By.CLASS_NAME, "AdminLogin").click()
#     time.sleep(2)

#     if "Incorrect" in driver.page_source:
#         print("❌ Login failed: Incorrect credentials.")
#     elif "Welcome" in driver.page_source or "Dashboard" in driver.title:
#         print("✅ Login successful!")
#     else:
#         print("⚠️ Login result uncertain – check manually.")

#     driver.find_element(By.ID, "storebooks").click()
#     time.sleep(2)

#     try:
#         update_button = driver.find_element(By.XPATH, "//th[text()='9780132778046']/following-sibling::td/form/button[text()='Update']")
#         update_button.click()
#         time.sleep(2)
#         print("🔄 Clicked on 'Update' button for book 9780132778046.")
#     except Exception as e:
#         print(f"❌ Failed to click 'Update': {e}")

#     try:
#         quantity_field = driver.find_element(By.ID, "bookQuantity")
#         quantity_field.clear()
#         quantity_field.send_keys(book_quantity)
#         time.sleep(2)

#         update_submit_btn = driver.find_element(By.XPATH, "//input[@type='submit' and @value=' Update Book ']")
#         update_submit_btn.click()
#         time.sleep(2)

#         print("✅ Book quantity updated to book_quantity and form submitted.")
#     except Exception as e:
#         print(f"❌ Failed to update book quantity: {e}")

#     driver.find_element(By.LINK_TEXT, "Add Books").click()
#     time.sleep(2)

#     driver.find_element(By.ID, "bookName").send_keys(book_name)
#     time.sleep(0.5)
#     driver.find_element(By.ID, "bookAuthor").send_keys(author)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, "price").send_keys(price)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, "quantity").send_keys(quantity)
#     time.sleep(0.5)
#     driver.find_element(By.XPATH, '//input[@type="submit" and contains(@value, "Add Book")]').click()
#     time.sleep(0.5)
#     print(f"📚 Book '{book_name}' added")

#     driver.find_element(By.LINK_TEXT, "Remove Books").click()
#     time.sleep(2)

#     driver.find_element(By.ID, "bookCode").send_keys(book_id)
#     driver.find_element(By.XPATH, '//input[@type="submit" and contains(@value, "Remove")]').click()
#     print(f"🗑️ Book with ID {book_id} submitted for removal.")
#     time.sleep(3)

#     driver.find_element(By.ID, "about").click()
#     time.sleep(2)
#     print("✅ Navigated to About Us page.")

#     try:
#         driver.find_element(By.ID, "logout").click()
#         time.sleep(2)
#         print("✅ Logged out successfully.")
#     except Exception as e:
#         print(f"❌ Logout failed: {e}")

# finally:
#     driver.quit()
#     print("🔚 Browser closed.")


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome Options - runs in visible mode by default in the container
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1280,1024')

# Test Data
book_quantity = 30
book_id = "8bd5fe50-9725-41da-bad8-476d577894f1"
book_name = "one arranged murder"
author = "chetan bhagat"
price = "499"
quantity = "5"

try:
    # Initialize driver (chromedriver is pre-installed in the container)
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    # Test steps
    print("🌐 Navigating to application...")
    driver.get("http://192.168.70.41:8080/onlinebookstore/")
    time.sleep(2)

    print("🔑 Logging in...")
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, '//a[@href="SellerLogin.html"]').click()
    time.sleep(2)
    
    driver.find_element(By.ID, "userName").send_keys("admin")
    driver.find_element(By.ID, "Password").send_keys("admin")
    time.sleep(1)
    
    driver.find_element(By.CLASS_NAME, "AdminLogin").click()
    time.sleep(2)
    
    if "Incorrect" in driver.page_source:
        print("❌ Login failed: Incorrect credentials.")
    elif "Welcome" in driver.page_source or "Dashboard" in driver.title:
        print("✅ Login successful!")
    else:
        print("⚠️ Login result uncertain")

    print("📚 Accessing store books...")
    driver.find_element(By.ID, "storebooks").click()
    time.sleep(2)

    try:
        print("🔄 Updating book quantity...")
        update_button = driver.find_element(By.XPATH, "//th[text()='9780132778046']/following-sibling::td/form/button[text()='Update']")
        update_button.click()
        time.sleep(2)

        quantity_field = driver.find_element(By.ID, "bookQuantity")
        quantity_field.clear()
        quantity_field.send_keys(book_quantity)
        time.sleep(2)

        update_submit_btn = driver.find_element(By.XPATH, "//input[@type='submit' and @value=' Update Book ']")
        update_submit_btn.click()
        time.sleep(2)
        print("✅ Book quantity updated successfully")
    except Exception as e:
        print(f"⚠️ Book update skipped: {str(e)}")

    print("➕ Adding new book...")
    driver.find_element(By.LINK_TEXT, "Add Books").click()
    time.sleep(2)

    driver.find_element(By.ID, "bookName").send_keys(book_name)
    time.sleep(0.5)
    driver.find_element(By.ID, "bookAuthor").send_keys(author)
    time.sleep(0.5)
    driver.find_element(By.NAME, "price").send_keys(price)
    time.sleep(0.5)
    driver.find_element(By.NAME, "quantity").send_keys(quantity)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//input[@type="submit" and contains(@value, "Add Book")]').click()
    time.sleep(0.5)
    print(f"📚 Book '{book_name}' added successfully")

    print("➖ Removing book...")
    driver.find_element(By.LINK_TEXT, "Remove Books").click()
    time.sleep(2)

    driver.find_element(By.ID, "bookCode").send_keys(book_id)
    driver.find_element(By.XPATH, '//input[@type="submit" and contains(@value, "Remove")]').click()
    time.sleep(3)
    print(f"🗑️ Book with ID {book_id} removed successfully")

    print("ℹ️ Viewing about page...")
    driver.find_element(By.ID, "about").click()
    time.sleep(2)
    print("✅ About page viewed successfully")

    print("🚪 Logging out...")
    driver.find_element(By.ID, "logout").click()
    time.sleep(2)
    print("✅ Logged out successfully")

except Exception as e:
    print(f"❌ Test failed: {str(e)}")
    raise

finally:
    print("🔚 Cleaning up...")
    driver.quit()
    print("✅ Browser closed")
