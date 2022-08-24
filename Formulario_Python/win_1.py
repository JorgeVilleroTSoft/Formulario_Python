from PyQt5.QtGui     import *;
from PyQt5.QtCore    import *;
from PyQt5.QtWidgets import *;

import win_2;
import variables;

boxText = "Elija la Compañía: "
radioButtonOption1 = "BV"
radioButtonOption2 = "HH"
buttonOption1 = "Salir"
buttonOption2 = "Siguiente"

class Window(QDialog):
    def __init__(self):
        super().__init__()

        print(">>>\tWindow 1")
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
        self.box.setStyleSheet("""QGroupBox {color: rgb(1, 130, 153);  }""")
        self.layout_groupbox = QVBoxLayout(self.box)
        layout.addWidget(self.box,1,1,1,3)

        # RadioButton BV
        self.radioButton(radioButtonOption1)
        if variables.__company__ == radioButtonOption1:
            self.radioBtn.setChecked(True)
        # # RadioButton HH
        # self.radioButton(radioButtonOption2)
        # if variables.__company__ == radioButtonOption2:
        #     self.radioBtn.setChecked(True)

        # Empty space
        self.labelEmpty = QLabel("")
        layout.addWidget(self.labelEmpty,2,0,1,5)

        # Button Next (put this line before the backButton so this button will be selected automatically when the windows is opened)
        self.buttonInGridLayout(buttonOption2, 3, 3, layout)
        # Button Quit
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
    def quit(self):
        print(">>>\tExiting")
        self.close()
        
        
    def nextPage(self):
        # This goes to the next window only if a radiobutton is selected.
        if variables.__company__ == radioButtonOption1 or variables.__company__ == radioButtonOption2:
            print("\t   Company: " + variables.__company__)
            self.cams = win_2.Window()
            self.cams.show()
            self.close()
        else:
            self. alertCheck()
        
    def onRadioButton(self):
        radioBtn = self.sender()
        # Set the variable according to the selected button
        if radioBtn.isChecked():
            variables.__company__ = radioBtn.text()
 
    def alertCheck(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("No hay una opción seleccionada.")
        messageBox.setText("Por favor, seleccione una opción.")
        messageBox.exec()

    def buttonInGridLayout(self, text :str, row :int, column :int, gridLayout, heightRow=1, widthColumn=1):
        self.button = QPushButton(text, self)
        self.button.setFont(QFont("Sanserif",11))
        if text == buttonOption1:
            self.button.clicked.connect(self.quit)
        elif text == buttonOption2:
            self.button.clicked.connect(self.nextPage)

        gridLayout.addWidget(self.button, row, column, heightRow, widthColumn)

    def radioButton(self, text :str):
        self.radioBtn = QRadioButton(text,self.box)
        self.radioBtn.setFont(QFont("Sanserif",10))
        self.radioBtn.toggled.connect(self.onRadioButton)
        self.layout_groupbox.addWidget(self.radioBtn)

    def image(self, path :str, scaledToWidth :int, row :int, column :int, heightRow :int, widthColumn :int, gridLayout, align=Qt.AlignLeading):
        self.labelPic2 = QLabel(self)
        pic2 = QPixmap(path)
        pic2 = pic2.scaledToWidth(scaledToWidth)
        self.labelPic2.setPixmap(pic2)
        gridLayout.addWidget(self.labelPic2, row, column, heightRow, widthColumn, align)

# import sys

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex=Window()
#     sys.exit(app.exec_())

































# from PyQt5.QtGui     import *;
# from PyQt5.QtCore    import *;
# from PyQt5.QtWidgets import *;

# import win_2;
# import variables;

# class Window(QDialog):
#     def __init__(self, boxText, radioButtonOption1, radioButtonOption2, buttonOption1, buttonOption2, global_var):
#         super().__init__()

#         # self.__boxText__ = boxText
#         self.__radioButtonOption1__ = radioButtonOption1
#         self.__radioButtonOption2__ = radioButtonOption2
#         self.__buttonOption1__ = buttonOption1
#         self.__buttonOption2__ = buttonOption2
#         # self.__global_var__ = global_var

#         print(">>>\tWindow 1")
#         self.setWindowIcon(QIcon('images/icon_decowraps.jpg'))
#         self.setWindowTitle('Deco  -  Formulario del Bot.')
#         self.resize(340, 238)
#         self.setMinimumSize(220, 220)
#         self.setMaximumSize(380, 400)

#         # Declaring layouts
#         layout = QGridLayout()

#         # Top Image
#         self.image("images/decowraps.png", 200, 0, 0, 1, 5, layout, Qt.AlignHCenter)
        
#         # Box contaning radio Buttons
#         self.box = QGroupBox(boxText)
#         self.box.setStyleSheet("""QGroupBox:title {color: rgb(1, 130, 153); font-weight: bold; }""")
#         self.layout_groupbox = QVBoxLayout(self.box)
#         layout.addWidget(self.box,1,1,1,3)

#         # RadioButton BV
#         self.radioButton(radioButtonOption1)
#         if global_var == radioButtonOption1:
#             self.radioBtn.setChecked(True)
#         # RadioButton HH
#         self.radioButton(radioButtonOption2)
#         if global_var == radioButtonOption2:
#             self.radioBtn.setChecked(True)

#         # Empty space
#         self.labelEmpty = QLabel("")
#         layout.addWidget(self.labelEmpty,2,0,1,5)

#         # Button Next (put this line before the backButton so this button will be selected automatically when the windows is opened)
#         self.buttonInGridLayout(buttonOption2, 3, 3, layout)
#         # Button Quit
#         self.buttonInGridLayout(buttonOption1, 3, 1, layout)

#         # Below image
#         self.image("images/tsoft1.png", 130, 4, 3, 1, 1, layout)

#         # Sizing layout
#         layout.setVerticalSpacing(0)
#         layout.setHorizontalSpacing(0)
#         layout.setContentsMargins(0,0,0,0)
#         layout.setSpacing(0)

#         # Showing layout
#         self.setLayout(layout)

#         #Showing Window
#         self.show()

#     @pyqtSlot()
#     def quit(self):
#         print(">>>\tExiting")
#         sys.exit()
        
#     def nextPage(self):
#         # This goes to the next Windows just whether a radiobutton is selected.
#         if self.__global_var__ == self.__radioButtonOption1__ or self.__global_var__ == self.__radioButtonOption2__:
#             print("\t   Company: " + self.__global_var__)
#             self.cams = win_2.Window()
#             self.cams.show()
#             self.close()
#         else:
#             self. alertCheck()
        
#     def onRadioButton(self):
#         radioBtn = self.sender()
#         if radioBtn.isChecked():
#             self.__global_var__ = radioBtn.text()
 
#     def alertCheck(self):
#         messageBox = QMessageBox()
#         messageBox.setWindowTitle("No hay una opción seleccionada.")
#         messageBox.setText("Por favor, seleccione una opción.")
#         messageBox.exec()

#     def buttonInGridLayout(self, text :str, row :int, column :int, gridLayout, heightRow=1, widthColumn=1):
#         self.button = QPushButton(text, self)
#         self.button.setFont(QFont("Sanserif",11))
#         if text == self.__buttonOption1__:
#             self.button.clicked.connect(self.quit)
#         elif text == self.__buttonOption2__:
#             self.button.clicked.connect(self.nextPage)

#         gridLayout.addWidget(self.button, row, column, heightRow, widthColumn)

#     def radioButton(self, text :str):
#         self.radioBtn = QRadioButton(text,self.box)
#         self.radioBtn.setFont(QFont("Sanserif",10))
#         self.radioBtn.toggled.connect(self.onRadioButton)
#         self.layout_groupbox.addWidget(self.radioBtn)

#     def image(self, path :str, scaledToWidth :int, row :int, column :int, heightRow :int, widthColumn :int, gridLayout, align=Qt.AlignLeading):
#         self.labelPic2 = QLabel(self)
#         pic2 = QPixmap(path)
#         pic2 = pic2.scaledToWidth(scaledToWidth)
#         self.labelPic2.setPixmap(pic2)
#         gridLayout.addWidget(self.labelPic2, row, column, heightRow, widthColumn, align)

#     # def define_var(boxText, radioButtonOption1, radioButtonOption2, buttonOption1, buttonOption2, __global_var__):
#     #     return(boxText, radioButtonOption1, radioButtonOption2, buttonOption1, buttonOption2, __global_var__)


# import sys

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex=Window("Elija la Compañía: ", "BV", "HH", "Salir", "Siguiente", variables.__company__)
#     # ex.define_var("Elija la Compañía: ", "BV", "HH", "Salir", "Siguiente", variables.__company__)
#     sys.exit(app.exec_())






































# # import sys;
# from PyQt5.QtGui     import *;
# from PyQt5.QtCore    import *;
# from PyQt5.QtWidgets import *;
# import win_2;
# import main;
# import variables
# # import window2;

# # # Global Variables
# # __company__ = ""
# # __NO_SE_QUE_WINDOW_1__ = ""
# # __stage__ = ""
# # __text__ = "Un texto cualquiera"




# class Window(QDialog):
#     def __init__(self):
#         super().__init__()

#         print(">>>\tWindow 1")
#         self.setWindowIcon(QIcon('icon_decowraps.jpg'))

#         self.setWindowTitle('Deco  -  Formulario del Bot.')
#         self.resize(260, 230)

#         # Declaring layouts
#         layout = QGridLayout()
  
#         # Superior Image
#         self.labelPic = QLabel(self)
#         pic = QPixmap("decowraps.jpg")
#         pic = pic.scaledToWidth(200)
#         self.labelPic.setPixmap(pic)
#         layout.addWidget(self.labelPic,0,0,1,5)

#         # Box contaning radibuttons
#         self.box = QGroupBox("Elija la Compañía: ")
#         self.box.setStyleSheet("""QGroupBox:title {color: rgb(1, 130, 153); font-weight: bold; }""")
#         self.layout_groupbox = QVBoxLayout(self.box)


#         # RadioButtons
#         self.radioBtnBv = QRadioButton('BV',self.box)
#         # self.radioBtnBv.setText( "Bv")
#         self.radioBtnBv.setFont(QFont("Sanserif",10))
#         self.radioBtnBv.toggled.connect(self.onRadioButton)
#         self.layout_groupbox.addWidget(self.radioBtnBv)
#         #############################################################################
#         #############################################################################
#         ##################### ADD THAT IT CAN GO AHEAD JUST IF BV IS SELECTED ##########
#         ########## ADD THAT WHEN THE company IS SELECTED, then go to the next windows and go back, then keep it SELECTED ##########
#         #############################################################################
#         #############################################################################
#         self.radioBtnHh = QRadioButton('HH',self.box)
#         self.radioBtnHh.setFont(QFont("Sanserif",10))
#         self.radioBtnHh.toggled.connect(self.onRadioButton)
#         self.layout_groupbox.addWidget(self.radioBtnHh)

#         layout.addWidget(self.box,1,1,1,3)


#         # Empty space
#         self.labelEmpty = QLabel("")
#         layout.addWidget(self.labelEmpty,2,0,1,5)


#         # Button Quit
#         self.button = QPushButton('Salir', self)
#         self.button.setFont(QFont("Sanserif",11))
#         self.button.clicked.connect(self.quit)
#         layout.addWidget(self.button,3,1)
        
#         # Button Next
#         self.buttonNext = QPushButton('Siguiente', self)
#         self.buttonNext.setFont(QFont("Sanserif",11))
#         self.buttonNext.clicked.connect(self.nextPage)
#         layout.addWidget(self.buttonNext,3,3)

#         # Below image
#         self.labelPic = QLabel(self)
#         pic = QPixmap("tsoft1.png")
#         pic = pic.scaledToWidth(130)
#         self.labelPic.setPixmap(pic)
#         layout.addWidget(self.labelPic,4,3,1,1)

#         # Sizing layout
#         layout.setVerticalSpacing(0)
#         layout.setHorizontalSpacing(0)
#         layout.setContentsMargins(0,0,0,0)
#         layout.setSpacing(0)

#         # Showing layout
#         self.setLayout(layout)

#         #Showing Window
#         self.show()

#     @pyqtSlot()
#     def quit(self):
#         print(">>>\tExiting")
#         sys.exit()
        
#     def nextPage(self):
#         print("\t   Company: "+variables.__company__)
#         # self.statusBar().showMessage("Switched to window 1")
#         # self.cams = Window1(self.lineEdit1.text()) 
#         self.cams = win_2.Window() 
#         self.cams.show()
#         self.close()

#     def onRadioButton(self):
#         radioBtn = self.sender()
#         if radioBtn.isChecked():
#             variables.__company__ = radioBtn.text()
 






# import sys

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex=Window()
#     sys.exit(app.exec_())






















# # import sys;
# from PyQt5.QtGui     import *;
# from PyQt5.QtCore    import *;
# from PyQt5.QtWidgets import *;
# import win_2;
# import main;
# import variables
# # import window2;

# # # Global Variables
# # __company__ = ""
# # __NO_SE_QUE_WINDOW_1__ = ""
# # __stage__ = ""
# # __text__ = "Un texto cualquiera"




# class Window(QDialog):
#     def __init__(self):
#         super().__init__()

#         print(">>>\tWindow 1")

#         # global __path_lc_duty_bv__
#         # print(__path_lc_duty_bv__)

#         self.setWindowTitle('Window 0')
#         # self.setGeometry(250, 100, 400, 400)
#         # self.resize(300, 240)
#         self.resize(400, 400)



#         # Declaring layouts
#         layoutV = QVBoxLayout()
#         layoutH = QHBoxLayout()
#         layoutH2 = QHBoxLayout()
#         layoutV2 = QVBoxLayout()


#         self.labelSpaceBetweenButtons = QLabel("  ")

#         self.labelIndication = QLabel("Elija la Compañía: ")
#         self.labelIndication.setFont(QFont("Sanserif",13))
#         layoutV.addWidget(self.labelIndication)


#         #Crear los RadioButtons
#         self.radioBtnBv = QRadioButton('BV',self)
#         self.radioBtnBv.setFont(QFont("Sanserif",13))
#         # self.radioBtnBv.setGeometry(700,110,82,17)
#         self.radioBtnBv.toggled.connect(self.onRadioButton)
#         layoutV.addWidget(self.radioBtnBv)
#         # self.radioBtnBv.setChecked(True)
#         # layoutH2.addWidget(self.labelSpaceBetweenButtons)
#         # layoutH2.addWidget(self.radioBtnBv)
#         #############################################################################
#         #############################################################################
#         ##################### ADD THAT IT CAN GO AHEAD JUST IF BV IS SELECTED ##########
#         ########## ADD THAT WHEN THE company IS SELECTED, then go to the next windows and go back, then keep it SELECTED ##########
#         #############################################################################
#         #############################################################################
#         self.radioBtnHh = QRadioButton('HH',self)
#         self.radioBtnHh.setFont(QFont("Sanserif",13))
#         # self.radioBtnHh.setGeometry(700,140,82,17)
#         self.radioBtnHh.toggled.connect(self.onRadioButton)
#         layoutV.addWidget(self.radioBtnHh)
#         # layoutH2.addWidget(self.radioBtnHh)
#         # layoutH2.addWidget(self.labelSpaceBetweenButtons)


   
#         layoutH.addWidget(self.labelSpaceBetweenButtons)

#         # Button Quit
#         self.button = QPushButton('Salir', self)
#         # self.button.move(100, 100)
#         self.button.setFont(QFont("Sanserif",11))
#         self.button.clicked.connect(self.quit)
#         layoutH.addWidget(self.button)
        

#         layoutH.addWidget(self.labelSpaceBetweenButtons)



#         # Button Next
#         self.buttonNext = QPushButton('Siguiente', self)
#         # self.buttonNext.move(100, 100)
#         self.buttonNext.setFont(QFont("Sanserif",11))
#         self.buttonNext.clicked.connect(self.nextPage)
#         layoutH.addWidget(self.buttonNext)

#         layoutH.addWidget(self.labelSpaceBetweenButtons)

#         # self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1]."+text_any, self)
#         # self.lineEdit1 = QLineEdit("Type here... "+__text__, self)
#         # self.lineEdit1.setGeometry(250, 100, 400, 30)
#         # layoutH.addWidget(self.lineEdit1)

#         # Layout Positioning
#         layoutV.addLayout(layoutH2)
#         layoutV.addLayout(layoutH)
#         self.setLayout(layoutV)


#         self.show()

#     @pyqtSlot()
    
#     def quit(self):
#         print(">>>\tExiting")
#         sys.exit()
        
#     def nextPage(self):
#         print("\t   Company: "+variables.__company__)
#         # self.statusBar().showMessage("Switched to window 1")
#         # self.cams = Window1(self.lineEdit1.text()) 
#         self.cams = win_2.Window() 
#         self.cams.show()
#         self.close()

#     def onRadioButton(self):
#         radioBtn = self.sender()
#         if radioBtn.isChecked():
#             variables.__company__ = radioBtn.text()
 




















        
# class Windowx(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         # Windows options
#         self.setWindowTitle('Window1')
#         self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

#         # Declaring layouts
#         layoutV = QVBoxLayout()
#         layoutH = QHBoxLayout()


#         # Text
#         # label1 = QLabel(value)
#         label1 = QLabel(__text__)
#         layoutV.addWidget(label1)

#         # ¿¿BUTTON?
#         self.button = QPushButton()
#         self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
#         self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
#         self.button.setIconSize(QSize(200, 200))
#         layoutV.addWidget(self.button)

#         # Back button
#         self.backButton = QPushButton(self)
#         self.backButton.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
#         self.backButton.setIconSize(QSize(50, 50))
#         # self.backButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
#         # self.backButton.setText('Atrás')
#         self.backButton.clicked.connect(self.goMainWindow)
#         layoutH.addWidget(self.backButton)

#         # Next button
#         self.nextButton = QPushButton(self)
#         self.nextButton.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))
#         self.nextButton.setIconSize(QSize(50, 50))
#         # self.nextButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
#         # self.nextButton.setText('Siguiente')
#         self.nextButton.clicked.connect(self.goThirdWindow)
#         layoutH.addWidget(self.nextButton)
        
        
#         # Layout Positioning
#         layoutV.addLayout(layoutH)
#         self.setLayout(layoutV)



#     def goMainWindow(self):
#         self.cams = Window()
#         self.cams.show()
#         self.close() 
    
#     @pyqtSlot()
#     def goThirdWindow(self):
#         # self.cams = Window2(text_any) 
#         self.cams =window2.Window2() 
#         self.cams.show()
#         self.close()
        
    
# class Windowcx2(QDialog):
#     # def __init__(self, value, parent=None):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         # Windows options
#         self.setWindowTitle('Window2')
#         self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        
#         # Declaring layouts
#         layoutV = QVBoxLayout()
#         layoutH = QHBoxLayout()


#         # Text
#         # label1 = QLabel(value)
#         label1 = QLabel(__text__)
#         layoutV.addWidget(label1)

#         # ¿¿BUTTON?
#         self.button = QPushButton()
#         self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
#         self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
#         self.button.setIconSize(QSize(200, 200))
#         layoutV.addWidget(self.button)
        
#         # Back button
#         self.backButton = QPushButton(self)
#         # self.backButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
#         # self.backButton.setIconSize(QSize(50, 50))
#         self.backButton.setText('Atrás')
#         self.backButton.clicked.connect(self.goFirstWindow)
#         layoutH.addWidget(self.backButton)
        
#         # Next button
#         self.nextButton = QPushButton(self)
#         # self.backButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
#         # self.nextButton.setIconSize(QSize(50, 50))
#         self.nextButton.setText('Siguiente')
#         self.nextButton.clicked.connect(self.goFourthWindow)
#         layoutH.addWidget(self.nextButton)

#         # Layout Positioning
#         layoutV.addLayout(layoutH)
#         self.setLayout(layoutV)

#     def goFirstWindow(self):
#         # self.cams = Window1(text_any)
#         self.cams = win_2.Window()
#         self.cams.show()
#         self.close()    

#     def goFourthWindow(self):
#         self.cams = Window()
#         self.cams.show()
#         self.close() 
        

# # if __name__ == '__main__':
# #     app=QApplication(sys.argv)
# #     ex=Window()
# #     sys.exit(app.exec_())

