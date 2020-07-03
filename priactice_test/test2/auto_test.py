# coding: utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

while True:
    # 登录xxx.com
    driver.get("https://10.47.121.15/skyeye/home/login")
    # 等10秒，浏览器打开和网页跳转需要时间
    time.sleep(5)
    # 取ID为txtLoginCode的网页元素(用户名输入元素)
    elem_user = driver.find_element_by_xpath('//*[@id="app-comp"]/div/div[2]/div[2]/div[1]/input')
    # 清空输入
    elem_user.clear()
    # 键入用户名
    elem_user.send_keys('admin')
    # 取ID为txtPwd的网页元素(密码输入元素)
    elem_pass = driver.find_element_by_xpath('//*[@id="app-comp"]/div/div[2]/div[2]/div[2]/input')
    # 清空输入
    elem_pass.clear()
    # 键入密码
    elem_pass.send_keys('admin123')
    # # 获取验证码
    # yzm = driver.find_element_by_xpath('//*[@id="app-comp"]/div/div[2]/div[2]/div[3]/img')
    # yzm.click()
    # # 输入验证码
    # input_yzm = driver.find_element_by_xpath('//*[@id="app-comp"]/div/div[2]/div[2]/div[3]/input')
    # input_yzm.send_keys('')
    # 取ID为btnLogin的登录按钮
    elem_login = driver.find_element_by_xpath('//*[@id="app-comp"]/div/div[2]/div[2]/button')
    # 点击登录按钮
    elem_login.click()
    # 静止3秒退出
    time.sleep(3)
    exit_box = driver.find_element_by_xpath('//*[@id="header"]/div/div[3]/div/div')
    exit_box.click()
    time.sleep(2)
    exit1 = driver.find_element_by_xpath('//*[@id="header"]/div/div[3]/div/ul/li[2]')
    exit1.click()
    continue
