
import xlwt
# import xlrd
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
#
import pymysql
import time
today_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
db = pymysql.connect('101.201.73.80', 'dvlink', 'Lrdata_2019', db='dvlink')
cursor = db.cursor()
# sql_date  = "SELECT B.PARENT_RESOURCE_ID,B.PARENT_RESOURCE_NAME,COUNT(A.LOG_ID) AS ZS,COUNT(CASE WHEN A.OP_STATUS = 0 THEN A.LOG_ID END) AS CG,COUNT(CASE WHEN A.OP_STATUS = 1 THEN A.LOG_ID END) AS SB,COUNT(CASE WHEN A.OP_STATUS = 2 THEN A.LOG_ID END) AS CS FROM ATT_LOG A INNER JOIN mmc_sys_resource_info_relation B ON A.RESOURCE_ID = B.RESOURCE_ID WHERE B.PARENT_RESOURCE_ID IN('analyse','platform','report','super') AND STR_TO_DATE('{}','%Y-%m-%d') BETWEEN DATE(A.START_DATE) AND DATE(A.END_DATE) AND SEQ_ID = 1 GROUP BY B.PARENT_RESOURCE_ID".format(today_time)
sql_date = """select * from ATT_LOG WHERE START_DATE BETWEEN '%s' AND '%s' """ % ('2019-12-3', '2019-12-4')
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
with open('/DV_link/DV_link_Test/excel_test21.xls','w')as f :
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('汇总')
    worksheet02 = workbook.add_sheet('详细情况')
    worksheet.write(0,1,label='剧烈')
    worksheet.write(1,1,label='剧烈')
    worksheet.write(2,1,label='剧烈')
    workbook.save('excel_test21.xls')
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import datetime
now = datetime.datetime.now()
date = now + datetime.timedelta(days = -1)
endow = date.strftime('%Y-%m-%d')
print(endow)
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
