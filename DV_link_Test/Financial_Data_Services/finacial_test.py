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
    def send_management(self):
        self.openpage.fist_iframe(1, '//*[@class="panel panel-htop"]/div/div/iframe')
        self.openpage.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                     '//*[@class="x-panel-body x-panel-body-noheader x-panel-body-noborder"]/iframe')
        self.task_name_main()
        self.openpage.all_check_button()
        self.pindu_status()
        ls = self.check_result()
        for x in ls:
            if x.text == "创建任务":
                x.click()
                self.tasek_name()
    def start_test(self):
        self.openpage.open_page()
        self.openpage.first_supervise(4, 3, 4)
        self.send_management()




    def main(self):
        self.start_test()


if __name__ == "__main__":
    test = Finacial_Data()
    test.main()
