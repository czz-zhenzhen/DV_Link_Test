from DV_link_Test.Financial_Data_Services.user_management_model import *


class User_managements:
    def __init__(self):
        self.users = User_management()

    def menu_management_test(self):
        count = 1
        RESOURCE_ID_main = "userServices"
        RESOURCE_ID = "userServices_01"
        RESOURCE = "platform"
        report_name = "菜单管理"
        try:
            self.users.user_model.open_page()
            # 菜单管理
            self.users.user_model.first_supervise(4, 2, 1)
            try:
                self.users.user_model.driver.switch_to.frame(
                    self.users.user_model.driver.find_element_by_xpath('//*[@id="mainTab_userServices_01"]/div/iframe'))
                self.users.user_model.write_error_mysql(count, RESOURCE_ID_main, report_name, "菜单管理", '操作输出', 0, "功能正常")
            except Exception as e:
                S_txt = '{}__进入菜单管理:'.format(report_name) + str(e)
                self.users.user_model.write_error_excel(S_txt)
                self.users.user_model.write_error_mysql(count, RESOURCE_ID_main, report_name, '菜单管理', '操作输出', 1,S_txt)
            self.users.menu_tree(count, RESOURCE_ID, report_name)
            self.users.menu_resource(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.users.menu_add(count, RESOURCE_ID, report_name)
            self.users.resources_maintain_list(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.users.menu_delete(count, RESOURCE_ID, report_name)
            time.sleep(1)
            self.users.user_model.delete_task_is_and_false(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.users.menu_editor(count, RESOURCE_ID, report_name)
            self.users.resources_maintain_list(count, RESOURCE_ID, report_name)
            self.users.user_model.write_error_mysql(count, RESOURCE, report_name, "用户服务_菜单管理", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户服务:'.format(report_name) + str(e)
            self.users.user_model.write_error_excel(S_txt)
            self.users.user_model.write_error_mysql(count, RESOURCE, report_name, '用户服务_菜单管理', '操作输出', 1,S_txt)
        count += 1
    def role_management_test(self):
        count = 1
        RESOURCE_ID_main = "userServices"
        RESOURCE_ID = "userServices_02"
        RESOURCE = "platform"
        report_name = "角色管理"
        try:
            # self.users.user_model.open_page()
            # 角色管理
            self.users.user_model.first_supervise(4, 2, 2)
            try:
                self.users.user_model.driver.switch_to.frame(
                    self.users.user_model.driver.find_element_by_xpath('//*[@id="mainTab_userServices_02"]/div/iframe'))
                self.users.user_model.write_error_mysql(count, RESOURCE_ID_main, report_name, "角色管理", '操作输出', 0, "功能正常")
            except Exception as e:
                S_txt = '{}__进入角色管理:'.format(report_name) + str(e)
                self.users.user_model.write_error_excel(S_txt)
                self.users.user_model.write_error_mysql(count, RESOURCE_ID_main, report_name, '角色管理', '操作输出', 1,S_txt)
            self.users.role_tree(count, RESOURCE_ID, report_name)
            self.users.menu_add(count, RESOURCE_ID, report_name)
            self.users.add_role_detail(count, RESOURCE_ID, report_name)
            # self.users.role_ensure_add(count, RESOURCE_ID, report_name)
            self.users.role_ensure_canle(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.users.menu_editor(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.users.role_ensure_add(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.users.menu_delete(count, RESOURCE_ID, report_name)
            time.sleep(1)
            self.users.user_model.delete_task_is_and_false(count, RESOURCE_ID, report_name)
            self.users.user_model.write_error_mysql(count, RESOURCE, report_name, "用户服务_角色管理", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户服务:'.format(report_name) + str(e)
            self.users.user_model.write_error_excel(S_txt)
            self.users.user_model.write_error_mysql(count, RESOURCE, report_name, '用户服务_角色管理', '操作输出', 1,S_txt)
        count += 1
    def user_management_test(self):
        count = 1
        RESOURCE_ID_main = "userServices"
        RESOURCE_ID = "userServices_03"
        RESOURCE = "platform"
        report_name = "用户管理"
        try:
            # self.users.user_model.open_page()
            # 角色管理
            self.users.user_model.first_supervise(4, 2, 3)
            try:
                self.users.user_model.driver.switch_to.frame(
                    self.users.user_model.driver.find_element_by_xpath('//*[@id="mainTab_userServices_03"]/div/iframe'))
                self.users.user_model.write_error_mysql(count, RESOURCE_ID_main, report_name, "用户管理", '操作输出', 0, "功能正常")
            except Exception as e:
                S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
                self.users.user_model.write_error_excel(S_txt)
                self.users.user_model.write_error_mysql(count, RESOURCE_ID_main, report_name, '用户管理', '操作输出', 1, S_txt)
            self.users.user_model.get_city_name(count, RESOURCE_ID)
            # 用户ID
            # self.users.user_id(count, RESOURCE_ID_main, report_name)
            # 用户用户名
            self.users.user_name(count, RESOURCE_ID_main, report_name)
            # self.users.user_model.all_check_button(count, RESOURCE_ID, report_name)
            # 用户列表
            # self.users.user_list_detail(count, RESOURCE_ID, report_name)
            self.users.menu_add(count, RESOURCE_ID_main, report_name)
            self.users.create_user(count, RESOURCE_ID_main, report_name)
            self.users.create_user_message(count, RESOURCE_ID_main, report_name)
            time.sleep(2)
            # self.users.user_model.get_city_name(count, RESOURCE_ID_main)
            self.users.user_sex(count, RESOURCE_ID_main, report_name)
            self.users.user_education(count, RESOURCE_ID_main, report_name)
            self.users.user_grade(count, RESOURCE_ID_main, report_name)
            self.users.role_ensure_add(count, RESOURCE_ID_main, report_name)
            time.sleep(2)
            self.users.menu_editor(count, RESOURCE_ID_main, report_name)
            self.users.role_ensure_canle(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.users.menu_delete(count, RESOURCE_ID, report_name)
            self.users.user_model.delete_task_is_and_false(count, RESOURCE_ID, report_name)
            time.sleep(2)
            self.users.reset_Password(count, RESOURCE_ID, report_name)
            time.sleep(1)
            self.users.get_user_info(count, RESOURCE_ID, report_name)
            self.users.get_user_info_model(count, RESOURCE_ID, report_name)
            self.users.user_model.write_error_mysql(count, RESOURCE, report_name, "用户服务_用户管理", '操作输出', 0, "功能正常")
        except Exception as e:
            S_txt = '{}__进入用户管理:'.format(report_name) + str(e)
            self.users.user_model.write_error_excel(S_txt)
            self.users.user_model.write_error_mysql(count, RESOURCE, report_name, '用户服务_用户管理', '操作输出', 1, S_txt)
        count += 1



    def main(self):
        self.menu_management_test()
        self.users.user_model.driver.refresh()
        time.sleep(2)
        self.role_management_test()
        self.users.user_model.driver.refresh()
        time.sleep(2)
        self.user_management_test()


if __name__ == "__main__":
    users_01 = User_managements()
    users_01.main()