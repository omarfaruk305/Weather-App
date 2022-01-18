from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout,QFileDialog, QMainWindow)
import mn
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys
import api
from db import get_tables
from db import get_city_information

class UI(QtWidgets.QMainWindow):
     def __init__(self):
           super(UI,self).__init__()
           uic.loadUi("untitled.ui",self)
           # self.button=self.findChild(QPushButton,"pushButton")
           # self.label=self.findChild(QLabel,"label")
           
           
           self.pushButton.clicked.connect(self.clicker)
           self.pushButton_USA.clicked.connect(self.country_selector)
           self.pushButton_NL.clicked.connect(self.country_selector_2)
           self.pushButton_TR.clicked.connect(self.country_selector_3)
           self.revert_button.clicked.connect(self.revert)
           self.code_2.setText("")
        #    self.tableWidget.selectionModel().selectionChanged.connect(self.kapo) 

           self.pixmap2=QPixmap("image\\weather.jpg")
           self.label_2.setPixmap(self.pixmap2)
           self.show()
     # def clicker(self):
     #   fname=QFileDialog.getOpenFileName(self,"C:\\Users\\betel\\Desktop\\New folder (8)\\01d.png")
     #   self.pixmap=QPixmap(fname[0])
     #   self.label.setPixmap(self.pixmap)

   
     def clicker(self):
     #   fname=QFileDialog.getOpenFileName(self,"C:\\Users\\betel\\Desktop\\New folder (8)\\Weather-App.py\\11d.png")
        #   _translate = QtCore.QCoreApplication.translate
        try:
                cityname=self.lineEdit.text().title() # capitalize olmuyor, herbir kelime buyukle baslamali
                
                city_gui=get_city_information(f"{cityname}")
                self.cityname_gui.setText(city_gui[0][0])
                self.provincename_gui.setText(city_gui[0][1])
                self.population_gui.setText(str(city_gui[0][2]))
                self.code_2.setText("")
                parameters=api.info.get_weather(f'{cityname}')
                self.pixmap=QPixmap(f"image\\{parameters[4]}.png")
                self.label.setPixmap(self.pixmap)
                self.code.setText(f"{parameters[0]}, {parameters[1]}")
                self.degree.setText(f"{parameters[2]}")
                self.description.setText(f"{parameters[3].title()}")
        
                

          
                # if parameters[1]=="TR":
                #     self.pixmap3=QPixmap("image\\TRflag.jpg")
                #     self.label_7.setPixmap(self.pixmap3)
                # elif parameters[1]=="US":
                #     self.pixmap3=QPixmap("image\\USAflag.png")
                #     self.label_7.setPixmap(self.pixmap3)
                # elif parameters[1]=="NL":
                #     self.pixmap3=QPixmap("image\\NLflag.jpg")
                #     self.label_7.setPixmap(self.pixmap3)
               
        except Exception as e:
            # self.pixmap3=QPixmap("image\sky.jpeg")
            # self.label_7.setPixmap(self.pixmap3)
            self.code_2.setText("Invalid city name")
            self.code.setText(f"")
            self.description.setText(f"<<--Check Table")
            self.cityname_gui.setText("-")
            self.provincename_gui.setText("-")
            self.population_gui.setText("-")
            self.pixmap=QPixmap()  ##derec resmi 
            self.label.setPixmap(self.pixmap)
            self.degree.setText("-")
            
     def country_selector(self):
         self.pixmap2=QPixmap("image\\USAflag.png")
         self.label_7.setPixmap(self.pixmap2)

         display_table=get_tables("America")
         row=0
         self.tableWidget.setRowCount(len(display_table))
         for i in display_table:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i[0]))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
            row+=1

     def country_selector_2(self):
         display_table=get_tables("Netherlands")
         self.pixmap2=QPixmap("image\\NLflag.jpg")
         self.label_7.setPixmap(self.pixmap2)
        #  self.pixmap5=QPixmap("image\\dutch.jpg")
        #  self.label_5.setPixmap(self.pixmap5)
         row=0
         self.tableWidget.setRowCount(len(display_table))
         for i in display_table:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i[0]))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
            row+=1
     def country_selector_3(self):
         display_table=get_tables("Turkey")
         self.pixmap2=QPixmap("image\\TRflag.jpg")
         self.label_7.setPixmap(self.pixmap2)
         row=0
         self.tableWidget.setRowCount(len(display_table))
         for i in display_table:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i[0]))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
            row+=1
     def revert(self):
        self.tableWidget.clearContents()
        self.pixmap3=QPixmap("image\sky.jpeg")
        self.label_7.setPixmap(self.pixmap3)
        self.degree.setText("-")
        
        self.code.setText("")
        self.description.setText(f"<<--Check Table")
        self.cityname_gui.setText("-")
        self.provincename_gui.setText("-")
        self.population_gui.setText("-")
        self.pixmap=QPixmap()  ##derec resmi 
        self.label.setPixmap(self.pixmap)
        self.degree.setText("-")
        self.lineEdit.setText("City Name")
        
    #  def kapo(self,selected):
    #     for location in selected.indexes():
    #         row=location.row()
    #         column=location.column()
    #         kontrol=UI.tableWidget.item(row,column)
    #         # print(row,column)
    #         if kontrol and column==0:
    #             cell_text=UI.tableWidget.item(row,column).text()
    #             # print(cell_text,"tablo")
    #             print(cell_text)



  # def display(self):

  #   self.pixmap=QPixmap(f"image\\{parameters[4]}.png")
  #   # self.pixmap2=QPixmap("image\\weather.jpg")
  #   self.pixmap3=QPixmap("image\\NLflag.jpg")
  #   self.label_7.setPixmap(self.pixmap3)
  #   self.label.setPixmap(self.pixmap)
  #   # print(api.info.get_weather(f'{self.Cityname}'))
  
  # def Display(self):

    
    

  

app=QApplication(sys.argv)
UIWindow=UI()
app.exec_()



# display_table=[{"City":"Izmir","Province":"DOgu anadolu","Population":"102021"},{"City":"Vvv","Province":"Dsd","Population":"325324"},{"City":"Vvv","Province":"Dsd","Population":"325324"},{"City":"Vvv","Province":"Dsd","Population":"325324"},{"City":"Vvv","Province":"Dsd","Population":"325324"}]
#         row=0
#         self.tableWidget.setRowCount(len(display_table))
#         for i in display_table:
#             self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i["City"]))
#             self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i["Province"]))
#             self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(i["Population"]))
#             row+=1