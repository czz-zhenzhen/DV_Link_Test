from DV_link_Test.main import *
import random


class Finacial_Data:
    def __init__(self):
        self.openpage = TestSystem()

    def pindu_status(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.openpage.driver.find_elements_by_xpath('//div[@class="x-column-inner"]/div')
            for y in ls:
                if y.text == "频度:":
                    y.click()
                    lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                    for x in lis:
                        if x.text == "日":
                            x.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入频度', '操作输出', 0,
                                                            "功能正常")
        except Exception as e:
            S_txt = '{}__进入频度:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入频度', '操作输出', 1, S_txt)

    def creste_task_datail(self, count, RESOURCE_ID_name1, report_name):
        # 创建任务详细
        try:
            ls = self.openpage.driver.find_elements_by_xpath('//*[@class="x-window-body x-border-layout-ct"]//div')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入创建任务详细', '操作输出', 0, "功能正常")
            return ls
        except Exception as e:
            S_txt = '{}__进入创建任务详细:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入创建任务详细', '操作输出', 1, S_txt)

    def create_task(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.check_result(count, RESOURCE_ID_name1, report_name)
            for x in ls:
                # print(x.text)
                if x.text == "创建任务":
                    x.click()
                    self.tasek_name(count, RESOURCE_ID_name1, report_name)
                    self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '创建任务', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入创建任务:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '创建任务', '操作输出', 1, S_txt)

    def create_pindu(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
            for x in ls:
                # print(x.text)
                if x.text == "频度*:":
                    x.click()
                    lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                    for x in lis:
                        if x.text == "日":
                            x.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作频度', '操作输出', 0,
                                                            "功能正常")
        except Exception as e:
            S_txt = '{}__进入频度:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作频度', '操作输出', 1, S_txt)

    def create_execute(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
            for x in ls:
                # print(x.text)
                if x.text == "自动执行*:":
                    x.click()
                    lis = self.openpage.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
                    for x in lis:
                        if x.text == "是":
                            x.click()
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '自动执行', '操作输出', 0,
                                                            "功能正常")
        except Exception as e:
            S_txt = '{}__进入自动执行:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '自动执行', '操作输出', 1, S_txt)

    def create_main_report(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
            for x in ls:
                if x.text == "报表主题*:":
                    x.click()
                    time.sleep(2)
                    self.openpage.onlink_img()
                    time.sleep(2)
                    city_name = self.openpage.driver.find_elements_by_xpath(
                        '//div[@class="x-menu x-menu-floating x-layer"]/ul/li/div/div/div/ul/li/ul/li[2]/ul//li/div/a/span')
                    list_name = []
                    time.sleep(2)
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
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '报表主题', '操作输出', 0,
                                                            "功能正常")
        except Exception as e:
            S_txt = '{}__进入报表主题:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '报表主题', '操作输出', 1, S_txt)

    def is_or_yes(self, count, RESOURCE_ID_name1, report_name):
        ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
        for x in ls:
            # print(x.text)
            if x.text == "是否结转*:":
                x.click()
                x.click()

    def need_date(self, count, RESOURCE_ID_name1, report_name):
        # 操作期限
        try:
            self.openpage.driver.find_element_by_name('finish_offset_days').send_keys('2')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作期限', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入操作期限:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作期限', '操作输出', 1, S_txt)

    def start_date(self, count, RESOURCE_ID_name1, report_name):
        # 开始时间
        try:
            self.openpage.driver.find_element_by_name('first_startup_time').send_keys(self.openpage.get_time())
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '开始时间', '操作输出', 0, "功能正常")
        except Exception as e:

            try:
                self.openpage.driver.find_element_by_name('startup_time').send_keys(self.openpage.get_time())
                self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '开始时间', '操作输出', 0, "功能正常")
            except Exception as e1:
                S_txt = '{}__进入开始时间:'.format(report_name) + str(e1)
                self.openpage.write_error_excel(S_txt)
                self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '开始时间', '操作输出', 1, S_txt)

    def excetue_message(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
            for x in ls:
                if x.text == "执行机构*:":
                    x.click()
                    self.openpage.get_city_name(count, RESOURCE_ID_name1)
                    self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '执行机构', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入执行机构:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '执行机构', '操作输出', 1, S_txt)

    def isor_and_false(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
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

    def data_date(self, count, RESOURCE_ID_name1, report_name):
        # 数据日期
        try:
            self.openpage.driver.find_element_by_name('rf_data_date').send_keys(self.openpage.get_time())
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '数据日期', '操作输出', 0,
                                            "功能正常")
        except Exception as e:
            try:
                self.openpage.driver.find_element_by_name('data_date').send_keys(self.openpage.get_time())
                self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '数据日期', '操作输出', 0, "功能正常")
            except Exception as e:
                S_txt = '{}__进入数据日期:'.format(report_name) + str(e)
                self.openpage.write_error_excel(S_txt)
                self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '数据日期', '操作输出', 1, S_txt)

    def chioce_flow(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
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

    def task_description(self, count, RESOURCE_ID_name1, report_name):
        # 描述
        try:
            self.openpage.driver.find_element_by_name('task_desc').send_keys("用于测试项目")
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作描述', '操作输出', 0,
                                            "功能正常")

        except Exception as e:
            S_txt = '{}__进入描述:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '操作描述', '操作输出', 1, S_txt)

    def data_source(self, count, RESOURCE_ID_name1, report_name):
        # 数据来源
        try:
            ls = self.creste_task_datail(count, RESOURCE_ID_name1, report_name)
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

    def check_result_button(self, count, RESOURCE_ID_name1, report_name):
        # 查询结果按钮
        try:
            self.openpage.driver.find_element_by_xpath(
                '//*[@class="x-panel-body x-panel-body-noheader x-column-layout-ct"]'
                '//div[@class="x-column-inner"]//button').click()
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '查询结果按钮', '操作输出', 0,
                                            "功能正常")
        except Exception as e:
            S_txt = '{}__进入查询结果:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '查询结果按钮', '操作输出', 1, S_txt)

    def check_result(self, count, RESOURCE_ID_name1, report_name):
        try:
            # 查询结果
            ls = self.openpage.driver.find_elements_by_xpath(
                '//*[@class=" x-panel x-panel-noborder x-border-panel"]'
                '//div[@class="x-toolbar x-small-editor x-toolbar-layout-ct"]//button')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '查询结果', '操作输出', 0, "功能正常")
            return ls

        except Exception as e:
            S_txt = '{}__进入查询结果:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '查询结果', '操作输出', 1, S_txt)

    def tasek_name(self, count, RESOURCE_ID_name1, report_name):
        # 任务名称
        try:
            self.openpage.driver.find_element_by_xpath('//*[@class="x-panel-body x-panel-body-'
                                                       'noheader x-column-layout-ct"]//input').send_keys('测试案列')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '任务名称', '操作输出', 0, "功能正常")

        except Exception as e:
            S_txt = '{}__进入任务名称:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '任务名称', '操作输出', 1, S_txt)

    def task_name_main(self, count, RESOURCE_ID_name1, report_name):
        # 主任务名称
        try:
            self.openpage.driver.find_element_by_name('task_name').send_keys('123')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '主任务名称', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入主任务名称:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '主任务名称', '操作输出', 1, S_txt)

    def report_code_name(self, count, RESOURCE_ID_name1, report_name):
        # 填报代码
        try:
            self.openpage.driver.find_element_by_name('searchKeyField').send_keys('123')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '填报代码', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入填报代码:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '填报代码', '操作输出', 1, S_txt)


    def creat_detail_list(self, count, RESOURCE_ID_name1, report_name):
        try:
            ls = self.openpage.driver.find_elements_by_xpath(
                '//*[@class=" x-panel x-grid-panel x-border-panel"]//div[@class="x-grid3-scroller"]/div/div')
            if len(ls) >= 0:
                for x in ls:
                    x.click()
                    ls0 = self.openpage.driver.find_elements_by_xpath(
                        '//*[@class="x-panel-body x-panel-body-noheader x-border-layout-ct"]//div[@class="x-grid3-body"]')
                    if len(ls0) >= 0:
                        for y in ls0:
                            print(y.text)
                            time.sleep(1)
                            y.click()
                    return
        except Exception as e:
            S_txt = '{}__进入取消按钮:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '取消按钮', '操作输出', 1, S_txt)

    def amend_task(self, count, RESOURCE_ID_name1, report_name):
        # 修改任务
        try:
            ls = self.openpage.driver.find_elements_by_xpath(
                '//*[@class=" x-panel x-grid-panel x-border-panel"]//div[@class="x-grid3-scroller"]/div/div')
            if len(ls) >= 0:
                for x in ls:
                    x.click()
                    ls = self.check_result(count, RESOURCE_ID_name1, report_name)
                    for i in ls:
                        if i.text == "修改任务":
                            i.click()
                            self.openpage.cancel_button(count, RESOURCE_ID_name1, report_name)
                            # self.save_button(count, RESOURCE_ID_name1, report_name)
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '取消按钮', '操作输出', 0,
                                                            "功能正常")
                    return
        except Exception as e:
            S_txt = '{}__进入修改任务:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '修改任务', '操作输出', 1, S_txt)



    def delete_task(self, count, RESOURCE_ID_name1, report_name):
        # 删除任务
        try:
            ls = self.openpage.driver.find_elements_by_xpath(
                '//*[@class=" x-panel x-grid-panel x-border-panel"]//div[@class="x-grid3-scroller"]/div/div')
            if len(ls) >= 0:
                for x in ls:
                    # print(x.text)
                    x.click()
                    ls = self.check_result(count, RESOURCE_ID_name1, report_name)
                    for i in ls:
                        if i.text == "删除任务":
                            i.click()
                            time.sleep(1)
                            self.openpage.delete_task_is_and_false(count, RESOURCE_ID_name1, report_name)
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '修改任务', '操作输出', 0,
                                                            "功能正常")
                    return
        except Exception as e:
            S_txt = '{}__进入修改任务:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '修改任务', '操作输出', 1, S_txt)

    def task_start_time(self, count, RESOURCE_ID_name1, report_name):
        try:
            self.openpage.driver.find_element_by_name('startDataDate').send_keys(self.openpage.get_time())
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '启动任务__数据时间', '操作输出', 0, "功能正常")

            ls = self.openpage.driver.find_elements_by_xpath(
                '//*[@class="x-panel-fbar x-small-editor x-toolbar-layout-ct"]//button')
            print(ls)
            for x in ls:
                print(x.text)
                s = x.text
                str1 = s.strip()
                print(str1)
                if str1 == "取消":
                    x.click()
                    self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '启动任务__数据时间', '操作输出', 0,
                                                    "功能正常")
        except Exception as e:
            S_txt = '{}__进入启动任务数据时间:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '启动任务__数据时间', '操作输出', 1, S_txt)

    def create_person(self, count, RESOURCE_ID_name1, report_name):
        # 创建人
        try:
            self.openpage.driver.find_element_by_name('username').send_keys('czz')
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '创建人', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入创建人:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '创建人', '操作输出', 1, S_txt)

    def task_start(self, count, RESOURCE_ID_name1, report_name):
        # 任务启动
        try:
            ls = self.openpage.driver.find_elements_by_xpath(
                '//*[@class=" x-panel x-grid-panel x-border-panel"]//div[@class="x-grid3-scroller"]/div/div')
            if len(ls) >= 0:
                for x in ls:
                    # print(x.text)
                    x.click()
                    ls = self.check_result(count, RESOURCE_ID_name1, report_name)
                    for i in ls:
                        if i.text == "任务启动":
                            i.click()
                            time.sleep(1)
                            self.task_start_time(count, RESOURCE_ID_name1, report_name)
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '启动任务', '操作输出', 0,
                                                            "功能正常")
                    return
        except Exception as e:
            S_txt = '{}__进入启动任务:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '启动任务', '操作输出', 1, S_txt)

    def Task_to_cancel(self, count, RESOURCE_ID_name1, report_name):
        # 任务撤销
        try:
            ls = self.openpage.driver.find_elements_by_xpath(
                '//*[@class=" x-panel x-grid-panel x-border-panel"]//div[@class="x-grid3-scroller"]/div/div')
            if len(ls) >= 0:
                for x in ls:
                    # print(x.text)
                    x.click()
                    ls = self.check_result(count, RESOURCE_ID_name1, report_name)
                    for i in ls:
                        if i.text == "任务撤销":
                            i.click()
                            time.sleep(1)
                            self.openpage.delete_task_is_and_false(count, RESOURCE_ID_name1, report_name)
                            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '任务撤销', '操作输出', 0,
                                                            "功能正常")
                    return
        except Exception as e:
            S_txt = '{}__进入任务撤销:'.format(report_name) + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '任务撤销', '操作输出', 1, S_txt)


if __name__ == "__main__":
    test = Finacial_Data()
    # test.main()
