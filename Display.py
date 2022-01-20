
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QFileDialog, QMainWindow)

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys
import api
import db

class UI(QtWidgets.QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("untitled.ui", self)

        self.pushButton.clicked.connect(self.clicker)
        self.tableWidget.selectionModel().selectionChanged.connect(self.TABLO)
        self.pushButton_USA.clicked.connect(self.country_selector)
        self.pushButton_NL.clicked.connect(self.country_selector_2)
        self.pushButton_TR.clicked.connect(self.country_selector_3)
        self.zoom_button.clicked.connect(self.zoomer)
        self.revert_zoom.clicked.connect(self.revert_map)
        self.revert_button.clicked.connect(self.revert)
        self.bacground_options.clicked.connect(self.options)
        self.code_2.setText("")
        self.countryname=0
        self.pixmap2 = QPixmap("image\\444.jfif")
        self.label_2.setPixmap(self.pixmap2)
        self.show()

    def clicker(self):
        try:
            # capitalize olmuyor, herbir kelime buyukle baslamali
            cityname = self.lineEdit.text().title()
            city_gui = db.get_city_information(f"{cityname}")
            self.cityname_gui.setText(city_gui[0][0])
            self.provincename_gui.setText(city_gui[0][1])
            self.population_gui.setText(str(city_gui[0][2]))
            self.code_2.setText("")
            parameters = api.info.get_weather(f'{cityname}')
            self.pixmap = QPixmap(f"image\\{parameters[4]}.png")
            self.label.setPixmap(self.pixmap)
            self.code.setText(
                f"on {parameters[5]}, in {parameters[0]},  {parameters[1]}")
            self.degree.setText(f"{parameters[2]}")
            self.description.setText(f"{parameters[3].title()}")
            self.label_9.setText(f"Sunrise at {parameters[6]} ,sunset at {parameters[7]} ")
            
            if parameters[10]<parameters[8] or parameters[10]>parameters[9]:
                self.pixmapnight=QPixmap("image\\night.jfif")
                self.label_5.setPixmap(self.pixmapnight)
            elif parameters[10]>=parameters[8] and parameters[10]<=parameters[9]:
                self.pixmapday=QPixmap("image\\daytime.jfif")
                self.label_5.setPixmap(self.pixmapday)
                
        except Exception as a:
            self.exception()

    def exception(self):
        self.code_2.setText("Invalid city name")
        self.revert()
        self.description.setText(f"<<-- Table")
        

    def set_country_table(self, country_name):
        row = 0
        self.tableWidget.setRowCount(len(country_name))
        for i in country_name:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            row += 1

    def TABLO(self, konum, y):
        # QTableWidget.selectionModel().selectionChanged.connect(TABLO) ====> 2 adet konum bilgisi donuyor.
        for location in konum.indexes():
            row = location.row()
            column = location.column()
            kontrol = self.tableWidget.item(row, column)
            # print(row,column)
            if kontrol and column == 0:
                city_name = self.tableWidget.item(row, column).text()
                self.lineEdit.setText(city_name)
                self.clicker()

    def country_selector(self):
        self.countryname="America"
        self.pixmap2 = QPixmap("image\\USAflag.png")
        self.label_7.setPixmap(self.pixmap2)
        self.pixmap4=QPixmap("image\\usa_map800x495.png")
        self.label_8.setGeometry(1090,60,300,170)
        self.label_8.setPixmap(self.pixmap4)
        display_table = db.get_tables(self.countryname)
        self.set_country_table(display_table)

    def country_selector_2(self):
        self.countryname="Netherlands"
        display_table = db.get_tables(self.countryname)
        self.pixmap2 = QPixmap("image\\NLflag.jpg")
        self.label_7.setPixmap(self.pixmap2)
        self.pixmap4=QPixmap("image\\nl_map800x948.png")
        self.label_8.setGeometry(1090,60,250,290)
        self.label_8.setPixmap(self.pixmap4)
        self.set_country_table(display_table)

    def country_selector_3(self):
        self.countryname="Turkey"
        display_table = db.get_tables(self.countryname)
        self.pixmap2 = QPixmap("image\\TRflag.jpg")
        self.label_7.setPixmap(self.pixmap2)
        self.pixmap4=QPixmap("image\\tr_map2000x1360.jpg")
        self.label_8.setGeometry(1090,60,300,170)
        self.label_8.setPixmap(self.pixmap4)
        self.set_country_table(display_table)

    def revert(self):
        self.tableWidget.clearContents()  # cleans table,
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)  # 3 column remain
        self.pixmap3 = QPixmap("image\sky.jpeg")
        self.label_7.setPixmap(self.pixmap3)
        self.degree.setText("-")
        self.pixmap2 = QPixmap("image\\444.jfif")
        self.label_2.setPixmap(self.pixmap2)
        self.code.setText("")
        self.description.setText(f"")
        self.cityname_gui.setText("-")
        self.provincename_gui.setText("-")
        self.population_gui.setText("-")
        self.pixmap = QPixmap()  # derec resmi
        self.label.setPixmap(self.pixmap)
        self.degree.setText("")
        self.lineEdit.setText("City Name")
        self.pixmap4=QPixmap()
        self.label_8.setPixmap(self.pixmap4)
        self.pixmapday=QPixmap()
        self.label_5.setPixmap(self.pixmapday)
        self.label_9.setText("")
        

    def revert_map(self):
        if self.countryname=="America":
            self.label_8.setGeometry(1090,60,300,170)
        elif self.countryname=="Turkey":
            self.label_8.setGeometry(1090,60,300,170)
        elif self.countryname=="Netherlands":
             self.label_8.setGeometry(1090,60,250,290)
    def zoomer(self):
        if self.countryname=="America":
            self.label_8.setGeometry(620,70,880,550)
        elif self.countryname=="Turkey":
            self.label_8.setGeometry(620,70,900,585)
        elif self.countryname=="Netherlands":
             self.label_8.setGeometry(620,70,770,800)
 
    def options(self):
       fname=QFileDialog.getOpenFileName(self,"image\\444.jfif")
       self.pixmap=QPixmap(fname[0])
       self.label_2.setPixmap(self.pixmap)

