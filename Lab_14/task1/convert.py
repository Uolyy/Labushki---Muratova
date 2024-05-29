
################################################################################
## Form generated from reading UI file 'convert.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resourse_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(675, 275)
        icon1 = QIcon()
        icon1.addFile(u":/icon/conv.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon1)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: #333;\n"
"	background-color: #E6E6FA;\n"
"	font-family: 'Constantia Bold';\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #787878;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #D8BFD8;\n"
"	border: 1px solid #a6a6a6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #e8c5e8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #ba70ba;\n"
"	border: 1px solid #7a7a7a;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"   	background-color: #D8BFD8;\n"
"   	padding: 4px;\n"
"	border: 1px solid #a6a6a6;\n"
"}\n"
"\n"
"QRadioButton::checked {\n"
"	background-color: #ba70ba;\n"
"	border: 1px solid #7a7a7a;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	background-color: #e8c5e8;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_rub_in = QRadioButton(self.centralwidget)
        self.btn_rub_in.setObjectName(u"btn_rub_in")

        self.gridLayout.addWidget(self.btn_rub_in, 2, 1, 1, 1)

        self.btn_rub_out = QPushButton(self.centralwidget)
        self.btn_rub_out.setObjectName(u"btn_rub_out")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rub_out.sizePolicy().hasHeightForWidth())
        self.btn_rub_out.setSizePolicy(sizePolicy)
        self.btn_rub_out.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_rub_out, 2, 5, 1, 1)

        self.btn_eur_out = QPushButton(self.centralwidget)
        self.btn_eur_out.setObjectName(u"btn_eur_out")
        sizePolicy.setHeightForWidth(self.btn_eur_out.sizePolicy().hasHeightForWidth())
        self.btn_eur_out.setSizePolicy(sizePolicy)
        self.btn_eur_out.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_eur_out, 2, 7, 1, 1)

        self.btn_usd_in = QRadioButton(self.centralwidget)
        self.btn_usd_in.setObjectName(u"btn_usd_in")

        self.gridLayout.addWidget(self.btn_usd_in, 2, 2, 1, 1)

        self.text_out = QLabel(self.centralwidget)
        self.text_out.setObjectName(u"text_out")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_out.sizePolicy().hasHeightForWidth())
        self.text_out.setSizePolicy(sizePolicy1)
        self.text_out.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.text_out, 1, 5, 1, 3)

        self.line_out = QLineEdit(self.centralwidget)
        self.line_out.setObjectName(u"line_out")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_out.sizePolicy().hasHeightForWidth())
        self.line_out.setSizePolicy(sizePolicy2)
        self.line_out.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_out.setReadOnly(True)

        self.gridLayout.addWidget(self.line_out, 3, 5, 1, 3)

        self.icon = QLabel(self.centralwidget)
        self.icon.setObjectName(u"icon")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy3)
        self.icon.setPixmap(QPixmap(u":/icon/conv.png"))

        self.gridLayout.addWidget(self.icon, 3, 4, 1, 1)

        self.btn_usd_out = QPushButton(self.centralwidget)
        self.btn_usd_out.setObjectName(u"btn_usd_out")
        sizePolicy.setHeightForWidth(self.btn_usd_out.sizePolicy().hasHeightForWidth())
        self.btn_usd_out.setSizePolicy(sizePolicy)
        self.btn_usd_out.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_usd_out, 2, 6, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(True)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 7)

        self.btn_eur_in = QRadioButton(self.centralwidget)
        self.btn_eur_in.setObjectName(u"btn_eur_in")

        self.gridLayout.addWidget(self.btn_eur_in, 2, 3, 1, 1)

        self.line_in = QLineEdit(self.centralwidget)
        self.line_in.setObjectName(u"line_in")
        sizePolicy2.setHeightForWidth(self.line_in.sizePolicy().hasHeightForWidth())
        self.line_in.setSizePolicy(sizePolicy2)
        self.line_in.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_in, 3, 1, 1, 3)

        self.text_in = QLabel(self.centralwidget)
        self.text_in.setObjectName(u"text_in")
        sizePolicy1.setHeightForWidth(self.text_in.sizePolicy().hasHeightForWidth())
        self.text_in.setSizePolicy(sizePolicy1)
        self.text_in.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.text_in, 1, 1, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0432\u0435\u0440\u0442\u0435\u0440 \u0432\u0430\u043b\u044e\u0442", None))
        self.btn_rub_in.setText(QCoreApplication.translate("MainWindow", u"RUB", None))
        self.btn_rub_out.setText(QCoreApplication.translate("MainWindow", u"RUB", None))
        self.btn_eur_out.setText(QCoreApplication.translate("MainWindow", u"EUR", None))
        self.btn_usd_in.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.text_out.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0432\u0430\u043b\u044e\u0442\u0443", None))
        self.line_out.setText("")
        self.icon.setText("")
        self.btn_usd_out.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.label.setText("")
        self.btn_eur_in.setText(QCoreApplication.translate("MainWindow", u"EUR", None))
        self.line_in.setText("")
        self.text_in.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437 \u0432\u0430\u043b\u044e\u0442\u044b", None))
    # retranslateUi

