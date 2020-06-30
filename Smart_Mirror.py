from PyQt5 import QtCore, QtGui, QtWidgets
import forecastio
import yapi
import feedparser
import datetime 
from time import sleep
import threading
import tkinter as tk
import requests
import json
import cv2
from PyQt5.QtGui import QPixmap, QImage   
import pafy


class Ui_MainWindow(object):
    hello_world = 0
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    News_url = "http://fs.jtbc.joins.com//RSS/newsflash.xml"
    start_or_stop=False
    start=True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        MainWindow.setPalette(palette)
        MainWindow.showFullScreen()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #clock 이라는 이름으로 label 생성
        self.clock = QtWidgets.QLabel(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(200,300,100,50))
        self.clock.setObjectName("clock")

        #time 이라는 이름으로 label 생성 [(오전/오후)시/분]
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(170,80,800,60))
        self.time.setObjectName("time")
        self.time.setFont(QtGui.QFont("맑은 고딕",50)) 

        #date 이라는 이름으로 label 생성 [년/월/일]
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(180, 15, 300, 50))
        self.date.setObjectName("date")
        self.date.setFont(QtGui.QFont("맑은 고딕",20))
        
        #news label 생성
        self.news1 = QtWidgets.QLabel(self.centralwidget)
        self.news1.setGeometry(QtCore.QRect(self.width-470,self.height-350,470,50))
        self.news1.setObjectName("news1")
        self.news1.setFont(QtGui.QFont("맑은 고딕",11))

        self.news2 = QtWidgets.QLabel(self.centralwidget)
        self.news2.setGeometry(QtCore.QRect(self.width-470,self.height-320,470,50))
        self.news2.setObjectName("news2")
        self.news2.setFont(QtGui.QFont("맑은 고딕",11))

        self.news3 = QtWidgets.QLabel(self.centralwidget)
        self.news3.setGeometry(QtCore.QRect(self.width-470,self.height-290,470,50))
        self.news3.setObjectName("news3")
        self.news3.setFont(QtGui.QFont("맑은 고딕",11))

        self.news4 = QtWidgets.QLabel(self.centralwidget)
        self.news4.setGeometry(QtCore.QRect(self.width-470,self.height-260,470,50))
        self.news4.setObjectName("news4")
        self.news4.setFont(QtGui.QFont("맑은 고딕",11))

        self.news5 = QtWidgets.QLabel(self.centralwidget)
        self.news5.setGeometry(QtCore.QRect(self.width-470,self.height-230,470,50))
        self.news5.setObjectName("news5")
        self.news5.setFont(QtGui.QFont("맑은 고딕",11))

        self.news6 = QtWidgets.QLabel(self.centralwidget)
        self.news6.setGeometry(QtCore.QRect(self.width-470,self.height-200,470,50))
        self.news6.setObjectName("news6")
        self.news6.setFont(QtGui.QFont("맑은 고딕",11))

        self.news7 = QtWidgets.QLabel(self.centralwidget)
        self.news7.setGeometry(QtCore.QRect(self.width-470,self.height-170,470,50))
        self.news7.setObjectName("news7")
        self.news7.setFont(QtGui.QFont("맑은 고딕",11))

        self.news8 = QtWidgets.QLabel(self.centralwidget)
        self.news8.setGeometry(QtCore.QRect(self.width-470,self.height-140,470,50))
        self.news8.setObjectName("news8")
        self.news8.setFont(QtGui.QFont("맑은 고딕",11))

        self.news9 = QtWidgets.QLabel(self.centralwidget)
        self.news9.setGeometry(QtCore.QRect(self.width-470,self.height-110,470,50))
        self.news9.setObjectName("news9")
        self.news9.setFont(QtGui.QFont("맑은 고딕",11))

        self.news10 = QtWidgets.QLabel(self.centralwidget)
        self.news10.setGeometry(QtCore.QRect(self.width-470,self.height-80,470,50))
        self.news10.setObjectName("news10")
        self.news10.setFont(QtGui.QFont("맑은 고딕",11))

        #video_viewer_label 생성
        self.video_viewer_label = QtWidgets.QLabel(self.centralwidget)
        self.video_viewer_label.setGeometry(QtCore.QRect(self.width-400,0,400,225))
        self.video_viewer_label.setObjectName("video_viewer_label")

        self.video_name_label = QtWidgets.QLabel(self.centralwidget)
        self.video_name_label.setGeometry(QtCore.QRect(self.width-400,250,400,20))
        self.video_name_label.setObjectName("video_name_label")
        self.video_name_label.setFont(QtGui.QFont("맑은 고딕",11))
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SmartMirror"))
        
    #시간을 알려주는 함수 메인 화면에 생성
    # now.(year,month,day,hour,minute,second)
    def set_time(self,MainWindow):
        EvenOrAfter = "오전"
        while True:
            now=datetime.datetime.now() #현재 시각을 시스템에서 가져옴
            hour=now.hour

            if(now.hour>=12):
                EvenOrAfter="오후"
                hour=now.hour%12

                if(now.hour==12):
                    hour=12

            else:
                EvenOrAfter="오전"

            self.date.setText("%s년 %s월 %s일"%(now.year,now.month,now.day))
            self.time.setText(EvenOrAfter+" %s시 %s분" %(hour,now.minute))
            sleep(1)

    
    def weather_icon(self,MainWindow):
        while True:
            sleep(300)
    
    #News (타이틀&기사 출력)
    def News(self,MainWindow) :
        d = feedparser.parse(self.News_url)
        while True :
            num = 1
            for e in d.entries :
                if num%10==1:
                    self.news1.setText("[%d] %s"%(num,e.title))
                elif num%10==2:
                    self.news2.setText("[%d] %s"%(num,e.title))
                elif num%10==3:
                    self.news3.setText("[%d] %s"%(num,e.title))
                elif num%10==4:
                    self.news4.setText("[%d] %s"%(num,e.title))
                elif num%10==5:
                    self.news5.setText("[%d] %s"%(num,e.title))
                elif num%10==6:
                    self.news6.setText("[%d] %s"%(num,e.title))
                elif num%10==7:
                    self.news7.setText("[%d] %s"%(num,e.title))
                elif num%10==8:
                    self.news8.setText("[%d] %s"%(num,e.title))
                elif num%10==9:
                    self.news9.setText("[%d] %s"%(num,e.title))
                elif num%10==0:
                    self.news10.setText("[%d] %s"%(num,e.title))
                num=num+1
                sleep(1)


    def Video_to_frame(self, MainWindow):
        while True:
            url = "https://www.youtube.com/watch?v=WwjUv4uuFn0"

            api = yapi.YoutubeAPI('')
            video_name=""
            results = api.general_search(video_name, max_results=2)
            
            str_results=str(results)

            i=0
            TrueOrFalse=False
            video_id=""
                  
            while True:
                try :

                    if "'" in str_results[i]:
                        if "=" in str_results[i-1]:
                            if "d" in str_results[i-2]:
                                if "I" in str_results[i-3]:
                                    if "o" in str_results[i-4]:
                                        i=i+1
                                        TrueOrFalse=True
                                        break
                    i=i+1

                except IndexError as e:
                    print("error")
                    break

            while TrueOrFalse:
                if "'" in str_results[i]:
                    break
                else :
                    video_id=video_id+str_results[i]

                i=i+1

            url = url+video_id

            try :
                vPafy = pafy.new(url)
                self.video_name_label.setText(vPafy.title)
                video_length=vPafy.length/60

            except Exception as e :
                self.video_viewer_label.setText("Error")
                self.start=False
            print(video_length/60)

            play = vPafy.getbest(preftype="mp4")
                
            cap = cv2.VideoCapture(play.url)

            while self.start:
                self.ret, self.frame = cap.read()
                if self.ret:
                    self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                    self.convertToQtFormat = QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)
                       
                    self.pixmap = QPixmap(self.convertToQtFormat)
                    self.p = self.pixmap.scaled(400, 225, QtCore.Qt.IgnoreAspectRatio)

                    self.video_viewer_label.setPixmap(self.p)
                    self.video_viewer_label.update()

                    sleep(0.0001) #Youtube 영상 1프레임당 0.0001초

                else :
                    break
                    
                if self.start_or_stop:
                    break

            cap.release()
            cv2.destroyAllWindows()

    def time_start(self,MainWindow):
        thread=threading.Thread(target=self.set_time,args=(self,))
        thread.daemon=True
        thread.start()

    def weather_start(self,MainWindow):
        thread=threading.Thread(target=self.weather_icon,args=(self,))
        thread.daemon=True
        thread.start()

    def News_start(self,MainWindow):
        thread=threading.Thread(target=self.News,args=(self,))
        thread.daemon=True
        thread.start()

    def video_thread(self,MainWindow):
        thread=threading.Thread(target=self.Video_to_frame,args=(self,))
        thread.daemon=True
        thread.start()


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    ui.time_start(MainWindow)
    ui.weather_start(MainWindow)
    ui.News_start(MainWindow)
    ui.video_thread(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())