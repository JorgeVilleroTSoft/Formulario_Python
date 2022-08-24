from PyQt5.QtGui     import *;
from PyQt5.QtCore    import *;
from PyQt5.QtWidgets import *;
import pandas as pd

import win_2a3;
import variables;

boxText = "¿Guardar y Salir?"
buttonOption1 = "Atrás"
buttonOption2 = "Terminar"

class Window(QDialog):
    def __init__(self):
        super().__init__()

        print(">>>\tWindow Save and quit [2a4]")
        self.setWindowIcon(QIcon('images/icon_decowraps.jpg'))
        self.setWindowTitle('Deco  -  Formulario del Bot.')
        self.resize(340, 278)
        self.setMinimumSize(220, 220)
        self.setMaximumSize(380, 400)

        # Declaring layouts
        layout = QGridLayout()

        # Top Image
        self.image("images/decowraps.png", 200, 0, 0, 1, 5, layout, Qt.AlignHCenter)

        # Box contaning radio Buttons
        self.box = QGroupBox(boxText)
        self.box.setStyleSheet("""QGroupBox {color: rgb(1, 130, 153); font-weight: bold; }""")
        self.layout_groupbox = QVBoxLayout(self.box)
        layout.addWidget(self.box,1,1,1,3)

        # Label
        label_text = self.label_text()
        self.labelIndication = QLabel(label_text)
        layout.addWidget(self.labelIndication,1,1,1,3)

        # Empty space
        self.labelEmpty = QLabel("")
        layout.addWidget(self.labelEmpty,2,0,1,5)

        # Button End
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
    def quit(self):
        dict_to_excel = {
            'Month':variables.__month_as_int__,
            'Year':variables.__year_as_int__,
            'Bv': ('True' if variables.__company__=="BV" else "False"),
            'Bv Semanal': ('True' if variables.__weekly_close__=="Bv Semanal" else "False"),
            'Bv Cierre': ('True' if variables.__weekly_close__=="Bv Cierre" else "False"),
            '1ra parte': ('True' if variables.__stage__=="1ra parte Check RD, LC DUTY and Change RD." else "False"),
            '2da parte': ('True' if variables.__stage__=="2da parte LC for Upload." else "False"),
            '3ra parte': ('False' if variables.__stage__=="3ra parte LC for Upload and provision Analysis." else "False"),
            'Fire Cx': ('True' if variables.__upload_fire_cx__=="Sí, cargar los asientos en Fire CX." else "False"),
            'Acctivate': ('True' if variables.__upload_acctivate__=="Sí, cargar los asientos en Acctivate." else "False")
            }
        print(dict_to_excel)
        df = pd.DataFrame.from_dict([dict_to_excel])
        df.to_excel(variables.__path_bot_report_date__, sheet_name = "report", index=False)
        print(">>>\tExiting")
        self.close()


        
    def backPage(self):
        self.cams = win_2a3.Window()
        self.cams.show()
        self.close()

    def alertCheck(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Terminar")
        messageBox.setText("¿Está seguro que desea guardar los datos cargados?\nEl bot se ejecutará de acuerdo a los datos cargados en este formulario.")
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        messageBox.buttonClicked.connect(self.quitornot)
        messageBox.exec()

    def quitornot(self,i):
        print ("Button pressed is:",i.text()[1:])
        if i.text() == "&Yes":
            self.quit()

            
    def buttonInGridLayout(self, text :str, row :int, column :int, gridLayout, heightRow=1, widthColumn=1):
        self.button = QPushButton(text, self)
        self.button.setFont(QFont("Sanserif",11))
        if text == buttonOption1:
            self.button.clicked.connect(self.backPage)
        elif text == buttonOption2:
            self.button.clicked.connect(self.alertCheck)
        gridLayout.addWidget(self.button, row, column, heightRow, widthColumn)

    def image(self, path :str, scaledToWidth :int, row :int, column :int, heightRow :int, widthColumn :int, gridLayout, align=Qt.AlignLeading):
        self.labelPic2 = QLabel(self)
        pic2 = QPixmap(path)
        pic2 = pic2.scaledToWidth(scaledToWidth)
        self.labelPic2.setPixmap(pic2)
        gridLayout.addWidget(self.labelPic2, row, column, heightRow, widthColumn, align)

    def label_text(self):
        # Text shown will depend on which path was followed to get here.
        if (variables.__weekly_close__ == "Bv Semanal" and variables.__upload_fire_cx__ == "") and variables.__upload_acctivate__ == "" and variables.__path_lc_duty_bv__ == "Seleccione el archivo que desea." or variables.__weekly_close__ == "Bv Cierre":
            text_label = (f"""

    El robot va a ejecutarse para:
        - Empresa: {variables.__company__}
        - {variables.__weekly_close__}
        - {variables.__stage__} 
        - Para el periodo: {variables.__month__}, {variables.__year__}.
    Recuerde que antes de ejecutar el Bot alguien 
    tiene que estar mirando la pantalla.
            """)
        elif variables.__weekly_close__ == "Bv Semanal":
            text_label = (f"""

    El robot va a ejecutarse para:
        - Empresa: {variables.__company__}
        - {variables.__weekly_close__}
        - {variables.__stage__} 
        - Lc Duty: {variables.__path_lc_duty_bv__.split("/")[-1]}
        - {variables.__upload_fire_cx__[4:].capitalize()}
        - {variables.__upload_acctivate__[4:].capitalize()}
        - Para el periodo: {variables.__month__}, {variables.__year__}.
    Recuerde que antes de ejecutar el Bot alguien 
    tiene que estar mirando la pantalla.
            """)

        return text_label

# If you want to resize fonts based on the layout size: https://stackoverflow.com/questions/29852498/syncing-label-fontsize-with-layout-in-pyqt

# import sys

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex=Window()
#     sys.exit(app.exec_())




























# from PyQt5.QtGui     import *;
# from PyQt5.QtCore    import *;
# from PyQt5.QtWidgets import *;
# import win_3a1;

# import variables;
# import win_3b2


# class Window(QDialog):
#     def __init__(self):
#         super().__init__()

#         print(">>>\tWindow Save and quit")

#         self.setWindowTitle('Window 4: Guardar y Salir')
#         # self.setGeometry(250, 100, 400, 400)
#         # self.resize(300, 240)s
#         self.resize(400, 400)



#         # Declaring layouts
#         layoutV = QVBoxLayout()
#         layoutH = QHBoxLayout()
#         layoutH2 = QHBoxLayout()
#         layoutV2 = QVBoxLayout()


#         self.labelSpaceBetweenButtons = QLabel("  ")

#         self.labelIndication = QLabel("¿Guardar y Salir?")
#         self.labelIndication.setFont(QFont("Sanserif",13))
#         layoutV.addWidget(self.labelIndication)



   
#         layoutH.addWidget(self.labelSpaceBetweenButtons)

#         # Button Quit
#         self.button = QPushButton('Atrás', self)
#         # self.button.move(100, 100)
#         self.button.setFont(QFont("Sanserif",11))
#         self.button.clicked.connect(self.goMainWindow)
#         layoutH.addWidget(self.button)
        

#         layoutH.addWidget(self.labelSpaceBetweenButtons)



#         # Button Next
#         self.buttonNext = QPushButton('Guardar y Salir', self)
#         # self.buttonNext.move(100, 100)
#         self.buttonNext.setFont(QFont("Sanserif",11))
#         self.buttonNext.clicked.connect(self.goThirdWindow)
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


        


#     def goMainWindow(self):
#         # self.cams = Window2(text_any) 
#         print("\t   Stage: "+variables.__stage__)
#         if variables.__stage__ == '1ra parte Check RD, LC DUTY and Change RD':
#             self.cams = win_3a1.Window()
#             self.cams.show()
#             self.close()
#         elif variables.__stage__ == '2da parte LC for Upload':
#             self.cams = win_3b2.Window()
#             self.cams.show()
#             self.close()
        
#     def goThirdWindow(self):
#         print(">>>\tQuiting")
#         sys.exit()


#     def onRadioButton(self):
#         radioBtn = self.sender()
#         if radioBtn.isChecked():
#             variables.__upload_acctivate__ = radioBtn.text()








# # import sys


# # if __name__ == '__main__':
# #     app=QApplication(sys.argv)
# #     ex=Window3()
# #     sys.exit(app.exec_())

