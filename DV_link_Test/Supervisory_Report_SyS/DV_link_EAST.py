from DV_link_Test.main import *
import random


class EAST_dv_link:
    def __init__(self):
        self.open = TestSystem()

    def first_supervise(self, number, number2):
        """
        报表填报功能测试
        传递元素节点，和节点元素序列号
        :param element_text: /html/body/div[1]/div/div[2]/ul/li[1]/div/div[2]/div/a[1]/div[2]/h3
                            /html/body/div[1]/div/div[2]/ul/li[1]/div/div[2]/div/a[?]/div[2]/h3.format(2)
        :param number:
        :return:
        """
        self.open.open_page()
        self.open.chioce_manage(number)
        time.sleep(2)
        ele_text = "/html/body/div[1]/div/div[2]/ul/li[1]/div/div[2]/div/a[" + str(number2) + "]/div[2]/h3"
        self.open.driver.find_element_by_xpath(ele_text).click()

        # 进入iframe层

    def fist_iframe(self, num, elem):
        # 第一个功能进入iframe层
        time.sleep(2)
        elems = str(elem)
        self.open.driver.switch_to.frame(self.open.driver.find_element_by_xpath(elems))
        self.open.driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[1]/ul/li[%s]/a[2]/em/span/span' % str(num)).click()
        self.open.driver.switch_to_default_content()

    def sencond_iframe(self, elem1, elem2):
        elems1 = str(elem1)
        elems2 = str(elem2)
        self.open.driver.switch_to_default_content()
        time.sleep(1)
        self.open.driver.switch_to.frame(self.open.driver.find_element_by_xpath(elems1))
        time.sleep(2)
        self.open.driver.switch_to.frame(self.open.driver.find_element_by_xpath(elems2))
        time.sleep(1)

    def text_status(self, elem1, elem2):
        # 点击显示列表
        elems1 = str(elem1)
        elems2 = str(elem2)
        self.open.driver.find_element_by_xpath(elems1).click()
        time.sleep(1)
        lists = self.open.driver.find_elements_by_xpath(elems2)
        num = random.randint(1, len(lists))
        self.open.driver.find_element_by_xpath(elems2 + '[%s]' % str(num)).click()

    def messsage_arg(self, elem1, elem2, elem3):
        """
         # 填报机构
        :param elem1: 获取点击元素
        :param elem2: 加号图片元素
        :param elem3: 省市元素
        :return:
        """
        elems1 = str(elem1)
        elems2 = str(elem2)
        elems3 = str(elem3)
        self.open.driver.find_element_by_xpath(elems1).click()
        time.sleep(2)
        self.open.driver.find_element_by_xpath(elems2).click()  # 点击图片
        time.sleep(3)
        list01 = self.open.driver.find_elements_by_xpath(elems3)
        num01 = random.randint(1, len(list01))
        time.sleep(2)
        self.open.driver.find_element_by_xpath(
            elems3+'[%s]/div/a/span' % str(num01)).click()

    def on_link(self, elem1):
        slems = str(elem1)
        self.open.driver.find_element_by_xpath(slems).click()

    def first_meassage(self):
        # 任务状态
        self.first_supervise(1, 2)
        self.fist_iframe(1, '//*[@id="mainTab_CBRC2"]/div/iframe')  # 第一个报表任务
        self.sencond_iframe('//*[@id="mainTab_CBRC2"]/div/iframe', '/html/body/div[1]/div[2]/div/div[1]/div/div/iframe')
        time.sleep(2)
        self.open.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div[1]/div/div/div/div[1]/input').send_keys('123')
        # 点击显示列表
        self.sencond_iframe('//*[@id="mainTab_CBRC2"]/div/iframe', '//*[@id="ext-gen30"]/iframe')
        self.text_status('/html/body/div[1]/div[2]/div/div/div/form/div/div[3]/div/div/div/div[1]/div/input[2]',
                         '/html/body/div[26]/div/div')
        # 填报代码
        time.sleep(1)
        self.open.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div[4]/div/div/div/div[1]/input').send_keys('qwe')
        # 填报机构
        self.messsage_arg('/html/body/div[1]/div[2]/div/div/div/form/div/div[6]/div/div/div/div[1]/div/input[2]',
                          '/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                          '/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        self.open.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div[7]/div/div/div/div[1]/div/input').send_keys(
            self.open.get_time())
        self.open.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/table/tbody/tr[2]/td[2]/em/button').click()

    def second_message(self):
        self.first_supervise(1, 2)
        self.fist_iframe(2, '//*[@id="mainTab_CBRC2"]/div/iframe')
        self.sencond_iframe('//*[@id="mainTab_CBRC2"]/div/iframe', '//*[@id="ext-gen33"]/iframe')
        time.sleep(2)
        self.open.driver.find_element_by_xpath('//*[@id="search"]').send_keys('存折')
        time.sleep(1)
        self.on_link(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/table/'
            'tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button')
        self.messsage_arg('//*[@id="bankCombo"]', '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                          '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        self.on_link('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/'
                     'div/form/div/div/div/div/table[1]/tbody/tr[2]/td[2]/em/button')
        time.sleep(3)

    def message_send(self):
        # 报文发送
        self.first_supervise(1, 2)
        self.fist_iframe(3, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')  # 第3个报表任务
        self.sencond_iframe('//*[@id="mainTab_CBRC2"]/div/iframe', '//*[@id="ext-gen33"]/iframe')
        time.sleep(3)
        self.open.driver.find_element_by_xpath('//*[@id="search_task_name"]').send_keys('qwqe')
        # # 点击显示列表
        self.sencond_iframe('//*[@id="mainTab_CBRC2"]/div/iframe', '//*[@id="ext-gen30"]/iframe')
        self.text_status('//*[@id="taskStatus"]', '/html/body/div[27]/div/div')
        # 填报代码
        time.sleep(1)
        self.open.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div[4]/div/div/div/div[1]/input').send_keys('0001')
        # 填报机构
        self.messsage_arg('//html/body/div[1]/div[2]/div/div/div/form/div/div[6]/div/div/div/div[1]/div/input[2]',
                          '/html/body/div[27]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                          '/html/body/div[27]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        self.open.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div[7]/div/div/div/div[1]/div/input').send_keys(
            self.open.get_time())
        self.on_link('/html/body/div[1]/div[2]/div/div/div/form/div/table/tbody/tr[2]/td[2]/em/button')
    def message_down(self):
        self.open.driver.switch_to_default_content()
        self.fist_iframe(4,'//*[@id="mainTab_CBRC2"]/div/iframe')
        self.sencond_iframe('//*[@id="mainTab_CBRC2"]/div/iframe','//*[@id="ext-gen33"]/iframe')
        self.messsage_arg('/html/body/div[1]/div/div/div[1]/div[2]/form/div/div[1]/div/div/div/div[1]/div/input[2]','/html/body/div[10]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]','/html/body/div[10]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        self.on_link('//*[@id="ext-gen78"]')
    def main(self):
        self.first_meassage()
        # self.second_message()
        # self.message_send()
        # self.message_down()

if __name__ == "__main__":
    test = EAST_dv_link()
    test.main()
