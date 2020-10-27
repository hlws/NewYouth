# 作者    lishaoteng
# 时间    2020-10-27 15:55
# IDE   PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("D:\python\chromedriver.exe")
url="";
driver.get(url)  #需要打开的网址
user = driver.find_element_by_id("username") #审查元素username的id
user.send_keys("hanlimang")  #输入账号
password = driver.find_element_by_name("password") #审查元素password的name
password.send_keys("han@123456")  #输入密码
password.send_keys(Keys.RETURN) #实现自动点击登陆
print('登陆成功')