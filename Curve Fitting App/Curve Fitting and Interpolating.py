from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import S, symbols, printing
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pylab as plt
import math 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.final_horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.final_horizontalLayout.setObjectName("final_horizontalLayout")
        self.base_verticalLayout = QtWidgets.QVBoxLayout()
        self.base_verticalLayout.setObjectName("base_verticalLayout")
        
        self.verticalLayout_for_Widget_and_equation = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_Widget_and_equation.setObjectName("verticalLayout_for_Widget_and_equation")

        self.TheFittingEquation_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TheFittingEquation_groupBox.setObjectName("TheFittingEquation_groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TheFittingEquation_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.verticalLayout_for_Widget_and_equation.addWidget(self.TheFittingEquation_groupBox)
        self.widget_for_percentag_error = QtWidgets.QWidget(self.centralwidget)
        self.widget_for_percentag_error.setObjectName("widget_for_percentag_error")
        self.widget_for_percentag_error.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.verticalLayout_for_percentag_error = QtWidgets.QVBoxLayout(self.widget_for_percentag_error)
        self.verticalLayout_for_percentag_error.setObjectName("verticalLayout_for_percentag_error")
        self.percentag_error = QtWidgets.QLabel(self.widget_for_percentag_error)
        self.percentag_error.setText("")
        self.percentag_error.setObjectName("percentag_error")
        self.verticalLayout_for_percentag_error.addWidget(self.percentag_error, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_for_Widget_and_equation.addWidget(self.widget_for_percentag_error)
        self.base_verticalLayout.addLayout(self.verticalLayout_for_Widget_and_equation)
        self.horizontalLayout_containsLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout_containsLayout.setObjectName("horizontalLayout_containsLayout")

        self.verticalLayout_for_maingraph_and_itscontrol = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_maingraph_and_itscontrol.setObjectName("verticalLayout_for_maingraph_and_itscontrol")
        self.main_graph= PlotWidget(self.centralwidget)
        self.main_graph.setObjectName("main_graph\n""")
        self.main_graph.setBackground("w")
        self.verticalLayout_for_maingraph_and_itscontrol.addWidget(self.main_graph)
        self.The_control_of_the_main_graph_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.The_control_of_the_main_graph_groupBox.setObjectName("The_control_of_the_main_graph_groupBox")
        self.verticalLayout_control_maingraph = QtWidgets.QVBoxLayout(self.The_control_of_the_main_graph_groupBox)
        self.verticalLayout_control_maingraph.setObjectName("verticalLayout_control_maingraph")
        self.Chunks_Equations_Combobox = QtWidgets.QComboBox(self.The_control_of_the_main_graph_groupBox)
        self.Chunks_Equations_Combobox.setObjectName("Chunks_Equations_Combobox")
        self.Chunks_Equations_Combobox.addItem("")
        self.verticalLayout_for_percentag_error.addWidget(self.Chunks_Equations_Combobox)

        self.label_for_Num_of_chunks = QtWidgets.QLabel(self.The_control_of_the_main_graph_groupBox)
        self.label_for_Num_of_chunks.setObjectName("label_for_Num_of_chunks")
        self.verticalLayout_control_maingraph.addWidget(self.label_for_Num_of_chunks)
        self.num_of_chunks = QtWidgets.QLineEdit(self.The_control_of_the_main_graph_groupBox)
        self.num_of_chunks.setObjectName("num_of_chunks")
        self.verticalLayout_control_maingraph.addWidget(self.num_of_chunks)
        self.label_for_Order_of_Fitting = QtWidgets.QLabel(self.The_control_of_the_main_graph_groupBox)
        self.label_for_Order_of_Fitting.setObjectName("label_for_Order_of_Fitting")
        self.verticalLayout_control_maingraph.addWidget(self.label_for_Order_of_Fitting)
        self.order_of_fitting = QtWidgets.QSpinBox(self.The_control_of_the_main_graph_groupBox)
        self.order_of_fitting.setObjectName("order_of_fitting")
        self.verticalLayout_control_maingraph.addWidget(self.order_of_fitting)
        self.label_for_Clipping = QtWidgets.QLabel(self.The_control_of_the_main_graph_groupBox)
        self.label_for_Clipping.setObjectName("label_for_Clipping")
        self.verticalLayout_control_maingraph.addWidget(self.label_for_Clipping)
        self.clipping_percentage = QtWidgets.QSpinBox(self.The_control_of_the_main_graph_groupBox)
        self.clipping_percentage.setObjectName("clipping_percentage")
        self.verticalLayout_control_maingraph.addWidget(self.clipping_percentage)
        self.verticalLayout_for_maingraph_and_itscontrol.addWidget(self.The_control_of_the_main_graph_groupBox)
        self.horizontalLayout_containsLayout.addLayout(self.verticalLayout_for_maingraph_and_itscontrol)
        self.verticalLayout_for_widget = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_widget.setObjectName("verticalLayout_for_widget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.Layout_for_errormap = QtWidgets.QVBoxLayout(self.widget)
        self.Layout_for_errormap.setObjectName("Layout_for_errormap")
        self.verticalLayout_for_widget.addWidget(self.widget)
        self.Control_of_errormap_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Control_of_errormap_groupBox.setObjectName("Control_of_errormap_groupBox")
        self.verticalLayout_for_errormap_and_itscontrol = QtWidgets.QVBoxLayout(self.Control_of_errormap_groupBox)
        self.verticalLayout_for_errormap_and_itscontrol.setObjectName("verticalLayout_for_errormap_and_itscontrol")

        self.horizontalLayout_for_xandy_comboboxes = QtWidgets.QHBoxLayout()
        self.horizontalLayout_for_xandy_comboboxes.setObjectName("horizontalLayout_for_xandy_comboboxes")
        self.x_axis = QtWidgets.QComboBox(self.Control_of_errormap_groupBox)
        self.x_axis.setObjectName("x_axis")
        self.x_axis.addItem("")
        self.x_axis.addItem("")
        self.x_axis.addItem("")
        self.x_axis.addItem("")
        self.horizontalLayout_for_xandy_comboboxes.addWidget(self.x_axis)
        self.y_axis = QtWidgets.QComboBox(self.Control_of_errormap_groupBox)
        self.y_axis.setObjectName("y_axis")
        self.y_axis.addItem("")
        self.y_axis.addItem("")
        self.y_axis.addItem("")
        self.y_axis.addItem("")
        self.horizontalLayout_for_xandy_comboboxes.addWidget(self.y_axis)
        self.verticalLayout_for_errormap_and_itscontrol.addLayout(self.horizontalLayout_for_xandy_comboboxes)
        self.Overlapping_Label = QtWidgets.QLabel(self.Control_of_errormap_groupBox)
        self.Overlapping_Label.setObjectName("Overlapping_Label")
        self.verticalLayout_for_errormap_and_itscontrol.addWidget(self.Overlapping_Label)
        self.Overlapping_EditLine = QtWidgets.QLineEdit(self.Control_of_errormap_groupBox)
        self.Overlapping_EditLine.setObjectName("Overlapping_EditLine")
        self.verticalLayout_for_errormap_and_itscontrol.addWidget(self.Overlapping_EditLine)
        self.generate_an_error_map = QtWidgets.QPushButton(self.Control_of_errormap_groupBox)
        self.generate_an_error_map.setObjectName("generate_an_error_map")
        self.verticalLayout_for_errormap_and_itscontrol.addWidget(self.generate_an_error_map)
        self.verticalLayout_for_widget.addWidget(self.Control_of_errormap_groupBox)
        self.horizontalLayout_containsLayout.addLayout(self.verticalLayout_for_widget)
        self.base_verticalLayout.addLayout(self.horizontalLayout_containsLayout)
        self.final_horizontalLayout.addLayout(self.base_verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 18))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuOpen.addAction(self.actionOpen)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.order_of_fitting.setValue(3)
        self.actionOpen.triggered.connect(lambda: self.open_file())
        self.order_of_fitting.valueChanged.connect(self.Update_maingraph)
        self.clipping_percentage.valueChanged.connect(self.extrapolation)
        self.num_of_chunks.setText("8")
        self.num_of_chunks.textChanged.connect(self.Update_maingraph)
        self.generate_an_error_map.clicked.connect(self.toggle_button)
        self.pbar = QtWidgets.QProgressBar()
        self.pbar.setGeometry(30, 40, 200, 25)
        self.verticalLayout_for_errormap_and_itscontrol.addWidget(self.pbar)
        self.pbar.setMaximum(100)
        self.pbar.hide()
        self.timer= QtCore.QTimer()
        self.Canvas_for_equation = MplCanvas(self, width=3, height=0.4)
        self.horizontalLayout.addWidget(self.Canvas_for_equation)
        self.Canvas_for_errormap = MplCanvas2(self)
        self.Layout_for_errormap.addWidget(self.Canvas_for_errormap)
        self.Chunks_Equations_Combobox.activated.connect(self.update_equation)
        self.generate_is_pressed = False
        self.generate_an_error_map.setStyleSheet("background-color : lightgreen")
        self.x_axis.activated.connect(self.updateText)
        self.y_axis.activated.connect(self.updateText)

    def updateText(self):
        self.currentIndex(self.x_axis.currentIndex(), self.y_axis.currentIndex())
                
    def currentIndex(self,x,y):
        sum = x+ y
        dic_labels={bool(sum==3):"overlapping percentage",bool(sum==4):"order of fitting",bool(sum==5):"number of chunks"}
        return self.Overlapping_Label.setText( dic_labels.get(True))

        
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "All Files (*);;csv Files (*.csv)", options=options)
        if fileName:
            self.read_file(fileName)

    def read_file(self, file_path):
        self.main_graph.clear()
        path = file_path
        data = pd.read_csv(path)
        self.t = data.values[:, 0]
        self.amp = data.values[:, 1]
        self.main_graph.plot(self.t, self.amp)
        self.interpolatian( 8,3)
        
    def interpolatian(self,number_of_chunks,order_of_polynomial):
        chunks_x = np.array_split(self.t,number_of_chunks)
        chunks_y=np.array_split(self.amp, number_of_chunks)
        self.All_chunks_parameters=[]
        self.equation_list=[]
        self.error_for_all_chunks=[]
        for chunk_number in range(len(chunks_x)):
            self.parameters_Array = np.polyfit(chunks_x[chunk_number],chunks_y[chunk_number],order_of_polynomial)
            self.All_chunks_parameters.append(self.parameters_Array)
            y_fitting_list=[]
            error_for_each_chunk=[]
            for x in (chunks_x[chunk_number]):
                index_x = list(chunks_x[chunk_number]).index(x)
                y_fitting=0
                for i in range(len( self.parameters_Array)):
                     y_fitting+=self.parameters_Array[i]*(x**(order_of_polynomial-i))
                error_for_each_point=(y_fitting-chunks_y[chunk_number][index_x])**2
                error_for_each_chunk.append(error_for_each_point)
                y_fitting_list.append( y_fitting)
            percentage_error_for_each_chunk=math.sqrt((sum(error_for_each_chunk)/len(chunks_x[chunk_number])))*100
            self.error_for_all_chunks.append( percentage_error_for_each_chunk)
            self.percentag_error.setText("Percentage Error= "+ str(round(percentage_error_for_each_chunk,2))+ "%")
            self.main_graph.plot(chunks_x[chunk_number],np.array(y_fitting_list),pen=pg.mkPen(color=(255, 148, 4),width=3, style=QtCore.Qt.DotLine))
            self.main_graph.plot(self.t, self.amp,pen=pg.mkPen(color=(0, 0, 0),width=2,style=QtCore.Qt.SolidLine))    
        x = symbols("x")
        for i in range(len(self.All_chunks_parameters)):
             poly = sum(S("{:6.2f}".format(v)) * x ** i for i, v in enumerate(self.All_chunks_parameters[i][::-1]))
             eq_latex = printing.latex(poly)
             label = "${}$".format(eq_latex)
             self.equation_list.append(label)
             self.Chunks_Equations_Combobox.addItem(str(i+1))
             self.Canvas_for_equation .fig.suptitle(label)
             self.Canvas_for_equation .draw()
        self.main_graph.addLegend()
        self.main_graph.setLabel("left", "Amplitude (volt)")
        self.main_graph.setLabel("bottom", "Time (t)")
        self.main_graph.showGrid(x=True, y=True)

    def Update_maingraph(self):
        self.main_graph.clear()
        self.main_graph.plot(self.t, self.amp,pen=pg.mkPen(color=(0, 0, 0),width=2,style=QtCore.Qt.SolidLine))
        self.interpolatian( int(self.num_of_chunks.text()),self.order_of_fitting.value())

    def  overlap(self,chunks_x,overlap):
        chunks_x_overlaped=[chunks_x[0]]
        for chunk_number in range(1,len(chunks_x)):
            num_of_elements = int(overlap*len(chunks_x[chunk_number]))*chunk_number
            chunkx_new=[]
            for x in (chunks_x[chunk_number]):
                 xnew=x-num_of_elements
                 chunkx_new.append(xnew)
            chunks_x_overlaped.append( chunkx_new) 
        return chunks_x_overlaped

    def calculate_error_map(self,number_of_chunks,order_of_polynomial,overlap):
        chunks_x = np.array_split(self.t,number_of_chunks)
        chunks_x = self.overlap(chunks_x,overlap)
        chunks_y=np.array_split(self.amp, number_of_chunks)
        error_for_all_chunks=[]
        for chunk_number in range(len(chunks_x)):
            self.parameters_Array = np.polyfit(chunks_x[chunk_number],chunks_y[chunk_number],order_of_polynomial)
            y_fitting_list=[]
            error_for_each_chunk=[]
            for x in (chunks_x[chunk_number]):
                 index_x = list(chunks_x[chunk_number]).index(x)
                 y_fitting=0

                 for i in range(len( self.parameters_Array)):
                     y_fitting+=self.parameters_Array[i]*(x**(order_of_polynomial-i))
                 error_for_each_point=(y_fitting-chunks_y[chunk_number][index_x])**2
                 error_for_each_chunk.append(error_for_each_point)
                 y_fitting_list.append( y_fitting)
            error_for_each_chunk=math.sqrt((sum(error_for_each_chunk)/len(chunks_x[chunk_number])))
            error_for_all_chunks.append( error_for_each_chunk)
        return (sum(error_for_all_chunks)/number_of_chunks)


    def Generate_error_map(self):
        self.Canvas_for_errormap.fig.clear()
        self.axes = self.Canvas_for_errormap.fig.add_subplot(111)
        self.Canvas_for_errormap.draw()
        rows, cols = 5,5
        x=self.x_axis.currentIndex()
        y= self.y_axis.currentIndex()
        overlap_list=np.arange(0,30,5)
        print(overlap_list)
        print(len(overlap_list))
        z = int( self.Overlapping_EditLine.text())
        arr=[]
        for i in range(rows):
           col = []
           for j in range( cols):
               dic={bool(x==1 and y==2):self.calculate_error_map(j+1,i+1,z/100),bool( x==2 and y==1):self.calculate_error_map(i+1,j+1,z/100),bool(x==3 and y==1):self.calculate_error_map(i+1,z,overlap_list[j]/100),bool( x==1 and y==3):self.calculate_error_map(j+1,z,overlap_list[i]/100),bool( x==3 and y==2):self.calculate_error_map(z,i+1,overlap_list[j]/100),bool( x==2 and y==3):self.calculate_error_map(z,j+1,overlap_list[i]/100)}
               a=dic.get(True)
               col.append(a)

           arr.append(col)
        self.canv = self.axes.imshow(np.array(arr), interpolation = 'nearest',cmap="rainbow", extent = [0.5,5.5,0.5,5.5],origin="lower")
        self.Canvas_for_errormap.draw()

        if self.x_axis.currentIndex()==3:
            self.axes.set_xticklabels(['0','5','10','15','20','25'])
        else:
            self.axes.set_xticks(np.arange(1,cols+1))

        if self.y_axis.currentIndex()==3:
            self.axes.set_yticklabels(['0','5','10','15','20','25'])
        else:
            self.axes.set_yticks(np.arange(1,rows+1))

        self.cbar = self.Canvas_for_errormap.fig.colorbar(self.canv)
        self.generate_an_error_map.setText("Generate an error map")
        self.generate_an_error_map.setStyleSheet("background-color : lightgreen")
        self.axes.set_xlabel(self.x_axis.currentText())
        self.axes.set_ylabel(self.y_axis.currentText())
        self.axes.set_title('error map')
        self.Canvas_for_errormap.draw()


    def extrapolation(self,clipping_percentage):
        self.main_graph.clear()
        chunks_x = np.array_split(self.t,10)
        chunks_y = np.array_split(self.amp,10)
        number_chunks_concatenating=clipping_percentage/10
        concatenating_list_x=[]
        concatenating_list_y=[]
        
        for i in range(int(number_chunks_concatenating)):
            concatenating_list_x+=list(chunks_x[i])
            concatenating_list_y+=list(chunks_y[i])
     
      
        self.parameters_Array = np.polyfit(concatenating_list_x,concatenating_list_y,self.order_of_fitting.value())
        y_fitting_list=[]
        for x in (self.t):
                y_fitting=0
                for i in range(len( self.parameters_Array)):
                     y_fitting += self.parameters_Array[i]*(x**(self.order_of_fitting.value()-i))
                y_fitting_list.append( y_fitting)

        self.main_graph.plot(self.t,self.amp,pen=pg.mkPen(color=(0, 0, 0),width=2,style=QtCore.Qt.SolidLine) , name='The Orignal Signal')
        self.main_graph.plot(self.t,np.array(y_fitting_list),pen=pg.mkPen(color=(0, 255, 255),width=5, style=QtCore.Qt.DotLine), name='The Fitted Curve')
        self.main_graph.addLegend()
        self.main_graph.setLabel("left", "Amplitude (volt)")
        self.main_graph.setLabel("bottom", "Time (t)")
        self.main_graph.showGrid(x=True, y=True)
    def update_equation(self):
        self.chunk_displayed(self.Chunks_Equations_Combobox.currentIndex())
    def chunk_displayed(self,i):
        self.Canvas_for_equation.fig.suptitle(self.equation_list[i-1])
        self.Canvas_for_equation.draw()
        self.percentag_error.setText("percentag error = "+ str(round(self.error_for_all_chunks[i],2))+"%")      

    def toggle_button(self):
        if  self.generate_an_error_map.text()=="Generate an error map":
            self.pbar.setVisible(True)    
            self.pbar.setValue(0)
            self.timer.start(30)
            self.timer.timeout.connect(self.update_progressbar)
        else :
            self.timer.stop()
            self.pbar.setVisible(False)
            self.generate_an_error_map.setText("Generate an error map")
            self.generate_an_error_map.setStyleSheet("background-color : lightgreen")
            self.Canvas_for_errormap.fig.clear()
            self.axes = self.Canvas_for_errormap.fig.add_subplot(111)
            self.Canvas_for_errormap.draw()

    def update_progressbar(self):
        self.pbar.setValue(self.pbar.value()+1)
        self.generate_an_error_map.setText("cancel")
        self.generate_an_error_map.setStyleSheet("background-color : red")
        if self.pbar.value()==100:
            self.Generate_error_map()
            self.pbar.setVisible(False)
            self.timer.stop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interpolation & Curve Fitting Application"))
        self.TheFittingEquation_groupBox.setTitle(_translate("MainWindow", "The fitting Equation"))
        self.The_control_of_the_main_graph_groupBox.setTitle(_translate("MainWindow", "The control of the main graph"))
        self.Chunks_Equations_Combobox.setItemText(0, _translate("MainWindow", "Chunks Equations"))
        self.label_for_Num_of_chunks.setText(_translate("MainWindow", "Num of chunks"))
        self.label_for_Order_of_Fitting.setText(_translate("MainWindow", "Order of Fitting"))
        self.label_for_Clipping.setText(_translate("MainWindow", "Clipping"))
        self.Control_of_errormap_groupBox.setTitle(_translate("MainWindow", "The control of the error map"))
        self.x_axis.setItemText(0, _translate("MainWindow", "x- axis "))
        self.x_axis.setItemText(1, _translate("MainWindow", "number of chunks"))
        self.x_axis.setItemText(2, _translate("MainWindow", "order of fitting"))
        self.x_axis.setItemText(3, _translate("MainWindow", "overlapping percentage"))
        self.y_axis.setItemText(0, _translate("MainWindow", "y - axis"))
        self.y_axis.setItemText(1, _translate("MainWindow", "number of chunks"))
        self.y_axis.setItemText(2, _translate("MainWindow", "order of fitting "))
        self.y_axis.setItemText(3, _translate("MainWindow", "overlapping percentage "))
        self.Overlapping_Label.setText(_translate("MainWindow","Z constant"))
        self.generate_an_error_map.setText(_translate("MainWindow", "Generate an error map"))
        self.menuOpen.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

class MplCanvas(FigureCanvasQTAgg):
   def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig) 

class MplCanvas2(FigureCanvasQTAgg):
   def __init__(self, parent=None, width=3.5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.tight_layout()      
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas2, self).__init__(self.fig) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
