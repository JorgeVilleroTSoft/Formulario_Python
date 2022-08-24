from PyQt5.QtGui     import *;
from PyQt5.QtCore    import *;
from PyQt5.QtWidgets import *;
import pandas as pd

import win_2b4;
import variables;

boxText = "¿Guardar y Salir?"
buttonOption1 = "Atrás"
buttonOption2 = "Terminar"

class Window(QDialog):
    def __init__(self):
        super().__init__()

        print(">>>\tWindow Save and quit [2b5]")
        self.setWindowIcon(QIcon('images/icon_decowraps.jpg'))
        self.setWindowTitle('Deco  -  Formulario del Bot.')
        self.resize(340, 288)
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
            '2da parte': ('True' if variables.__stage__=="2da parte Prorrateos y DUTY Analysis." else "False"),
            '3ra parte': ('True' if variables.__stage__=="3ra parte LC for Upload and provision Analysis." else "False"),
            'Fire Cx': ('True' if variables.__upload_fire_cx__=="Sí, cargar los asientos en Fire CX." else "False"),
            'Acctivate': ('True' if variables.__upload_acctivate__=="Sí, cargar los asientos en Acctivate." else "False")
            }
        df = pd.DataFrame.from_dict([dict_to_excel])
        df.to_excel(variables.__path_bot_report_date__, sheet_name = "report", index=False)
        print(">>>\tExiting")
        self.close()

        
    def backPage(self):
        self.cams = win_2b4.Window()
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
        if (variables.__upload_fire_cx__ != "" or variables.__upload_acctivate__ != "") and (variables.__path_duty_analysis__ != "Seleccione el archivo que desea." or variables.__path_apportionment__ != "Seleccione el archivo que desea."):
            text_label = (f"""

    El robot va a ejecutarse para:
        - Empresa: {variables.__company__}
        - {variables.__weekly_close__}
        - {variables.__stage__} 
        - Prorrateos: {variables.__path_apportionment__.split("/")[-1] if variables.__path_apportionment__.split("/")[-1]!= "Seleccione el archivo que desea." else "Archivo no seleccionado."}
        - DUTY Analysis: {variables.__path_duty_analysis__.split("/")[-1] if variables.__path_duty_analysis__.split("/")[-1]!= "Seleccione el archivo que desea." else "Archivo no seleccionado."}
        - {variables.__upload_fire_cx__[4:].capitalize()}
        - {variables.__upload_acctivate__[4:].capitalize()}
        - Para el periodo: {variables.__month__}, {variables.__year__}.
    Recuerde que antes de ejecutar el Bot alguien 
    tiene que estar mirando la pantalla.
            """)
        else:
            text_label = (f"""

    El robot va a ejecutarse para:
        - Empresa: {variables.__company__}
        - {variables.__weekly_close__}
        - {variables.__stage__} 
        - Lc Duty: {variables.__path_lc_duty_bv__.split("/")[-1]}
        - Para el periodo: {variables.__month__}, {variables.__year__}.
    Recuerde que antes de ejecutar el Bot alguien 
    tiene que estar mirando la pantalla.
            """)

        return text_label

# import sys

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex=Window()
#     sys.exit(app.exec_())



