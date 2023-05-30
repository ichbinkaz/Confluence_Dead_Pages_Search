import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_driver_path = “path_to_your_web_driver”

conf_link = “your_confluence_link_of_pages”


# Set up the headless browser options
options = Options()
options.add_argument("--headless")

with open("credentials.txt", "r") as file:
    data = file.readlines()
    username = data[0].strip()
    password = data[1].strip()

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 20)
    driver.get(conf_link)
    # Find the login form elements and enter the username and password
    username_field = driver.find_element(By.ID, "userNameInput")
    password_field = driver.find_element(By.ID, "passwordInput")
    login_button = driver.find_element(By.ID, "submitButton")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

dead_spaces = []
page_index = 0
shouldContinue = True


def wait_for_element(selector):
    return WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )


def investigate_links():
    links = driver.find_elements(By.CSS_SELECTOR, ".space-name a")
    links = [link.get_attribute("href") for link in links]

    for link in links:
        driver.get(link)
        wait_for_element('#title-text')
        dead_space = driver.find_element(By.ID, "title-text")
        if dead_space.text == "Page Not Found":
            print(f"This space is dead for {link}")
            dead_spaces.append(link)
        else:
            print(f'The space is alive for {dead_space.text}')
    return links


def navigate_next_page():
    next_page = wait_for_element('.aui-nav-pagination .aui-nav-next a')
    driver.execute_script("arguments[0].click();", next_page)
    time.sleep(6)


main_url = driver.current_url

while shouldContinue:
    # Execute the JavaScript code that triggers the pagination event listener

    navigate_next_page()
    wait_for_element('#space-directory-wrapper')
    links = investigate_links()
    driver.get(main_url)

    page_index += 1
    print(page_index)
    for page in range(page_index):
        navigate_next_page()



