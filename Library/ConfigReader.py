from configparser import ConfigParser

def readconfigData(section,key):
    config=ConfigParser()
    config.read("C:/Users/pankaj_kumar4/PycharmProjects/End_To_End_Automation_23_Dec'19/ConfigurationFiles/Config.cfg")
    return config.get(section,key)


#print(readconfigData("section1","Application_URL"))
def fetchElementLocater(section,key):
    config = ConfigParser()
    config.read("C:/Users/pankaj_kumar4/PycharmProjects/End_To_End_Automation_23_Dec'19/ConfigurationFiles/Elements.cfg")
    return config.get(section, key)
