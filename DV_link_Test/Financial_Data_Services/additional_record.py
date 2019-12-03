'''
!/usr/bin/python3
coding = utf-8
@Author: Qiu
@Time: 2019-10-30
'''
from selenium import webdriver
import unittest
import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from DV_link_Test.main import *


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # setUpClass()方法是所有用例执行前运行该方法

        driver = webdriver.Chrome()

        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('http://192.168.0.98:8080/dvlink/')
        cls.driver = driver
        driver.find_element_by_id('username').send_keys('00000')
        driver.find_element_by_id('password').send_keys("demo123.com")
        driver.find_element_by_class_name('blue_button').click()

    @classmethod
    def tearDownClass(cls):  # tearDownClass()方法是所有用例执行结束后运行该方法，关闭浏览器
        pass

    def setUp(self):  # setUp()方法是每个用例执行前运行该方法

        driver = self.driver  # 执行完一个用例后回到首页
        time.sleep(5)
        # driver.refresh()

    def tearDown(self):  # tearDown()方法是每个用例执行后运行该方法
        pass

    # 这四个方法都是unittest内部的方法

    def test00(self):  # 下面的是具体的用例，就是定位和操作之类的---第一个测试用例

        '''创建用例，执行'''

        driver = self.driver
        move = self.driver.find_element_by_xpath('//*[@id="menu_top_ul"]/li[4]/h2/a')
        self.driver.find_element_by_xpath('//*[@id="menu_top_ul"]/li[4]/h2/a')
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.find_element_by_xpath('//*[@id="menu_top_ul"]/li[4]/h2/a')
        driver.find_element_by_xpath('//*[@id="menu_top_ul"]/li[4]/div/div[3]/div/a[3]/div[2]/h3').click()  # 进入补录管理
        driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="mainTab_businessServices_06"]/div/iframe'))
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ext-gen24"]/em/span/span').click()  # 补录模板
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="ext-gen31"]/iframe'))
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='ext-gen124']//table//button").click()  # 创建任务
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="x-menu-item-text"]').click()
        self.driver.find_element_by_id('ext-comp-1081').send_keys('python')
        self.driver.find_element_by_id('ext-gen213').click()  # 选择启动方式
        self.driver.find_element_by_class_name('x-combo-list-item').click()
        self.driver.find_element_by_xpath('//*[@id="ext-comp-1082"]').send_keys('2019-11-08')
        self.driver.find_element_by_xpath('//*[@id="ext-gen227"]').click()  # 执行机构的选择
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="ext-gen270"]/li[2]/div/img[1]').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="ext-gen275"]/li[1]/div/img[1]').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="ext-gen275"]/li[1]/div/a/span').click()
        # time.sleep(2)
        self.driver.find_element_by_id('rf_data_date_bl').send_keys('2019-10-01')
        # self.driver.find_element_by_name('rf_data_date').send_keys('2019-10-23')
        self.driver.find_element_by_id('ext-comp-1087').send_keys('上个月数据的统计')
        self.driver.find_element_by_id('ext-comp-1084').send_keys('10')
        self.driver.find_element_by_xpath('//*[@id="ext-gen244"]').click()
        self.driver.find_element_by_xpath('//*[@id="ext-gen266"]/div').click()
        self.driver.find_element_by_id('ext-gen184').click()
        self.driver.find_element_by_class_name('c-message--close').click()
        self.driver.find_element_by_xpath('//*[@id="ext-gen114"]/div[1]/table/tbody/tr/td[2]/div/span').click()  # 选择任务
        time.sleep(2)
        self.driver.find_element_by_id('ext-gen78').click()  # 点击增加模板
        self.driver.find_element_by_xpath('//*[@id="ext-gen327"]/li/div/img[1]').click()  # 下拉按钮
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ext-gen337"]/li[1]/div/input').click()  # 选择模板
        self.driver.find_element_by_xpath('//*[@id="ext-gen321"]').click()  # 保存
        self.driver.find_element_by_class_name('c-message--close').click()
        self.driver.find_element_by_xpath('//*[@id="ext-gen114"]/div[1]/table/tbody/tr/td[2]/div/span').click()

        self.driver.find_element_by_xpath('//*[@id="ext-gen137"]').click()  # 启动
        # self.driver.find_element_by_xpath('//*[@id="ext-gen412"]').click()
        self.driver.find_element_by_xpath('//*[@id="startDataDate"]').send_keys('2019-11-11')  # 启动时间
        self.driver.find_element_by_id('ext-gen409').click()
        self.driver.find_element_by_css_selector('.c-message--close').click()  # 启动完成后
        self.driver.find_element_by_id('search_task_name').send_keys('系统增量补录')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="frequency_code_s"]').click()  # 选择过滤条件，频度随机筛选
        time.sleep(5)
        lists = self.driver.find_elements_by_xpath('/html/body/div[25]/div/div')
        num = random.randint(1, len(lists))
        self.driver.find_element_by_xpath('/html/body/div[25]/div/div[%s]' % str(num)).click()
        self.driver.find_element_by_xpath('//*[@id="ext-gen44"]').click()

    def test01(self):
        driver1 = self.driver
        move = self.driver.find_element_by_xpath('//*[@id="menu_top_ul"]/li[4]/h2/a')
        self.driver.find_element_by_xpath('//*[@id="menu_top_ul"]/li[4]/h2/a')
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.find_element_by_xpath('//*[@id="menu_top_ul"]/li[4]/h2/a')
        driver1.find_element_by_xpath('//*[@id="menu_top_ul"]/li[4]/div/div[3]/div/a[3]/div[2]/h3').click()  # 进入补录管理
        driver1.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="mainTab_businessServices_06"]/div/iframe'))
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ext-gen26"]/em/span/span').click()  # 补录任务
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="ext-gen31"]/iframe'))
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='ext-gen125']//table//button").click()  # 创建任务
        time.sleep(2)


if __name__ == "__main__":
    test011 = unittest.main
    test011.start
