from DV_link_Test.main import *
import random


class Finacial_Data:
    def __init__(self):
        self.openpage = TestSystem()

    def administration_management(self):
        self.openpage.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/ul/li[2]/a[1]/span[1]').click()

    def report_project(self):
        # 报表主题
        self.openpage.driver.find_element_by_xpath('//*[@id="reportThemeCombo"]').click()
        time.sleep(3)
        list01 = self.openpage.driver.find_elements_by_xpath('/html/body/div[32]/ul/li/div/div/div/ul/li/ul/li')
        print(len(list01))
        if len(list01) == 0:
            self.openpage.driver.find_element_by_xpath('//*[@id="reportThemeCombo"]').click()
            time.sleep(2)
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen276"]/li[2]/div/img[1]').click()
            time.sleep(2)
            self.openpage.driver.find_element_by_xpath(
                '/html/body/div[27]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li[2]/div/a/span').click()
            time.sleep(1)
        else:
            mun = random.randint(1, len(list01) + 1)
            time.sleep(3)
            self.openpage.driver.find_element_by_xpath(
                '/html/body/div[26]/ul/li/div/div/div/ul/li/ul/li[%s]' % str(mun) + '/div/img[1]').click()
            # 获得下一级目录
            time.sleep(3)
            list02 = self.openpage.driver.find_elements_by_xpath(
                '/html/body/div[31]/ul/li/div/div/div/ul/li/ul/li[%s]/ul/li' % (str(mun)))
            mun2 = random.randint(1, len(list02) + 1)
            time.sleep(2)
            self.openpage.driver.find_element_by_xpath(
                '/html/body/div[31]/ul/li/div/div/div/ul/li/ul/li[%s]/ul/li[%s]/div/a/span' % (
                    str(mun), str(mun2))).click()

    def send_management(self):
        self.openpage.fist_iframe(1, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
        self.openpage.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div/div/div/iframe')
        self.openpage.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/div/div/div[1]/input').send_keys('123')
        # 频度
        time.sleep(1)
        try:
            self.openpage.text_status(
                '/html/body/div[1]/div/div/div/div[2]/form/div/div[2]/div/div/div/div[1]/div/input[2]',
                '/html/body/div[20]/div/div')
        except Exception as e:
            S_txt = '报送管理_频度获取列:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.check_button(
                '/html/body/div[1]/div/div/div/div[2]/form/div/table/tbody/tr[2]/td[2]/em/button')
        except Exception as e:
            S_txt = '报送管理_查询:' + str(e)
            self.openpage.write_error_excel(S_txt)
        # 创建任务
        self.openpage.create_message()
        self.open_create('//*[@id="ext-gen125"]', '/html/body/div[21]/ul/li/a/span')
        try:
            self.openpage.driver.find_element_by_xpath(
                '/html/body/div[23]/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button').click()
            print('任务状态')
        except Exception as e:
            S_txt = '报送管理_创建任务:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.return_page()
            self.openpage.fist_iframe(2, '//*[@id="mainTab_businessServices_05"]/div/iframe')
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen24"]/em/span/span').click()
        except Exception as e:
            S_txt = '报送任务:' + str(e)
            self.openpage.write_error_excel(S_txt)
        # 进入iframe
        try:
            self.openpage.sencond_iframe('//*[@id="mainTab_businessServices_05"]/div/iframe',
                                         '//*[@id="ext-gen29"]/iframe')
            self.openpage.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/input').send_keys('1104')
        except Exception as e:
            S_txt = '报送任务_任务名称:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            time.sleep(2)
            self.openpage.text_status(
                '/html/body/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/div/input',
                '/html/body/div[20]/div/div')
            self.openpage.check_button('//*[@id="ext-gen42"]')
            self.openpage.check_box('/html/body/div[21]/a')
            print('111')
        except Exception as e:
            S_txt = '报送任务_确认按钮:' + str(e)
            self.openpage.write_error_excel(S_txt)
        time.sleep(2)
        self.open_create('//*[@id="ext-gen122"]', '/html/body/div[21]/ul/li/a/span')
        # 创建任务
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-comp-1078"]').send_keys('test1104')
        except Exception as e:
            S_txt = '报送任务_创建任务__任务名称:' + str(e)
            self.openpage.write_error_excel(S_txt)
        # 启动方式

        try:
            list002 = self.openpage.driver.find_elements_by_xpath('/html/body/div[27]/div/div')
            if len(list002) == 0:
                self.openpage.driver.find_element_by_xpath('/*[@id="startup_mode1"]').click()
                self.openpage.driver.find_element_by_xpath('/html/body/div[27]/div/div[1]').click()
            else:
                self.openpage.text_status('//*[@id="startup_mode1"]', '/html/body/div[27]/div/div')
        except Exception as e:
            S_txt = '报送任务_创建任务__启动方式:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-comp-1081"]').send_keys(str(random.randint(5)))
        except Exception as e:
            S_txt = '报送任务_创建任务__完成期限:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="flowSelector"]')
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen279"]/div').click()
        except Exception as e:
            S_txt = '报送任务_创建任务__选择流程:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen242"]').send_keys(self.openpage.get_time())
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-comp-1084"]').send_keys('报送管理测试')
        except Exception as e:
            S_txt = '报送任务_创建任务__数据日期:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            time.sleep(1)
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-comp-1084"]')
        except Exception as e:
            S_txt = '报送任务_创建任务__关闭按钮:' + str(e)
            self.openpage.write_error_excel(S_txt)


    def get_message_list(self):
        list01 = self.openpage.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[1]/ul/li')
        return len(list01)

    def write_message(self):
        self.openpage.fist_iframe(1, '/html/body/div[2]/div/div[2]/div/div/div/iframe')
        self.openpage.sencond_iframe('/html/body/div[2]/div/div[2]/div/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div/div/div/iframe')
        self.openpage.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/div/div/div[1]/input').send_keys('123')
        # 频度
        time.sleep(1)
        try:
            self.openpage.text_status(
                '/html/body/div[1]/div/div/div/div[2]/form/div/div[2]/div/div/div/div[1]/div/input[2]',
                '/html/body/div[20]/div/div')
        except Exception as e:
            S_txt = '填报管理_频度获取列:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.check_button(
                '/html/body/div[1]/div/div/div/div[2]/form/div/table/tbody/tr[2]/td[2]/em/button')
        except Exception as e:
            S_txt = '填报管理_查询:' + str(e)
            self.openpage.write_error_excel(S_txt)
            self.openpage.create_message()
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen125"]').click()
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen125"]').click()
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-comp-1050"]').click()
        except Exception as e:
            S_txt = '填报管理_创建任务:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen125"]').send_keys('1104')
        except Exception as e:
            S_txt = '填报管理_创建任务_任务名称:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.text_status('//*[@id="frequency_code1"]', '//*[@id="ext-gen289"]/div')
        except Exception as e:
            S_txt = '报送管理_创建任务_频度获取列:' + str(e)
            self.openpage.write_error_excel(S_txt)

        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="startup_mode1"]').click()
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen292"]/div[2]').click()
        except Exception as e:
            S_txt = '报送管理_创建任务_启动方式:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-comp-1086"]').send_keys('2')
        except Exception as e:
            S_txt = '报送管理_创建任务_完成天数:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.messsage_arg('//*[@id="execute_org_combo"]',
                                       '/html/body/div[26]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                                       '/html/body/div[26]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        except Exception as e:
            S_txt = '报送管理_创建任务_执行机构:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="is_temp1"]').click()
            print('000')
        except Exception as e:
            S_txt = '报送管理_创建任务_是否是临时任务:' + str(e)
            self.openpage.write_error_excel(S_txt)
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-gen295"]/div[1]').click()

        except Exception as e:
            S_txt = '报送管理_创建任务_是否是临时任务:' + str(e)
            self.openpage.write_error_excel(S_txt)
            print(e)
            print('12121')
        try:
            self.openpage.driver.find_element_by_xpath('//*[@id="ext-comp-1088"]').send_keys('测试创建报表任务')
        except Exception as e:
            S_txt = '报送管理_创建任务_任务描述:' + str(e)
            self.openpage.write_error_excel(S_txt)
        self.openpage.save_butom('//*[@id="ext-gen186"]')

    def start_test(self):
        self.openpage.open_page()
        list01 = self.openpage.driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/ul/li[4]/div/div[3]/div/a')
        num = len(list01)
        # for x in range(1,num+1):
        #     self.openpage.driver.refresh()
        #     time.sleep(1)
        #     self.openpage.first_supervise(4,3,x)
        self.openpage.first_supervise(4, 3, 4)
        self.write_message()
        # self.send_management()

    def main(self):
        self.start_test()


if __name__ == "__main__":
    test = Finacial_Data()
    test.main()
