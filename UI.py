# -*- coding: utf-8 -*-

import socket
import sys
import threading
import time
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

import img_rc
from send2hass import change_state

event_log = []  # 操作日志缓存
log = []  # 生成日志缓存


class Ui_MainWindow(object):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):

        MainWindow.resize(1200, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(10, -50, 1001, 871))
        self.background.setStyleSheet("image: url(:/home/sensorlayout2.png);")
        self.background.setObjectName("background")

        self.temp_button_list = []
        self.temp_label_list = []
        self.temp_slider_list = []
        self.light_button_list = []

        position = open("position.txt", "r")
        for p in position.readlines():
            obj_name, pos_x, pos_y = p.split()
            if obj_name[0] == 't':  # 温度传感器三个控件组合
                self.temp_button_list.append(
                    QtWidgets.QPushButton(self.centralwidget))
                self.temp_button_list[-1].setGeometry(
                    QtCore.QRect(int(pos_x), int(pos_y), 50, 20))
                self.temp_button_list[-1].setObjectName(obj_name)
                self.temp_button_list[-1].setText(obj_name)
                self.temp_button_list[-1].setStyleSheet(
                    "background-color: rgb(255, 255, 0);")

                self.temp_slider_list.append(
                    QtWidgets.QSlider(self.centralwidget))
                self.temp_slider_list[-1].setGeometry(
                    QtCore.QRect(int(pos_x), int(pos_y)+20, 50, 20))
                self.temp_slider_list[-1].setObjectName(obj_name+'_slider')
                self.temp_slider_list[-1].setOrientation(QtCore.Qt.Horizontal)
                self.temp_slider_list[-1].setValue(20)
                self.temp_slider_list[-1].setMaximum(40)
                self.temp_slider_list[-1].setMinimum(0)

                self.temp_label_list.append(
                    QtWidgets.QLabel(self.centralwidget))
                self.temp_label_list[-1].setGeometry(
                    QtCore.QRect(int(pos_x)+50, int(pos_y), 50, 20))
                self.temp_label_list[-1].setObjectName(obj_name+'_label')
                self.temp_label_list[-1].setText(
                    str(self.temp_slider_list[-1].value()))

                self.temp_slider_list[-1].valueChanged.connect(
                    lambda: self.changeTemp(
                        self.sender(),
                        self.findChild(
                            QtWidgets.QLabel, self.sender().objectName()[:-7]+"_label"),
                        self.findChild(QtWidgets.QPushButton,
                                       self.sender().objectName()[:-7])
                    )
                )
                self.temp_slider_list[-1].sliderReleased.connect(
                    lambda: self.temperatureChange(self.sender()))

            else:  # 普通传感器按钮控件
                self.light_button_list.append(
                    QtWidgets.QPushButton(self.centralwidget))
                self.light_button_list[-1].setGeometry(
                    QtCore.QRect(int(pos_x), int(pos_y), 50, 20))
                self.light_button_list[-1].setObjectName(obj_name)
                self.light_button_list[-1].setText(obj_name)
                self.light_button_list[-1].setCheckable(True)
                self.light_button_list[-1].clicked.connect(
                    lambda: self.lightsclick(self.sender().objectName())
                )

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(1000, 250, 180, 30))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(1000, 300, 180, 30))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setDisplayFormat("HH:mm:ss")
        self.timeEdit.setTime(QtCore.QTime.currentTime())

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(1000, 80, 100, 35))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setText("打开日志")

        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(1000, 40, 100, 35))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.setText("保存日志")

        self.logButton = QtWidgets.QToolButton(self.centralwidget)
        self.logButton.setGeometry(QtCore.QRect(1000, 200, 100, 35))
        self.logButton.setObjectName("logButton")
        self.logButton.setCheckable(True)
        self.logButton.setText("生成日志")

        self.listenButton = QtWidgets.QToolButton(self.centralwidget)
        self.listenButton.setGeometry(QtCore.QRect(1000, 400, 100, 35))
        self.listenButton.setObjectName("listenButton")
        self.listenButton.setCheckable(True)
        self.listenButton.setText("监听模式")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolButton.clicked.connect(self.open_f)
        self.toolButton_2.clicked.connect(self.save_f)
        self.logButton.clicked.connect(self.logGenerator)
        self.listenButton.clicked.connect(self.listenUDP)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowTitle("smart home UI")

    def changeTemp(self, slider, temp_label, temp_button):
        value = slider.value()
        if value < 16:
            temp_button.setStyleSheet("background-color: rgb(65, 105 ,225);")
        elif value < 26:
            temp_button.setStyleSheet("background-color: rgb(255, 255, 0);")
        else:
            temp_button.setStyleSheet("background-color: rgb(255, 69, 0);")
        temp_label.setText(str(value))

    def open_f(self):
        fileName1, _ = QFileDialog.getOpenFileName(
            self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        # print(fileName1,filetype)
        f = open(fileName1, 'r')
        old_time = datetime.strptime(
            ' 2100-01-01 00:00:0.0', " %Y-%m-%d %H:%M:%S.%f")
        for line in f:
            if len(line) < 5:
                f.close()
                print('FINISHED!!!')
                break

            print(line)
            tmp = line.split('\t')

            if tmp[1][0] == 'T':
                slider = self.findChild(QtWidgets.QSlider, tmp[1])
                slider.setValue(int(tmp[2]))
                QApplication.processEvents()
            else:
                button = self.findChild(QtWidgets.QPushButton, tmp[1].lower())
                button.click()
                QApplication.processEvents()

            new_time = datetime.strptime(tmp[0], " %Y-%m-%d %H:%M:%S.%f")
            if new_time >= old_time:
                t = new_time - old_time
                t = t.seconds
            else:
                t = 0
            old_time = new_time
            time.sleep(t)

    def save_f(self):
        fileName2, _ = QFileDialog.getSaveFileName(
            self, "文件保存", "./", "All Files (*);;Text Files (*.txt)")
        f = open(fileName2, 'w')
        f.writelines(event_log)
        f.close()

    def lightsclick(self, lname):
        entity_id = 'light.'+lname
        button = self.findChild(QtWidgets.QPushButton, lname)
        if button.isChecked():  # 点击与check改变同时发生
            new_state = 'on'
        else:
            new_state = 'off'

        if self.logButton.isChecked():
            event_time = self.dateEdit.date().toString(" yyyy-MM-dd") + \
                self.timeEdit.time().toString(" HH:mm:ss")
            log_line = event_time+'\t' + lname.upper()+'\t'+new_state.upper()+'\n'
            log.append(log_line)
        else:
            event_time = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
            change_state(entity_id, new_state)
            log_line = event_time+'\t' + lname.upper()+'\t'+new_state.upper()+'\n'
            event_log.append(log_line)

    def temperatureChange(self, slider):
        tname = slider.objectName()
        entity_id = 'sensor.'+tname[:-7]
        new_state = str(slider.value())

        if self.logButton.isChecked():
            event_time = self.dateEdit.date().toString(" yyyy-MM-dd") + \
                self.timeEdit.time().toString(" HH:mm:ss")
            log_line = event_time+'\t' + tname+'\t'+new_state+'\n'
            log.append(log_line)
        else:
            event_time = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
            change_state(entity_id, new_state)
            log_line = event_time+'\t' + tname+'\t'+new_state+'\n'
            event_log.append(log_line)

    def logGenerator(self):
        if self.logButton.isChecked():
            self.logButton.setText("完成")
        else:
            self.logButton.setText("生成日志")
            fileName2, _ = QFileDialog.getSaveFileName(
                self, "文件保存", "./", "All Files (*);;Text Files (*.txt)")
            f = open(fileName2, 'w')
            f.writelines(log)
            f.close()

    def listenUDP(self):
        global s
        if self.listenButton.isChecked():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(('127.0.0.1', 5678))
            print('Bind UDP on 5678...')
            self.listenButton.setText("退出监听")
            t = threading.Thread(target=self.udphandle)
            t.start()
        else:
            s.sendto(b'end\tend', ('127.0.0.1', 5678))
            self.listenButton.setText("监听模式")

    def udphandle(self):
        global s
        while self.listenButton.isChecked():
            data, addr = s.recvfrom(1024)
            print('Received from %s:%s------%s.' %
                  (addr[0], addr[1], data.decode('utf-8')))
            tmp = data.decode('utf-8').split('\t')
            if tmp[0][0] == 't':
                slider = self.findChild(QtWidgets.QSlider, tmp[0].upper())
                slider.setValue(int(tmp[1]))
                QApplication.processEvents()
            else:
                button = self.findChild(QtWidgets.QPushButton, tmp[0])
                if tmp[1] == 'on':
                    button.setChecked(True)
                if tmp[1] == 'off':
                    button.setChecked(False)
                QApplication.processEvents()

        print("END")
        s.close()


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
