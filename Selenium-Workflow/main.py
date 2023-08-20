from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time,os
from dotenv import load_dotenv

import requests
import time
from bs4 import BeautifulSoup

from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'AC456d58d8a126e03030ba7dac3dc3930f'
auth_token = 'cebfde1985621293eee0bd214e326482'

# Create a Twilio client object
client = Client(account_sid, auth_token)

load_dotenv()

# webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
# "proxyType": "pac",
# "proxyAutoconfigUrl": "https://remote.iitm.ac.in:8371/proxy.pac"
# }

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=Options())
driver.get("http://workflow.iitm.ac.in/student")

uname = driver.find_element("xpath","""//*[@id="txtUserName"]""")
uname.send_keys(os.environ['rollno'])

pwd = driver.find_element("xpath","""//*[@id="txtPassword"]""")
pwd.send_keys(os.environ['password'])

login = driver.find_element("xpath","""//*[@id="Login"]""")
login.click()

x = driver.find_element("xpath","""/html/body/form/div[5]/div/ul/li[6]/a/span""")
x.click()

while(True):
    y = driver.find_element("xpath","""//*[@id="btnViewAvailablityElec"]""")
    y.click()

    time.sleep(5)

    z = driver.switch_to.frame("ifElectiveCourses")

    z = driver.find_elements("xpath","""//*[@id="courseDetails"]""")

    with open("./courses.txt", "w") as f:
        for i in z:
            ccode = i.find_element(By.CLASS_NAME,"lblCourseNo").text
            if(ccode=="HS5340" or ccode=="CS6111"):
                client.calls.create(
                    url='http://demo.twilio.com/docs/voice.xml',
                    to='+916305520922',
                    from_='+16073576154'
                )
                print(ccode)
            f.write(i.find_element(By.CLASS_NAME,"lblCourseNo").text+"\n")

    driver.refresh()