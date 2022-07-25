from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/alerts")

driver.find_element(By.ID,"timerAlertButton").click()

try:
    WebDriverWait(driver,100).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("Alert dipencet")

except TimeoutException:
    print("Alert tidak muncul")
    pass