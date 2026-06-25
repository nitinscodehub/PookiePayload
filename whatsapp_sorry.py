import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CONTACT = "jis name se contact save kiya hai wo likh like : shivam"
NUMBER = "number yaha enter kar +91xxxxx"
MESSAGE = "sorry"

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/kali/.config/google-chrome")
options.add_argument("--profile-directory=Profile 1")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
service = Service("/usr/bin/chromedriver")

print("Opening Chrome...")
driver = webdriver.Chrome(service=service, options=options)
print("Chrome opened! Loading WhatsApp Web...")
driver.get(f"https://web.whatsapp.com/send?phone={NUMBER}")
wait = WebDriverWait(driver, 120)

time.sleep(5)
print(f"Page title: {driver.title}")

try:
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
    print(f"Chat with {CONTACT} opened!")
except:
    try:
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @spellcheck="true"]')))
        print(f"Chat with {CONTACT} opened! (alt selector)")
    except:
        driver.save_screenshot("/home/kali/Desktop/whatsapp_debug.png")
        print("Screenshot saved. Chat not found.")
        input("Press Enter to try the search box method...")

        search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
        search_box.click()
        search_box.send_keys(CONTACT)
        time.sleep(3)

        contact = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{CONTACT}"]')))
        contact.click()
        time.sleep(2)

        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))

count = 1
try:
    while True:
        input_box.send_keys(MESSAGE)
        input_box.send_keys(Keys.ENTER)
        print(f"Sent '{MESSAGE}' #{count}")
        count += 1
        time.sleep(2)
except KeyboardInterrupt:
    print("\nStopped.")
    driver.quit()
