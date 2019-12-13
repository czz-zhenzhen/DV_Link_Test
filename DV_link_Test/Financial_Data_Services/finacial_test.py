from DV_link_Test.main import *
import random


class Finacial_Data:
    def __init__(self):
        self.openpage = TestSystem()

    def pindu_status(self):
        ls = self.openpage.driver.find_elements_by_xpath('//div[@class="x-column-inner"]/div')
        for y in ls:
            if y.text == "频度:":
                y.click()
                lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                for x in lis:
                    if x.text == "日":
                        x.click()
    def creste_task_datail(self):
        ls = self.openpage.driver.find_elements_by_xpath('//*[@class="x-window-body x-border-layout-ct"]//div')
        return ls

    def create_task(self):
        ls = self.check_result()
        for x in ls:
            if x.text == "创建任务":
                x.click()
                self.tasek_name()
    def create_pindu(self):
        ls = self.creste_task_datail()
        for x in ls:
            print(x.text)
            if x.text == "频度*:":
                x.click()
                lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                for x in lis:
                    if x.text == "日":
                        x.click()
    def create_execute(self):
        ls = self.creste_task_datail()
        for x in ls:
            print(x.text)
            if x.text == "自动执行*:":
                x.click()
                lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                for x in lis:
                    if x.text == "是":
                        x.click()
    def create_main_report(self):
        ls = self.creste_task_datail()
        for x in ls:
            if x.text == "报表主题*:":
                x.click()
                time.sleep(1)
                self.openpage.onlink_img()
                time.sleep(1)
                city_name = self.openpage.driver.find_elements_by_xpath(
                    '//div[@class="x-menu x-menu-floating x-layer"]/ul/li/div/div/div/ul/li/ul/li[2]/ul//li/div/a/span')
                list_name = []
                for a in city_name:
                    names = a.text
                    list_name.append(names)
                lens = len(list_name)
                length_num = random.randint(1, lens)
                print(lens)
                time.sleep(2)
                on_link = list_name[length_num]
                for c in city_name:
                    if c.text == on_link:
                        c.click()
    def need_date(self):
        self.openpage.driver.find_element_by_name('finish_offset_days').send_keys('2')
    def start_date(self):
        self.openpage.driver.find_element_by_name('first_startup_time').send_keys(self.openpage.get_time())
    def excetue_message(self,count, RESOURCE_ID_name1):
        ls = self.creste_task_datail()
        for x in ls:
            if x.text =="执行机构*:":
                x.click()
                self.openpage.get_city_name(count, RESOURCE_ID_name1)
    def isor_and_false(self):
        ls = self.creste_task_datail()
        for x in ls:
            if x.text =="是否临时任务*:":
                x.click()
                ls01 = self.openpage.driver.find_elements_by_xpath('//*[@class="x-combo-list-inner"]/div')
                for y in ls01:
                    if y.text =="否":
                        y.click()
    def data_date(self):
        self.openpage.driver.find_element_by_name('rf_data_date').send_keys(self.openpage.get_time())


    def chioce_flow(self):
        ls = self.creste_task_datail()
        for x in ls:
            if x.text == "选择流程*:":
                x.click()
                ls01 = self.openpage.driver.find_elements_by_xpath('//*[@class="x-layer x-combo-list "]/div')
                for y in ls01:
                    if y.text =="报表填报默认流程":
                        y.click()

    def task_description(self):
        self.openpage.driver.find_element_by_name('task_desc').send_keys("用于测试项目")

    def data_source(self):
        # 数据来源
        ls = self.creste_task_datail()
        for x in ls:
            if x.text == "数据来源*:":
                x.click()
                time.sleep(1)
                x.click()

    def check_result_button(self):
        self.openpage.driver.find_element_by_xpath('//*[@class="x-panel-body x-panel-body-noheader x-column-layout-ct"]'
                                                   '//div[@class="x-column-inner"]//button').click()




    def check_result(self):
        # 查询结果
        ls = self.openpage.driver.find_elements_by_xpath(
            '//*[@class=" x-panel x-panel-noborder x-border-panel"]'
            '//div[@class="x-toolbar x-small-editor x-toolbar-layout-ct"]//button')
        return ls
    def tasek_name(self):
        self.openpage.driver.find_element_by_xpath('//*[@class="x-panel-body x-panel-body-'
                                                   'noheader x-column-layout-ct"]//input').send_keys('测试案列')
    def task_name_main(self):
        self.openpage.driver.find_element_by_name('task_name').send_keys('123')

    def report_code_name(self):
        self.openpage.driver.find_element_by_name('searchKeyField').send_keys('123')


    def send_management(self):
        count=1
        RESOURCE_ID_name1="ces"
        self.openpage.fist_iframe(1, '//*[@class="panel panel-htop"]/div/div/iframe')
        self.openpage.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                     '//*[@class="x-panel-body x-panel-body-noheader x-panel-body-noborder"]/iframe')
        self.task_name_main()
        self.openpage.all_check_button()
        self.pindu_status()
        # 创建任务
        self.create_task()
        # 创建频度
        # self.create_pindu()
        #创建执行
        # self.create_execute()
        # 创建主题
        # self.create_main_report()
        # 启动时间
        # self.start_date()
        # # 完成期限
        # self.need_date()
        # self.excetue_message(count, RESOURCE_ID_name1)
        # self.isor_and_false()
        # # 数据日期
        # self.data_date()
        # # 选择流程
        # self.chioce_flow()
        # 项目描述
        self.task_description()
        self.data_source()
        self.report_code_name()
        self.check_result_button()
        count+=1
    def start_test(self):
        self.openpage.open_page()
        self.openpage.first_supervise(4, 3, 4)
        self.send_management()




    def main(self):
        self.start_test()


if __name__ == "__main__":
    test = Finacial_Data()
    test.main()
