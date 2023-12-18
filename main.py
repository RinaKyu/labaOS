import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QTableWidgetItem
from main_ui import Ui_MainWindow
from algorithms import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.algorithm = FCFS()
        self.algorithm2 = RR()
        self.algorithm3 = SJF()
        self.algorithm4 = PSJF_PSJF()
        self.algorithm5 = RR_SJF()
        # кнопки добавить
        self.ui.pushButton_12.clicked.connect(self.line_fcfs)
        self.ui.pushButton_10.clicked.connect(self.line_rr)
        self.ui.pushButton_8.clicked.connect(self.line_sjf)
        self.ui.pushButton_6.clicked.connect(self.line_psjf)
        self.ui.pushButton.clicked.connect(self.line_rr_sjf)
        # Кнопки сброс
        self.ui.pushButton_11.clicked.connect(self.cleaning)
        self.ui.pushButton_9.clicked.connect(self.cleaning)
        self.ui.pushButton_7.clicked.connect(self.cleaning)
        self.ui.pushButton_5.clicked.connect(self.cleaning)
        self.ui.pushButton_2.clicked.connect(self.cleaning)
        # Кнопки вычислить
        self.ui.pushButton_14.clicked.connect(self.calculating)
        self.ui.pushButton_13.clicked.connect(self.calculating)
        self.ui.pushButton_15.clicked.connect(self.calculating)
        self.ui.pushButton_16.clicked.connect(self.calculating)
        self.ui.pushButton_17.clicked.connect(self.calculating)

        self.update_data()

    def update_data(self):
        #fcfs table 
        self.ui.tableWidget_fcfs.setColumnCount(sum(self.algorithm.processes))
        self.ui.tableWidget_fcfs.setRowCount(len(self.algorithm.processes))
        self.ui.tableWidget_fcfs.setHorizontalHeaderLabels(list(str(i+1) for i in range(sum(self.algorithm.processes))))
        self.ui.tableWidget_fcfs.setVerticalHeaderLabels([f'Процесс {i+1}' for i in range(len(self.algorithm.processes))])
        self.ui.tableWidget_fcfs.setColumnCount(sum(self.algorithm.processes))
        self.ui.tableWidget_fcfs.setRowCount(len(self.algorithm.processes))

        for i in range(sum(self.algorithm.processes)):
          self.ui.tableWidget_fcfs.setColumnWidth(i,1)
        
        for row_index in range(len(self.algorithm.visual_representation)):
            for column_index in range(len(self.algorithm.visual_representation[row_index])):
                self.ui.tableWidget_fcfs.setItem(row_index, column_index, QTableWidgetItem(self.algorithm.visual_representation[row_index][column_index]))  
        # rr table
        self.ui.tableWidget_rr.setColumnCount(sum(self.algorithm2.processes))
        self.ui.tableWidget_rr.setRowCount(len(self.algorithm2.processes))
        self.ui.tableWidget_rr.setHorizontalHeaderLabels(list(str(i+1) for i in range(sum(self.algorithm2.processes))))
        self.ui.tableWidget_rr.setVerticalHeaderLabels([f'Процесс {i+1}' for i in range(len(self.algorithm2.processes))])
        self.ui.tableWidget_rr.setColumnCount(sum(self.algorithm2.processes))
        self.ui.tableWidget_rr.setRowCount(len(self.algorithm2.processes))

        for i in range(sum(self.algorithm2.processes)):
          self.ui.tableWidget_rr.setColumnWidth(i,1)
        
        for row_index in range(len(self.algorithm2.visual_representation)):
            for column_index in range(len(self.algorithm2.visual_representation[row_index])):
                self.ui.tableWidget_rr.setItem(row_index, column_index, QTableWidgetItem(self.algorithm2.visual_representation[row_index][column_index]))  
        # sjf table
        self.ui.tableWidget_sjf.setColumnCount(sum(self.algorithm3.processes))
        self.ui.tableWidget_sjf.setRowCount(len(self.algorithm3.processes))
        self.ui.tableWidget_sjf.setHorizontalHeaderLabels(list(str(i+1) for i in range(sum(self.algorithm3.processes))))
        self.ui.tableWidget_sjf.setVerticalHeaderLabels([f'Процесс {i+1}' for i in range(len(self.algorithm3.processes))])
        self.ui.tableWidget_sjf.setColumnCount(sum(self.algorithm3.processes))
        self.ui.tableWidget_sjf.setRowCount(len(self.algorithm3.processes))

        for i in range(sum(self.algorithm3.processes)):
          self.ui.tableWidget_sjf.setColumnWidth(i,1)
        
        for row_index in range(len(self.algorithm3.visual_representation)):
            for column_index in range(len(self.algorithm3.visual_representation[row_index])):
                self.ui.tableWidget_sjf.setItem(row_index, column_index, QTableWidgetItem(self.algorithm3.visual_representation[row_index][column_index]))
        # psjf table
        self.ui.tableWidget_psjf_psjf.setColumnCount(sum(self.algorithm4.processes))
        self.ui.tableWidget_psjf_psjf.setRowCount(len(self.algorithm4.processes))
        self.ui.tableWidget_psjf_psjf.setHorizontalHeaderLabels(list(str(i+1) for i in range(sum(self.algorithm4.processes))))
        self.ui.tableWidget_psjf_psjf.setVerticalHeaderLabels([f'Процесс {i+1}' for i in range(len(self.algorithm4.processes))])
        self.ui.tableWidget_psjf_psjf.setColumnCount(sum(self.algorithm4.processes))
        self.ui.tableWidget_psjf_psjf.setRowCount(len(self.algorithm4.processes))

        for i in range(sum(self.algorithm4.processes)):
          self.ui.tableWidget_psjf_psjf.setColumnWidth(i,1)
        
        for row_index in range(len(self.algorithm4.visual_representation)):
            for column_index in range(len(self.algorithm4.visual_representation[row_index])):
                self.ui.tableWidget_psjf_psjf.setItem(row_index, column_index, QTableWidgetItem(self.algorithm4.visual_representation[row_index][column_index]))
        # rr sjf table
        self.ui.tableWidget_rr_sjf.setColumnCount(sum(self.algorithm5.processes))
        self.ui.tableWidget_rr_sjf.setRowCount(len(self.algorithm5.processes))
        self.ui.tableWidget_rr_sjf.setHorizontalHeaderLabels(list(str(i+1) for i in range(sum(self.algorithm5.processes))))
        self.ui.tableWidget_rr_sjf.setVerticalHeaderLabels([f'Процесс {i+1}' for i in range(len(self.algorithm5.processes))])
        self.ui.tableWidget_rr_sjf.setColumnCount(sum(self.algorithm5.processes))
        self.ui.tableWidget_rr_sjf.setRowCount(len(self.algorithm5.processes))

        for i in range(sum(self.algorithm5.processes)):
          self.ui.tableWidget_rr_sjf.setColumnWidth(i,1)
        
        for row_index in range(len(self.algorithm5.visual_representation)):
            for column_index in range(len(self.algorithm5.visual_representation[row_index])):
                self.ui.tableWidget_rr_sjf.setItem(row_index, column_index, QTableWidgetItem(self.algorithm5.visual_representation[row_index][column_index]))
        
    def line_fcfs(self):
        try:
            num = int(str(self.ui.lineEdit_6.text()))
            self.algorithm.add_process(num)
            self.algorithm2.add_process(num)
            self.algorithm3.add_process(num)
            self.algorithm4.add_process(num)
            self.algorithm5.add_process(num)
            self.ui.lineEdit_6.clear()
            self.update_data()
        except ValueError:
            pass
    
    def line_rr(self):
        try:    
            num = int(str(self.ui.lineEdit_5.text()))
            self.algorithm.add_process(num)
            self.algorithm2.add_process(num)
            self.algorithm3.add_process(num)
            self.algorithm4.add_process(num)
            self.algorithm5.add_process(num)
            self.ui.lineEdit_5.clear()
            self.update_data()
        except ValueError:
            pass

    def line_sjf(self):
        try: 
            num = int(str(self.ui.lineEdit_4.text()))
            self.algorithm.add_process(num)
            self.algorithm2.add_process(num)
            self.algorithm3.add_process(num)
            self.algorithm4.add_process(num)
            self.algorithm5.add_process(num)
            self.ui.lineEdit_4.clear()
            self.update_data()
        except ValueError:
            pass   

    
    def line_psjf(self):
        try:
            num = int(str(self.ui.lineEdit_3.text()))
            self.algorithm.add_process(num)
            self.algorithm2.add_process(num)
            self.algorithm3.add_process(num)
            self.algorithm4.add_process(num)
            self.algorithm5.add_process(num)
            self.ui.lineEdit_3.clear()
            self.update_data()
        except ValueError:
            pass
    def line_rr_sjf(self):
        try:
            num = int(str(self.ui.lineEdit.text()))
            self.algorithm.add_process(num)
            self.algorithm2.add_process(num)
            self.algorithm3.add_process(num)
            self.algorithm4.add_process(num)
            self.algorithm5.add_process(num)
            self.ui.lineEdit.clear()
            self.update_data()
        except ValueError:
            pass
    def cleaning(self):
        self.algorithm.clean()
        self.algorithm2.clean()
        self.algorithm3.clean()
        self.algorithm4.clean()
        self.algorithm5.clean()
        self.update_data()

    def calculating(self):
        try:    
            self.algorithm.time_calculate()
            self.algorithm2.time_calculate()
            self.algorithm3.time_calculate()
            self.algorithm4.time_calculate()
            self.algorithm5.time_calculate()
            # fcfs
            self.ui.label_fcfs_wait.setText(str(self.algorithm.avg_wait))
            self.ui.label_fcfs_all.setText(str(self.algorithm.avg_all))
            # rr
            self.ui.label_rr_t.setText(str(self.algorithm2.T))
            self.ui.label_rr_m.setText(str(self.algorithm2.M))
            self.ui.label_rr_r.setText(str(self.algorithm2.R))
            self.ui.label_rr_p.setText(str(self.algorithm2.P))
            # sjf
            self.ui.label_sjf_t.setText(str(self.algorithm3.T))
            self.ui.label_sjf_m.setText(str(self.algorithm3.M))
            self.ui.label_sjf_r.setText(str(self.algorithm3.R))
            self.ui.label_sjf_p.setText(str(self.algorithm3.P))
            # psjf
            self.ui.label_psjf_psjf_t.setText(str(self.algorithm4.T))
            self.ui.label_psjf_psjf_m.setText(str(self.algorithm4.M))
            self.ui.label_psjf_psjf_m_2.setText(str(self.algorithm4.R))
            self.ui.label_psjf_psjf_p.setText(str(self.algorithm4.P))
            # rr_sjf 
            self.ui.label_rr_sjf_t.setText(str(self.algorithm2.T))
            self.ui.label_rr_sjf_m.setText(str(self.algorithm2.M))
            self.ui.label_rr_sjf_r.setText(str(self.algorithm2.R))
            self.ui.label_rr_sjf_p.setText(str(self.algorithm2.P))
        except AttributeError:
            pass
def create_app():
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

create_app()