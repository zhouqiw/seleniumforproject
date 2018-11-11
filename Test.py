#selenium学习网页
# https://blog.csdn.net/c406495762/article/details/72331737#2-问题分析

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# 设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.baidu.com")
q = driver.find_element_by_id("kw")
time.sleep(0.5)
q.send_keys("周齐")
q.send_keys(Keys.RETURN)
driver.quit()