
def changeTemp(slider, temp_label, temp_button):
    value = slider.value()
    if value < 16:
        temp_button.setStyleSheet("background-color: rgb(65, 105 ,225);")
    elif value < 26:
        temp_button.setStyleSheet("background-color: rgb(255, 255, 0);")
    else:
        temp_button.setStyleSheet("background-color: rgb(255, 69, 0);")
    temp_label.setText(str(value))

def openLogFile(self):
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

def saveLogFile(self):
    fileName2, _ = QFileDialog.getSaveFileName(
        self, "文件保存", "./", "All Files (*);;Text Files (*.txt)")
    f = open(fileName2, 'w')
    f.writelines(event_log)
    f.close()

def lightsClick(self, lname):
    entity_id = 'light.'+lname
    button = self.findChild(QtWidgets.QPushButton, lname)
    if button.isChecked():  # 点击与check改变同时发生
        new_state = 'on'
    else:
        new_state = 'off'

    if self.logGenButton.isChecked():
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

    if self.logGenButton.isChecked():
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
    if self.logGenButton.isChecked():
        self.logGenButton.setText("完成")
    else:
        self.logGenButton.setText("生成日志")
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
        t = threading.Thread(target=self.udpHandle)
        t.start()
    else:
        s.sendto(b'end\tend', ('127.0.0.1', 5678))
        self.listenButton.setText("监听模式")

def udpHandle(self):
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

def layoutSetUp():

def 

