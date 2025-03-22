import sys
sys.stdout.reconfigure(encoding='utf-8')  # Fix console output on Windows

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# XPaths
dropdown_button_xpath = "/html/body/div[2]/div[1]/div[1]/div/main/div[1]/div/div[2]/div/div[1]/button/i"
prev_button_xpath = "/html/body/div[2]/div[1]/div[1]/div/main/div[1]/div/div[2]/div/div[2]/div/div/button[1]/i"
next_button_xpath = "/html/body/div[2]/div[1]/div[1]/div/main/div[1]/div/div[2]/div/div[2]/div/div/button[2]/i"
last_song_xpath = "/html/body/div[2]/div[1]/div[1]/div/main/div[1]/div/div[3]/div/div[40]"

week_xpaths = [
    f"/html/body/div[2]/div[1]/div[1]/div/main/div[1]/div/div[2]/div/div[2]/div/ul/li[{i}]/span[2]" for i in range(1, 7)
]

def close_popup():
    """Close any popup if present."""
    popup_xpath = "/html/body/div[2]/div[2]/div/button"
    try:
        popup_button = wait.until(EC.element_to_be_clickable((By.XPATH, popup_xpath)))
        popup_button.click()
        print("✅ Closed popup")
        time.sleep(1)
    except Exception:
        print("⚠️ No popup found or already closed.")

def navigate_to_august_2018():
    """Navigate to August 2018 by clicking 'Previous' 78 times."""
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))).click()
        time.sleep(1)
    except Exception:
        print("⚠️ Failed to open dropdown menu.")

    for i in range(78):  # Click 'Previous' 78 times to reach August 2018
        try:
            prev_button = wait.until(EC.element_to_be_clickable((By.XPATH, prev_button_xpath)))
            driver.execute_script("arguments[0].click();", prev_button)
            time.sleep(0.3)
            print(f"🔄 Click {i+1}/78")
        except Exception:
            print(f"⚠️ Failed on click {i+1}")
            break

    time.sleep(1)

def count_weeks():
    """Count how many weeks are available in the current month."""
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))).click()
        time.sleep(1)
    except Exception:
        print("⚠️ Failed to open dropdown menu.")

    available_weeks = []
    
    for xpath in week_xpaths:
        try:
            week_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            week_label = week_element.text.strip()
            if week_label:
                available_weeks.append((week_label, xpath))
        except Exception:
            break  # Stop if no more weeks are found

    print(f"📅 Found {len(available_weeks)} weeks: {[w[0] for w in available_weeks]}")
    return available_weeks

def scrape_chart(week_label, csv_writer):
    """Scrape the top 40 songs for the given week."""
    print(f"📌 Scraping {week_label}...")

    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        if driver.find_elements(By.XPATH, last_song_xpath):
            break

    song_count = 0
    for i in range(1, 41):
        try:
            song_container_xpath = f"/html/body/div[2]/div[1]/div[1]/div/main/div[1]/div/div[3]/div/div[{i}]"
            song_element = wait.until(EC.presence_of_element_located((By.XPATH, song_container_xpath)))
            driver.execute_script("arguments[0].scrollIntoView();", song_element)
            time.sleep(0.3)

            song_data = song_element.text.split("\n")

            if len(song_data) >= 3:
                rank = song_data[0].strip()
                if song_data[1].strip().isdigit() or song_data[1].strip().startswith(("+", "-")):
                    song_name = song_data[2].strip()
                    artist = song_data[3].strip() if len(song_data) > 3 else "Unknown"
                else:
                    song_name = song_data[1].strip()
                    artist = song_data[2].strip()
            else:
                rank, song_name, artist = "?", "?", "?"

            print(f"{rank}. {song_name} - {artist}")
            csv_writer.writerow([week_label, rank, song_name, artist])
            song_count += 1

        except Exception:
            print(f"⚠️ Skipping song {i}")

    if song_count == 0:
        print(f"⚠️ No songs found for {week_label}, moving to the next week.")

def move_to_next_month():
    """Navigate to the next month."""
    try:
        next_button = driver.find_element(By.XPATH, next_button_xpath)
        if next_button.is_enabled():
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(2)
            print("➡️ Moved to next month.")
            return True
    except Exception:
        print("⚠️ Could not move to next month.")
    return False

# CSV File Setup
csv_filename = "zing_weekly_chart_2018_2024.csv"
with open(csv_filename, "w", newline="", encoding="utf-8-sig") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Week", "Rank", "Song Name", "Artist"])

    try:
        driver.get("https://zingmp3.vn/zing-chart-tuan/bai-hat-Viet-Nam/IWZ9Z08I.html")
        close_popup()
        navigate_to_august_2018()

        while True:
            weeks_in_month = count_weeks()

            for week_label, week_xpath in weeks_in_month:
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))).click()
                    time.sleep(1)
                    wait.until(EC.element_to_be_clickable((By.XPATH, week_xpath))).click()
                    time.sleep(2)
                    scrape_chart(week_label, csv_writer)
                except Exception:
                    print(f"⚠️ Failed to select {week_label}")

            if not move_to_next_month():
                break  # Stop when reaching December 2024

    finally:
        driver.quit()
        print("Browser closed.")

print(f"✅ Data saved to '{csv_filename}'!")
