from logging import exception
from PyQt5.QtGui     import *;
from PyQt5.QtCore    import *;
from PyQt5.QtWidgets import *;
import pandas as pd;
import os;

import win_2a;
import win_2a2b;
import variables;

boxText = "Archivo de Excel (LC DUTY): "
buttonOption1 = "Atrás"
buttonOption2 = "Siguiente"

class Window(QDialog):
    def __init__(self):
        super().__init__()

        print(">>>\tWindow 2a2a")
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

        # Editable box
        self.lineEdit = QLineEdit(variables.__path_lc_duty_bv__, self)
        self.layout_groupbox.addWidget(self.lineEdit)

        # Button Browse
        self.buttonBrowse = QPushButton('Examinar', self)
        self.buttonBrowse.setFont(QFont("Sanserif",11))
        self.buttonBrowse.clicked.connect(self.browseFile)
        self.layout_groupbox.addWidget(self.buttonBrowse)

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
        self.cams = win_2a.Window()
        self.cams.show()
        self.close()
        
    def nextPage(self):
        # This goes to the next window only the selected file meets the specification.
            # "the name contains..."
        if "lc duty" in variables.__path_lc_duty_bv__.lower():
            # "the sheets and columns are..."
            if self.checkColumnNames(variables.__path_lc_duty_bv__, variables.__col_lc_duty__, ['ORIGINAL']):
                print("\t   PathFile Lc Duty: " + variables.__path_lc_duty_bv__)
                # Move file(from, to)
                try:
                    os.rename(variables.__path_lc_duty_bv__, variables.__path_lc_duty_bv_to_move__+"\\"+variables.__path_lc_duty_bv__.split("/")[-1])
                    print("\t   File moved to: " + variables.__path_lc_duty_bv_to_move__)
                    self.cams = win_2a2b.Window()
                    self.cams.show()
                except OSError as e:
                    print('No folder exists at the location specified.\nError:',e)
                    self.cams = folderAccesDenied()
                    self.cams.show()
                self.close()
            else:
                self. alertCheck()
        else:
            self. alertCheck()

    def alertCheck(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Error sobre el archivo seleccionado.")
        messageBox.setText("Error en el archivo seleccionado.\nExtienda los detalles para conocer qué características debe tener.")
        # Add a button and a dropdown text to the window
        messageBox.setDetailedText(f"""Nombre del archivo:
    - Debe contener "LC DUTY".
El Excel debe tener la siguiente hoja y columnas correspondientes (en el orden presentado):
    - Planilla "ORIGINAL": {variables.__col_lc_duty__["ORIGINAL"]}
    """)
    # - Planilla "PO": {variables.__col_lc_duty__["PO"]}
    # - Planilla "RD": {variables.__col_lc_duty__["RD"]}
    # - Planilla "Consolidates": {variables.__col_lc_duty__["Consolidates"]}
    # - Planilla "W4": {variables.__col_lc_duty__["W4"]}
    # """)
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

    def browseFile(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', variables.__path_lc_duty_bv__, 'Excel files(*.xlsx *.xls)')
        if fname[0] != "":
            self.lineEdit.setText(fname[0])
        variables.__path_lc_duty_bv__ = self.lineEdit.text()

    def checkColumnNames(self, path :str, dict_excel :dict, list_sheets :list =[0,0,0]):
        '''If no list is given, this function will compare the whole Excel file (all sheets available).'''
        xl = pd.ExcelFile(path)
        sheetnames = xl.sheet_names
        dict_columns = {}
        if list_sheets == [0,0,0]:
            for item in sheetnames:
                if item in dict_excel.keys():
                    df = pd.read_excel(xl, sheet_name=item)
                    column_list = list(df.columns)
                    dict_columns[item] = column_list
                    boolReturn = dict_excel == dict_columns
                else:
                    boolReturn = False
        else:
            dict_excel_compare={}
            for item in list_sheets:
                if item in dict_excel.keys() and item in sheetnames:
                    df = pd.read_excel(xl, sheet_name=item)
                    column_list = list(df.columns)
                    dict_columns[item] = column_list
                    dict_excel_compare[item] = dict_excel[item]
                    boolReturn = dict_excel_compare == dict_columns 
                else:
                    boolReturn = False
        return boolReturn

class folderAccesDenied(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(folderAccesDenied, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('images/icon_decowraps.jpg'))
        self.setWindowTitle("ERROR.")
        self.setFixedSize(200, 150)
        self.label = QLabel("""
NO TIENE ACCESO A LA CARPETA
DONDE DEBE GUARDAR EL 
ARCHIVO.""", self)
        self.label.setGeometry(10,-15,180,100)
        self.buttonOk = QPushButton("Terminar",self)
        self.buttonOk.setGeometry(70,90,60,40)
        self.buttonOk.clicked.connect(self.quit)
    def quit(self):
        print(">>>\tExiting")
        self.close()




# import sys

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     ex=Window()
#     sys.exit(app.exec_())
































# from PyQt5.QtGui     import *;
# from PyQt5.QtCore    import *;
# from PyQt5.QtWidgets import *;
# import win_3;

# import win_3b2;
# import os;

# import variables


# class Window(QDialog):
#     def __init__(self):
#         super().__init__()

#         print(">>>\tWindow 3-b-1")

#         # variables.__path_lc_duty_bv__ = "asdfasdf"
  
#         # # Global variable???
#         # global __path_lc_duty_bv__
#         # __path_lc_duty_bv__ = os.path.join("C:\\", "Bv", "2. Input File for LC for Upload (USER)")


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


#         # self.lineEdit = QLineEdit("Type here what you want to transfer for [Window1]."+text_any, self)
#         self.lineEdit = QLineEdit(variables.__path_lc_duty_bv__, self)
#         self.lineEdit.setGeometry(250, 100, 400, 30)
#         layoutV.addWidget(self.lineEdit)


#         # Button Browse
#         self.buttonBrowse = QPushButton('Examinar', self)
#         # self.buttonNext.move(100, 100)
#         self.buttonBrowse.setFont(QFont("Sanserif",11))
#         self.buttonBrowse.clicked.connect(self.browseFile)
#         layoutV.addWidget(self.buttonBrowse)


   
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
#         layoutV.addLayout(layoutH)
#         self.setLayout(layoutV)



#         self.show()


        
#     def goMainWindow(self):
#         self.cams = win_3.Window()
#         self.cams.show()
#         self.close() 
        
#     def goThirdWindow(self):
#         # self.cams = Window2(text_any) 
#         print("\t   Path file: "+variables.__path_lc_duty_bv__)
#         self.cams = win_3b2.Window() 
#         self.cams.show()
#         self.close()

#     def browseFile(self):

#         fname=QFileDialog.getOpenFileName(self, 'Open file', variables.__path_lc_duty_bv__, 'Excel files(*.xlsx *xls)')
#         if fname[0] != "":
#             self.lineEdit.setText(fname[0])
        
#         # global __path_lc_duty_bv__
#         variables.__path_lc_duty_bv__ = self.lineEdit.text()


