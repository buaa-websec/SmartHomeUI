# -*- coding: utf-8 -*-
import shutil
import socket
import sys
import threading
import time
from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from send2hass import change_state, hass_reboot

event_log = []  # 操作日志缓存
log = []  # 生成日志缓存
s = None
position = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1200, 850)  # 预留出标题栏
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.resize(1200, 800)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowTitle("smart home UI")

        self.temp_button_list = []
        self.temp_label_list = []
        self.temp_slider_list = []
        self.light_button_list = []

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

        self.logOpenButton = QtWidgets.QToolButton(self.centralwidget)
        self.logOpenButton.setGeometry(QtCore.QRect(1000, 80, 100, 35))
        self.logOpenButton.setObjectName("logOpenButton")
        self.logOpenButton.setText("打开日志")
        self.logOpenButton.clicked.connect(self.openLogFile)

        self.logSaveButton = QtWidgets.QToolButton(self.centralwidget)
        self.logSaveButton.setGeometry(QtCore.QRect(1000, 40, 100, 35))
        self.logSaveButton.setObjectName("logSaveButton")
        self.logSaveButton.setText("保存日志")
        self.logSaveButton.clicked.connect(self.saveLogFile)

        self.logGenButton = QtWidgets.QToolButton(self.centralwidget)
        self.logGenButton.setGeometry(QtCore.QRect(1000, 200, 100, 35))
        self.logGenButton.setObjectName("logGenButton")
        self.logGenButton.setCheckable(True)
        self.logGenButton.setText("生成日志")
        self.logGenButton.clicked.connect(self.logGenerator)

        self.listenButton = QtWidgets.QToolButton(self.centralwidget)
        self.listenButton.setGeometry(QtCore.QRect(1000, 400, 100, 35))
        self.listenButton.setObjectName("listenButton")
        self.listenButton.setCheckable(True)
        self.listenButton.setText("监听模式")
        self.listenButton.clicked.connect(self.listenUDP)

        self.layoutButton = QtWidgets.QToolButton(self.centralwidget)
        self.layoutButton.setGeometry(QtCore.QRect(100, 10, 100, 35))
        self.layoutButton.setObjectName("layoutButton")
        self.layoutButton.setText("载入布局")
        self.layoutButton.clicked.connect(self.layoutSetup)

        self.deviceButton = QtWidgets.QToolButton(self.centralwidget)
        self.deviceButton.setGeometry(QtCore.QRect(300, 10, 100, 35))
        self.deviceButton.setObjectName("deviceButton")
        self.deviceButton.setText("载入设备")
        self.deviceButton.clicked.connect(self.deviceSetup)

        self.ruleButton = QtWidgets.QToolButton(self.centralwidget)
        self.ruleButton.setGeometry(QtCore.QRect(500, 10, 100, 35))
        self.ruleButton.setObjectName("ruleButton")
        self.ruleButton.setText("载入规则")
        self.ruleButton.clicked.connect(self.ruleSetup)

        if position:
            for p in position.readlines():
                obj_name, pos_x, pos_y = p.split()

                if obj_name == "background":
                    self.background = QtWidgets.QLabel(self.centralwidget)
                    self.background.setGeometry(QtCore.QRect(0, 0, 1000, 800))
                    self.background.setScaledContents(True)
                    self.background.setPixmap(QPixmap(pos_y))  # pos_y此处为路径
                    self.background.setObjectName("background")

                elif obj_name[0] == "t":  # 温度传感器三个控件组合
                    self.temp_button_list.append(
                        QtWidgets.QPushButton(self.centralwidget)
                    )
                    self.temp_button_list[-1].setGeometry(
                        QtCore.QRect(int(pos_x), int(pos_y), 50, 20)
                    )
                    self.temp_button_list[-1].setObjectName(obj_name)
                    self.temp_button_list[-1].setText(obj_name)
                    self.temp_button_list[-1].setStyleSheet(
                        "background-color: rgb(255, 255, 0);"
                    )

                    self.temp_slider_list.append(QtWidgets.QSlider(self.centralwidget))
                    self.temp_slider_list[-1].setGeometry(
                        QtCore.QRect(int(pos_x), int(pos_y) + 20, 50, 20)
                    )
                    self.temp_slider_list[-1].setObjectName(obj_name + "_slider")
                    self.temp_slider_list[-1].setOrientation(QtCore.Qt.Horizontal)
                    self.temp_slider_list[-1].setValue(20)
                    self.temp_slider_list[-1].setMaximum(40)
                    self.temp_slider_list[-1].setMinimum(0)

                    self.temp_label_list.append(QtWidgets.QLabel(self.centralwidget))
                    self.temp_label_list[-1].setGeometry(
                        QtCore.QRect(int(pos_x) + 50, int(pos_y), 50, 20)
                    )
                    self.temp_label_list[-1].setObjectName(obj_name + "_label")
                    self.temp_label_list[-1].setText(
                        str(self.temp_slider_list[-1].value())
                    )

                    self.temp_slider_list[-1].valueChanged.connect(
                        lambda: self.changeTemp(
                            self.sender(),
                            self.findChild(
                                QtWidgets.QLabel,
                                self.sender().objectName()[:-7] + "_label",
                            ),
                            self.findChild(
                                QtWidgets.QPushButton, self.sender().objectName()[:-7]
                            ),
                        )
                    )
                    self.temp_slider_list[-1].sliderReleased.connect(
                        lambda: self.temperatureChange(self.sender())
                    )

                else:  # 普通传感器按钮控件
                    self.light_button_list.append(
                        QtWidgets.QPushButton(self.centralwidget)
                    )
                    self.light_button_list[-1].setGeometry(
                        QtCore.QRect(int(pos_x), int(pos_y), 50, 20)
                    )
                    self.light_button_list[-1].setObjectName(obj_name)
                    self.light_button_list[-1].setText(obj_name)
                    self.light_button_list[-1].setCheckable(True)
                    self.light_button_list[-1].clicked.connect(
                        lambda: self.lightsClick(self.sender().objectName())
                    )

    def changeTemp(self, slider, temp_label, temp_button):
        value = slider.value()
        if value < 16:
            temp_button.setStyleSheet("background-color: rgb(65, 105 ,225);")
        elif value < 26:
            temp_button.setStyleSheet("background-color: rgb(255, 255, 0);")
        else:
            temp_button.setStyleSheet("background-color: rgb(255, 69, 0);")
        temp_label.setText(str(value))

    def openLogFile(self):
        log_file_name, _ = QFileDialog.getOpenFileName(
            self, "选取日志文件", "./", "All Files (*);;Text Files (*.txt)"
        )
        if log_file_name:
            f = open(log_file_name, "r")
            old_time = datetime.strptime(
                " 2100-01-01 00:00:0.0", " %Y-%m-%d %H:%M:%S.%f"
            )
            for line in f:
                if len(line) < 5:
                    f.close()
                    print("FINISHED!!!")
                    break

                print(line)
                tmp = line.split("\t")

                if tmp[1][0] == "T":
                    slider = self.findChild(
                        QtWidgets.QSlider, tmp[1].lower() + "_slider"
                    )
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

    def saveLogFile(self):
        save_file_name, _ = QFileDialog.getSaveFileName(
            self, "日志文件保存", "./", "All Files (*);;Text Files (*.txt)"
        )
        if save_file_name:
            f = open(save_file_name, "w")
            f.writelines(event_log)
            f.close()

    def lightsClick(self, lname):
        entity_id = "light." + lname
        button = self.findChild(QtWidgets.QPushButton, lname)
        if button.isChecked():  # 点击与check改变同时发生
            new_state = "on"
        else:
            new_state = "off"

        if self.logGenButton.isChecked():
            event_time = self.dateEdit.date().toString(
                " yyyy-MM-dd"
            ) + self.timeEdit.time().toString(" HH:mm:ss")
            log_line = (
                event_time + "\t" + lname.upper() + "\t" + new_state.upper() + "\n"
            )
            log.append(log_line)
        else:
            event_time = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
            change_state(entity_id, new_state)
            log_line = (
                event_time + "\t" + lname.upper() + "\t" + new_state.upper() + "\n"
            )
            event_log.append(log_line)

    def temperatureChange(self, slider):
        tname = slider.objectName()
        entity_id = "sensor." + tname[:-7]
        new_state = str(slider.value())

        if self.logGenButton.isChecked():
            event_time = self.dateEdit.date().toString(
                " yyyy-MM-dd"
            ) + self.timeEdit.time().toString(" HH:mm:ss")
            log_line = event_time + "\t" + tname + "\t" + new_state + "\n"
            log.append(log_line)
        else:
            event_time = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
            change_state(entity_id, new_state)
            log_line = event_time + "\t" + tname + "\t" + new_state + "\n"
            event_log.append(log_line)

    def logGenerator(self):
        if self.logGenButton.isChecked():
            self.logGenButton.setText("完成")
        else:
            self.logGenButton.setText("生成日志")
            save_file_name, _ = QFileDialog.getSaveFileName(
                self, "生成日志保存", "./", "All Files (*);;Text Files (*.txt)"
            )
            f = open(save_file_name, "w")
            f.writelines(log)
            f.close()

    def listenUDP(self):
        global s
        if self.listenButton.isChecked():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(("127.0.0.1", 5678))
            print("Bind UDP on 5678...")
            self.listenButton.setText("退出监听")
            t = threading.Thread(target=self.udpHandle)
            t.start()
        else:
            s.sendto(b"end\tend", ("127.0.0.1", 5678))
            self.listenButton.setText("监听模式")

    def udpHandle(self):
        global s
        while self.listenButton.isChecked():
            data, addr = s.recvfrom(1024)
            print(
                "Received from %s:%s------%s."
                % (addr[0], addr[1], data.decode("utf-8"))
            )
            tmp = data.decode("utf-8").split("\t")
            if tmp[0][0] == "t":
                slider = self.findChild(QtWidgets.QSlider, tmp[0].upper())
                slider.setValue(int(tmp[1]))
                QApplication.processEvents()
            else:
                button = self.findChild(QtWidgets.QPushButton, tmp[0])
                if tmp[1] == "on":
                    button.setChecked(True)
                if tmp[1] == "off":
                    button.setChecked(False)
                QApplication.processEvents()

        print("END")
        s.close()

    def layoutSetup(self):
        global position
        layout_file_name, _ = QFileDialog.getOpenFileName(
            self, "选取布局文件", "./", "All Files (*);;Text Files (*.txt)"
        )
        if layout_file_name:
            position = open(layout_file_name, "r")
            self.setupUi(self)

    def deviceSetup(self):
        device_file_name, _ = QFileDialog.getOpenFileName(
            self, "选取设备文件", "./", "All Files (*);;Text Files (*.txt)"
        )
        if device_file_name:
            shutil.copy(device_file_name, "~/.homeassistant/configuration.yaml")
            hass_reboot()

    def ruleSetup(self):
        rule_file_name, _ = QFileDialog.getOpenFileName(
            self, "选取规则文件", "./", "All Files (*);;Text Files (*.txt)"
        )
        if rule_file_name:
            shutil.copy(rule_file_name, "~/.homeassistant/automations.yaml")
            hass_reboot()


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
