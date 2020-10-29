# 作者    lishaoteng
# 时间    2020-10-27 15:55
# IDE   PyCharm
from selenium import webdriver
import time
import random
# 指定驱动路径
driver = webdriver.Chrome("D:\python\chromedriver.exe")
# 需要打开的URL地址
url = "http://bqtw.baicgroup.com.cn:1200/"
# 定义人员列表
listMember = ['王超','方佳佳','马海欧','于雷','马少杰','乔振兴','张宁宁','黄硕','张荣祥','王琴','李轩','王永祺','王若男',
            '郭春慧','卢艺盟','王缘','王海勇','鲁文霞','魏久磊','王涛','亢雯','王梓','刘汉青','包阳','王哲轩','陈湘涛',
            '梁冰','陈鑫泽','王力','张惟琛','佟桐','孙建丽','曹文莹','侯莉红','赵志华','王亚平','李天宇','李思','张燕楠',
            '张峣','张雅楠','张泽宇','陈薇','李然','王斐','刘艳','王俊荣','王伟涛','何昊阳','徐燕茹','杨婧','董倩妤',
            '高健城','宁培','白建伟','何金鸿','刘涛','陈珏成','高玉祥','孙飞','景灿','郭洪凯','马雨晴','秦赓雨','周颖',
            '卢晓萌','马敏','张兵','吴童语','冯鹏辉','刘慧婷','齐远航','李少腾','张凯','庞久鹤','杨琳','李加城','徐茂苗',
            '陈思哲','别汉华','肖骞','李振鹏','李昀岭','许文韬','代欣','殷韵','王瑛珊','刘荧','李莹','张佳惠','李壮',
            '乔亚杰','刘聚源','陈正才','陈雨凝','周明宇','宋烨空']
for i in listMember:
    driver.get(url)
    time.sleep(3)
    AylcId = driver.find_element_by_id("AylcId")
    AylcId.send_keys("北汽福田汽车股份有限公司团委")
    BylcName = driver.find_element_by_id("BylcName")
    BylcName.send_keys("总部团委")
    Username = driver.find_element_by_id("Username")
    Username.send_keys(i)
    driver.find_element_by_class_name("btn").click()
    time.sleep(2)
    driver.find_element_by_class_name("layui-layer-btn0").click()
    time.sleep(2)
    driver.find_element_by_id("team").click()
    driver.switch_to.frame("layui-layer-iframe1")
    time.sleep(2)
    driver.find_element_by_id("word").click()
    time.sleep(2)
    word = driver.find_element_by_id("word")
    time.sleep(2)
    word.send_keys("北京汽车集团有限公司团委")
    time.sleep(2)
    driver.find_element_by_id("btn-search").click()
    time.sleep(2)
    driver.find_element_by_class_name("team").click()
    time.sleep(2)
    driver.find_element_by_class_name("btn").click()
    time.sleep(2)
    driver.find_element_by_class_name("layui-layer-btn0").click()
    print(i)
    time.sleep(random.randint(10, 200))
