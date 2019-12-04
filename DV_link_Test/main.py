from selenium import webdriver
import time, datetime
import random
import pymysql
import xlwt
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os


class TestSystem():
    def __init__(self):
        # self.driver = webdriver.Ie()
        self.driver = webdriver.Chrome()
        # 本地
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.db = pymysql.connect('101.201.73.80', 'dvlink', 'Lrdata_2019', db='dvlink')
        self.cursor = self.db.cursor()
        self.driver.get("http://192.168.0.98:8080/dvlink/")
        # 云环境
        # self.driver.get("http://cloud.shuhaosoft.com/dvlink/")
        self.smtp = 'smtp.qq.com'
        self.mail_user = "823178484@qq.com"
        self.mail_pass = "zfhaqkkzpnqhbbbd"
        self.sender = "823178484@qq.com"

    def open_page(self):
        """
        打开主页面
        :return:
        """
        # self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div/div[2]/div/input').send_keys('00000')
        self.driver.find_element_by_id('username').send_keys('00000')
        time.sleep(2)
        # self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div/div[4]/div/input').send_keys("demo123.com")
        self.driver.find_element_by_id('password').send_keys("demo123.com")
        self.driver.find_element_by_class_name('blue_button').click()
        time.sleep(3)

    def first_supervise(self, number1, number2, number3):
        """
        报表填报功能测试
        传递元素节点，和节点元素序列号
        :param element_text: /html/body/div[1]/div/div[2]/ul/li[1]/div/div[2]/div/a[1]/div[2]/h3
                            /html/body/div[1]/div/div[2]/ul/li[1]/div/div[2]/div/a[?]/div[2]/h3.format(2)
        :param number1:第一级模板
        :param number2:第二级模板
        :param number3:第三级模板
        :return:
        """
        # self.open_page()
        self.chioce_manage(number1)
        time.sleep(2)
        ele_text = "/html/body/div[1]/div/div[2]/ul/li[%s]/div/div[%s]/div/a[%s]/div[2]/h3" % (
            str(number1), str(number2), str(number3))
        time.sleep(1)
        self.driver.find_element_by_xpath(ele_text).click()

    def text_status(self, elem1, elem2):
        # 点击显示列表
        elems1 = str(elem1)
        elems2 = str(elem2)
        self.driver.find_element_by_xpath(elems1).click()
        time.sleep(1)
        lists = self.driver.find_elements_by_xpath(elems2)
        num = random.randint(1, len(lists))
        time.sleep(1)
        self.driver.find_element_by_xpath(elems2 + '[%s]' % str(num)).click()

    def check_button(self, elem):
        self.driver.find_element_by_xpath(str(elem)).click()

    def put_time(self, elem):
        self.driver.find_element_by_xpath(str(elem)).send_keys(self.get_time())

    def check_box(self, elem):
        time.sleep(1)
        self.driver.find_element_by_xpath(elem).click()

    def task_name(self, elem1, elem2):
        """
        任务名称
        :param elem1: 节点
        :param elem2: 内容
        :return:
        """
        elems1 = str(elem1)
        elems2 = str(elem2)
        self.driver.find_element_by_xpath(elems1).send_keys(elems2)

    def messsage_arg(self, elem1, elem2, elem3):
        """
         # 填报机构
        :param elem1: 获取点击元素
        :param elem2: 加号图片元素
        :param elem3: 省市元素
        :return:
        """
        try:
            elems1 = str(elem1)
            elems2 = str(elem2)
            elems3 = str(elem3)
            self.driver.find_element_by_xpath(elems1).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(elems2).click()  # 点击图片
            time.sleep(3)
            list01 = self.driver.find_elements_by_xpath(elems3)
            num01 = random.randint(1, len(list01))
            time.sleep(2)
            self.driver.find_element_by_xpath(
                elems3 + '[%s]/div/a/span' % str(num01)).click()
        except Exception as e:
            S_txt = '机构管理:' + str(e)
            self.write_error_excel(S_txt)

    def save_butom(self, elem):
        elems = str(elem)
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath(elems).click()
        except Exception as e:
            S_txt = '报送管理_创建任务_保存按钮:' + str(e)
            self.write_error_excel(S_txt)

    def fist_iframe(self, num, elem):
        # 第一个功能进入iframe层
        time.sleep(2)
        elems = str(elem)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(elems))
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[1]/ul/li[%s]/a[2]/em/span/span' % str(num)).click()
        self.driver.switch_to.default_content()

    def sencond_iframe(self, elem1, elem2):
        elems1 = str(elem1)
        elems2 = str(elem2)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(elems1))
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(elems2))
        time.sleep(1)

    def chioce_manage(self, number):
        """
        传入元素节点和元素序列号，选择页面上方功能
        :param element_text:'/html/body/div[1]/div/div[2]/ul/li{}/h2/a'
        :param number:format(number)
        :return:
        """

        element_texts = '//*[@id="menu_top_ul"]/li[' + str(number) + ']'
        self.driver.find_element_by_xpath(element_texts).click()

    def get_time(self):
        today_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return today_time

    def on_link(self, elem1):
        slems = str(elem1)
        self.driver.find_element_by_xpath(slems).click()

    def return_page(self):
        time.sleep(1)
        self.driver.switch_to.default_content()

    def test_first(self, number1, number2):
        self.first_supervise(1, number1, number2)
        self.fist_iframe(1, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
        self.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                            '/html/body/div[1]/div[2]/div/div/div/div/iframe')

        self.driver.find_element_by_xpath('//*[@id="search_task_name"]').send_keys('123')
        time.sleep(5)
        self.task_list(number1, number2)

    def report_detail(self, number1, number2):
        count = 1
        if number1 == 2:
            RESOURCE_ID_name1 = 'CBRC%d1' % number2
            RESOURCE_ID = 'CBRC%d' % number2
            self.write_error_mysql(count, "CBRC", '报表填表', '刷新按钮', '操作输出', 0, '功能正常')
        elif number1 == 3:
            RESOURCE_ID_name1 = 'PBOC%d1' % number2
            RESOURCE_ID = 'PBOC%d' % number2
            self.write_error_mysql(count, "PBOC", '报表填表', '刷新按钮', '操作输出', 0, '功能正常')
        else:
            RESOURCE_ID_name1 = 'SAFE%d1' % number2
            RESOURCE_ID = 'SAFE%d' % number2
            self.write_error_mysql(count, "SAFE", '报表填表', '刷新按钮', '操作输出', 0, '功能正常')
        time.sleep(2)
        self.return_page()
        try:
            self.fist_iframe(1, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
            self.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                '/html/body/div[1]/div[2]/div/div/div/div/iframe')
            self.driver.find_element_by_xpath(
                '/html/body/div[23]/div[2]/div[1]/div/div/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/'
                'table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/button').click()
            self.write_error_mysql(count, RESOURCE_ID, '报表填表', '进入iframe层', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表填报__进入iframe层:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID, '报表填表', '进入iframe层', '操作输出', 1, S_txt)
        time.sleep(2)
        # 关闭按钮
        try:
            if self.driver.find_element_by_xpath('//*[@id="ext-gen3"]/div[12]/a').click() == False:
                self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '刷新按钮', '操作输出', 0, '功能正常')
                print('0000')
        except Exception as e:
            S_txt = '报表填报__填报__返回确认按钮:' + str(e)
            self.write_error_excel(S_txt)
        try:
            self.driver.find_element_by_xpath('//*[@id="ext-gen201"]').click()
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '导入数据', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表填报__填报__计算公式:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '导入数据', '操作输出', 1, S_txt)
        print('123')
        try:
            time.sleep(1)
            print('345')
            # self.driver.find_element_by_tag_name('x-btn-text').click()
            self.driver.find_element_by_tag_name('//*[@id="ext-gen267"]').click()
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填报__导入数据', '关闭按钮', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表填报__导入数据__关闭按钮:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '关闭按钮', '操作输出', 1, S_txt)
        try:
            self.driver.find_element_by_xpath('//*[@id="ext-gen398"]').click()
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填报__计算公式', '计算公式', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表填报__导入数据__关闭按钮:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表__计算公式', '计算公式', '操作输出', 1, S_txt)

        try:
            self.driver.find_element_by_xpath('//*[@id="ext-gen209"]').click()
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '报表导出', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表填报__报表导出:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '报表导出', '操作输出', 1, S_txt)
        try:
            self.driver.find_element_by_xpath('//*[@id="ext-gen213"]').click()
            self.driver.find_element_by_xpath('//*[@id="ext-gen430"]')
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表_填报', '刷新按钮', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表填表_刷新按钮:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表_填报', '刷新按钮', '操作输出', 1, S_txt)
            time.sleep(2)
        try:
            self.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                '/html/body/div[1]/div[2]/div/div/div/div/iframe')
            self.driver.find_element_by_xpath('/html/body/div[25]/a').click()
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '完成按钮', '操作输出', 0, '功能正常')

        except Exception as e:
            S_txt = '报表填表_刷新按钮:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '完成按钮', '操作输出', 1, S_txt)
        try:
            self.driver.find_element_by_xpath('//*[@id="ext-gen217"]').click()
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '重新校验', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表填表_重新校验:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '重新校验', '操作输出', 1, S_txt)
        try:
            self.driver.find_element_by_xpath('//*[@id="ext-gen229"]"]').click()
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '关闭按钮', '操作输出', 0, '功能正常')
        except Exception as e:
            S_txt = '报表填表_关闭按钮:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '关闭按钮', '操作输出', 1, S_txt)
        self.return_page()
        try:
            self.driver.find_element_by_xpath('//*[@id="ext-gen174"]').click()
        except Exception as e:
            S_txt = '报表填表_刷新按钮:' + str(e)
            self.write_error_excel(S_txt)
            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '刷新按钮', '操作输出', 1, S_txt)

    def task_list(self, number1, number2):
        count = 1
        if number1 == 2:
            RESOURCE_ID_name1 = 'CBRC%d1' % number2
            self.write_error_mysql(count, "CBRC", '报表填表', '刷新按钮', '操作输出', 0, '功能正常')
        elif number1 == 3:
            RESOURCE_ID_name1 = 'PBOC%d1' % number2
            self.write_error_mysql(count, "PBOC", '报表填表', '刷新按钮', '操作输出', 0, '功能正常')
        else:
            RESOURCE_ID_name1 = 'SAFE%d1' % number2
            self.write_error_mysql(count, "SAFE", '报表填表', '刷新按钮', '操作输出', 0, '功能正常')
        time.sleep(3)
        lists = self.driver.find_elements_by_xpath(
            '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div')
        details_num = self.driver.find_elements_by_xpath(
            '/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div')
        num = len(lists)
        if num > 0:
            for x in range(1, num + 1):
                try:
                    txt = '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[%s]' \
                          '/table/tbody/tr/td[2]/div/span' % str(x)
                    self.driver.find_element_by_xpath(txt).click()
                    self.write_error_mysql(count, RESOURCE_ID_name1, '监管报送系', '获取列表', '查询按钮', 0, '功能正常')
                except Exception as e:
                    S_txt = '监管报送系统__获取列表:' + str(e)
                    self.write_error_excel(S_txt)
                    self.write_error_mysql(count, RESOURCE_ID_name1, '监管报送系', '获取列表', '查询按钮', 1, S_txt)

                if len(details_num) < 0:
                    try:
                        self.driver.find_element_by_tag_name('c-message-close-btn').click()
                    except Exception as e:
                        print(e)
                    return
                else:
                    for y in range(1, len(details_num) + 1):
                        try:
                            self.driver.find_element_by_xpath(
                                '/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[%s]'
                                '/table/tbody/tr/td[4]/div/a' % str(
                                    y)).click()
                            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '判断任务明细', '操作输出', 0, '功能正常')
                        except Exception as e:
                            S_txt = '任务列表__判断任务明细:' + str(e)
                            self.write_error_excel(S_txt)
                            self.write_error_mysql(count, RESOURCE_ID_name1, '报表填表', '判断任务明细', '操作输出', 1, S_txt)
                            continue
                        self.report_detail(number1, number2)
                        time.sleep(2)

    def test_second_message(self):
        self.return_page()
        self.fist_iframe(2, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
        self.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                            '/html/body/div[1]/div[2]/div/div[2]/div/div/iframe')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr/td[1]'
            '/table/tbody/tr/td[1]/input').send_keys(
            '存折信息')
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath('/html/body/div[15]/a').click()
        except Exception as e:
            print(e)
        time.sleep(2)
        list02 = self.driver.find_elements_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div')
        nums = len(list02)
        for x in range(nums):
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div'
                '/div[%s]/table/tbody/tr/td[1]/div' % str(x))

    def write_error_excel(self, text):
        time_str2 = time.strftime('%Y-%m-%d:%H:%M', time.localtime())
        time_str = time.strftime('%Y-%m-%d', time.localtime())
        path = '/DV_link/DV_link_Test/record_test/ecord_form_' + time_str + '.txt'
        with open(path, 'a', encoding='utf-8')as f:
            f.write(str(time_str2) + '\n')
            f.write(text)

    def write_error_mysql(self, num, name_id, op_name, op_put, op_out, op_status, text):
        """
        :param num: 测试次数
        :param name_id:菜单ID
        :param op_name:操作步骤'
        :param op_put:操作输入
        :param op_out:操作输出
        :param op_status:操作结果状态：0成功1失败2超时
        :param text:操作结果描述
        :return:
        """
        try:
            sql = """insert into ATT_LOG(SEQ_ID,RESOURCE_ID,OP_NAME,OP_INPUT,OP_OUTPUT,START_DATE,END_DATE,OP_STATUS,OP_DESC) 
            value (%d,'%s','%s','%s','%s',sysdate(),sysdate(),%d,'%s')""" % (
                num, name_id, op_name, op_put, op_out, op_status, text)
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print('sql语句错误', e)

    def read_mysql(self, start_date, end_date, text):
        count = 1
        try:
            sql_date = """select * from ATT_LOG WHERE START_DATE BETWEEN '%s' AND '%s' """ % (
                start_date, end_date)
            # 当日运行总次数
            sql_date_total = "SELECT B.PARENT_RESOURCE_ID,B.PARENT_RESOURCE_NAME,COUNT(A.LOG_ID) AS ZS," \
                             "COUNT(CASE WHEN A.OP_STATUS = 0 THEN A.LOG_ID END) AS CG,COUNT" \
                             "(CASE WHEN A.OP_STATUS = 1 THEN A.LOG_ID END) AS SB,COUNT(CASE WHEN A.OP_STATUS = 2 THEN A.LOG_ID END)" \
                             " AS CS FROM ATT_LOG A INNER JOIN mmc_sys_resource_info_relation B " \
                             "ON A.RESOURCE_ID = B.RESOURCE_ID WHERE B.PARENT_RESOURCE_ID IN('analyse','platform','report','super') " \
                             "AND STR_TO_DATE('{}','%Y-%m-%d') BETWEEN DATE(A.START_DATE) AND DATE(A.END_DATE) AND" \
                             " SEQ_ID = 1 GROUP BY B.PARENT_RESOURCE_ID".format(start_date)
            self.cursor.execute(sql_date_total)
            ls = self.cursor.fetchall()
            # 获取数组
            self.cursor.execute(sql_date)
            ls1 = self.cursor.fetchall()
            time_str = str(self.get_time())
            path = '/DV_link/DV_link_Test/Supervisory_Report_SyS/' + time_str + '_Test_report.xls'
            list_name = ['日期', '总计', '成功', '失败']
            list_name01 = ['LOG_ID', 'SEQ_ID', 'RESOURCE_ID', 'OP_NAME', 'OP_INPUT', 'OP_OUTPUT', 'START_DATE',
                           'END_DATE', 'OP_STATUS', 'OP_DESC']
            list_name02 = ['监管报送系统', '敏捷报表平台', '智能分析平台', '金融数据中台']
            with open(path, 'w')as f:
                workbook = xlwt.Workbook(encoding='utf-8')
                worksheet = workbook.add_sheet('汇总')
                worksheet02 = workbook.add_sheet('测试详细')
                for x in range(len(list_name)):
                    worksheet.write(0, x + 1, label=list_name[x])
                    if x >= 1:
                        worksheet.write(1, 1 + x, label=ls[0][1 + x])
                        worksheet.write(2, 1 + x, label=ls[1][1 + x])
                for y in range(len(list_name01)):
                    worksheet02.write(0, y, label=list_name01[y])
                for i in range(len(list_name02)):
                    worksheet.write(i + 1, 0, label=list_name02[i])
                    worksheet.write(i + 1, 1, label=self.get_time())
                for row in ls1:
                    for rx in range(len(row)):
                        worksheet02.write(count, rx, label=row[rx])
                    count += 1
                    workbook.save(time_str + '_Test_report.xls')
                self.send_email(text, path)
        except Exception as e:
            print('sql语句错误', e)

    def send_email(self, text, filepath):

        with open('/DV_link/DV_link_Test/Supervisory_Report_SyS/list_name.txt')as f:
            ls = f.read()
            receivers = ls.split(',')
        message = MIMEMultipart()
        subject = 'Python SMTP 邮件测试'
        # mes = MIMEText('<html><h1>测试附件功能</h1><h2>自动测试邮件发送</h2></html>', 'html', 'utf-8')
        mes = MIMEText(text, 'plain', 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        with open(filepath, 'rb')as f:
            ls_txt = f.read().decode('utf-8', 'ignore')
        down_txt = MIMEText(ls_txt, 'base64', 'utf-8')
        down_txt['Content-Type'] = 'application/octet-stream'
        down_txt['Content-Disposition'] = 'attachment;filename="Recode_test%s.xls"' % str(self.get_time())
        message.attach(down_txt)
        message.attach(mes)
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp)
        smtp.login(self.mail_user, self.mail_pass)
        smtp.sendmail(self.sender, receivers, message.as_string())
        smtp.quit()

    def report_project(self):
        # 报表主题
        self.driver.find_element_by_xpath('//*[@id="reportThemeCombo"]').click()
        time.sleep(3)
        list01 = self.driver.find_elements_by_xpath('/html/body/div[32]/ul/li/div/div/div/ul/li/ul/li')
        print(len(list01))
        if len(list01) == 0:
            self.driver.find_element_by_xpath('//*[@id="reportThemeCombo"]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="ext-gen276"]/li[2]/div/img[1]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '/html/body/div[27]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li[2]/div/a/span').click()
            time.sleep(1)
        else:
            mun = random.randint(1, len(list01) + 1)
            time.sleep(3)
            self.driver.find_element_by_xpath(
                '/html/body/div[26]/ul/li/div/div/div/ul/li/ul/li[%s]' % str(mun) + '/div/img[1]').click()
            # 获得下一级目录
            time.sleep(3)
            list02 = self.driver.find_elements_by_xpath(
                '/html/body/div[31]/ul/li/div/div/div/ul/li/ul/li[%s]/ul/li' % (str(mun)))
            mun2 = random.randint(1, len(list02) + 1)
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '/html/body/div[31]/ul/li/div/div/div/ul/li/ul/li[%s]/ul/li[%s]/div/a/span' % (
                    str(mun), str(mun2))).click()

    def create_message(self):
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[24]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/form/div[1]/div/'
                'div/div/div[1]/div/div/div[1]/div[1]/input').send_keys(
                'test')
            time.sleep(1)
            self.text_status('//*[@id="frequency_code1"]', '/html/body/div[26]/div/div')
            self.driver.find_element_by_xpath('//*[@id="ext-comp-1084"]').send_keys(self.get_time())
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="ext-comp-1087"]').send_keys(random.randint(1, 5))
            self.messsage_arg('//*[@id="execute_org_combo"]',
                              '/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                              '/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="ext-comp-1085"]').send_keys(self.get_time())
            self.driver.find_element_by_xpath('//*[@id="flowSelector"]').click()
            self.driver.find_element_by_xpath('/html/body/div[29]/div/div').click()
            self.driver.find_element_by_xpath('//*[@id="ext-comp-1090"]').send_keys('测试需求')
            time.sleep(3)
            # 报表主题
            self.report_project()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '/html/body/div[23]/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/'
                'table/tbody/tr[2]/td[2]/em/button').click()
            time.sleep(2)
        except Exception as e:
            S_txt = '报送管理_创建任务:' + str(e)
            self.write_error_excel(S_txt)

    def main(self):
        self.open_page()
        self.test_first(2, 1)
        # self.test_second_message()
        # self.read_mysql('2019-11-28', '2019-11-29','123')


if __name__ == "__main__":
    Test = TestSystem()
    Test.main()
