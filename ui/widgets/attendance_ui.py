# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attendance.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_AttendanceWidget(object):
    def setupUi(self, AttendanceWidget):
        if not AttendanceWidget.objectName():
            AttendanceWidget.setObjectName(u"AttendanceWidget")
        AttendanceWidget.resize(1009, 741)
        self.horizontalLayout = QHBoxLayout(AttendanceWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.label = QLabel(AttendanceWidget)
        self.label.setObjectName(u"label")

        self.titleLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titleLayout.addItem(self.horizontalSpacer)

        self.addButton = QPushButton(AttendanceWidget)
        self.addButton.setObjectName(u"addButton")

        self.titleLayout.addWidget(self.addButton)

        self.pushButton = QPushButton(AttendanceWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.titleLayout.addWidget(self.pushButton)


        self.mainLayout.addLayout(self.titleLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filterBar = QHBoxLayout()
        self.filterBar.setObjectName(u"filterBar")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.filterBar.addItem(self.horizontalSpacer_2)

        self.dateField = QDateEdit(AttendanceWidget)
        self.dateField.setObjectName(u"dateField")

        self.filterBar.addWidget(self.dateField)

        self.orgField = QComboBox(AttendanceWidget)
        self.orgField.setObjectName(u"orgField")

        self.filterBar.addWidget(self.orgField)


        self.verticalLayout.addLayout(self.filterBar)

        self.tableView = QTableView(AttendanceWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)

        self.mainLayout.addLayout(self.verticalLayout)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 8)

        self.horizontalLayout.addLayout(self.mainLayout)


        self.retranslateUi(AttendanceWidget)

        QMetaObject.connectSlotsByName(AttendanceWidget)
    # setupUi

    def retranslateUi(self, AttendanceWidget):
        AttendanceWidget.setWindowTitle(QCoreApplication.translate("AttendanceWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("AttendanceWidget", u"Attendance", None))
        self.addButton.setText(QCoreApplication.translate("AttendanceWidget", u"Add", None))
        self.pushButton.setText(QCoreApplication.translate("AttendanceWidget", u"PushButton", None))
    # retranslateUi

