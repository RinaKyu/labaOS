import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QTableWidgetItem
from a import Ui_MainWindow
from algorithms import FCFS

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.algorithm = FCFS()
        self.update_data()
            
    def update_data(self):
        self.ui.tableWidget.setColumnCount(sum(self.algorithm.processes))
        self.ui.tableWidget.setRowCount(len(self.algorithm.processes))
        self.ui.tableWidget.setHorizontalHeaderLabels(list(str(i+1) for i in range(sum(self.algorithm.processes))))
        self.ui.tableWidget.setVerticalHeaderLabels([f'Процесс {i+1}' for i in range(len(self.algorithm.processes))])

        for i in range(sum(self.algorithm.processes)):
          self.ui.tableWidget.setColumnWidth(i,1)

        for row_index in range(len(self.algorithm.visual_representation)):
            for column_index in range(len(self.algorithm.visual_representation[row_index])):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(self.algorithm.visual_representation[row_index][column_index]))  
            
        

def create_app():
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

create_app()