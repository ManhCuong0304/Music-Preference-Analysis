from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta

# Credentials for login
USERNAME = "datevent09@gmail.com"
PASSWORD = "D@tevent092001"

# Set up WebDriver
driver = webdriver.Chrome()

def get_next_week_date(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    next_week_date = start_date + timedelta(days=7)
    return next_week_date.strftime("%Y-%m-%d")

try:
    # Navigate to the login page
    login_url = "https://charts.spotify.com/charts/overview/global"
    driver.get(login_url)

    # Wait for the login button and click it
    wait = WebDriverWait(driver, 20)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/header/div/div[2]/a/span[1]')))
    login_button.click()

    # Input username and password
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[1]/input')))
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/input')

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    # Click the "Log In" button
    login_submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]')))
    login_submit_button.click()

    # Wait for the redirection to complete and page to load
    time.sleep(5)

    start_date_str = "2018-03-15"
    end_date_str = "2024-12-26"
    current_date_str = start_date_str

    while current_date_str <= end_date_str:
        # Redirect to the desired URL with dynamically updated date
        target_url = f"https://charts.spotify.com/charts/view/regional-vn-weekly/{current_date_str}"
        driver.get(target_url)

        # Wait for any possible overlay to disappear (Option 1)
        try:
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.ot-sdk-row')))
        except:
            pass  # If overlay doesn't exist, proceed without waiting

        # Wait for the download button to be clickable, and use JavaScript click if necessary (Option 3)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[2]/span/span/button')))
        driver.execute_script("arguments[0].click();", download_button)
        
        # Wait to ensure the download completes
        time.sleep(10)

        # Move to the next week's date
        current_date_str = get_next_week_date(current_date_str)

finally:
    driver.quit()
