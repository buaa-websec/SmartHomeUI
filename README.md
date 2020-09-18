# SmartHomeUI

A GUI for showing the data from Home Assistant and controlling virtual devices or sending event log. 

![flow](IMG/flow.png)

* Use builder.py to generate the layout file.

![builder](IMG/builder.png)  

* Run UI.py to show the window.Please load home layout file (e.g. position.txt) first, then you can see the devices.

![UI](IMG/UI.png)

* Tested based on Home Assistant (version: 0.103.4)

* 监听功能需要在 core.py 的575行处添加发送状态的程序

* Log file example:

![log](IMG/log.png)

# Virtual Reality Platform
![design](IMG/design.png)
