from selenium import webdriver
import configure
import datetime
import time
import csv
import os

os.chdir(configure.my_path)

URL = 'https://ja.socialclub.rockstargames.com'

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=' + configure.chrome_path)
browser = webdriver.Chrome(options=options)

browser.get(URL)
time.sleep(10)

# For Singin Function at Firsttime
def Sitelogin():
    signin_btn = browser.find_element_by_xpath('//*[@id="app-page"]/div[1]/div/div/div/div/div/div[1]/a[1]')
    signin_btn.click()

    email = browser.find_element_by_xpath('//*[@id="app-page"]/div[2]/div[1]/div/div/form/fieldset[1]/span/input')
    email.send_keys(configure.email)

    password = browser.find_element_by_xpath('//*[@id="app-page"]/div[2]/div[1]/div/div/form/fieldset[2]/span[1]/span[1]/input')
    password.send_keys(configure.password)

    login_btn = browser.find_element_by_xpath('//*[@id="app-page"]/div[2]/div[1]/div/div/form/fieldset[3]/div/button')
    login_btn.click()

browser.get('/'.join([URL, 'games/gtav/pc/career/overview/gtaonline']))
time.sleep(3)

getcash = browser.find_element_by_xpath('//*[@id="cash-value"]').text
getbank = browser.find_element_by_xpath('//*[@id="bank-value"]').text

# Change datatype integer
cash = int(getcash[1:].replace(',', ''))
bank = int(getbank[1:].replace(',', ''))

gettime = datetime.datetime.today().strftime('%Y/%m/%d %H:%M')

with open('.\\data\\gtacashflow.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([gettime, cash, bank])


browser.close()
browser.quit()


