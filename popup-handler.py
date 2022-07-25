from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://tees.co.id/")

try:
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
    print("pop up muncul pak")
    driver.find_element(By.CLASS_NAME,"btn-modal-close").click( )
    print("pop up di close")

except TimeoutException:
    print("up tidak muncul")
    pass
