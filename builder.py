import sys

from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QInputDialog,
    QPushButton,
    QWidget,
    QLabel,
)


class DraggableButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.btnPosition = [0, 0]
        self.abs_pos = QPoint(0, 0)
        self.setGeometry(QRect(300, 50, 50, 20))

    def mousePressEvent(self, e):
        self.btnPosition[0] = e.x()
        self.btnPosition[1] = e.y()

    def mouseMoveEvent(self, e):
        x = e.x() - self.btnPosition[0]
        y = e.y() - self.btnPosition[1]
        self.abs_pos = self.mapToParent(QPoint(x, y))  # 需要maptoparent得到绝对位置
        self.move(self.abs_pos)

    def mouseReleaseEvent(self, e):
        x = self.abs_pos.x()
        y = self.abs_pos.y()
        print(self.objectName(), "控件位置", x, y)


class builder_ui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.btn_list = []

    def initUI(self):
        self.setWindowTitle("Layout Generator")
        self.resize(1200, 800)

        self.devices = QWidget(self)
        self.devices.resize(1000, 800)

        self.background = QLabel(self.devices)
        self.background.setGeometry(QRect(0, 0, 1000, 800))
        self.background.setScaledContents(True)

        self.set_bg_btn = QPushButton(self)
        self.set_bg_btn.setGeometry(QRect(100, 10, 100, 35))
        self.set_bg_btn.setObjectName("set_bg_btn")
        self.set_bg_btn.setText("设置背景")
        self.set_bg_btn.clicked.connect(self.backgroundSet)

        self.add_device_btn = QPushButton(self)
        self.add_device_btn.setGeometry(QRect(300, 10, 100, 35))
        self.add_device_btn.setObjectName("add_device_btn")
        self.add_device_btn.setText("添加设备")
        self.add_device_btn.clicked.connect(self.deviceAdd)

        self.layout_save_btn = QPushButton(self)
        self.layout_save_btn.setGeometry(QRect(500, 10, 100, 35))
        self.layout_save_btn.setObjectName("layout_save_btn")
        self.layout_save_btn.setText("保存布局")
        self.layout_save_btn.clicked.connect(self.layoutSave)

    def backgroundSet(self):

        self.background_file_name, _ = QFileDialog.getOpenFileName(
            self, "选取布局文件", "./", "All Files (*);;Image Files (*.jpg *.png)"
        )
        self.background.setPixmap(QPixmap(self.background_file_name))

    def deviceAdd(self):
        device_name, ok = QInputDialog.getText(self, "设备选项", "设备名称:")

        if device_name[0] in ["t", "l", "m", "d", "r", "i", "f", "e"]:
            print(device_name)
            self.btn_list.append(DraggableButton(device_name, self.devices))
            self.btn_list[-1].setObjectName(device_name)
            self.btn_list[-1].show()

        # elif device_name[0] == "t":

        else:
            print("无效命名")

    def layoutSave(self):
        layout = []
        for btn in self.btn_list:
            layout.append(
                btn.objectName() + "\t" + str(btn.x()) + "\t" + str(btn.y()) + "\n"
            )
        save_file_name, _ = QFileDialog.getSaveFileName(
            self, "设备文件保存", "./", "All Files (*);;Text Files (*.txt)"
        )
        if save_file_name:
            f = open(save_file_name, "w")
            f.write(
                "background" + "\tpath\t" + self.background_file_name + "\n"
            )  # 补全三个值，格式对应
            f.writelines(layout)
            f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    builder = builder_ui()
    builder.show()
    app.exec_()
