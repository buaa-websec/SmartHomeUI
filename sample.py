# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from send2hass import  change_state
lights = {'l008':1, 'l001':1, 'l004':1,'l011':1}

def lightsclick(button,lname):
    entity_id = 'light.'+lname
    if lights[lname] == 1:
        button.setStyleSheet("background-color: rgb(255, 255, 255);")
        new_state='off'    
        lights[lname] = 0
    else:
        button.setStyleSheet("background-color: rgb(0, 255, 0);")
        new_state='on'    
        lights[lname] = 1
    change_state(entity_id, new_state)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -50, 1001, 871))
        self.label.setStyleSheet("image: url(:/home/sensorlayout2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 83, 50, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 83, 50, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 150, 50, 21))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 230, 50, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 290, 50, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 230, 50, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(152, 150, 50, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 290, 50, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 348, 50, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 348, 50, 20))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 410, 50, 20))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(160, 410, 50, 20))
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(240, 410, 50, 20))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(300, 410, 50, 20))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(240, 460, 50, 20))
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(321, 477, 50, 20))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(123, 502, 50, 20))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(218, 505, 50, 20))
        self.pushButton_18.setStyleSheet("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(220, 575, 50, 20))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(125, 576, 50, 20))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(125, 654, 50, 19))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(218, 653, 50, 20))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(320, 561, 50, 20))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(320, 632, 50, 20))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(320, 662, 50, 20))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(491, 97, 50, 20))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(590, 94, 50, 20))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(490, 179, 50, 21))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(590, 180, 50, 21))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(690, 180, 50, 21))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(690, 94, 50, 21))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(800, 92, 50, 21))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(800, 178, 50, 21))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(800, 266, 50, 21))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(771, 348, 50, 21))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(770, 380, 50, 21))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setGeometry(QtCore.QRect(770, 480, 50, 21))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_38.setGeometry(QtCore.QRect(770, 560, 50, 21))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setGeometry(QtCore.QRect(490, 268, 50, 21))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setGeometry(QtCore.QRect(569, 348, 50, 21))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(770, 561, 50, 21))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(670, 561, 50, 20))
        self.pushButton_42.setStyleSheet("")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(698, 267, 50, 20))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(590, 268, 50, 20))
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_45.setGeometry(QtCore.QRect(669, 306, 50, 20))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setGeometry(QtCore.QRect(563, 382, 50, 20))
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_47.setGeometry(QtCore.QRect(569, 563, 50, 20))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_48.setGeometry(QtCore.QRect(570, 480, 50, 20))
        self.pushButton_48.setStyleSheet("")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_49.setGeometry(QtCore.QRect(480, 666, 50, 20))
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_50.setGeometry(QtCore.QRect(561, 667, 50, 20))
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_51.setGeometry(QtCore.QRect(481, 584, 50, 20))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_52.setGeometry(QtCore.QRect(770, 654, 50, 20))
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_53.setGeometry(QtCore.QRect(152, 166, 50, 20))
        self.pushButton_53.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_54.setGeometry(QtCore.QRect(122, 517, 50, 20))
        self.pushButton_54.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_54.setObjectName("pushButton_54")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 180, 50, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 530, 50, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 210, 50, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 300, 50, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton_55 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_55.setGeometry(QtCore.QRect(229, 277, 50, 20))
        self.pushButton_55.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_55.setObjectName("pushButton_55")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(800, 510, 50, 20))
        self.label_6.setObjectName("label_6")
        self.pushButton_56 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_56.setGeometry(QtCore.QRect(771, 495, 50, 20))
        self.pushButton_56.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_57.setGeometry(QtCore.QRect(590, 196, 50, 20))
        self.pushButton_57.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_58.setGeometry(QtCore.QRect(540, 710, 50, 20))
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_59.setGeometry(QtCore.QRect(750, 42, 50, 20))
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_60.setGeometry(QtCore.QRect(700, 410, 50, 20))
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_61.setGeometry(QtCore.QRect(700, 384, 50, 20))
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_62 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_62.setGeometry(QtCore.QRect(230, 442, 50, 20))
        self.pushButton_62.setStyleSheet("")
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_63 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_63.setGeometry(QtCore.QRect(170, 310, 50, 20))
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_64 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_64.setGeometry(QtCore.QRect(170, 310, 50, 20))
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_65 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_65.setGeometry(QtCore.QRect(332, 648, 50, 20))
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_66.setGeometry(QtCore.QRect(820, 653, 50, 20))
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_67 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_67.setGeometry(QtCore.QRect(770, 656, 50, 20))
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_68.setGeometry(QtCore.QRect(662, 635, 50, 20))
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_69.setGeometry(QtCore.QRect(229, 247, 50, 20))
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_70.setGeometry(QtCore.QRect(376, 279, 50, 25))
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_71 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_71.setGeometry(QtCore.QRect(40, 280, 50, 25))
        self.pushButton_71.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_72.setGeometry(QtCore.QRect(730, 108, 50, 20))
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_73 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_73.setGeometry(QtCore.QRect(660, 653, 50, 25))
        self.pushButton_73.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_74 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_74.setGeometry(QtCore.QRect(514, 641, 50, 25))
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_75.setGeometry(QtCore.QRect(321, 583, 50, 25))
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_76.setGeometry(QtCore.QRect(380, 580, 50, 25))
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_77.setGeometry(QtCore.QRect(374, 678, 50, 25))
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_78.setGeometry(QtCore.QRect(320, 684, 50, 25))
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_79.setGeometry(QtCore.QRect(110, 679, 50, 25))
        self.pushButton_79.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_80.setGeometry(QtCore.QRect(391, 464, 50, 25))
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_81.setGeometry(QtCore.QRect(680, 209, 50, 20))
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_82 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_82.setGeometry(QtCore.QRect(680, 230, 50, 20))
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_83 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_83.setGeometry(QtCore.QRect(101, 399, 50, 25))
        self.pushButton_83.setObjectName("pushButton_83")
        self.pushButton_84 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_84.setGeometry(QtCore.QRect(307, 437, 50, 20))
        self.pushButton_84.setObjectName("pushButton_84")
        self.pushButton_85 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_85.setGeometry(QtCore.QRect(470, 324, 50, 20))
        self.pushButton_85.setObjectName("pushButton_85")
        self.pushButton_86 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_86.setGeometry(QtCore.QRect(488, 339, 50, 20))
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_87 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_87.setGeometry(QtCore.QRect(469, 251, 50, 20))
        self.pushButton_87.setObjectName("pushButton_87")
        self.pushButton_88 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_88.setGeometry(QtCore.QRect(766, 457, 50, 25))
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_89 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_89.setGeometry(QtCore.QRect(490, 308, 50, 20))
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_90 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_90.setGeometry(QtCore.QRect(624, 128, 100, 40))
        self.pushButton_90.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_90.setCheckable(False)
        self.pushButton_90.setChecked(False)
        self.pushButton_90.setObjectName("pushButton_90")
        self.pushButton_91 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_91.setGeometry(QtCore.QRect(620, 404, 50, 20))
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_92 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_92.setGeometry(QtCore.QRect(841, 392, 50, 30))
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_93 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_93.setGeometry(QtCore.QRect(841, 482, 50, 30))
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_94 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_94.setGeometry(QtCore.QRect(841, 525, 50, 30))
        self.pushButton_94.setObjectName("pushButton_94")
        self.pushButton_95 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_95.setGeometry(QtCore.QRect(841, 560, 50, 30))
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_96 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_96.setGeometry(QtCore.QRect(700, 458, 50, 20))
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_97 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_97.setGeometry(QtCore.QRect(692, 511, 50, 20))
        self.pushButton_97.setObjectName("pushButton_97")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(910, 130, 123, 26))
        self.timeEdit.setObjectName("timeEdit")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(900, 70, 91, 32))
        self.toolButton.setObjectName("toolButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(910, 100, 83, 26))
        self.checkBox.setObjectName("checkBox")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(900, 40, 91, 32))
        self.toolButton_2.setObjectName("toolButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.pushButton_90.clicked.connect(self.pushButton_90.show)
        self.pushButton_90.clicked.connect(lambda:lightsclick(self.pushButton_90,'l008'))
        self.pushButton_71.clicked.connect(lambda:lightsclick(self.pushButton_71,'l001'))
        self.pushButton_79.clicked.connect(lambda:lightsclick(self.pushButton_79,'l004'))
        self.pushButton_73.clicked.connect(lambda:lightsclick(self.pushButton_73,'l011'))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "smart home UI"))
        self.pushButton.setText(_translate("MainWindow", "M047"))
        self.pushButton_2.setText(_translate("MainWindow", "M048"))
        self.pushButton_3.setText(_translate("MainWindow", "M046"))
        self.pushButton_4.setText(_translate("MainWindow", "M045"))
        self.pushButton_5.setText(_translate("MainWindow", "M044"))
        self.pushButton_6.setText(_translate("MainWindow", "M050"))
        self.pushButton_7.setText(_translate("MainWindow", "M049"))
        self.pushButton_8.setText(_translate("MainWindow", "M044"))
        self.pushButton_9.setText(_translate("MainWindow", "M043"))
        self.pushButton_10.setText(_translate("MainWindow", "M042"))
        self.pushButton_11.setText(_translate("MainWindow", "M027"))
        self.pushButton_12.setText(_translate("MainWindow", "M028"))
        self.pushButton_13.setText(_translate("MainWindow", "M029"))
        self.pushButton_14.setText(_translate("MainWindow", "M037"))
        self.pushButton_15.setText(_translate("MainWindow", "M030"))
        self.pushButton_16.setText(_translate("MainWindow", "M038"))
        self.pushButton_17.setText(_translate("MainWindow", "M031"))
        self.pushButton_18.setText(_translate("MainWindow", "M036"))
        self.pushButton_19.setText(_translate("MainWindow", "M035"))
        self.pushButton_20.setText(_translate("MainWindow", "M032"))
        self.pushButton_21.setText(_translate("MainWindow", "M033"))
        self.pushButton_22.setText(_translate("MainWindow", "M034"))
        self.pushButton_23.setText(_translate("MainWindow", "M039"))
        self.pushButton_24.setText(_translate("MainWindow", "M040"))
        self.pushButton_25.setText(_translate("MainWindow", "M041"))
        self.pushButton_26.setText(_translate("MainWindow", "M004"))
        self.pushButton_27.setText(_translate("MainWindow", "M005"))
        self.pushButton_28.setText(_translate("MainWindow", "M003"))
        self.pushButton_29.setText(_translate("MainWindow", "M006"))
        self.pushButton_30.setText(_translate("MainWindow", "M010"))
        self.pushButton_31.setText(_translate("MainWindow", "M011"))
        self.pushButton_32.setText(_translate("MainWindow", "M012"))
        self.pushButton_33.setText(_translate("MainWindow", "M013"))
        self.pushButton_34.setText(_translate("MainWindow", "M014"))
        self.pushButton_35.setText(_translate("MainWindow", "M015"))
        self.pushButton_36.setText(_translate("MainWindow", "M016"))
        self.pushButton_37.setText(_translate("MainWindow", "M017"))
        self.pushButton_38.setText(_translate("MainWindow", "M018"))
        self.pushButton_39.setText(_translate("MainWindow", "M002"))
        self.pushButton_40.setText(_translate("MainWindow", "M001"))
        self.pushButton_41.setText(_translate("MainWindow", "M018"))
        self.pushButton_42.setText(_translate("MainWindow", "M019"))
        self.pushButton_43.setText(_translate("MainWindow", "M009"))
        self.pushButton_44.setText(_translate("MainWindow", "M007"))
        self.pushButton_45.setText(_translate("MainWindow", "M008"))
        self.pushButton_46.setText(_translate("MainWindow", "M023"))
        self.pushButton_47.setText(_translate("MainWindow", "M021"))
        self.pushButton_48.setText(_translate("MainWindow", "M022"))
        self.pushButton_49.setText(_translate("MainWindow", "M025"))
        self.pushButton_50.setText(_translate("MainWindow", "M024"))
        self.pushButton_51.setText(_translate("MainWindow", "M026"))
        self.pushButton_52.setText(_translate("MainWindow", "M051"))
        self.pushButton_53.setText(_translate("MainWindow", "T004"))
        self.pushButton_54.setText(_translate("MainWindow", "T003"))
        self.label_2.setText(_translate("MainWindow", "21"))
        self.label_3.setText(_translate("MainWindow", "20.5"))
        self.label_4.setText(_translate("MainWindow", "20.5"))
        self.label_5.setText(_translate("MainWindow", "20.5"))
        self.pushButton_55.setText(_translate("MainWindow", "T005"))
        self.label_6.setText(_translate("MainWindow", "20.5"))
        self.pushButton_56.setText(_translate("MainWindow", "T002"))
        self.pushButton_57.setText(_translate("MainWindow", "T001"))
        self.pushButton_58.setText(_translate("MainWindow", "D001"))
        self.pushButton_59.setText(_translate("MainWindow", "D002"))
        self.pushButton_60.setText(_translate("MainWindow", "D009"))
        self.pushButton_61.setText(_translate("MainWindow", "D008"))
        self.pushButton_62.setText(_translate("MainWindow", "D003"))
        self.pushButton_63.setText(_translate("MainWindow", "D004"))
        self.pushButton_64.setText(_translate("MainWindow", "D004"))
        self.pushButton_65.setText(_translate("MainWindow", "D006"))
        self.pushButton_66.setText(_translate("MainWindow", "D011"))
        self.pushButton_67.setText(_translate("MainWindow", "D051"))
        self.pushButton_68.setText(_translate("MainWindow", "M020"))
        self.pushButton_69.setText(_translate("MainWindow", "E002"))
        self.pushButton_70.setText(_translate("MainWindow", "L002"))
        self.pushButton_71.setText(_translate("MainWindow", "L001"))
        self.pushButton_72.setText(_translate("MainWindow", "E001"))
        self.pushButton_73.setText(_translate("MainWindow", "L011"))
        self.pushButton_74.setText(_translate("MainWindow", "L009"))
        self.pushButton_75.setText(_translate("MainWindow", "L006"))
        self.pushButton_76.setText(_translate("MainWindow", "F001"))
        self.pushButton_77.setText(_translate("MainWindow", "F002"))
        self.pushButton_78.setText(_translate("MainWindow", "L007"))
        self.pushButton_79.setText(_translate("MainWindow", "L004"))
        self.pushButton_80.setText(_translate("MainWindow", "L005"))
        self.pushButton_81.setText(_translate("MainWindow", "I008"))
        self.pushButton_82.setText(_translate("MainWindow", "I009"))
        self.pushButton_83.setText(_translate("MainWindow", "L003"))
        self.pushButton_84.setText(_translate("MainWindow", "D005"))
        self.pushButton_85.setText(_translate("MainWindow", "I011"))
        self.pushButton_86.setText(_translate("MainWindow", "I012"))
        self.pushButton_87.setText(_translate("MainWindow", "R002"))
        self.pushButton_88.setText(_translate("MainWindow", "L010"))
        self.pushButton_89.setText(_translate("MainWindow", "D003"))
        self.pushButton_90.setText(_translate("MainWindow", "L008"))
        self.pushButton_91.setText(_translate("MainWindow", "D012"))
        self.pushButton_92.setText(_translate("MainWindow", "D016"))
        self.pushButton_93.setText(_translate("MainWindow", "D007"))
        self.pushButton_94.setText(_translate("MainWindow", "D014"))
        self.pushButton_95.setText(_translate("MainWindow", "D015"))
        self.pushButton_96.setText(_translate("MainWindow", "D010"))
        self.pushButton_97.setText(_translate("MainWindow", "R001"))
        self.toolButton.setText(_translate("MainWindow", "打开日志"))
        self.checkBox.setText(_translate("MainWindow", "定时执行"))
        self.toolButton_2.setText(_translate("MainWindow", "保存日志"))
import img_rc
