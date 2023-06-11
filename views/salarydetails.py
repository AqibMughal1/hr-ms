from PySide6.QtWidgets import QMainWindow, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

from core.database import cursor
from ui.screens.salarydetails_ui import Ui_SalaryDetailWindow


class SalaryDetailModel(QAbstractTableModel):
    
    def __init__(self, details: list):
        super(SalaryDetailModel, self).__init__()
        self.details = details
        self.header = [
            "Employee ID",
            "Employee Name",
            "Organization",
            "Salary",
            "Deductions",
            "Net Salary"
        ]
        
    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.details)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.header)
    
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            detail = self.details[index.row()]
            if index.column() == 0:
                return detail[0]
            elif index.column() == 1:
                return detail[1]
            elif index.column() == 2:
                return detail[2]
            elif index.column() == 3:
                return detail[3]
            elif index.column() == 4:
                return detail[4]
            elif index.column() == 5:
                return detail[5]
            
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]
            

class SalaryDetailWindow(QMainWindow):
    
    def __init__(self, salary):
        super(SalaryDetailWindow, self).__init__()
        self.ui = Ui_SalaryDetailWindow()
        self.ui.setupUi(self)
        
        self.salary = salary
        
        self.setWindowTitle("Salary Details")
        
    def populateFields(self):
        month_year = f"{self.salary[1]} {self.salary[2]}"
        self.ui.monthField.setText(month_year)
        self.ui.monthField.setReadOnly(True)
