from selenium.webdriver import Chrome
from Library import ConfigReader
import pandas as pd

def startBrowser(self):
        global driver

        driver = Chrome("C:\\Users\\pankaj_kumar4\\Downloads\\chromedriver79.exe")
      #  driver.get("https://thetestingworld.com/testings/")
        driver.get(ConfigReader.readconfigData("section1","Application_URL"))

        driver.maximize_window()
        return driver

def closeBrowser(self):
        driver.close()