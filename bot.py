import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

EMAIL = os.getenv("prasadrmore786@gmail.com")
PASSWORD = os.getenv("Seema@786")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.naukri.com")
    time.sleep(5)

    driver.find_element(By.ID, "login_Layer").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Email')]").send_keys(EMAIL)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'password')]").send_keys(PASSWORD)

    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(7)

    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(7)

    upload = driver.find_element(By.XPATH, "//input[@type='file']")
    upload.send_keys(os.path.abspath("resume.pdf"))

    time.sleep(5)
    print("✅ Resume uploaded successfully!")

finally:
    driver.quit()