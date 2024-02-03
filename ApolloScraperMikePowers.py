import re
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

# In case you forgot how the plugin works check out this video :)

# https://www.youtube.com/watch?v=IgoIQutaVvg

# Make sure to have the following done:
# Python Installed
# Selenium Installed
# Chrome Driver Working
# Input your local user in the user_data_dir
# Login to apollo on the user instance (run it one time to see if your logged in or not and if not just log in)

# And then enjoy :)

chrome_options = Options()
user_data_dir = r'C:\Users\91731\AppData\Local\Google\Chrome\User Data\Default'
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_driver_path = './chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Link and name of CSV

driver.get("https://app.apollo.io/#/people?finderViewId=5b6dfc5a73f47568b2e5f11c&page=1&personLocations[]=Noida%2C%20India&personTitles[]=teacher&prospectedByCurrentTeam[]=yes")
csv_file_name = 'Developers.csv'

time.sleep(8)

def find_email_address(page_source):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, page_source)

def filter_emails(emails, excluded_domain):
    filtered = [email for email in emails if not email.endswith(excluded_domain)]
    return filtered[:2]

def split_name(name):
    parts = name.split()
    first_name = parts[0] if parts else ''
    last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
    return first_name, last_name

while True:
    try:
        loaded_section_selector = "[data-cy-loaded='true']"
        loaded_section = driver.find_element(By.CSS_SELECTOR, loaded_section_selector)

        tbodies = loaded_section.find_elements(By.TAG_NAME, 'tbody')
        if not tbodies:
            break

        for tbody in tbodies:
            first_anchor_text = tbody.find_element(By.TAG_NAME, 'a').text
            first_name, last_name = split_name(first_anchor_text)

            linkedin_url = ''
            for link in tbody.find_elements(By.TAG_NAME, 'a'):
                href = link.get_attribute('href')
                if 'linkedin.com' in href:
                    linkedin_url = href
                    break
            
            Apollo_url = ''
            for link in tbody.find_elements(By.TAG_NAME, 'a'):
                href = link.get_attribute('href')
                if 'app.apollo.io/#/contacts' in href:
                    Apollo_url = href
                    print(Apollo_url)
                    break


            job_title_element = tbody.find_element(By.CLASS_NAME, 'zp_Y6y8d')
            job_title = job_title_element.text if job_title_element else ''
            elements_with_class = tbody.find_elements(By.CLASS_NAME, 'zp_Y6y8d')
            location=''
            # Check if there is a second occurrence
            if len(elements_with_class) > 1:
                # Get the second occurrence for location
                location_element = elements_with_class[1]
                location = location_element.text
                print("location",location)
            else:
                location = ''
            

            company_name = ''
            for link in tbody.find_elements(By.TAG_NAME, 'a'):
                if 'accounts' in link.get_attribute('href'):
                    company_name = link.text
                    break

            phone_number = tbody.find_elements(By.TAG_NAME, 'a')[0].text

            button_classes = ["zp-button", "zp_zUY3r", "zp_hLUWg", "zp_n9QPr", "zp_B5hnZ", "zp_MCSwB", "zp_IYteB"]
            
            try:
                time.sleep(2)
                button = tbody.find_element(By.CSS_SELECTOR, "." + ".".join(button_classes))
                if button:
                    button.click()
                    email_addresses = find_email_address(driver.page_source)
                    filtered_emails = filter_emails(email_addresses, 'sentry.io')
                    print("asa",type(csv_file_name))
                    # Specify the location and file name variables
                    csv_location = 'C:/Users/91731/OneDrive/Desktop/New folder (2)'
                    csv_file_name = 'your_file.csv'

                    # Combine location and file name to get the full path
                    csv_file_path = os.path.join(csv_location, csv_file_name)
                    # Column names
                    columns = ["firstName", "lastName", "jobTitle", "companyName", "location", "email", "email2", "linkedinUrl", "phone_number", "ApolloUrl"]
                    with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        if file.tell() == 0:
                            writer.writerow(columns)
                        print("file",file)
                        print(f"{first_name} has been poached!")
                        if len(filtered_emails) == 1:
                            writer.writerow([first_name, last_name, job_title, company_name,location, filtered_emails[0], '', linkedin_url, phone_number,Apollo_url])
                        elif len(filtered_emails) == 2:
                            writer.writerow([first_name, last_name, job_title, company_name,location, filtered_emails[0], filtered_emails[1], linkedin_url, phone_number])
                    button.click()
                    tbody_height = driver.execute_script("return arguments[0].offsetHeight;", tbody)
                    driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", loaded_section, tbody_height)
            except NoSuchElementException:
                continue

        # Pagination Logic
        next_button_selector = ".zp-button.zp_zUY3r.zp_MCSwB.zp_xCVC8[aria-label='right-arrow']"
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, next_button_selector)
            next_button.click()
            time.sleep(1)
        except NoSuchElementException:
            print("No more pages to navigate.")
            break

    except Exception as e:
        error_message = str(e)
        if "element click intercepted" in error_message:
            print("Your leads are ready!")
            break
        else:
            print(f"An error occurred: {error_message}")
            break

driver.quit()