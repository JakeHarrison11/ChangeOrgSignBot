from selenium import webdriver as wd
from pyautogui import press
from time import sleep
from faker import Faker
import json
import random

print("""
  ____  _             ____        _
 / ___|(_) __ _ _ __ | __ )  ___ | |_
 \___ \| |/ _` | '_ \|  _ \ / _ \| __|
  ___) | | (_| | | | | |_) | (_) | |_
 |____/|_|\__, |_| |_|____/ \___/ \__|
          |___/
""")

link = input("Paste share link here: ")

fname = json.loads(open('fnames.json').read())
lname = json.loads(open('lnames.json').read())
defualt_driver = wd.Chrome()
fake = Faker()

def sendForm(runs):
        randfname = random.randrange(1000)
        randlname = random.randrange(1000)
        randemail = fake.email()
        fnamebox = defualt_driver.find_element_by_name("firstName")
        lnamebox = defualt_driver.find_element_by_name("lastName")
        emailbox = defualt_driver.find_element_by_name("email")
        signbutton = defualt_driver.find_element_by_xpath("""//*[@id="page"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button[2]""")
        publiccheck = defualt_driver.find_element_by_name("public")
        print("Using name", fname[randfname], lname[randlname], "and email", randemail, "This is run number", runs)
        fnamebox.send_keys(fname[randfname])
        lnamebox.send_keys(lname[randlname])
        emailbox.send_keys(randemail)
        sleep(0.5)
        publiccheck.click()
        sleep(0.5)
        signbutton.click()
        sleep(1)
        defualt_driver.delete_all_cookies()
        defualt_driver.get(link)

def main():
    defualt_driver.get(link)
    runsMade = 0
    for _ in range(1, 1000):
        try:
            sendForm(runsMade)
            runsMade += 1
        except:
            defualt_driver.delete_all_cookies()
            defualt_driver.get(link)
            print("Error filling form. Refreshing...")
main()
