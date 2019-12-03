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
            self.page.fist_iframe(1, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
            self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div/div/div/iframe')
            count += 1
            self.page.write_error_mysql(count, RESOURCE_ID, '报表填表', '操作输入', '进入iframe层', 0, '功能正常')
        except Exception as e:
            S_txt = '进入iframe层:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '操作输入', '进入iframe层', 1, S_txt)
        try:
            self.page.driver.find_element_by_xpath('//*[@id="search_task_name"]').send_keys('')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '输入框', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '输入框:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '输入框', '操作输出', 1, S_txt)
        time.sleep(3)
        try:
            self.page.driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/form/div/div[4]/div/div/div/div[1]/input').send_keys('')
            self.page.text_status(
                '/html/body/div[1]/div[2]/div/div/div/form/div/div[3]/div/div/div/div[1]/div/input[2]',
                '/html/body/div[26]/div/div')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '任务状态', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '任务状态:' + str(e)
            self.page.write_error_excel(S_txt)

            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '任务状态', '操作输出', 1, S_txt)
        try:
            self.page.messsage_arg(
                '/html/body/div[1]/div[2]/div/div/div/form/div/div[6]/div/div/div/div[1]/div/input[2]',
                '/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                '/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '填报机构', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '填报机构:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '填报机构', '操作输出', 1, S_txt)

        try:
            self.page.driver.find_element_by_xpath('//*[@id="ext-comp-1022"]').send_keys(self.page.get_time())
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '输入时间', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表填表_输入时间:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '输入时间', '操作输出', 1, S_txt)

        try:
            self.page.on_link('/html/body/div[1]/div[2]/div/div/div/form/div/table/tbody/tr[2]/td[2]/em/button')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '查询按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表填表_查询按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '查询按钮', '操作输出', 1, S_txt)

        try:
            self.page.driver.find_element_by_xpath('//*[@id="ext-gen138"]/div[1]/table/tbody/tr/td[2]/div/span').click()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '刷新按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            # 刷新按钮
            S_txt = '报表填表_刷新按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '刷新按钮', '操作输出', 1, S_txt)

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
        try:
            self.page.fist_iframe(2, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
            self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div[2]/div/div/iframe')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '操作输入', '进入iframe层', 0, '功能正常')

        except Exception as e:
            S_txt = '报表查询_进入iframe层:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '操作输入', '进入iframe层', 1, S_txt)

        try:
            self.page.driver.find_element_by_xpath('//*[@id="search"]').send_keys('存折信息')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '输入框', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表查询_输入框:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '输入框', '操作输出', 1, S_txt)

        try:
            self.page.on_link(
                '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr/td[1]/table/'
                'tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '查询', '操作输出', 0, '功能正常')


        except Exception as e:
            S_txt = '报表查询_查询:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '查询', '操作输出', 1, S_txt)

        try:
            self.page.messsage_arg('//*[@id="bankCombo"]',
                                   '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                                   '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '机构管理', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表查询_机构管理:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '机构管理', '操作输出', 1, S_txt)

        # 查询
        try:
            self.page.driver.find_element_by_xpath('//*[@id="ext-gen83"]').click()
        except Exception as e:
            S_txt = '报表查询_机构管理:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '机构管理', '操作输出', 1, S_txt)

        try:
            self.page.return_page()

            self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div[2]/div/div/iframe')
            time.sleep(2)
            self.page.driver.find_element_by_xpath('/html/body/div[15]/a').click()
            time.sleep(2)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '提示按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表查询_提示按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报表查询', '提示按钮', '操作输出', 1, S_txt)

    def three_message(self, number1, number2):
        if number1 == 2:
            RESOURCE_ID_name1 = 'CBRC%d1' % number2
        elif number1 == 3:
            RESOURCE_ID_name1 = 'PBOC%d1' % number2
        else:
            RESOURCE_ID_name1 = 'SAFE%d2' % number2
        count = 1
        self.page.return_page()
        try:
            self.page.fist_iframe(3, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
            self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div[3]/div/div/iframe')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '操作输入', '进入iframe层', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_进入iframe层:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '操作输入', '进入iframe层', 1, S_txt)

        try:
            self.page.task_name('/html/body/div[1]/div[2]/div/div/div/form/div/div[1]/div/div/div/div[1]/input', '1104')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '任务名称', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_任务名称:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '任务名称', '操作输出', 1, S_txt)

        try:
            self.page.text_status('//*[@id="taskStatus"]', '/html/body/div[26]/div/div')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '任务状态', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_任务状态:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '任务状态', '操作输出', 1, S_txt)

        try:
            self.page.task_name('//*[@id="queryKey"]', '123')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '报文代码', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_报文代码:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '报文代码', '操作输出', 1, S_txt)

        # 报送机构
        try:
            self.page.messsage_arg(
                '/html/body/div[1]/div[2]/div/div/div/form/div/div[6]/div/div/div/div[1]/div/input[2]',
                '/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                '/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '机构管理', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_机构管理:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '机构管理', '操作输出', 1, S_txt)

        try:
            self.page.put_time('/html/body/div[1]/div[2]/div/div/div/form/div/div[7]/div/div/div/div[1]/div/input')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '日期输入', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文发送_日期输入:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文发送', '日期输入', '操作输出', 1, S_txt)

        try:
            self.page.on_link('//*[@id="ext-gen53"]')
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
            self.page.fist_iframe(4, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
            self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div[4]/div/div/iframe')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文下载', '操作输入', '进入iframe层', 0, '功能正常')

        except Exception as e:
            S_txt = '报文下载_进入iframe层:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文下载', '操作输入', '进入iframe层', 1, S_txt)

        try:
            self.page.messsage_arg(
                '/html/body/div[1]/div/div/div[1]/div[2]/form/div/div[1]/div/div/div/div[1]/div/input[2]',
                '/html/body/div[9]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                '/html/body/div[9]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文下载', '机构管理', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报文下载_机构管理:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '报文下载', '机构管理', '操作输出', 1, S_txt)

        try:
            self.page.check_button('/html/body/div[1]/div/div/div[1]/div[2]/form/div/table/tbody/tr[2]/td[2]')
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
    def start_test(self, number1, number):
        self.page.chioce_manage(2)
        count = 1
        RESOURCE_ID = 'report%d' % number1
        RESOURCE_ID_name1 = 'report1%d1' % number
        try:
            self.chioce_report(number)
        except Exception as e:
            S_txt = '敏捷报表平台' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, 'report', '点击按钮', '操作输入', '操作输出', 1, S_txt)
        try:
            self.page.fist_iframe(1, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
            self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div/div/div/iframe')
            self.page.write_error_mysql(count, RESOURCE_ID, '点击按钮', '操作输入', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '敏捷报表平台__进入iframe层:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID, '敏捷报表平台', '进入iframe层', '操作输出', 1, S_txt)

        try:
            self.page.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]'
                '/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/input').send_keys(
                '123')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '点击', '返回按钮', 0, '功能正常')
        except Exception as e:
            S_txt = '敏捷报表平台__输入框:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '点击', '返回按钮', 1, S_txt)

        try:
            self.page.check_button(
                '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr/'
                'td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '点击', '机构管理', 0, '功能正常')
        except Exception as e:
            S_txt = '敏捷报表平台__关闭:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '点击', '机构管理', 1, S_txt)
        try:
            self.page.messsage_arg(
                '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/form/'
                'div/div/div/div/div[1]/div/div/div/div[1]/div/input[2]',
                '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '点击', '机构管理', 0, '功能正常')

        except Exception as e:
            S_txt = '敏捷报表平台__机构管理:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '点击', '机构管理', 1, S_txt)

        try:
            self.page.check_button(
                '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]'
                '/div/form/div/div/div/div/table[1]/tbody/tr[2]/td[2]/em/button')
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '点击', '机构管理', 0, '功能正常')

        except Exception as e:
            S_txt = '敏捷报表平台__查询按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '返回', '查询按钮', 1, S_txt)

        self.page.return_page()
        try:
            self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div/div/div/iframe')
            self.page.driver.find_element_by_xpath('/html/body/div[15]/a').click()
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '返回', '确认按钮', 0, '功能正常')

        except Exception as e:
            S_txt = '敏捷报表平台__返回确认按钮:' + str(e)
            self.page.write_error_excel(S_txt)
            self.page.write_error_mysql(count, RESOURCE_ID_name1, '敏捷报表平台', '返回', '确认按钮', 1, S_txt)
        count += 1

    def main_report(self):
        time.sleep(2)
        self.page.return_page()
        lens = self.page.driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/ul/li[2]/div/div[2]/div/a')
        for x in range(1, len(lens) + 1):
            self.page.driver.refresh()
            self.start_test(1, x)

    def main_Area(self):
        self.page.open_page()
        now = datetime.datetime.now()
        date = now + datetime.timedelta(days=1)
        endow = date.strftime('%Y-%m-%d')
        for mun in range(1, 10):
            start_time = time.time()
            # self.page.main()
            self.page.driver.refresh()
            time.sleep(1)
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
