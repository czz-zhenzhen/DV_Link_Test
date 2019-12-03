from DV_link_Test.main import *


class Custom_riosk:
    def __init__(self):
        self.page = TestSystem()

    def first_message(self):
        self.page.first_supervise(1,2, 3)
        self.page.fist_iframe(1, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
        self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                 '/html/body/div[1]/div[2]/div/div/div/div/iframe')
        self.page.driver.find_element_by_xpath('//*[@id="search_task_name"]').send_keys('123')
        self.page.text_status('/html/body/div[1]/div[2]/div/div/div/form/div/div[3]/div/div/div/div[1]/div/input[2]',
                              '//*[@id="ext-gen240"]/div')
        self.page.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div[4]/div/div/div/div[1]/input').send_keys('321')
        # self.page.messsage_arg('/html/body/div[1]/div[2]/div/div/div/form/div/div[6]/div/div/div/div[1]/div/input[2]',
        #                        '//*[@id="ext-gen253"]/li[2]/div/img[1]',
        #                        '/html/body/div[29]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        self.page.driver.find_element_by_xpath('//*[@id="ext-comp-1022"]').send_keys(self.page.get_time())
        self.page.on_link('/html/body/div[1]/div[2]/div/div/div/form/div/table/tbody/tr[2]/td[2]/em/button')
        print('测试完成')

    def second_message(self):
        self.page.return_page()
        self.page.fist_iframe(2, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
        self.page.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                 '/html/body/div[1]/div[2]/div/div[2]/div/div/iframe')
        self.page.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/input').send_keys(
            '存折信息')
        self.page.on_link(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button')
        self.page.messsage_arg('//*[@id="bankCombo"]', '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                               '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        # 查询
        self.page.driver.find_element_by_xpath('//*[@id="ext-gen83"]').click()

    def three_message(self):
        self.page.return_page()
        # self.page.first_supervise(1,3)
        self.page.fist_iframe(3, '//*[@id="mainTab_CBRC3"]/div/iframe')
        self.page.sencond_iframe('//*[@id="mainTab_CBRC3"]/div/iframe',
                                 '/html/body/div[1]/div[2]/div/div[2]/div/div/iframe')
        self.page.task_name('//*[@id="search_task_name"]', 'qwe')
        self.page.text_status('//*[@id="taskStatus"]', '/html/body/div[26]/div/div')
        self.page.task_name('//*[@id="queryKey"]', '123')
        # 报送机构
        # self.page.messsage_arg('//*[@id="ext-comp-1009"]','/html/body/div[28]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]','/html/body/div[29]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        self.page.put_time('/html/body/div[1]/div[2]/div/div/div/form/div/div[7]/div/div/div/div[1]/div/input')
        self.page.on_link('//*[@id="ext-gen53"]')
    def message_down(self):
        self.page.return_page()
        # self.page.first_supervise(1,3)
        self.page.fist_iframe(4,'//*[@id="mainTab_CBRC3"]/div/iframe')
        self.page.sencond_iframe('//*[@id="mainTab_CBRC3"]/div/iframe','/html/body/div[1]/div[2]/div/div[2]/div/div/iframe')
        self.page.messsage_arg('/html/body/div[1]/div/div/div[1]/div[2]/form/div/div[1]/div/div/div/div[1]/div/input[2]','/html/body/div[9]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]','/html/body/div[9]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        self.page.check_button('/html/body/div[1]/div/div/div[1]/div[2]/form/div/table/tbody/tr[2]/td[2]')
        self.page.check_box('/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/table/thead/tr/td[1]/div/div')
    def main(self):
        self.first_message()
        self.second_message()
        self.three_message()
        self.message_down()


if __name__ == "__main__":
    Test01 = Custom_riosk()
    Test01.main()
