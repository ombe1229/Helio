import sys
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QMouseEvent, QKeyEvent
from PySide2.QtWidgets import QApplication, QMainWindow


from ui_main import Ui_MainWindow
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def moveWindow(event: QMouseEvent):
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.setMinimumSize(QSize(500, 400))
        self.setWindowIcon(QIcon("saebasol.icon.png"))
        self.setWindowTitle("Helio")

        self.show()

    def mousePressEvent(self, event: QMouseEvent):
        self.dragPos = event.globalPos()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())