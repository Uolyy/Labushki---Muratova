################################################################################
## Form generated from reading UI file '╨╛╨║╨╜╨╛.ui'
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
                               QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)
import picture_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(314, 466)
        icon = QIcon()
        icon.addFile(u":/icon/\u043a\u043e\u0442\u043e\u0432\u043e\u0435.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                 "	background-color: #FFDEAD;\n"
                                 "	font-family: 'Montserrat';\n"
                                 "	font-size: 16pt;\n"
                                 "	font-weight: 600;\n"
                                 "	color: #212121;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "	background-color: #F4A460;\n"
                                 "	border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: #f7b77e;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: #CD853F;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: #696969;")
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setObjectName(u"line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_edit.sizePolicy().hasHeightForWidth())
        self.line_edit.setSizePolicy(sizePolicy1)
        self.line_edit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.line_edit.setStyleSheet(u"font-size: 35pt;\n"
                                     "border: none;")
        self.line_edit.setMaxLength(10)
        self.line_edit.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)
        self.line_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.line_edit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.but_7 = QPushButton(self.centralwidget)
        self.but_7.setObjectName(u"but_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.but_7.sizePolicy().hasHeightForWidth())
        self.but_7.setSizePolicy(sizePolicy2)
        self.but_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_7, 1, 0, 1, 1)

        self.but_4 = QPushButton(self.centralwidget)
        self.but_4.setObjectName(u"but_4")
        sizePolicy2.setHeightForWidth(self.but_4.sizePolicy().hasHeightForWidth())
        self.but_4.setSizePolicy(sizePolicy2)
        self.but_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_4, 2, 0, 1, 1)

        self.but_clear = QPushButton(self.centralwidget)
        self.but_clear.setObjectName(u"but_clear")
        sizePolicy2.setHeightForWidth(self.but_clear.sizePolicy().hasHeightForWidth())
        self.but_clear.setSizePolicy(sizePolicy2)
        self.but_clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_clear, 0, 0, 1, 1)

        self.but_1 = QPushButton(self.centralwidget)
        self.but_1.setObjectName(u"but_1")
        sizePolicy2.setHeightForWidth(self.but_1.sizePolicy().hasHeightForWidth())
        self.but_1.setSizePolicy(sizePolicy2)
        self.but_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_1, 3, 0, 1, 1)

        self.but_0 = QPushButton(self.centralwidget)
        self.but_0.setObjectName(u"but_0")
        sizePolicy2.setHeightForWidth(self.but_0.sizePolicy().hasHeightForWidth())
        self.but_0.setSizePolicy(sizePolicy2)
        self.but_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_0, 4, 1, 1, 1)

        self.but_sign = QPushButton(self.centralwidget)
        self.but_sign.setObjectName(u"but_sign")
        sizePolicy2.setHeightForWidth(self.but_sign.sizePolicy().hasHeightForWidth())
        self.but_sign.setSizePolicy(sizePolicy2)
        self.but_sign.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_sign, 4, 0, 1, 1)

        self.but_tochka = QPushButton(self.centralwidget)
        self.but_tochka.setObjectName(u"but_tochka")
        sizePolicy2.setHeightForWidth(self.but_tochka.sizePolicy().hasHeightForWidth())
        self.but_tochka.setSizePolicy(sizePolicy2)
        self.but_tochka.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_tochka, 4, 2, 1, 1)

        self.but_rez = QPushButton(self.centralwidget)
        self.but_rez.setObjectName(u"but_rez")
        sizePolicy2.setHeightForWidth(self.but_rez.sizePolicy().hasHeightForWidth())
        self.but_rez.setSizePolicy(sizePolicy2)
        self.but_rez.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_rez, 4, 3, 1, 1)

        self.but_2 = QPushButton(self.centralwidget)
        self.but_2.setObjectName(u"but_2")
        sizePolicy2.setHeightForWidth(self.but_2.sizePolicy().hasHeightForWidth())
        self.but_2.setSizePolicy(sizePolicy2)
        self.but_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_2, 3, 1, 1, 1)

        self.but_5 = QPushButton(self.centralwidget)
        self.but_5.setObjectName(u"but_5")
        sizePolicy2.setHeightForWidth(self.but_5.sizePolicy().hasHeightForWidth())
        self.but_5.setSizePolicy(sizePolicy2)
        self.but_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_5, 2, 1, 1, 1)

        self.but_8 = QPushButton(self.centralwidget)
        self.but_8.setObjectName(u"but_8")
        sizePolicy2.setHeightForWidth(self.but_8.sizePolicy().hasHeightForWidth())
        self.but_8.setSizePolicy(sizePolicy2)
        self.but_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_8, 1, 1, 1, 1)

        self.but_ce = QPushButton(self.centralwidget)
        self.but_ce.setObjectName(u"but_ce")
        sizePolicy2.setHeightForWidth(self.but_ce.sizePolicy().hasHeightForWidth())
        self.but_ce.setSizePolicy(sizePolicy2)
        self.but_ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_ce, 0, 1, 1, 1)

        self.but_backspace = QPushButton(self.centralwidget)
        self.but_backspace.setObjectName(u"but_backspace")
        sizePolicy2.setHeightForWidth(self.but_backspace.sizePolicy().hasHeightForWidth())
        self.but_backspace.setSizePolicy(sizePolicy2)
        self.but_backspace.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_backspace, 0, 2, 1, 1)

        self.but_div = QPushButton(self.centralwidget)
        self.but_div.setObjectName(u"but_div")
        sizePolicy2.setHeightForWidth(self.but_div.sizePolicy().hasHeightForWidth())
        self.but_div.setSizePolicy(sizePolicy2)
        self.but_div.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_div, 0, 3, 1, 1)

        self.but_multi = QPushButton(self.centralwidget)
        self.but_multi.setObjectName(u"but_multi")
        sizePolicy2.setHeightForWidth(self.but_multi.sizePolicy().hasHeightForWidth())
        self.but_multi.setSizePolicy(sizePolicy2)
        self.but_multi.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_multi, 1, 3, 1, 1)

        self.but_9 = QPushButton(self.centralwidget)
        self.but_9.setObjectName(u"but_9")
        sizePolicy2.setHeightForWidth(self.but_9.sizePolicy().hasHeightForWidth())
        self.but_9.setSizePolicy(sizePolicy2)
        self.but_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_9, 1, 2, 1, 1)

        self.but_6 = QPushButton(self.centralwidget)
        self.but_6.setObjectName(u"but_6")
        sizePolicy2.setHeightForWidth(self.but_6.sizePolicy().hasHeightForWidth())
        self.but_6.setSizePolicy(sizePolicy2)
        self.but_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_6, 2, 2, 1, 1)

        self.but_min = QPushButton(self.centralwidget)
        self.but_min.setObjectName(u"but_min")
        sizePolicy2.setHeightForWidth(self.but_min.sizePolicy().hasHeightForWidth())
        self.but_min.setSizePolicy(sizePolicy2)
        self.but_min.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_min, 2, 3, 1, 1)

        self.but_plus = QPushButton(self.centralwidget)
        self.but_plus.setObjectName(u"but_plus")
        sizePolicy2.setHeightForWidth(self.but_plus.sizePolicy().hasHeightForWidth())
        self.but_plus.setSizePolicy(sizePolicy2)
        self.but_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_plus, 3, 3, 1, 1)

        self.but_3 = QPushButton(self.centralwidget)
        self.but_3.setObjectName(u"but_3")
        sizePolicy2.setHeightForWidth(self.but_3.sizePolicy().hasHeightForWidth())
        self.but_3.setSizePolicy(sizePolicy2)
        self.but_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.but_3, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041a\u043e\u0442\u043e\u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440",
                                                             None))
        self.label.setText("")
        self.line_edit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.but_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        # if QT_CONFIG(shortcut)
        self.but_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
        # endif // QT_CONFIG(shortcut)
        self.but_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        # if QT_CONFIG(shortcut)
        self.but_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
        # endif // QT_CONFIG(shortcut)
        self.but_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.but_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        # if QT_CONFIG(shortcut)
        self.but_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
        # endif // QT_CONFIG(shortcut)
        self.but_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        # if QT_CONFIG(shortcut)
        self.but_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
        # endif // QT_CONFIG(shortcut)
        self.but_sign.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.but_tochka.setText(QCoreApplication.translate("MainWindow", u",", None))
        # if QT_CONFIG(shortcut)
        self.but_tochka.setShortcut(QCoreApplication.translate("MainWindow", u",", None))
        # endif // QT_CONFIG(shortcut)
        self.but_rez.setText(QCoreApplication.translate("MainWindow", u"=", None))
        # if QT_CONFIG(shortcut)
        self.but_rez.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
        # endif // QT_CONFIG(shortcut)
        self.but_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        # if QT_CONFIG(shortcut)
        self.but_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
        # endif // QT_CONFIG(shortcut)
        self.but_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        # if QT_CONFIG(shortcut)
        self.but_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
        # endif // QT_CONFIG(shortcut)
        self.but_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        # if QT_CONFIG(shortcut)
        self.but_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
        # endif // QT_CONFIG(shortcut)
        self.but_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        # if QT_CONFIG(shortcut)
        self.but_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
        # endif // QT_CONFIG(shortcut)
        self.but_backspace.setText(QCoreApplication.translate("MainWindow", u"\u232b ", None))
        # if QT_CONFIG(shortcut)
        self.but_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
        # endif // QT_CONFIG(shortcut)
        self.but_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        # if QT_CONFIG(shortcut)
        self.but_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
        # endif // QT_CONFIG(shortcut)
        self.but_multi.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        # if QT_CONFIG(shortcut)
        self.but_multi.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
        # endif // QT_CONFIG(shortcut)
        self.but_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        # if QT_CONFIG(shortcut)
        self.but_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
        # endif // QT_CONFIG(shortcut)
        self.but_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        # if QT_CONFIG(shortcut)
        self.but_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
        # endif // QT_CONFIG(shortcut)
        self.but_min.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        # if QT_CONFIG(shortcut)
        self.but_min.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
        # endif // QT_CONFIG(shortcut)
        self.but_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        # if QT_CONFIG(shortcut)
        self.but_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
        # endif // QT_CONFIG(shortcut)
        self.but_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        # if QT_CONFIG(shortcut)
        self.but_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
# endif // QT_CONFIG(shortcut)
# retranslateUi
