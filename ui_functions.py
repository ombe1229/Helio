from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip
from PySide2.QtCore import Qt

from main import MainWindow

GLOBAL_STATE = 0


class UIFunctions(MainWindow):
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            GLOBAL_STATE = 1
            self.showMaximized()
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: rgb(44, 49, 60); border-radius: 0px;"
            )
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.drop_shadow_layout.setContentsMargins(8, 8, 8, 8)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: rgb(44, 49, 60); border-radius: 8px;"
            )

    def uiDefinitions(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)
        self.ui.btn_maxmize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }"
        )

    def returnStatus():
        return GLOBAL_STATE
