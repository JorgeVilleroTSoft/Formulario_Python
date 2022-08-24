from PyQt5.QtGui     import *;
from PyQt5.QtCore    import *;
from PyQt5.QtWidgets import *;

import win_2a2a;
import win_2a2c;
import win_2a3;
import variables;

boxText = "¿Desea cargar los asientos en Fire CX?"
radioButtonOption1 = "Sí, cargar los asientos en Fire CX."
radioButtonOption2 = "No, no cargar los asientos en Fire CX."
buttonOption1 = "Atrás"
buttonOption2 = "Siguiente"
buttonOption3 = "Tax Name"


class Window(QDialog):
    def __init__(self):
        super().__init__()

        print(">>>\tWindow 2a2b")
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
        self.layout_groupbox = QVBoxLayout(self.box)
        layout.addWidget(self.box,1,1,1,3)

        # RadioButton BV
        self.radioButton(radioButtonOption1)
        if variables.__upload_fire_cx__ == radioButtonOption1:
            self.radioBtn.setChecked(True)
        # RadioButton HH
        self.radioButton(radioButtonOption2)
        if variables.__upload_fire_cx__ == radioButtonOption2:
            self.radioBtn.setChecked(True)

        # Button Tax Name
        self.buttonInGridLayout(buttonOption3, 2, 1, layout, 1,3)

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
        self.cams = win_2a2a.Window()
        self.cams.show()
        self.close()
        
    def nextPage(self):
        # This goes to the next window only if a radiobutton is selected and depends on which one was selected.
        if variables.__upload_fire_cx__ == radioButtonOption1:
            print("\t   Upload to Fire CX: " + variables.__upload_fire_cx__)
            self.cams = win_2a2c.Window()
            self.cams.show()
            self.close()
        elif variables.__upload_fire_cx__ == radioButtonOption2:
            print("\t   Upload to Fire CX: " + variables.__upload_fire_cx__)
            self.cams = win_2a3.Window()
            self.cams.show()
            self.close()
        else:
            self. alertCheck()
        

    def onRadioButton(self):
        radioBtn = self.sender()
        # Set the variable according to the selected button
        if radioBtn.isChecked():
            variables.__upload_fire_cx__ = radioBtn.text()
 

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
        elif text == buttonOption3:
            self.button.clicked.connect(self.winTax)
        gridLayout.addWidget(self.button, row, column, heightRow, widthColumn)

    def winTax(self):
        dialog = EditorTax(self)
        dialog.show()

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


class EditorTax(QMainWindow):
    def __init__(self, *args, **kwargs):
        #This window is not responsive, its sizes and positions are fixed.
        super(EditorTax, self).__init__(*args, **kwargs)
        self.setWindowTitle("Editar Tax Names")
        self.setFixedSize(400, 400)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(25,20,350,300)

        self.buttonOk = QPushButton("Guardar",self)
        self.buttonOk.setGeometry(200,330,60,40)

        self.buttonnCancelar = QPushButton("Atrás",self)
        self.buttonnCancelar.setGeometry(130,330,60,40)

        self.buttonnCancelar.clicked.connect(self.salir)
        self.buttonOk.clicked.connect(self.guardarMod)

    def showEvent(self,event): 
        # Open text file.
        fileTaxName = open (variables.__path_tax_name__,'r')
        # Read file
        textFileTaxName = fileTaxName.read()
        fileTaxName.close()
        # Show file text
        self.textEdit.insertPlainText(textFileTaxName)
         

    def salir(self):
        self.close()

    def guardarMod(self):
        self. alertCheck()
        newTextModif = self.textEdit.toPlainText()
        # Open text file.
        fileTaxName = open (variables.__path_tax_name__,'w')
        # Modify file
        fileTaxName.write (newTextModif)
        fileTaxName.close()

    def alertCheck(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Guardando el archivo Tax Name.")
        messageBox.setText("El archivo se guardó satisfactoriamente.")
        messageBox.exec()


# class EditorVendor(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super(EditorVendor, self).__init__(*args, **kwargs)
#         self.setWindowTitle("Editar...")
#         self.setFixedSize(400, 400)

#         self.textEdit = QTextEdit(self)
#         self.textEdit.setGeometry(25,20,350,300)

#         self.buttonOk = QPushButton("Guardar",self)
#         self.buttonOk.setGeometry(130,330,60,40)
#         self.buttonOk.clicked.connect(self.guardarMod)

#         self.buttonnCancelar = QPushButton("Cancelar",self)
#         self.buttonnCancelar.setGeometry(200,330,60,40)
#         self.buttonnCancelar.clicked.connect(self.salir)


#     def showEvent(self,event):            
#         fileVendorLocPurchase = open ('Vendor Local Purchase.txt','r')
#         textFileVendorLocPurchase = fileVendorLocPurchase.read()
#         fileVendorLocPurchase.close()
#         self.textEdit.insertPlainText(textFileVendorLocPurchase)

#     def salir(self):
#         self.close()

#     def guardarMod(self):
#         newTextModif = self.textEdit.toPlainText()
#         fileVendorLocPurchase = open ('Vendor Local Purchase.txt','w')
#         fileVendorLocPurchase.write (newTextModif)
#         fileVendorLocPurchase.close()

#     def alertCheck(self):
#         messageBox = QMessageBox()
#         messageBox.setWindowTitle("Guardando el archivo Tax Name.")
#         messageBox.setText("El archivo se guardó satisfactoriamente.")
#         messageBox.exec()



# import sys 

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex= Window()
#     sys.exit(app.exec_())




































# from PyQt5.QtGui     import *;
# from PyQt5.QtCore    import *;
# from PyQt5.QtWidgets import *;
# import win_3b1;
# import win_4;

# import variables;


# class Window(QDialog):
#     def __init__(self):
#         super().__init__()

#         print(">>>\tWindow 3-b-2")

#         self.setWindowTitle('Window 1')
#         # self.setGeometry(250, 100, 400, 400)
#         # self.resize(300, 240)s
#         self.resize(400, 400)



#         # Declaring layouts
#         layoutV = QVBoxLayout()
#         layoutH = QHBoxLayout()
#         layoutH2 = QHBoxLayout()
#         layoutV2 = QVBoxLayout()


#         self.labelSpaceBetweenButtons = QLabel("  ")

#         self.labelIndication = QLabel("Coloque la ruta del archivo: ")
#         self.labelIndication.setFont(QFont("Sanserif",13))
#         layoutV.addWidget(self.labelIndication)


#         #Crear los RadioButtons
#         self.radioBtnBv = QRadioButton('Sí, subir los archivos a Acctivates.',self)
#         self.radioBtnBv.setFont(QFont("Sanserif",13))
#         # self.radioBtnBv.setGeometry(700,110,82,17)
#         self.radioBtnBv.toggled.connect(self.onRadioButton)
#         layoutV.addWidget(self.radioBtnBv)
#         # self.radioBtnBv.setChecked(True)
#         # layoutH2.addWidget(self.labelSpaceBetweenButtons)
#         # layoutH2.addWidget(self.radioBtnBv)
#         self.radioBtnHh = QRadioButton('No, no subir los archivos a Acctivates.',self)
#         self.radioBtnHh.setFont(QFont("Sanserif",13))
#         # self.radioBtnHh.setGeometry(700,140,82,17)
#         self.radioBtnHh.toggled.connect(self.onRadioButton)
#         layoutV.addWidget(self.radioBtnHh)
#         # layoutH2.addWidget(self.radioBtnHh)
#         # layoutH2.addWidget(self.labelSpaceBetweenButtons)
#         #############################################################################
#         #############################################################################
#         ##################### ADD THAT IT CAN GO AHEAD JUST IF BV semanal o cierre IS SELECTED ##########
#         ########## ADD THAT WHEN THE company IS SELECTED, then go to the next windows and go back, then keep it SELECTED ##########
#         #############################################################################
#         #############################################################################


#         # layoutV.addWidget(self.labelSpaceBetweenButtons)



#         layoutH2.addWidget(self.labelSpaceBetweenButtons)

#         # Button Tax
#         self.buttonTax = QPushButton('Tax Name', self)
#         # self.buttonTax.move(100, 100)
#         self.buttonTax.setFont(QFont("Sanserif",11))
#         self.buttonTax.clicked.connect(self.winTax)
#         layoutH2.addWidget(self.buttonTax)
        

#         layoutH2.addWidget(self.labelSpaceBetweenButtons)



#         # # Button Vendor
#         # self.buttonVendor = QPushButton('Vendor', self)
#         # # self.buttonVendor.move(100, 100)
#         # self.buttonVendor.setFont(QFont("Sanserif",11))
#         # self.buttonVendor.clicked.connect(self.winVendor)
#         # layoutH2.addWidget(self.buttonVendor)

#         # layoutH2.addWidget(self.labelSpaceBetweenButtons)




   
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

#         # self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1]."+text_any, self)
#         # self.lineEdit1 = QLineEdit("Type here... "+__text__, self)
#         # self.lineEdit1.setGeometry(250, 100, 400, 30)
#         # layoutH.addWidget(self.lineEdit1)

#         # Layout Positioning
#         layoutV.addLayout(layoutH2)
#         layoutV.addLayout(layoutH)
#         self.setLayout(layoutV)


#         self.show()


#     def winTax(self):
#         dialog= EditorTax(self)
#         dialog.show()
        
#     def winVendor(self):
#         dialog= EditorVendor(self)
#         dialog.show()
        
#     def goMainWindow(self):
#         self.cams = win_3b1.Window()
#         self.cams.show()
#         self.close() 
        
#     def goThirdWindow(self):
#         # self.cams = Window2(text_any) 
#         print("\t   Acctivate: "+variables.__upload_acctivate__)
#         self.cams = win_4.Window() 
#         self.cams.show()
#         self.close()


#     def onRadioButton(self):
#         radioBtn = self.sender()
#         if radioBtn.isChecked():
#             variables.__upload_acctivate__ = radioBtn.text()



