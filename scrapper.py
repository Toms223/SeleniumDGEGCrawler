import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.FirefoxOptions()
options.add_argument("-headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", os.getcwd())

if __name__ == "__main__":
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1920, 1080)

    browser.get('https://precoscombustiveis.dgeg.gov.pt/')
    browser.find_element(By.CLASS_NAME, "btn-refuse").click()
    select = Select(browser.find_element(By.ID, "cboTipoCombustivel"))
    select.select_by_value("3201")
    select = Select(browser.find_element(By.ID, "cboMarca"))
    select.select_by_value("38")
    select = Select(browser.find_element(By.ID, "cboDistrito"))
    select.select_by_value("14")
    select = Select(browser.find_element(By.ID, "cboMunicipio"))
    select.select_by_value("218")
    browser.find_element(By.CLASS_NAME, "btn_pesquisar").click()
    time.sleep(10)
    browser.find_element(By.CLASS_NAME, "alert-link").click()
    time.sleep(10)
    browser.find_element(By.CLASS_NAME, "link_csv").find_element(By.TAG_NAME, "a").click()
    browser.close()
