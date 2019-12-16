from DV_link_Test.main import *
import datetime


class Custom_riosk:
    def __init__(self):
        self.page = TestSystem()

    def first_message(self, number1, number2):
        self.page.first_supervise(1, number1, number2)
        count = 1
        if number1 == 2:
            RESOURCE_ID = 'CBRC%d' % number1
            RESOURCE_ID_name1 = 'CBRC%d1' % number2
        elif number1 == 3:
            RESOURCE_ID = 'PBOC%d' % number1
            RESOURCE_ID_name1 = 'PBOC%d1' % number2
        else:
            RESOURCE_ID = 'SAFE%d' % number1
            RESOURCE_ID_name1 = 'SAFE%d2' % number2

        try:
            self.page.fist_iframe(1, '//*[@class="panel panel-htop"]/div/div/iframe')
            self.page.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                     '//*[@class="x-panel-body x-panel-body-noheader x-panel-body-noborder"]/iframe')
            count += 1
            self.page.write_error_mysql(count, RESOURCE_ID, '报表填表', '操作输入', '进入iframe层', 0, '功能正常')
        except Exception as e:
            S_txt = '进入iframe层:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '操作输入', '进入iframe层', 1, S_txt)
        try:
            self.page.task_name()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '输入框', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '输入框:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '输入框', '操作输出', 1, S_txt)
        time.sleep(1)

        try:
            # 报文代码
            self.page.driver.find_element_by_name('query_key').send_keys('22')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '报表代码', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表代码:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '报表代码', '操作输出', 1, S_txt)

        try:
            self.page.text_status()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '任务状态', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '任务状态:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '任务状态', '操作输出', 1, S_txt)
        # 机构管理
        self.page.get_city_name(count, RESOURCE_ID_name1)
        try:
            # 输入时间
            self.page.input_date()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '输入时间', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表填表_输入时间:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '输入时间', '操作输出', 1, S_txt)

        try:
            self.page.all_check_button(count, RESOURCE_ID_name1,'查询按钮')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '查询按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表填表_查询按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '查询按钮', '操作输出', 1, S_txt)

        try:
            self.page.driver.find_element_by_xpath('//*[@id="ext-comp-1031"]/tbody/tr[2]/td[3]').click()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '刷新按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            # 刷新按钮
            S_txt = '报表填表_刷新按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '刷新按钮', '操作输出', 1, S_txt)
        time.sleep(2)
        self.page.task_list(number1, number2)
        count += 1

    def second_message(self, number1, number2):
        self.page.return_page()
        if number1 == 2:
            RESOURCE_ID_name1 = 'CBRC%d1' % number2
        elif number1 == 3:
            RESOURCE_ID_name1 = 'PBOC%d1' % number2
        else:
            RESOURCE_ID_name1 = 'SAFE%d2' % number2
        count = 1
        report_name = "报表查询"
        try:
            self.page.fist_iframe(2, '//*[@class="panel panel-htop"]/div/div/iframe')
            self.page.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div[2]/div/div/iframe')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '操作输入', '进入iframe层', 0, '功能正常')
        except Exception as e:
            S_txt = '报表查询_进入iframe层:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '操作输入', '进入iframe层', 1, S_txt)
        # 输入字符串
        self.page.report_check_button(count, RESOURCE_ID_name1, report_name)
        # 点击查询按钮
        self.page.report_check(count, RESOURCE_ID_name1, report_name)
        # 机构管理
        self.page.report_messages(count, RESOURCE_ID_name1, report_name)
        self.page.report_onlink_button(count, RESOURCE_ID_name1, report_name)
        self.page.close_buttons()
        # 返回确认
        self.page.report_return_onlink(count, RESOURCE_ID_name1, report_name)
        count += 1

    def three_message(self, number1, number2):
        self.page.return_page()
        report_name = '报文发送'
        if number1 == 2:
            RESOURCE_ID_name1 = 'CBRC%d1' % number2
        elif number1 == 3:
            RESOURCE_ID_name1 = 'PBOC%d1' % number2
        else:
            RESOURCE_ID_name1 = 'SAFE%d2' % number2
        count = 1
        try:
            self.page.fist_iframe(3, '//*[@class="panel panel-htop"]/div/div/iframe')
            self.page.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div[3]/div/div/iframe')
        except Exception as e:
            print(e)
        try:
            ls = self.page.driver.find_elements_by_xpath('//div[@class="x-column-inner"]/div')
            for y in ls:
                if y.text == "报表代码:":
                    y.click()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '任务名称', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_任务名称:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '任务名称', '操作输出', 1, S_txt)

        try:
            self.page.text_status()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '任务状态', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_任务状态:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '任务状态', '操作输出', 1, S_txt)

        try:
            self.page.task_name()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '报文代码', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_报文代码:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '报文代码', '操作输出', 1, S_txt)

        # 报送机构
        self.page.get_city_name(count, RESOURCE_ID_name1)
        try:
            self.page.input_date()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '日期输入', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_日期输入:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '日期输入', '操作输出', 1, S_txt)

        try:
            self.page.all_check_button(count, RESOURCE_ID_name1,report_name)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文报送', '查询按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_查询按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文报送', '查询按钮', '操作输出', 1, S_txt)

        try:
            self.page.task_list(number1, number2)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文报送', '任务列表', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文报送_任务列表:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文报送', '任务列表', '操作输出', 1, S_txt)

    def message_down(self, number1, number2):
        self.page.return_page()
        if number1 == 2:
            RESOURCE_ID_name1 = 'CBRC%d1' % number2
        elif number1 == 3:
            RESOURCE_ID_name1 = 'PBOC%d1' % number2
        else:
            RESOURCE_ID_name1 = 'SAFE%d2' % number2
        count = 1
        try:
            self.page.fist_iframe(4, '//*[@class="panel panel-htop"]/div/div/iframe')
            self.page.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div[4]/div/div/iframe')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文下载', '操作输入', '进入iframe层', 0, '功能正常')

        except Exception as e:
            S_txt = '报文下载_进入iframe层:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文下载', '操作输入', '进入iframe层', 1, S_txt)

        self.page.get_city_name(count, RESOURCE_ID_name1)
        try:
            self.page.all_check_button(count, RESOURCE_ID_name1, '查询按钮')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表报送', '查询按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表发送_查询按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表报送', '查询按钮', '操作输出', 1, S_txt)

        try:
            self.page.check_box(
                '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]'
                '/div[1]/div[1]/div/table/thead/tr/td[1]/div/div')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表报送', '刷新按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表报送_刷新按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表报送', '刷新按钮', '操作输出', 1, S_txt)

    def one_level(self, number):
        lists = self.page.driver.find_elements_by_xpath(
            '/html/body/div[1]/div/div[2]/ul/li[1]/div/div[%s]/div/a' % str(number))
        return len(lists)

    def chioce_report(self, number):
        time.sleep(2)
        self.page.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/ul/li[2]/div/div[2]/div/a[%s]/div[2]/h3' % str(number)).click()
        time.sleep(2)

    def test_report(self):
        self.page.open_page()

    def start_test(self, number):
        self.page.chioce_manage(2)
        count = 1
        report_name = '敏捷报表平台'
        if 0<number<14:
            if number <= 9:
                RESOURCE_ID = 'report1'
                RESOURCE_ID_name1 = 'report1%d1' % number
            else:
                str_num = str(number)
                s = str_num[1]
                RESOURCE_ID = 'report2%s'%s
                RESOURCE_ID_name1 = 'report2%s1' % s
            try:
                self.chioce_report(number)
            except Exception as e:
                S_txt = '敏捷报表平台' + str(e)
                self.page.write_error_excel(S_txt)
                self.page.write_error_mysql(count, 'report', '点击按钮', '操作输入', '操作输出', 1, S_txt)
            try:
                self.page.fist_iframe(1, '//*[@class="panel panel-htop"]/div/div/iframe')
                self.page.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                         '/html/body/div[1]/div[2]/div/div/div/div/iframe')
                self.page.write_error_mysql(count, RESOURCE_ID, '点击按钮', '操作输入', '操作输出', 0, '功能正常')

            except Exception as e:
                S_txt = '敏捷报表平台__进入iframe层:' + str(e)
                self.page.write_error_excel(S_txt)
                self.page.write_error_mysql(count, RESOURCE_ID, '敏捷报表平台', '进入iframe层', '操作输出', 1, S_txt)
            # 输入字符串
            self.page.report_check_button(count, RESOURCE_ID_name1, report_name)
            # 点击查询按钮
            self.page.report_check(count, RESOURCE_ID_name1, report_name)
            # 机构管理
            self.page.report_messages(count, RESOURCE_ID_name1, report_name)
            # 点击查询
            self.page.report_onlink_button(count, RESOURCE_ID_name1, report_name)
            try:
                self.page.close_buttons()
            except Exception as e:
                S_txt = '敏捷报表平台__进入iframe层:' + str(e)
                self.page.write_error_excel(S_txt)
                self.page.write_error_mysql(count, RESOURCE_ID, '敏捷报表平台', '进入iframe层', '操作输出', 1, S_txt)
            # 返回确认
            self.page.report_return_onlink(count, RESOURCE_ID_name1, report_name)
            count += 1
            time.sleep(1)
            self.page.driver.refresh()

    def main_report(self):
        time.sleep(2)
        self.page.return_page()
        lens = self.page.driver.find_elements_by_xpath('//*[@class="menu_top"]//div[@class="list"]/a')
        for x in range(1, len(lens) + 1):
            self.page.driver.refresh()
            self.start_test(x)

    def main_Area(self):
        self.page.open_page()
        now = datetime.datetime.now()
        date = now + datetime.timedelta(days=1)
        endow = date.strftime('%Y-%m-%d')
        for mun in range(1, 5):
            start_time = time.time()
            self.page.driver.refresh()
            for i in range(2, 5):
                num = self.one_level(i)
                for x in range(1, num + 1):
                    self.first_message(i, x)
                    self.second_message(i, x)
                    self.three_message(i, x)
                    self.message_down(i, x)
                    self.page.driver.refresh()
            self.main_report()
            self.page.driver.refresh()
            end_time = time.time()
            self.page.write_error_excel('第%s次运行时间为:' % mun + str(end_time - start_time) + '\n')
            print('第%s次运行时间为:' % mun + str(end_time - start_time) + '\n')
            text = ('第%s次运行时间为:' % mun + str(end_time - start_time) + '\n')
            self.page.read_mysql(self.page.get_time(), endow, text)
        self.page.db.close()

if __name__ == "__main__":
    Test01 = Custom_riosk()
    Test01.main_Area()
