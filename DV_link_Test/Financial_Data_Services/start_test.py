from DV_link_Test.Financial_Data_Services.finacial_model import *

class Test01:
    def __init__(self):
        self.first1 = Finacial_Data()

    def send_management(self):
        RESOURCE_main = 'businessServices'
        report_name1 = "填报管理"
        count1= 1
        count = 1
        RESOURCE_ID_name1 = "businessServices_04"
        RESOURCE_ID = "TB_0401"
        report_name = "填报模板"
        try:
            try:
                self.first1.openpage.fist_iframe(1, '//*[@class="panel panel-htop"]/div/div/iframe')
                self.first1.openpage.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                             '//*[@class="x-panel-body x-panel-body-noheader x-panel-body-noborder"]/iframe')
                self.first1.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, report_name, '操作输出', 0, "功能正常")
            except Exception as e:
                S_txt = '{}__进入iframe层:'.format(report_name) + str(e)
                self.first1.openpage.write_error_excel(S_txt)
                self.first1.openpage.write_error_mysql(count, RESOURCE_ID_name1, report_name, '进入iframe层', '操作输出', 1, S_txt)

            self.first1.task_name_main(count, RESOURCE_ID, report_name)
            self.first1.openpage.all_check_button(count, RESOURCE_ID, report_name)
            time.sleep(1)
            self.first1.creat_detail_list(count, RESOURCE_ID, report_name)
            self.first1.pindu_status(count, RESOURCE_ID, report_name)
            # 创建任务
            self.first1.create_task(count, RESOURCE_ID, report_name)
            # 创建频度
            self.first1.create_pindu(count, RESOURCE_ID, report_name)
            # 创建执行
            self.first1.create_execute(count, RESOURCE_ID, report_name)
            # 创建主题
            self.first1.create_main_report(count, RESOURCE_ID, report_name)
            # 启动时间
            self.first1.start_date(count, RESOURCE_ID, report_name)
            # 完成期限
            self.first1.need_date(count, RESOURCE_ID,report_name)
            self.first1.excetue_message(count, RESOURCE_ID,report_name)
            self.first1.isor_and_false(count, RESOURCE_ID,report_name)
            # 数据日期
            self.first1.data_date(count, RESOURCE_ID,report_name)
            # 选择流程
            self.first1.chioce_flow(count, RESOURCE_ID,report_name)
            # 项目描述
            self.first1.task_description(count, RESOURCE_ID,report_name)
            self.first1.data_source(count, RESOURCE_ID,report_name)
            # self.report_code_name(count, RESOURCE_ID, report_name)
            self.first1.check_result_button(count, RESOURCE_ID,report_name)
            self.first1.cancel_button(count, RESOURCE_ID, report_name)
            # self.save_button(count, RESOURCE_ID, report_name)
            # 任务启动
            self.first1.task_start(count, RESOURCE_ID, report_name)
            self.first1.delete_task(count, RESOURCE_ID, report_name)
            self.first1.amend_task(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.first1.openpage.all_check_button(count, RESOURCE_ID, report_name)
            self.first1.openpage.driver.switch_to.default_content()
            self.first1.openpage.write_error_mysql(count1, RESOURCE_main, report_name1, '进入iframe层', '操作输出', 0, "功能正常")
            count += 1

        except Exception as e:
            S_txt = '{}__进入iframe层:'.format(report_name1) + str(e)
            self.first1.openpage.write_error_excel(S_txt)
            self.first1.openpage.write_error_mysql(count1, RESOURCE_main, report_name1, '进入iframe层', '操作输出', 1, S_txt)
        count1 +=1

    def send_message_task(self):
        report_name = "填报任务"
        RESOURCE_ID_name1 = "TB_02"
        RESOURCE_ID = "businessServices_04"
        RESOURCE_main = "businessServices"
        count1 = 1
        count = 1
        try:
            try:
                self.first1.openpage.fist_iframe(2, '//*[@class="panel panel-htop"]/div/div/iframe')
                self.first1.openpage.sencond_iframe('//*[@class="panel panel-htop"]/div/div/iframe',
                                             '//*[@class="x-tab-panel-body x-tab-panel-body-top"]/div[2]//div/iframe')
                self.first1.openpage.write_error_mysql(count, RESOURCE_ID, report_name, report_name, '操作输出', 0, "功能正常")
            except Exception as e:
                S_txt = '{}__进入iframe层:'.format(report_name) + str(e)
                self.first1.openpage.write_error_excel(S_txt)
                self.first1.openpage.write_error_mysql(count1, RESOURCE_ID, report_name, '进入iframe层', '操作输出', 1, S_txt)

            self.first1.task_name_main(count, RESOURCE_ID_name1, report_name)
            self.first1.pindu_status(count, RESOURCE_ID_name1, report_name)
            self.first1.openpage.all_check_button(count, RESOURCE_ID_name1, report_name)
            self.first1.create_task(count, RESOURCE_ID_name1, report_name)
            self.first1.need_date(count, RESOURCE_ID_name1, report_name)
            self.first1.isor_and_false(count, RESOURCE_ID_name1, report_name)
            self.first1.create_main_report(count, RESOURCE_ID_name1, report_name)
            self.first1.start_date(count, RESOURCE_ID_name1, report_name)
            self.first1.is_or_yes(count, RESOURCE_ID_name1, report_name)
            self.first1.excetue_message(count, RESOURCE_ID_name1, report_name)
            self.first1.chioce_flow(count, RESOURCE_ID_name1, report_name)
            self.first1.data_date(count, RESOURCE_ID_name1, report_name)
            self.first1.data_source(count, RESOURCE_ID_name1, report_name)
            self.first1.task_description(count, RESOURCE_ID_name1, report_name)
            # self.report_code_name(count, RESOURCE_ID_name1, report_name)
            # self.save_button(count1, RESOURCE_ID_name1, report_name)
            self.first1.openpage.all_check_button(count1, RESOURCE_ID_name1, report_name)
            self.first1.cancel_button(count, RESOURCE_ID_name1, report_name)
        except Exception as e:
            S_txt = '{}__进入iframe层:'.format(report_name) + str(e)
            self.first1.openpage.write_error_excel(S_txt)
            self.first1.openpage.write_error_mysql(count1, RESOURCE_main, report_name, '进入iframe层', '操作输出', 1, S_txt)
        count1 += 1

    def four_report_messages(self):
        RESOURCE_main_name = 'platform'
        count=1
        report_name = "金融数据中台"
        try:
            self.send_management()
            self.first1.openpage.return_page()
            self.send_message_task()
        except Exception as e:
            S_txt = '{}__进入金融数据中台:'.format(report_name) + str(e)
            self.first1.openpage.write_error_excel(S_txt)
            self.first1.openpage.write_error_mysql(count, RESOURCE_main_name, report_name, '进入iframe层', '操作输出', 1, S_txt)
        count += 1

    def start_test(self):
        self.first1.openpage.open_page()
        self.first1.openpage.first_supervise(4, 3, 4)
        self.four_report_messages()


    def main(self):
        self.start_test()

if __name__ == "__main__":
    test = Test01()
    test.start_test()