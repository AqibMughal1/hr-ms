# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attendancedetails.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_AttendanceDetailsWindow(object):
    def setupUi(self, AttendanceDetailsWindow):
        if not AttendanceDetailsWindow.objectName():
            AttendanceDetailsWindow.setObjectName(u"AttendanceDetailsWindow")
        AttendanceDetailsWindow.resize(1009, 845)
        AttendanceDetailsWindow.setStyleSheet(u"background-color:#04395e;")
        self.centralwidget = QWidget(AttendanceDetailsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.dateField = QLineEdit(self.centralwidget)
        self.dateField.setObjectName(u"dateField")
        self.dateField.setStyleSheet(u"margin: 3px 0;border-radius:10px;\n"
"width:300px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;\n"
"padding: 3px;")

        self.gridLayout.addWidget(self.dateField, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 20px;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"border-radius:15px;\n"
"min-height:70px;\n"
"padding:10px;\n"
"margin:0 10px;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.mainLayout.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.mainLayout.addLayout(self.verticalLayout)

        self.mainLayout.setStretch(1, 10)

        self.horizontalLayout.addLayout(self.mainLayout)

        AttendanceDetailsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AttendanceDetailsWindow)

        QMetaObject.connectSlotsByName(AttendanceDetailsWindow)
    # setupUi

    def retranslateUi(self, AttendanceDetailsWindow):
        AttendanceDetailsWindow.setWindowTitle(QCoreApplication.translate("AttendanceDetailsWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AttendanceDetailsWindow", u"Attendance Details", None))
    # retranslateUi

