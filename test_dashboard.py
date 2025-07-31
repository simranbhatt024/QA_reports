from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open login page
    driver.get("https://auth.segwise.ai/en/login")
    time.sleep(2)

    # Step 2: Fill email and password
    input_fields = driver.find_elements(By.TAG_NAME, "input")
    input_fields[0].send_keys("qa@segwise.ai")
    input_fields[1].send_keys("segwise_test")

    # Step 3A: Try clicking the login button
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()
    except:
        # Step 3B: Fallback – try submitting through password field
        input_fields[1].submit()

    # Step 4: Wait for successful login → redirected to app/ua dashboard
    WebDriverWait(driver, 15).until(
        EC.url_contains("https://ua.segwise.ai/qa_assignment/creatives/35?")
    )

    # Step 5: Assert chart is present
    chart = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.recharts, "recharts-cartesian-grid-horizontal"))
    )
    assert chart.is_displayed(), "Chart not visible"
    print(" Chart is visible on dashboard.")



finally:
    time.sleep(5)
    driver.quit()
