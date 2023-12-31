import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

opcion = Options()
ser = Service(ChromeDriverManager().install())
opcion.add_argument("--window-size= 600, 600")

navegador = webdriver.Chrome(service=ser, options=opcion)
navegador.get("https://pypi.org/account/login/")


user = navegador.find_element(By.ID, "username")
user.send_keys("Tuanzy.f")

password = navegador.find_element(By.ID, "password")
password.send_keys("ZCy!9*b$m85+395")

login = navegador.find_element(By.CSS_SELECTOR, "button.button--primary")
login.click()

time.sleep(120)

navegador.save_screenshot("screenshot.png")
navegador.quit()