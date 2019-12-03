import pymysql
import time
t1 = time.time()
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