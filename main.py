from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

# URL = "https://www.linkedin.com/jobs/search/?f_L=Seoul%2C%20South%20Korea&f_LF=f_AL&geoId=103588929&keywords=python%20developer&location=Seoul%2C%20South%20Korea"
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

chrome_driver_path = "C:/development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(URL)

login_button = driver.find_element_by_class_name("nav__button-secondary") #driver.find_element_by_link_text("Sign in")
login_button.click()

user_name = driver.find_element_by_id("username")
user_name.send_keys("wolfthestrider@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("NaruisTenacious9")
login = driver.find_element_by_class_name("login__form_action_container")
login.click() #password.send_keys(Keys.ENTER)

time.sleep(6)

job_list = driver.find_elements_by_class_name("job-card-list__title")
for i in job_list:
    print("called")
    i.click()
    time.sleep(2)
    try:
        job_apply_button = driver.find_element_by_class_name("jobs-apply-button--top-card")  # driver.find_element_by_css_selector(".jobs-s-apply button")
        job_apply_button.click()

        phone_number = driver.find_element_by_class_name("ember-text-field")
        phone_number.send_keys("01055447365")

        submit_button = driver.find_element_by_css_selector("footer .display-flex .artdeco-button")  # "footer button"

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_css_selector(".artdeco-modal__actionbar .artdeco-button--primary")
            #discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complexity detected. Skip.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button. Skip.")
        continue

driver.quit()