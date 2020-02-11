from BaseFiles import InitiateDriver
from Library import ConfigReader
from selenium.webdriver import Chrome
from Pages import RegistrationPage
def test_validRegisteration(self=None): # This is for entering all the elements of Registration.
    driver=InitiateDriver.startBrowser(self)
    #driver.find_element_by_name(ConfigReader.fetchElementLocater("Registration","username")).send_keys("Pankaj Kumar")
    #driver.find_element_by_name(ConfigReader.fetchElementLocater("Registration","email")).send_keys("pks@gmail.com")
    #driver.find_element_by_name(ConfigReader.fetchElementLocater("Registration","password")).send_keys("123456")
    #driver.find_element_by_name(ConfigReader.fetchElementLocater("Registration","cnf_fld_cpassword")).send_keys("123456")
    register=RegistrationPage.RegistrationClass(driver)
    register.enter_username('Pankaj Kumar Singh')
    register.enter_email('pks@gmail.com')
    register.enter_password('123456')
    register.cnf_password('123456')