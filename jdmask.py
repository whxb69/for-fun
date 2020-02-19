from selenium import webdriver
import time
from jdui import *
import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import PyQt5.sip
import traceback
import _thread

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()


class Mainwindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self._login)
        self.pushButton.clicked.connect(self._buy)


    def login(self, no):
        phone = self.line_Edit.text()
        pword = self.line_Edit_2.text()
        print(phone, pword)

        url = 'https://item.jd.com/100011385146.html'
        # url = 'https://item.jd.com/100004521157.html'  #测试

        driver = eval('driver%d' % no)
        driver.get(url)

        login = driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]')
        login.click()
        time.sleep(2)
        tab = driver.find_element_by_class_name('login-tab-r')
        tab.click()
        time.sleep(1)

        name = driver.find_element_by_xpath('//*[@id="loginname"]')
        name.send_keys(phone)
        pwd = driver.find_element_by_xpath('//*[@id="nloginpwd"]')
        pwd.send_keys(pword)
        driver.find_element_by_xpath('//*[@id="formlogin"]/div[5]/div').click()

    def _buy(self):
        # flag = self.lineEdit_4.text()
        _thread.start_new_thread( self.buy1, () )
        _thread.start_new_thread( self.buy2, () )
        _thread.start_new_thread( self.buy3, () )
    
    def _login(self):
        _thread.start_new_thread( self.login, (1,) )
        _thread.start_new_thread( self.login, (2,) )
        _thread.start_new_thread( self.login, (3,) )
        # if flag == '1':
        #     self.buy1()
        # elif flag == '2':
        #     self.buy2()            
        # elif flag == '3':
        #     self.buy3()
            
    def buy1(self):
        try:      
            print('方法一启动!')
            self.pushButton.setEnabled(False)
            ltm = time.localtime()
            th = ltm.tm_hour
            tmin = tm = ltm.tm_min
            t = ('%d:%d:%d' % (th, tm, ltm.tm_sec))
            target = '19:59:58'
            print('%s开抢!' % target)
            while t != target:
                ltm = time.localtime()
                th = ltm.tm_hour
                tm = ltm.tm_min
                t = ('%d:%d:%d' % (th, tm, ltm.tm_sec)) 
                if tm > tmin:
                    print('%d点%d' % (th, tm))
                    tmin = tm
                QApplication.processEvents()

            driver1.find_element_by_link_text('立即抢购').click()
            # driver.find_element_by_link_text('加入购物车').click()  #测试
            driver1.find_element_by_link_text('去购物车结算').click()
            driver1.find_element_by_link_text('去结算').click()
            driver1.find_element_by_link_text('提交订单').click()
        except:
            print(traceback.print_exc())
            self.pushButton.setEnabled(True)
            print('重新开始')
            url = 'https://item.jd.com/100011385146.html'
            driver1.get(url)
            return self.buy1()
    
    def buy2(self):
        try:      
            print('方法二启动!')
            self.pushButton.setEnabled(False)
            ltm = time.localtime()
            tmin = tm = ltm.tm_min
            btn = driver2.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[14]/a[1]')
            while btn.get_attribute('href') == 'https://item.jd.com/100011385146.html#none':
                ltm = time.localtime()
                tm = ltm.tm_min
                th = ltm.tm_hour
                if tm > tmin:
                    print('%d点%d' % (th, tm))
                    tmin = tm
                btn = driver2.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[14]/a[1]')   
                QApplication.processEvents()

            btn.click()
            # driver.find_element_by_link_text('加入购物车').click()  #测试
            driver2.find_element_by_link_text('去购物车结算').click()
            driver2.find_element_by_link_text('去结算').click()
            driver2.find_element_by_link_text('提交订单').click()
        except:
            print(traceback.print_exc())
            self.pushButton.setEnabled(True)
            print('重新开始')
            url = 'https://item.jd.com/100011385146.html'
            driver2.get(url)
            return self.buy2()
    
    def buy3(self):
        try:      
            print('方法三启动!')
            self.pushButton.setEnabled(False)
            ltm = time.localtime()
            tmin = tm = ltm.tm_min
            btn = driver3.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[14]/a[1]')
            while 'btn-disable' in btn.get_attribute('class'):
                ltm = time.localtime()
                tm = ltm.tm_min
                th = ltm.tm_hour
                if tm > tmin:
                    print('%d点%d' % (th, tm))
                    tmin = tm
                btn = driver3.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[14]/a[1]')   
                QApplication.processEvents()

            btn.click()
            # driver.find_element_by_link_text('加入购物车').click()  #测试
            driver3.find_element_by_link_text('去购物车结算').click()
            driver3.find_element_by_link_text('去结算').click()
            driver3.find_element_by_link_text('提交订单').click()
        except:
            print(traceback.print_exc())
            self.pushButton.setEnabled(True)
            print('重新开始')
            url = 'https://item.jd.com/100011385146.html'
            driver3.get(url)
            return self.buy3()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    sys.exit(app.exec_())
