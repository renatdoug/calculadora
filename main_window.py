import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget



class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None, *args, **kwargs ) -> None:

        super().__init__(parent, *args, **kwargs)


        # Configurado o layout básico

        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout) 
        self.setCentralWidget(self.cw)

        #Titulo da janela

        self.setWindowTitle('Calcuradora')
                 

    def adjustFixedSize(self):

        #Última coisa a ser feita

        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    

    #Resolvendo a profundidade dos níveis

    def addToLayout(self, widget:QWidget):
        self.vLayout.addWidget(widget)
       