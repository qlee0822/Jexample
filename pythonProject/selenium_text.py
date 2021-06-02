from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time
import requests
import json

browser = webdriver.Chrome("./chromedriver.exe")

#1. CNE메일 이동
browser.get("https://mail.cne.go.kr/account/except/login.do")

#2.ID, PW입력
browser.find_element_by_id("userId").send_keys("opencert")
browser.find_element_by_id("password").send_keys("rydbrwjdqh!!")

#3 로그인 버튼 클릭
browser.find_element_by_xpath("//*[@id='loginForm']/div/div/div/section[1]/div/button").submit()

try:
    #10동안 기다렸다가 수행
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='mailListPane']/div[1]")))
    agent_url = "https://mail.cne.go.kr/common/json/agent.do"
    user_agent = browser.execute_script("return navigator.userAgent;")
    s = requests.session()
    headers = {"User-Agent": "{}".format(user_agent)}
    s.headers.update(headers)

    for cookie in browser.get_cookies():
        c = {cookie['name']: cookie['value']}
        s.cookies.update(c)

    res = s.get(agent_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    jsonRes = json.loads(soup.text)
    mailList = jsonRes['mailboxlist']
    for mail_name in mailList:
        print("forderkey: {0}".format(mail_name['folderKey']))
        print("folderName: {0}".format(mail_name['folderName']))
        print("mailcount: {0}".format(mail_name['mailcount']))
        print("newmailcount: {0}".format(mail_name['newmailcount']))
        print("isAlarm: {0}".format(mail_name['isAlarm']))
        print("-" * 100)
finally:
    browser.quit()
#time.sleep(3)

#4 브라우저 새로고침
#browser.find_element_by_xpath("//*[@id='btn_reload']").click()


