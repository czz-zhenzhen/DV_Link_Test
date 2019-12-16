from DV_link_Test.main import *
import random


class Finacial_Data:
    def __init__(self):
        self.openpage = TestSystem()

    def pindu_status(self,count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.openpage.driver.find_elements_by_xpath('//div[@class="x-column-inner"]/div')
            for y in ls:
                if y.text == "频度:":
                    y.click()
                    lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                    for x in lis:
                        if x.text == "日":
                            x.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入频度', '操作输出',0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入频度:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入频度', '操作输出', 1, S_txt)

    def creste_task_datail(self,count, RESOURCE_ID_name1, report_name):
        # 创建任务详细
        try:
            ls = self.openpage.driver.find_elements_by_xpath('//*[@class="x-window-body x-border-layout-ct"]//div')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入创建任务详细', '操作输出',0, "功能正常")
            return ls
        except Exception as e:
            S_txt = '{}__进入创建任务详细:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入创建任务详细', '操作输出', 1, S_txt)

    def create_task(self,count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.check_result(count, RESOURCE_ID_name1,report_name)
            for x in ls:
                print(x.text)
                if x.text == "创建任务":
                    x.click()
                    self.tasek_name(count, RESOURCE_ID_name1, report_name)
                    self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '创建任务', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入创建任务:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '创建任务', '操作输出', 1, S_txt)

    def create_pindu(self,count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
            for x in ls:
                print(x.text)
                if x.text == "频度*:":
                    x.click()
                    lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                    for x in lis:
                        if x.text == "日":
                            x.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作频度', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入频度:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作频度', '操作输出', 1, S_txt)

    def create_execute(self,count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
            for x in ls:
                print(x.text)
                if x.text == "自动执行*:":
                    x.click()
                    lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                    for x in lis:
                        if x.text == "是":
                            x.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '自动执行', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入自动执行:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '自动执行', '操作输出', 1, S_txt)

    def create_main_report(self,count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
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
                    time.sleep(3)
                    on_link = list_name[length_num]
                    for c in city_name:
                        if c.text == on_link:
                            c.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '报表主题', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入报表主题:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '报表主题', '操作输出', 1, S_txt)

    def need_date(self,count, RESOURCE_ID_name1,report_name):
        # 操作期限
        try:
            self.openpage.driver.find_element_by_name('finish_offset_days').send_keys('2')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作期限', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入操作期限:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作期限', '操作输出', 1, S_txt)

    def start_date(self,count, RESOURCE_ID_name1, report_name):
        # 开始时间
        try:
            self.openpage.driver.find_element_by_name('first_startup_time').send_keys(self.openpage.get_time())
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '开始时间', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入开始时间:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '开始时间', '操作输出', 1, S_txt)

    def excetue_message(self, count, RESOURCE_ID_name1,report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1,report_name)
            for x in ls:
                if x.text == "执行机构*:":
                    x.click()
                    self.openpage.get_city_name(count, RESOURCE_ID_name1)
                    self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '执行机构', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入执行机构:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '执行机构', '操作输出', 1, S_txt)

    def isor_and_false(self,count, RESOURCE_ID_name1,report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1,report_name)
            for x in ls:
                if x.text == "是否临时任务*:":
                    x.click()
                    ls01 = self.openpage.driver.find_elements_by_xpath('//*[@class="x-combo-list-inner"]/div')
                    for y in ls01:
                        if y.text == "否":
                            y.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '是否临时任务', '操作输出', 0,
                                                            "功能正常")

        except Exception as e:
            S_txt = '{}__进入是否临时任务:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '是否临时任务', '操作输出', 1, S_txt)

    def data_date(self,count, RESOURCE_ID_name1,report_name):
        # 数据日期
        try:
            self.openpage.driver.find_element_by_name('rf_data_date').send_keys(self.openpage.get_time())
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '数据日期', '操作输出', 0,
                                            "功能正常")
        except Exception as e:
            S_txt = '{}__进入数据日期:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '数据日期', '操作输出', 1, S_txt)

    def chioce_flow(self,count, RESOURCE_ID_name1,report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1,report_name)
            for x in ls:
                if x.text == "选择流程*:":
                    x.click()
                    ls01 = self.openpage.driver.find_elements_by_xpath('//*[@class="x-layer x-combo-list "]/div')
                    for y in ls01:
                        if y.text == "报表填报默认流程":
                            y.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '选择流程*', '操作输出', 0,
                                                            "功能正常")

        except Exception as e:
            S_txt = '{}__进入选择流程*:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '选择流程*', '操作输出', 1, S_txt)

    def task_description(self,count, RESOURCE_ID_name1,report_name):
        # 描述
        try:
            self.openpage.driver.find_element_by_name('task_desc').send_keys("用于测试项目")
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作描述', '操作输出', 0,
                                            "功能正常")

        except Exception as e:
            S_txt = '{}__进入描述:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作描述', '操作输出', 1, S_txt)

    def data_source(self,count, RESOURCE_ID_name1,report_name):
        # 数据来源
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1,report_name)
            for x in ls:
                if x.text == "数据来源*:":
                    x.click()
                    time.sleep(1)
                    x.click()
                    self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作数据来源', '操作输出', 0,
                                                    "功能正常")
        except Exception as e:
            S_txt = '{}__进入数据来源:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作数据来源', '操作输出', 1, S_txt)

    def check_result_button(self,count, RESOURCE_ID_name1,report_name):
        # 查询结果按钮
        try:
            self.openpage.driver.find_element_by_xpath('//*[@class="x-panel-body x-panel-body-noheader x-column-layout-ct"]'
                                                       '//div[@class="x-column-inner"]//button').click()
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '查询结果按钮', '操作输出', 0,
                                            "功能正常")
        except Exception as e:
            S_txt = '{}__进入查询结果:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '查询结果按钮', '操作输出', 1, S_txt)

    def check_result(self,count, RESOURCE_ID_name1,report_name):
        try:
            # 查询结果
            ls = self.openpage.driver.find_elements_by_xpath(
                '//*[@class=" x-panel x-panel-noborder x-border-panel"]'
                '//div[@class="x-toolbar x-small-editor x-toolbar-layout-ct"]//button')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '查询结果', '操作输出', 0,"功能正常")
            return ls

        except Exception as e:
            S_txt = '{}__进入查询结果:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '查询结果', '操作输出', 1, S_txt)

    def tasek_name(self,count, RESOURCE_ID_name1,report_name):
        # 任务名称
        try:
            self.openpage.driver.find_element_by_xpath('//*[@class="x-panel-body x-panel-body-'
                                                       'noheader x-column-layout-ct"]//input').send_keys('测试案列')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '任务名称', '操作输出', 0, "功能正常")

        except Exception as e:
            S_txt = '{}__进入任务名称:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '任务名称', '操作输出', 1, S_txt)

    def task_name_main(self,count, RESOURCE_ID_name1, report_name):
        # 主任务名称
        try:
            self.openpage.driver.find_element_by_name('task_name').send_keys('123')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '主任务名称', '操作输出', 0,"功能正常")
        except Exception as e:
            S_txt = '{}__进入主任务名称:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '主任务名称', '操作输出', 1, S_txt)

    def report_code_name(self,count, RESOURCE_ID_name1, report_name):
        # 填报代码
        try:
            self.openpage.driver.find_element_by_name('searchKeyField').send_keys('123')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '填报代码', '操作输出', 0,"功能正常")
        except Exception as e:
            S_txt = '{}__进入填报代码:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '填报代码', '操作输出', 1, S_txt)

    def save_button(self,count, RESOURCE_ID_name1, report_name):
        # 保存按钮
        try:
            ls = self.openpage.driver.find_elements_by_xpath('//*[@class="x-window-footer x-panel-btns"]//button')
            for x in ls:
                if x.text == "保存":
                    x.click()
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '保存按钮', '操作输出', 0,"功能正常")
            time.sleep(3)
        except Exception as e:
            S_txt = '{}__进入保存按钮:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '保存按钮', '操作输出', 1, S_txt)
            time.sleep(3)

    def cancel_button(self,count, RESOURCE_ID_name1, report_name):
        # 取消按钮
        try:
            ls = self.openpage.driver.find_elements_by_xpath('//*[@class="x-window-footer x-panel-btns"]//button')
            for x in ls:
                if x.text == "取消":
                    x.click()
                    self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '取消按钮', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入取消按钮:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '取消按钮', '操作输出', 1, S_txt)

    def send_management(self):
        RESOURCE_main = 'businessServices'
        report_name1 = "填报管理"
        count1= 1
        try:
            count = 1
            RESOURCE_ID_name1 = "businessServices_04"
            RESOURCE_ID = "TB_0401"
            report_name ="填报模板"

            try:
                self.openpage.fist_iframe(1, '//*[@class="panel panel-htop"]/div/div/iframe')
                self.openpage.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                             '//*[@class="x-panel-body x-panel-body-noheader x-panel-body-noborder"]/iframe')
            except Exception as e:
                S_txt = '{}__进入iframe层:'.format(report_name) + str(e)
                self.openpage.write_error_excel(S_txt)
                self.openpage.write_error_mysql(count, RESOURCE_ID, report_name, '进入iframe层', '操作输出', 1, S_txt)
            self.task_name_main(count, RESOURCE_ID_name1, report_name)
            self.openpage.all_check_button(count, RESOURCE_ID_name1, report_name)
            self.pindu_status(count, RESOURCE_ID_name1, report_name)
            # 创建任务
            self.create_task(count, RESOURCE_ID_name1, report_name)
            # 创建频度
            self.create_pindu(count, RESOURCE_ID_name1, report_name)
            # 创建执行
            self.create_execute(count, RESOURCE_ID_name1, report_name)
            # 创建主题
            self.create_main_report(count, RESOURCE_ID_name1, report_name)
            # 启动时间
            self.start_date(count, RESOURCE_ID_name1, report_name)
            # 完成期限
            self.need_date(count, RESOURCE_ID_name1,report_name)
            self.excetue_message(count, RESOURCE_ID_name1,report_name)
            self.isor_and_false(count, RESOURCE_ID_name1,report_name)
            # 数据日期
            self.data_date(count, RESOURCE_ID_name1,report_name)
            # 选择流程
            self.chioce_flow(count, RESOURCE_ID_name1,report_name)
            # 项目描述
            self.task_description(count, RESOURCE_ID_name1,report_name)
            self.data_source(count, RESOURCE_ID_name1,report_name)
            self.report_code_name(count, RESOURCE_ID_name1, report_name)
            self.check_result_button(count, RESOURCE_ID_name1,report_name)
            # self.cancel_button(count, RESOURCE_ID_name1, report_name)
            self.save_button(count, RESOURCE_ID_name1, report_name)
            time.sleep(2)
            self.openpage.driver.switch_to.default_content()
            self.openpage.write_error_mysql(count1, RESOURCE_main, report_name1, '进入iframe层', '操作输出', 0, "功能正常")
            count += 1
        except Exception as e:
            S_txt = '{}__进入iframe层:'.format(report_name1) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count1, RESOURCE_main, report_name1, '进入iframe层', '操作输出', 1, S_txt)
        count1 +=1
    def send_message_task(self,count1, RESOURCE_main, report_name1):
        count = 1
        RESOURCE_ID_name1 = "ces"
        self.openpage.fist_iframe(2, '//*[@class="panel panel-htop"]/div/div/iframe')
        self.openpage.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                     '//*[@class="x-tab-panel-body x-tab-panel-body-top"]/div[2]//div/iframe')
        self.task_name_main(count1, RESOURCE_main, report_name1)
        self.pindu_status(count1, RESOURCE_main, report_name1)
        self.openpage.all_check_button(count1, RESOURCE_main, report_name1)
        self.create_task(count1, RESOURCE_main, report_name1)
        self.need_date(count1, RESOURCE_main, report_name1)
        self.isor_and_false(count1, RESOURCE_main, report_name1)
        self.create_main_report(count1, RESOURCE_main, report_name1)
        self.save_button()
        # self.cancel_button()

    def four_report_messages(self):
        self.send_management()
        # self.send_message_task()

    def start_test(self):
        self.openpage.open_page()
        self.openpage.first_supervise(4, 3, 4)
        self.four_report_messages()

    def main(self):
        self.start_test()


if __name__ == "__main__":
    test = Finacial_Data()
    test.main()
