import re
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import random

def find_email_address(page_source):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, page_source)

def filter_emails(emails, excluded_domain):
    filtered = [email for email in emails if email and not email.endswith(excluded_domain)]
    return filtered[:2]

def split_name(name):
    parts = name.split()
    first_name = parts[0] if parts else ''
    last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
    return first_name, last_name
def my_selenium_module(url, csv_file,csv_location,pagesfrom):
    # chrome_options = Options()
    # user_data_dir = r'C:\Users\91731\AppData\Local\Google\Chrome\User Data\Default'
    # chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    # chrome_driver_path = './chromedriver.exe'
    # service = Service(chrome_driver_path)
    # driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--user-agent={}'.format(random.choice(list(self.user_agents))))

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(90)

    url=url
    csv_file_name='he.csv'
    if not csv_file.endswith('.csv'):
        csv_file_name = csv_file + '.csv'
    else:
        csv_file_name = csv_file
    csv_location =csv_location
    csv_file_path = os.path.join(csv_location, csv_file_name)
    try:
        # Navigate to the initial link
        driver.implicitly_wait(6)
        driver.get(url)
        
        
        time.sleep(1)
        pages = int(pagesfrom)
        NumberOfRecordsLeft = 26
        
        while NumberOfRecordsLeft>25  and pages > 0:
            print("pages",pages)
            time.sleep(20)
            # Perform actions on the page
            netNewButton = driver.find_element(By.XPATH, "(//div[contains(@class, 'zp-tabs')]/a[2])[3]")
        
            netNewButton.click()
            print("netNewButton")
            try :
                time.sleep(1)
                selectButton = driver.find_element(By.XPATH, "//button[@class='zp-button zp_zUY3r zp_B5hnZ zp_rhXT_ zp_FVbJk finder-select-multiple-entities-button']")

                selectButton.click()
                print("selectButton")
                time.sleep(1)
                selectPageButton = driver.find_element(By.CSS_SELECTOR,"a.zp-menu-item:nth-child(1)")
                # Click the element
                selectPageButton.click()
                print("selectPageButton")
                time.sleep(2)
                saveButton = driver.find_element(By.XPATH, "//button[@id='lists']")
                # Click the element
                saveButton.click()
                print("saveButton")
                addList = driver.find_element(By.XPATH, "//a[@class='zp-menu-item zp_fZtsJ zp_pEvFx']")
                addList.click()
                time.sleep(2)
                saveFinal = driver.find_element(By.XPATH, "//button[@data-cy='confirm']")

                # Click the element
                saveFinal.click()
                print("saveFinal")
                time.sleep(5)
                try:
                    refreshButton = driver.find_element(By.XPATH, "//div[@class='zp_QLlkg zp_CIHaN' and text()='Refresh prospects']")
                    refreshButton.click()
                    print("Refresh prospects button clicked")
                except NoSuchElementException:
                    print("Refresh prospects button not found")

                time.sleep(1)
                element = driver.find_element(By.XPATH, "//span[contains(@class, 'zp_VVYZh')]")
                print("number found")
                # Get the text content of the element and store it in a variable
                element_text = element.text if element else '' 

                number_after_of = element_text.split('of')[-1].strip()

                # Convert the extracted string to an integer
                extracted_number = int(''.join(filter(str.isdigit, number_after_of)))

                NumberOfRecordsLeft = extracted_number
                time.sleep(3)
                # Refresh the page
                print("1")
                driver.refresh()
            except NoSuchElementException:
                break
            pages = pages - 1

        time.sleep(2)
        # driver.refresh()
        while True:
            print("2")
            driver.get(url)
            time.sleep(5)
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
                        if link:
                            href = link.get_attribute('href')
                            if 'linkedin.com' in href:
                                linkedin_url = href
                                break
                    Apollo_url = ''
                    for link in tbody.find_elements(By.TAG_NAME, 'a'):
                        if link:
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
                        location = location_element.text if location_element else ''
                        print("location",location)
                    else:
                        location = ''
                    company_name = ''
                    for link in tbody.find_elements(By.TAG_NAME, 'a'):
                        if link and 'accounts' in link.get_attribute('href'):
                            company_name = link.text if link else ''
                            break

                    contactNo = tbody.find_elements(By.TAG_NAME, 'a')[-1].text  if tbody.find_elements(By.TAG_NAME, 'a')[-1] else ''

                    button_classes = ["zp-button", "zp_zUY3r", "zp_hLUWg", "zp_n9QPr", "zp_B5hnZ", "zp_MCSwB", "zp_IYteB"]
                    
                    try:
                        button = tbody.find_element(By.CSS_SELECTOR, "." + ".".join(button_classes))
                        if button:
                            button.click()
                            email_addresses = find_email_address(driver.page_source)
                            filtered_emails = filter_emails(email_addresses, 'sentry.io')
                            time.sleep(3)
                            # Column names
                            columns = ["firstName", "lastName","contactNo", "jobTitle", "companyName","email1","email2", "linkedinUrl",  "ApolloUrl","location"]
                            with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
            
                                writer = csv.writer(file)
                                if file.tell() == 0:
                                    writer.writerow(columns)   
                                print(f"{first_name} has been poached!")
                                if len(filtered_emails) == 1:
                                    writer.writerow([first_name, last_name,contactNo, job_title, company_name,filtered_emails[0], '', linkedin_url, Apollo_url,location])
                                elif len(filtered_emails) == 2:
                                    writer.writerow([first_name, last_name,contactNo, job_title, company_name,filtered_emails[0], filtered_emails[1], linkedin_url, Apollo_url,location])
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
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()
# Run the module
# my_selenium_module(url, csv_file_name)
