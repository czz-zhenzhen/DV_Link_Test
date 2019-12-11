from DV_link_Test.main import *
import random
class Test:
    def __init__(self):
        self.open = TestSystem()

    def test(self):
        self.open.first_supervise(1, 2, 1)
        self.open.fist_iframe(1, '//*[@class="panel panel-htop"]/div/div/iframe')
        self.open.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                            '/html/body/div[1]/div[2]/div/div[1]/div/div/iframe')
        self.open.task_name()
        ls = self.open.driver.find_elements_by_xpath('//div[@class="x-column-inner"]/div')
        for y in ls:
            if y.text == "任务状态:":
                y.click()
        lis = self.open.driver.find_elements_by_xpath('//div[@class="x-combo-list-inner"]/div')
        for x in lis:
            if x.text=="报表代码:":
                x.click()
        for o in ls:
            if o.text in ["填报机构:","机构:" ,"报送机构:"]:
                o.click()
        # time.sleep(2)
        # city_name = self.open.driver.find_elements_by_xpath('//div[@class="x-tree-node-el x-unselectable x-tree-node-collapsed"]//span/img')
        # self.open.driver.find_element_by_xpath('//div[@class="x-menu x-menu-floating x-layer"]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]').click()
        # time.sleep(2)
        # city_name = self.open.driver.find_elements_by_xpath('//div[@class="x-menu x-menu-floating x-layer"]/ul/li/div/div/div/ul/li/ul/li[2]/ul//li/div/a/span')
        # list_name = []
        # for a in city_name:
        #     names = a.text
        #     list_name.append(names)
        # time.sleep(1)
        # for c in city_name:
        #     length_num = random.randint(1, len(list_name))
        #     on_link = list_name[length_num]
        #     if c.text==on_link:
        #         c.click()
        td_list = self.open.driver.find_elements_by_xpath('//*[@id="mainPanel"]//div[@class="x-grid3-body"]/div')
        ls01 = []
        for t in td_list:
            print(t)
            t.click()
            s = t.text
            ls01.append(s)
            print(ls01)
            # 获取详细
            ts_list = self.open.driver.find_elements_by_xpath('//*[@id="report_list"]//div[@class="x-grid3-body"]/div')
            time.sleep(1)
            for p in ts_list:
                print(p.text)
                p.click()
                onlink = self.open.driver.find_elements_by_xpath('//*[@id="report_list"]//div[@class="x-grid3-body"]/div/div/table/tbody/tr/td[4]/div/a/href')
                for lin in onlink:
                    print(lin)
                # p.find_element_by_xpath('/table/tbody/tr/td[4]/div/a/href').click()
                return
            return


    def main_test(self):
        self.open.open_page()
        self.test()

if __name__ == "__main__":
    test = Test()
    test.main_test()




















import xlwt
# import xlrd
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
#
# import pymysql
# import time
# today_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# db = pymysql.connect('101.201.73.80', 'dvlink', 'Lrdata_2019', db='dvlink')
# cursor = db.cursor()
# # sql_date  = "SELECT B.PARENT_RESOURCE_ID,B.PARENT_RESOURCE_NAME,COUNT(A.LOG_ID) AS ZS,COUNT(CASE WHEN A.OP_STATUS = 0 THEN A.LOG_ID END) AS CG,COUNT(CASE WHEN A.OP_STATUS = 1 THEN A.LOG_ID END) AS SB,COUNT(CASE WHEN A.OP_STATUS = 2 THEN A.LOG_ID END) AS CS FROM ATT_LOG A INNER JOIN mmc_sys_resource_info_relation B ON A.RESOURCE_ID = B.RESOURCE_ID WHERE B.PARENT_RESOURCE_ID IN('analyse','platform','report','super') AND STR_TO_DATE('{}','%Y-%m-%d') BETWEEN DATE(A.START_DATE) AND DATE(A.END_DATE) AND SEQ_ID = 1 GROUP BY B.PARENT_RESOURCE_ID".format(today_time)
# sql_date = """select * from ATT_LOG WHERE START_DATE BETWEEN '%s' AND '%s' """ % ('2019-12-3', '2019-12-4')
# cursor.execute(sql_date)
# ls = cursor.fetchall()
# for x in ls:
#     print(x)
# print(ls[0][1])
# print(ls[1][1])
# print(ls)
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# with open('/DV_link/DV_link_Test/excel_test21.xls','w')as f :
#     workbook = xlwt.Workbook(encoding='utf-8')
#     worksheet = workbook.add_sheet('汇总')
#     worksheet02 = workbook.add_sheet('详细情况')
#     worksheet.write(0,1,label='剧烈')
#     worksheet.write(1,1,label='剧烈')
#     worksheet.write(2,1,label='剧烈')
#     workbook.save('excel_test21.xls')
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# import os
# import datetime
# now = datetime.datetime.now()
# date = now + datetime.timedelta(days = -1)
# endow = date.strftime('%Y-%m-%d')
# print(endow)
"""
smtpserver = 'smtp.qq.com'
mail_user = "823178484@qq.com"
mail_pass = "zfhaqkkzpnqhbbbd"
sender = '"823178484@qq.com"'
# receivers = ['932787585@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['932787585@qq.com','823178484@qq.com','869744857@qq.com','czz_zhenzhen@sina.com','18375836065@163.com']
# receivers = ['"zhenzhen.cai@shuhaosoft.com"']
subject = 'Python SMTP 邮件测试'

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEMultipart()
message['Subject'] = Header(subject, 'utf-8')
filepath = '/DV_link/DV_link_Test/record_form_2019-11-21.txt'
with open(filepath,'rb')as f :
    ls_txt = f.read().decode('utf-8','ignore')
text1 = MIMEText(ls_txt,'base64','utf-8')
text1['Content-Type']='application/octet-stream'
text1['Content-Disposition']='attachment;filename="test.txt"'
message.attach(text1)
message = MIMEText('<html><h1>你好！测试功能</h1></html>','html','utf-8')
message.attach(message)
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(mail_user,mail_pass)
smtp.sendmail(sender,receivers,message.as_string())
smtp.quit()
"""

# filename = '/DV_link/DV_link_Test/record_test'
# list_name = os.listdir(filename)
#
# print(list_name[-1])
# def get_filename(self):
#     filename = '/DV_link/DV_link_Test/record_test'
#     list_name = os.listdir(filename)
#     last_filename = list_name[-1]
#     return last_filename
import pymysql
# import time
# t1 = time.time()
# time_str2 = time.strftime('%Y-%m-%d:%H:%M', time.localtime())
# time_str = time.strftime('%Y-%m-%d', time.localtime())
# path = '/DV_link/DV_link_Test/record_form_'+time_str+'.txt'
# with open(path, 'a', encoding='utf-8')as f:
#     f.write(str(time_str2)+'\n')
# time.sleep(3)
# t2 = time.time()
#
# print(t2-t1)

# db = pymysql.connect('101.201.73.80','dvlink','Lrdata_2019',db='dvlink')
# cursor = db.cursor()
# sql = """insert into ATT_LOG(SEQ_ID,RESOURCE_ID,OP_NAME,OP_INPUT,OP_OUTPUT,START_DATE,END_DATE,OP_STATUS,OP_DESC) values (2,'2','操作步骤','操作输入','操作输出',sysdate(),sysdate(),1,'描述')"""
# cursor.execute(sql)
# db.commit()
# db.close()

# ls = [1,2,3]
# print(ls[-1])
