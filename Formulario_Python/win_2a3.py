from PyQt5.QtGui     import *;
from PyQt5.QtCore    import *;
from PyQt5.QtWidgets import *;
# import calendar
from datetime import datetime
# import locale

import win_2a;
import win_2a2b;
import win_2a2c;
import win_2b;
import win_2a4;
import variables;


boxText = "Indique la fecha: "
buttonOption1 = "Atrás"
buttonOption2 = "Siguiente"

class Window(QDialog):
    def __init__(self):
        super().__init__()

        # Set names (as months) to Spanish (THIS WORKS IF THE USER PC IS SETTED IN SPANISH)
        # locale.setlocale(locale.LC_TIME, 'es_ES')

        print(">>>\tWindow 2a3")
        self.setWindowIcon(QIcon('images/icon_decowraps.jpg'))
        self.setWindowTitle('Deco  -  Formulario del Bot.')
        self.resize(340, 238)
        self.setMinimumSize(220, 220)
        self.setMaximumSize(380, 400)

        # Declaring layouts
        layout = QGridLayout()

        # Top Image
        self.image("images/decowraps.png", 200, 0, 0, 1, 5, layout, Qt.AlignHCenter)
        
        # Box contaning radio Buttons
        self.box = QGroupBox(boxText)
        self.box.setStyleSheet("""QGroupBox {color: rgb(1, 130, 153); }""")
        self.layout_groupbox1 = QGridLayout(self.box)
        
        # Month label
        self.labelMonth = QLabel('Mes:', self)
        self.layout_groupbox1.addWidget(self.labelMonth,0,0)
        # Month ComboBox
        self.comboBoxMonth = QComboBox(self)
        listMonths = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.comboBoxMonth.addItems(listMonths)
        # self.comboBoxMonth.addItems([month.capitalize() for month in calendar.month_name[1:]])
            # if no month is selected then the current month remains selected.
        if variables.__month__ == "":
            currentMonth = int(datetime.today().strftime('%m')) -1
            self.comboBoxMonth.setCurrentText(listMonths[currentMonth])
            # self.comboBoxMonth.setCurrentText(datetime.today().strftime('%B').capitalize())
        else:
            self.comboBoxMonth.setCurrentText(variables.__month__)
        self.layout_groupbox1.addWidget(self.comboBoxMonth,1,0)
        # Year label
        self.labelYear = QLabel('Año:', self)
        self.layout_groupbox1.addWidget(self.labelYear,0,1)
        # Year ComboBox
        self.comboBoxYear = QComboBox(self)
        self.comboBoxYear.addItems(self.yearscombobox())
        self.comboBoxYear.setCurrentText(variables.__year__) 
        self.layout_groupbox1.addWidget(self.comboBoxYear,1,1)

        # Put Radio Buttons into the box
        layout.addWidget(self.box,1,1,1,3)

        # Empty space
        self.labelEmpty = QLabel("")
        layout.addWidget(self.labelEmpty,2,0,1,5)

        # Button Next (put this line before the backButton so this button will be selected automatically when the windows is opened)
        self.buttonInGridLayout(buttonOption2, 3, 3, layout)
        # Button Back
        self.buttonInGridLayout(buttonOption1, 3, 1, layout)

        # Below image
        self.image("images/tsoft1.png", 130, 4, 3, 1, 1, layout)

        # Sizing layout
        layout.setVerticalSpacing(0)
        layout.setHorizontalSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        # Showing layout
        self.setLayout(layout)

        #Showing Window
        self.show()

    @pyqtSlot()
    def backPage(self):
        print("\t   Stage: " + variables.__stage__)
        # This goes to the previous window depending on which path was followed to get here.
        if variables.__stage__ == '1ra parte Check RD, LC DUTY and Change RD.' and variables.__weekly_close__ == 'Bv Semanal':
            self.cams = win_2a.Window()
            self.cams.show()
            self.close()
        elif variables.__stage__ == '2da parte LC for Upload.' and variables.__upload_fire_cx__ == "Sí, cargar los asientos en Fire CX.":
            self.cams = win_2a2c.Window()
            self.cams.show()
            self.close()
        elif variables.__stage__ == '2da parte LC for Upload.' and variables.__upload_fire_cx__ == "No, no cargar los asientos en Fire CX.":
            self.cams = win_2a2b.Window()
            self.cams.show()
            self.close()
        elif variables.__stage__ == '1ra parte Check RD, LC DUTY and Change RD.' and variables.__weekly_close__ == 'Bv Cierre':
            self.cams = win_2b.Window()
            self.cams.show()
            self.close()
        
    def nextPage(self):
        variables.__month__ = self.comboBoxMonth.currentText()
        variables.__month_as_int__ = self.comboBoxMonth.currentIndex()+1
        variables.__year__ = self.comboBoxYear.currentText()
        variables.__year_as_int__ = int(self.comboBoxYear.currentText())
        print("\t   Month: "+variables.__month__)
        print("\t   Month: "+str(variables.__month_as_int__))
        print("\t   Year: "+variables.__year__)
        print("\t   Year: "+str(variables.__year_as_int__))
        self.cams = win_2a4.Window()
        self.cams.show()
        self.close()

    def alertCheck(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("No hay una opción seleccionada.")
        messageBox.setText("Por favor, seleccione una opción.")
        messageBox.exec()

    def buttonInGridLayout(self, text :str, row :int, column :int, gridLayout, heightRow=1, widthColumn=1):
        self.button = QPushButton(text, self)
        self.button.setFont(QFont("Sanserif",11))
        if text == buttonOption1:
            self.button.clicked.connect(self.backPage)
        elif text == buttonOption2:
            self.button.clicked.connect(self.nextPage)
        gridLayout.addWidget(self.button, row, column, heightRow, widthColumn)


    def image(self, path :str, scaledToWidth :int, row :int, column :int, heightRow :int, widthColumn :int, gridLayout, align=Qt.AlignLeading):
        self.labelPic2 = QLabel(self)
        pic2 = QPixmap(path)
        pic2 = pic2.scaledToWidth(scaledToWidth)
        self.labelPic2.setPixmap(pic2)
        gridLayout.addWidget(self.labelPic2, row, column, heightRow, widthColumn, align)

    def yearscombobox(self):
        # This returns a list with the current year and the next two.
        return [str(int(datetime.today().strftime('%Y'))+a) for a in range(0,3)]


# import sys

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex=Window()
#     sys.exit(app.exec_())





























# from PyQt5.QtGui     import *;
# from PyQt5.QtCore    import *;
# from PyQt5.QtWidgets import *;
# import win_3;
# import win_4;

# # from tkcalendar import *;
# import locale
# import calendar
# from datetime import datetime

# import variables


# class Window(QDialog):
#     def __init__(self):
#         super().__init__()

#         print(">>>\tWindow 3-a-1")

#         locale.setlocale(locale.LC_TIME, 'es_ES')

#         # variables.__path_lc_duty_bv__ = "asdfasdf"
  
#         # # Global variable???
#         # global __path_lc_duty_bv__
#         # __path_lc_duty_bv__ = os.path.join("C:\\", "Bv", "2. Input File for LC for Upload (USER)")


#         self.setWindowTitle('Window 3')
#         # self.setGeometry(250, 100, 400, 400)
#         # self.resize(300, 240)s
#         self.resize(400, 400)



#         # Declaring layouts
#         layoutV = QVBoxLayout()
#         layoutH = QHBoxLayout()
#         layoutH2 = QHBoxLayout()
#         layoutH3 = QHBoxLayout()
#         layoutV2 = QVBoxLayout()


#         self.labelSpaceBetweenButtons = QLabel("  ")

#         self.labelIndication = QLabel("Indique la fecha: ")
#         self.labelIndication.setFont(QFont("Sanserif",13))
#         layoutV.addWidget(self.labelIndication)

#         layoutH2.addWidget(self.labelSpaceBetweenButtons)
#         self.labelMonth = QLabel('Mes:', self)
#         self.labelMonth.setGeometry(30, 10, 41, 21)        
#         layoutH2.addWidget(self.labelMonth)
#         layoutH2.addWidget(self.labelSpaceBetweenButtons)
#         self.labelYear = QLabel('Año:',self)
#         self.labelYear.setGeometry(150,10,41,21)
#         layoutH2.addWidget(self.labelYear)
#         layoutH2.addWidget(self.labelSpaceBetweenButtons)


#         layoutH3.addWidget(self.labelSpaceBetweenButtons)
       
#         # Crear los comboBox
#         self.comboBoxMonth = QComboBox(self)
#         # self.comboBoxMonth.setGeometry(20,40,69,22)
#         self.comboBoxMonth.addItems([month.capitalize() for month in calendar.month_name[1:]])
#         if variables.__month__ == "":
#             self.comboBoxMonth.setCurrentText(datetime.today().strftime('%B').capitalize())
#         else:
#             self.comboBoxMonth.setCurrentText(variables.__month__)
#         layoutH3.addWidget(self.comboBoxMonth)

#         layoutH3.addWidget(self.labelSpaceBetweenButtons)

#         self.comboBoxYear = QComboBox(self)
#         # self.comboBoxYear.setGeometry(130,40,69,22)
#         self.comboBoxYear.addItems(self.yearscombobox())
#         self.comboBoxYear.setCurrentText(variables.__year__)
#         layoutH3.addWidget(self.comboBoxYear)
        
#         layoutH3.addWidget(self.labelSpaceBetweenButtons)

        
   
#         layoutH.addWidget(self.labelSpaceBetweenButtons)

#         # Button Quit
#         self.button = QPushButton('Atrás', self)
#         # self.button.move(100, 100)
#         self.button.setFont(QFont("Sanserif",11))
#         self.button.clicked.connect(self.goMainWindow)
#         layoutH.addWidget(self.button)

#         layoutH.addWidget(self.labelSpaceBetweenButtons)

 
#         # Button Next
#         self.buttonNext = QPushButton('Siguiente', self)
#         # self.buttonNext.move(100, 100)
#         self.buttonNext.setFont(QFont("Sanserif",11))
#         self.buttonNext.clicked.connect(self.goThirdWindow)
#         layoutH.addWidget(self.buttonNext)

#         layoutH.addWidget(self.labelSpaceBetweenButtons)


#         # Layout Positioning
#         layoutV.addLayout(layoutH2)
#         layoutV.addLayout(layoutH3)
#         layoutV.addLayout(layoutH)
#         self.setLayout(layoutV)



#         self.show()


        
#     def goMainWindow(self):
#         self.cams = win_3.Window()
#         self.cams.show()
#         self.close() 
        
#     def goThirdWindow(self):
#         # self.cams = Window2(text_any) 
#         variables.__month__ = self.comboBoxMonth.currentText()
#         variables.__month_as_int__ = self.comboBoxMonth.currentIndex()+1
#         variables.__year__ = self.comboBoxYear.currentText()
#         variables.__year_as_int__ = int(self.comboBoxYear.currentText())
#         print("\t   Month: "+variables.__month__)
#         print("\t   Month: "+str(variables.__month_as_int__))
#         print("\t   Year: "+variables.__year__)
#         print("\t   Year: "+str(variables.__year_as_int__))
#         self.cams = win_4.Window() 
#         self.cams.show()
#         self.close()

#     def yearscombobox(self):
#         return [str(int(datetime.today().strftime('%Y'))+a) for a in range(0,3)]



# import sys 

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex= Window()
#     sys.exit(app.exec_())
