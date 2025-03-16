from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()

# Define the range of years and weeks to loop through
start_year = 2019
end_year = 2024
start_week_2019 = 45  # Starting week for 2019
end_week_2024 = 52  # Ending week for 2024

# Loop through years and weeks
for year in range(start_year, end_year + 1):
    # Determine the starting and ending week for each year
    start_week = start_week_2019 if year == 2019 else 1
    end_week = end_week_2024 if year == 2024 else 52

    for week in range(start_week, end_week + 1):
        # Construct the URL for the current week
        url = f"https://www.top-charts.com/songs/all-genres/vietnam/apple-music/{year}-W{week:02d}"
        
        # Open the website
        driver.get(url)
        print(f"Opened URL: {url}")

        try:
            # Wait for the element to be clickable
            xpath = "/html/body/div[5]/div[2]/div/div[2]/div/div[1]/a"
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            # Click on the element
            element.click()

            # Wait for a few seconds to ensure the action is completed
            time.sleep(5)

        except Exception as e:
            print(f"Error on {url}: {e}")

# Close the browser
driver.quit()
