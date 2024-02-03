from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def find_and_click_btn(selector):
    try:
        btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        btn.click()
        return True
    except Exception as e:
        return False

def delay(seconds):
    time.sleep(seconds)

def set_and_click_list_value(value):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.zp_hZQVt input:nth-child(2)'))
        )
        last_value = element.get_attribute('value')
        element.clear()
        element.send_keys(value)
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        return True
    except Exception as e:
        return False

def waiting_to_next_page():
    try:
        btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="right-arrow"]'))
        )
        btn.click()
        return True
    except Exception as e:
        return False

def is_loaded_data():
    try:
        data_loading = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'table.zp_mxeOQ'))
        )
        return True
    except Exception as e:
        return False

def start(saved_data):
    for i in range(saved_data['leadCount']):
        if is_stop:
            break
        find_and_click_btn('button.zp-button.zp_zUY3r.zp_B5hnZ.zp_rhXT_.zp_FVbJk.finder-select-multiple-entities-button')
        find_and_click_btn('a.zp-menu-item.zp_fZtsJ.zp_pEvFx.zp_tEPsU')
        delay(1)
        find_and_click_btn('button#lists')
        find_and_click_btn('a.zp-menu-item.zp_fZtsJ.zp_pEvFx')
        set_and_click_list_value(saved_data['listName'])
        find_and_click_btn('button[data-cy="confirm"]')
        waiting_to_next_page()
        is_loaded_data()
        delay(1)

    find_and_click_btn('a.zp-menu-item.zp_fZtsJ.zp_pEvFx'); 
    delay(100)           
# Provide the URL of the page you want to automate
page_url = 'https://app.apollo.io/#/people?finderViewId=5b6dfc5a73f47568b2e5f11c&personTitles[]=recruiter&page=1&personLocations[]=Nashik%2C%20India&prospectedByCurrentTeam[]=no&pendo=t6mU4Y6iEdhxX5MQid4c4G8N1hc'

# Set up the Selenium WebDriver (you may need to download the appropriate driver for your browser)
driver = webdriver.Chrome()

# Open the webpage
driver.get(page_url)

# Set the initial stop condition
is_stop = False

# Your saved data
saved_data = {
    'leadCount': 2,  # Example value, replace with your actual data
    'listName': 'abcd'  # Example value, replace with your actual data
}

# Execute your main function
start(saved_data)

# Close the browser
driver.quit()
