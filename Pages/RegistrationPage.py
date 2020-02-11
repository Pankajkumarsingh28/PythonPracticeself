from Library import  ConfigReader
class RegistrationClass:

    def __init__(self,obj):## This is constructor
        global driver
        driver=obj



    def enter_username(self,username):
        driver.find_element_by_name(ConfigReader.fetchElementLocater("Registration", "username")).send_keys(username)

    def enter_email(self,email):
        driver.find_element_by_name(ConfigReader.fetchElementLocater("Registration", "email")).send_keys(email)

    def enter_password(self,password):
        driver.find_element_by_name(ConfigReader.fetchElementLocater("Registration", "password")).send_keys(password)

    def cnf_password(self,cnfpassword):
        driver.find_element_by_name(ConfigReader.fetchElementLocater("Registration", "cnf_fld_cpassword")).send_keys(cnfpassword)