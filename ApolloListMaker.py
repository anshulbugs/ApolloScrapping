from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def my_selenium_module():
    chrome_options = Options()
    user_data_dir = r'C:\Users\91731\AppData\Local\Google\Chrome\User Data\Default'
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    chrome_driver_path = './chromedriver.exe'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the initial link
        driver.get("https://app.apollo.io/?utm_campaign=Transactional%3A+Account+Activation&utm_medium=transactional_message&utm_source=cio#/people?finderViewId=5b6dfc5a73f47568b2e5f11c&personTitles[]=teacher&page=1&personLocations[]=delhi")

        while True:
            time.sleep(4)
            # Perform actions on the page
            # Example: Clicking buttons
            button1 = driver.find_element(By.XPATH, "//html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/a[2]")
            
            button1.click()
            time.sleep(1)
            button2 = driver.find_element(By.XPATH, "//html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/div[1]/div[1]/div/button/div/div")
            button2.click()

            time.sleep(1)
            
            button3 = driver.find_element(By.CSS_SELECTOR,"a.zp-menu-item:nth-child(1)")
            # Click the element
            button3.click()
            time.sleep(2)
            button4 = driver.find_element(By.XPATH, "//html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/div[1]/div[3]/span[1]/button")
            
            # Click the element
            button4.click()

            # time.sleep(1)
            
            # button5 = driver.find_element(By.XPATH, "//div[@class='Select-placeholder' and text()='Enter or create lists...']")
            # # Click the element
            # button5.click()
            time.sleep(2)
            button6 = driver.find_element(By.XPATH, "//div[@class='zp_kxUTD' and @data-elem='button-label' and text()='Save']")
            # Click the element
            button6.click()
            time.sleep(2)

            # Find the element using the specified class in XPath
            element = driver.find_element(By.XPATH, "//span[contains(@class, 'zp_VVYZh')]")

            # Get the text content of the element and store it in a variable
            element_text = element.text

            # Now you can use the 'element_text' variable as needed
            print("Element text:", element_text)
            # Split the text based on the word 'of' and get the second part
            number_after_of = element_text.split('of')[-1].strip()

            # Convert the extracted string to an integer
            extracted_number = int(''.join(filter(str.isdigit, number_after_of)))

            # Now 'extracted_number' holds the value 1809
            print("Extracted number after 'of':", extracted_number)
            time.sleep(2)
            # Refresh the page
            driver.refresh()
            
            # Check for a specific condition
            # condition_met = check_condition(driver)
            # if condition_met:
            #     print("Condition met. Exiting loop.")
            #     break

            # Introduce a delay to avoid constant refreshing
            time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()
# Run the module
my_selenium_module()
