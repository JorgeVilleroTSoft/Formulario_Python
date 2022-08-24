from PyQt5.QtGui     import *;
from PyQt5.QtCore    import *;
from PyQt5.QtWidgets import *;

import win_2;
import win_2a3;
import win_2b2a;
import win_2b3a;
import variables;

boxText = "Elija qué parte del bot desea ejecutar: "
radioButtonOption1 = "1ra parte Check RD, LC DUTY and Change RD."
radioButtonOption2 = "2da parte Prorrateos y DUTY Analysis."
radioButtonOption3 = "3ra parte LC for Upload and provision Analysis."
buttonOption1 = "Atrás"
buttonOption2 = "Siguiente"


class Window(QDialog):
    def __init__(self):
        super().__init__()

        print(">>>\tWindow 2b")
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
        layout.addWidget(self.box,1,0,1,5)

        # RadioButton 1
        self.radioButton(radioButtonOption1)
        if variables.__stage__ == radioButtonOption1:
            self.radioBtn.setChecked(True)
        # RadioButton 2
        self.radioButton(radioButtonOption2)
        if variables.__stage__ == radioButtonOption2:
            self.radioBtn.setChecked(True)
        # RadioButton 3
        self.radioButton(radioButtonOption3)
        if variables.__stage__ == radioButtonOption3:
            self.radioBtn.setChecked(True)

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
        self.cams = win_2.Window()
        self.cams.show()
        self.close()
        
    def nextPage(self):
        # This goes to the next window only if a radiobutton is selected and depends on which one was selected.
        print("\t   Stage: " + variables.__stage__)
        if variables.__stage__ == radioButtonOption1:
            self.cams = win_2a3.Window()
            self.cams.show()
            self.close()
        elif variables.__stage__ == radioButtonOption2:
            self.cams = win_2b2a.Window()
            self.cams.show()
            self.close()
        elif variables.__stage__ == radioButtonOption3:
            self.cams = win_2b3a.Window()
            self.cams.show()
            self.close()
        else:
            self. alertCheck()

    def onRadioButton(self):
        radioBtn = self.sender()
        # Set the variable according to the selected button
        if radioBtn.isChecked():
            variables.__stage__ = radioBtn.text()
 

    def alertCheck(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("No hay una opción seleccionada.")
        messageBox.setText("Por favor, seleccione una opción.")
        messageBox.exec()

    def buttonInGridLayout(self, text :str, row :int, column :int, gridLayout, heightRow=1, widthColumn=1):
        self.button = QPushButton(text, self)
        self.button.setFont(QFont("Sanserif",11))
        if text == "Atrás":
            self.button.clicked.connect(self.backPage)
        elif text == "Siguiente":
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



















