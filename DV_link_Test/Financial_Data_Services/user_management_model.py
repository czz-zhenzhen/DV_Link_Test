from DV_link_Test.main import *

import random


class User_management:
    def __init__(self):
        self.user_model = TestSystem()

    def menu_tree(self, count, RESOURCE_ID, report_name):
        try:
            ls = self.user_model.driver.find_elements_by_xpath(
                '//div[@class="x-toolbar x-small-editor x-toolbar-layout-ct"]//button')
            # for x in ls:
            #     print(x.text)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, report_name, '操作输出', 0, "功能正常")
            return ls
        except Exception as e:
            S_txt = '{}__进入金融数据中台:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '进入iframe层', '操作输出', 1, S_txt)

    def add_role_detail(self, count, RESOURCE_ID, report_name):
        try:
            # 角色ID
            self.user_model.driver.find_element_by_name('role_id').send_keys('admin01')
            # 角色名
            self.user_model.driver.find_element_by_name('role_name').send_keys('管理员')
            # 角色等级
            self.user_model.driver.find_element_by_name('role_hierarchy').send_keys('3')
            # 角色描述
            self.user_model.driver.find_element_by_name('describe').send_keys('角色测试')

            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '操作输入', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入金融数据中台:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '进入iframe层', '操作输出', 1, S_txt)

    def role_ensure_add(self, count, RESOURCE_ID, report_name):
        try:
            ls = self.user_model.driver.find_elements_by_xpath(
                '//*[@class="x-panel-fbar x-small-editor x-toolbar-layout-ct"]//button')
            print(ls)
            for x in ls:
                s = x.text
                str1 = s.strip()
                print(str1)
                if str1 == "添加":
                    x.click()
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '操作输入', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入金融数据中台:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '进入iframe层', '操作输出', 1, S_txt)

    def role_ensure_canle(self, count, RESOURCE_ID, report_name):
        try:
            ls = self.user_model.driver.find_elements_by_xpath(
                '//*[@class="x-panel-fbar x-small-editor x-toolbar-layout-ct"]//button')
            for x in ls:
                s = x.text
                str1 = s.strip()
                if str1 == "取消":
                    x.click()
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '操作输入', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入金融数据中台:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '进入iframe层', '操作输出', 1, S_txt)

    def role_tree(self, count, RESOURCE_ID, report_name):
        try:
            ls = self.user_model.driver.find_elements_by_xpath(
                '//*[@id="gridPanel"]//div[@class="x-grid3-scroller"]/div/div')
            for x in ls:
                # print(x.text)
                x.click()
                return
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, report_name, '操作输出', 0, "功能正常")
            return ls
        except Exception as e:
            S_txt = '{}__进入金融数据中台:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '进入iframe层', '操作输出', 1, S_txt)

    def role_add(self, count, RESOURCE_ID, report_name):
        try:
            ls = self.menu_tree(count, RESOURCE_ID, report_name)
            for x in ls:
                if x.text == "添加(a)":
                    x.click()
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, "菜单管理_添加", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入菜单管理_添加:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '菜单管理_添加', '操作输出', 1, S_txt)

    def menu_add(self, count, RESOURCE_ID, report_name):
        try:
            ls = self.menu_tree(count, RESOURCE_ID, report_name)
            for x in ls:
                if x.text == "添加(a)":
                    x.click()
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, "菜单管理_添加", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入菜单管理_添加:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '菜单管理_添加', '操作输出', 1, S_txt)

    def menu_editor(self, count, RESOURCE_ID, report_name):
        try:
            self.user_list_detail(count, RESOURCE_ID, report_name)
            ls = self.menu_tree(count, RESOURCE_ID, report_name)
            for x in ls:
                print(x.text)
                if x.text in ["编辑(s)", "修改(e)","编辑(e)"]:
                    x.click()
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, "菜单管理_编辑", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入菜单管理_编辑:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '菜单管理_编辑', '操作输出', 1, S_txt)

    def menu_delete(self, count, RESOURCE_ID, report_name):
        try:
            self.user_list_detail(count, RESOURCE_ID, report_name)
            ls = self.menu_tree(count, RESOURCE_ID, report_name)
            for x in ls:
                if x.text in["删除(s)","删除(d)"] :
                    x.click()
                    time.sleep(2)
                    self.resources_maintain_list(count, RESOURCE_ID, report_name)

                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, "菜单管理_删除", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入菜单管理_删除:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '菜单管理_删除', '操作输出', 1, S_txt)

    def menu_resource(self, count, RESOURCE_ID, report_name):
        # 菜单资源
        try:
            ls = self.user_model.driver.find_elements_by_xpath('//*[@class="x-panel-body"]/ul/li')
            time.sleep(1)
            for x in ls:
                # print(x.text)
                time.sleep(1)
                x.click()
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, report_name, '操作输入', 0, "功能正常")
            return ls
        except Exception as e:
            S_txt = '{}__进入菜单管理_菜单资源:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '操作输入', '操作输出', 1, S_txt)

    def resources_maintain_list(self, count, RESOURCE_ID, report_name):
        # 资源维护
        try:
            ls = self.user_model.driver.find_elements_by_xpath('//*[@class="x-plain-bwrap"]//div')
            for x in ls:
                if x.text == "资源代码:":
                    self.user_model.driver.find_element_by_name('resource_id').send_keys('234')
            # 资源名称
            self.user_model.driver.find_element_by_name('resource_name').send_keys('234')
            # 节点动作
            self.user_model.driver.find_element_by_name('handler').send_keys('234')
            # 权限字符
            self.user_model.driver.find_element_by_name('permissions').send_keys('234')
            # 显示图标
            self.user_model.driver.find_element_by_name('icon').send_keys('234')
            self.user_model.cancel_button(count, RESOURCE_ID, report_name)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '进入资源维护', '操作输出', 0, "功能正常")
            return ls
        except Exception as e:
            S_txt = '{}__进入资源维护:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '进入资源维护', '操作输出', 1, S_txt)

    def user_name(self, count, RESOURCE_ID, report_name):
        try:
            self.user_model.driver.find_element_by_name('realname').send_keys('czz000')
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_用户名', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_用户名', '操作输出', 1, S_txt)

    def user_id(self, count, RESOURCE_ID, report_name):
        try:
            self.user_model.driver.find_element_by_name('username').send_keys('zt000')
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_用户名', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_用户名', '操作输出', 1, S_txt)

    def user_list_detail(self, count, RESOURCE_ID, report_name):
        try:
            ls = self.user_model.driver.find_elements_by_xpath('//*[@class="x-panel-body x-panel-body-noborder"]//div[@class="x-grid3-body"]/div')
            for x in ls:
                x.click()
                time.sleep(0.5)
                self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_用户列表', '操作输出', 0, "功能正常")
                return
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_用户列表', '操作输出', 1, S_txt)
    def create_user(self, count, RESOURCE_ID, report_name):
        try:
            ls = self.user_model.driver.find_elements_by_xpath('//*[@class="x-window-body x-window-body-noborder"]//div')
            print(ls)
            for x in ls:
                print(x.text)
                if x.text=="用户ID*:":
                    x.click()
                    self.user_model.driver.find_element_by_xpath('//*[@id="add_user_id"]').send_keys('czz000')
                    self.user_model.driver.find_element_by_xpath('//*[@id="add_user_name"]').send_keys('czz000')
                    self.user_model.driver.find_element_by_name('job_num').send_keys('00001')
                    self.user_model.driver.find_element_by_name('phonenumber').send_keys('15123412345')

            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_用户列表', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_用户列表', '操作输出', 1, S_txt)

    def create_user_message(self, count, RESOURCE_ID, report_name):
        # 创建用户_归属机构
        try:
            ls = self.user_model.driver.find_elements_by_xpath(
                '//*[@class="x-window-body x-window-body-noborder"]//div')
            for x in ls:
                print(x.text)
                if x.text == "归属机构*:":
                    x.click()
                    time.sleep(1)
                    li = self.user_model.driver.find_elements_by_xpath('//*[@class="x-menu x-menu-floating x-layer"]//li')
                    lens = len(li)
                    num = random.randint(1,lens)
                    li[num].click()
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_创建用户_归属机构', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_创建用户_归属机构', '操作输出', 1, S_txt)
    def user_sex(self,count, RESOURCE_ID, report_name):
        try:
            ls = self.user_model.driver.find_elements_by_xpath(
                '//*[@class="x-window-body x-window-body-noborder"]//div')
            for x in ls:
                print(x.text)
                if x.text == "性别*:":
                    x.click()
                    ls01 = self.user_model.driver.find_elements_by_xpath('//*[@class="x-combo-list-inner"]/div')
                    for y in ls01:
                        if y.text == "男":
                            y.click()

                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_创建用户_性别', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_创建用户_性别', '操作输出', 1, S_txt)
    def user_education(self,count, RESOURCE_ID, report_name):
        # 用户学历
        try:
            ls = self.user_model.driver.find_elements_by_xpath(
                '//*[@class="x-window-body x-window-body-noborder"]//div')
            for x in ls:
                print(x.text)
                if x.text == "学历*:":
                    x.click()
                    ls01 = self.user_model.driver.find_elements_by_xpath('//*[@class="x-combo-list-inner"]/div')
                    for y in ls01:
                        if y.text == "本科":
                            y.click()
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_创建用户_学历', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_创建用户_学历', '操作输出', 1, S_txt)
    def user_grade(self,count, RESOURCE_ID, report_name):
        # 用户职称
        try:
            ls = self.user_model.driver.find_elements_by_xpath(
                '//*[@class="x-window-body x-window-body-noborder"]//div')
            for x in ls:
                print(x.text)
                if x.text == "职称*:":
                    x.click()
                    ls01 = self.user_model.driver.find_elements_by_xpath('//*[@class="x-combo-list-inner"]/div')
                    for y in ls01:
                        if y.text == "高级":
                            y.click()
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_创建用户_职称', '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '用户管理_创建用户_职称', '操作输出', 1, S_txt)


    def reset_Password(self,count, RESOURCE_ID, report_name):
        # 重置密码
        try:
            self.user_list_detail(count, RESOURCE_ID, report_name)
            ls = self.menu_tree(count, RESOURCE_ID, report_name)
            for x in ls:
                if x.text =="重置密码(r)" :
                    x.click()
                    time.sleep(2)
                    self.user_model.delete_task_is_and_false(count, RESOURCE_ID, report_name)
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, "菜单管理_重置密码", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入菜单管理_重置密码:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '菜单管理_重置密码', '操作输出', 1, S_txt)
    def get_user_info(self,count, RESOURCE_ID, report_name):
        try:
            self.user_list_detail(count, RESOURCE_ID, report_name)
            ls = self.menu_tree(count, RESOURCE_ID, report_name)
            for x in ls:
                if x.text =="导出用户信息" :
                    x.click()
                    time.sleep(1)
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, "菜单管理_导出用户信息", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入菜单管理_导出用户信息:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '菜单管理_导出用户信息', '操作输出', 1, S_txt)
    def get_user_info_model(self,count, RESOURCE_ID, report_name):
        try:
            self.user_list_detail(count, RESOURCE_ID, report_name)
            ls = self.menu_tree(count, RESOURCE_ID, report_name)
            for x in ls:
                if x.text =="导出用户模板" :
                    x.click()
                    time.sleep(1)
                    self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, "菜单管理_导出用户模板", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入菜单管理_导出用户模板:'.format(report_name) + str(e)
            self.user_model.write_error_excel(S_txt)
            self.user_model.write_error_mysql(count, RESOURCE_ID, report_name, '菜单管理_导出用户模板', '操作输出', 1, S_txt)