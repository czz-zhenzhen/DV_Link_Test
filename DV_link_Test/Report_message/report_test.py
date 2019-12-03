from DV_link_Test.main import *


class Test_Report:
    def __init__(self):
        self.test = TestSystem()

    def chioce_report(self, number):
        time.sleep(2)
        self.test.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/ul/li[2]/div/div[2]/div/a[%s]/div[2]/h3' % str(number)).click()
        time.sleep(2)

    def test_report(self):
        self.test.open_page()

    def start_test(self, number):
        self.test.chioce_manage(2)
        self.chioce_report(number)
        try:
            self.test.fist_iframe(1, '/html/body/div[2]/div/div[2]/div[2]/div/div/iframe')
            self.test.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe',
                                     '/html/body/div[1]/div[2]/div/div/div/div/iframe')
        except Exception as e:
            S_txt = '敏捷报表平台__进入iframe层:' + str(e)
            self.test.write_error_excel(S_txt)
        try:
            self.test.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/input').send_keys(
                '123')
        except Exception as e:
            S_txt = '敏捷报表平台__输入框:' + str(e)
            self.test.write_error_excel(S_txt)

        self.test.check_button(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button')
        try:
            self.test.messsage_arg(
                '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/form/div/div/div/div/div[1]/div/div/div/div[1]/div/input[2]',
                '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/div/img[1]',
                '/html/body/div[14]/ul/li/div/div/div/ul/li/ul/li[2]/ul/li')
        except Exception as e:
            S_txt = '敏捷报表平台__机构管理:' + str(e)
            self.test.write_error_excel(S_txt)
        try:
            self.test.check_button(
                '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/form/div/div/div/div/table[1]/tbody/tr[2]/td[2]/em/button')
        except Exception as e:
            S_txt = '敏捷报表平台__查询按钮:' + str(e)
            self.test.write_error_excel(S_txt)
        self.test.return_page()
        try:
            self.test.sencond_iframe('/html/body/div[2]/div/div[2]/div[2]/div/div/iframe','/html/body/div[1]/div[2]/div/div/div/div/iframe')
            self.test.driver.find_element_by_xpath('/html/body/div[15]/a').click()
        except Exception as e:
            S_txt = '敏捷报表平台__返回确认按钮:' + str(e)
            self.test.write_error_excel(S_txt)
    def main_report(self):
        self.test_report()
        # self.test.return_page()
        lens = self.test.driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/ul/li[2]/div/div[2]/div/a')
        for x in range(1, len(lens)+1):
            self.test.driver.refresh()
            self.start_test(x)
            time.sleep(4)
if __name__ == "__main__":
    Test = Test_Report()
    Test.main_report()
