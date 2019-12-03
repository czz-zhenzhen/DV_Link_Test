from DV_link_Test.main import *


class CRC_DV_link():
    """
    银保监会测试功能
    """

    def __init__(self):
        self.open_pages = TestSystem()

    def first_supervise(self, number):
        """
        传递元素节点，和节点元素序列号
        :param element_text: /html/body/div[1]/div/div[2]/ul/li[1]/div/div[2]/div/a[1]/div[2]/h3
                            /html/body/div[1]/div/div[2]/ul/li[1]/div/div[2]/div/a[?]/div[2]/h3.format(2)
        :param number:
        :return:
        """
        self.open_pages.open_page()
        self.open_pages.chioce_manage(number)
        time.sleep(2)
        ele_text = "/html/body/div[1]/div/div[2]/ul/li[1]/div/div[2]/div/a[" + str(number) + "]/div[2]/h3"

        self.open_pages.driver.find_element_by_xpath(ele_text).click()
        time.sleep(2)
        # self.open_pages.driver.find_element_by_xpath(ele_text).click()
        # 进入iframe层
        # self.open_pages.frame_html()
        # time.sleep(2)
        # 测试输入功能
        # self.open_pages.driver.find_element_by_xpath('//*[@id="search_task_name"]').send_keys('1233')

    def main(self, number):
        self.first_supervise(number)


if __name__ == "__main__":
    dvlink_crc = CRC_DV_link()
    dvlink_crc.main(1)
