import sys


from main_window import MainWindow
from info import Info
from display import Display
from PySide6.QtWidgets import QApplication, QLineEdit
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH


if __name__ == '__main__':

    #Cria aplicação

    app = QApplication(sys.argv)
    window = MainWindow()


    #Definindo o icone

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info

    info = Info('2 ^ 10.0 = 1024')
    window.addToLayout(info)

    #Display

    display = Display()
    window.addToLayout(display)
    #window.addToLayout(Display('Display 2'))
    #window.addToLayout(Display('Display 3'))

    #Resolvendo o problema da profundidade de nível     window.v_layout.addWidget(label1)
   
    window.adjustFixedSize()
    window.show()
    app.exec_()