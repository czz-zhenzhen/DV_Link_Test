from DV_link_Test.Financial_Data_Services.user_management import *
from DV_link_Test.Supervisory_Report_SyS.Area_manage import *


class Begin_start_Test:
    def __init__(self):
        self.begin_start = User_managements()
        self.begin_start02 = Custom_riosk()


    def main(self):
        self.begin_start02.main_Area()
        self.begin_start.main()


if __name__ =='__main__':
    test = Begin_start_Test()
    test.main()