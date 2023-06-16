import sys
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variaables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    #Definindo o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    label1 = QLabel('Renato Douglas')
    label1.setStyleSheet('font-size: 50px;color: red')

    #Resolvendo o problema da profundidade de nível     window.v_layout.addWidget(label1)
    window.addWidgetToLayout(label1)

    window.adjustFixedSize()

    window.show()
    app.exec_()