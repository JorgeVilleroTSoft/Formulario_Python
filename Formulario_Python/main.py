# import os;
import sys;
from PyQt5.QtGui     import *;
from PyQt5.QtCore    import *;
from PyQt5.QtWidgets import *;

import win_1;


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=win_1.Window()
    app.exec_()
    del ex, app
    # sys.exit(app.exec_())
 