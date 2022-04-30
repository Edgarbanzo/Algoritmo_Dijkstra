# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1074, 814)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPuntos = QAction(MainWindow)
        self.actionPuntos.setObjectName(u"actionPuntos")
        self.actionPuntos_mas_cercanos = QAction(MainWindow)
        self.actionPuntos_mas_cercanos.setObjectName(u"actionPuntos_mas_cercanos")
        self.actionMostrar_Grafo = QAction(MainWindow)
        self.actionMostrar_Grafo.setObjectName(u"actionMostrar_Grafo")
        self.actionRecorrido_de_Grafo = QAction(MainWindow)
        self.actionRecorrido_de_Grafo.setObjectName(u"actionRecorrido_de_Grafo")
        self.actionPrim = QAction(MainWindow)
        self.actionPrim.setObjectName(u"actionPrim")
        self.actionKruskal = QAction(MainWindow)
        self.actionKruskal.setObjectName(u"actionKruskal")
        self.actionDijkstra = QAction(MainWindow)
        self.actionDijkstra.setObjectName(u"actionDijkstra")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 1040, 799))
        self.gridLayout_20 = QGridLayout(self.groupBox)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buscar_pushButton = QPushButton(self.tab_4)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.sortDist_pushButton = QPushButton(self.tab_4)
        self.sortDist_pushButton.setObjectName(u"sortDist_pushButton")

        self.gridLayout_3.addWidget(self.sortDist_pushButton, 1, 5, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_4)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_4)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 1, 6)

        self.id_lineEdit = QLineEdit(self.tab_4)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_3.addWidget(self.id_lineEdit, 1, 0, 1, 1)

        self.sortVel_pushButton = QPushButton(self.tab_4)
        self.sortVel_pushButton.setObjectName(u"sortVel_pushButton")

        self.gridLayout_3.addWidget(self.sortVel_pushButton, 1, 4, 1, 1)

        self.sortId_pushButton = QPushButton(self.tab_4)
        self.sortId_pushButton.setObjectName(u"sortId_pushButton")

        self.gridLayout_3.addWidget(self.sortId_pushButton, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_6 = QGridLayout(self.tab_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.dibujar = QPushButton(self.tab_7)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_6.addWidget(self.dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.tab_7)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_6.addWidget(self.limpiar, 1, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_7)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_6.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_7, "")

        self.gridLayout_20.addWidget(self.tabWidget, 0, 2, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_17 = QGridLayout(self.groupBox_10)
        self.gridLayout_17.setObjectName(u"gridLayout_17")

        self.gridLayout_20.addWidget(self.groupBox_10, 1, 1, 1, 2)

        self.groupBox_11 = QGroupBox(self.groupBox)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_19 = QGridLayout(self.groupBox_11)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_5 = QGroupBox(self.groupBox_11)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_14 = QGridLayout(self.groupBox_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.origen_x_spinBox = QSpinBox(self.groupBox_5)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(1000)

        self.gridLayout_14.addWidget(self.origen_x_spinBox, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_14.addWidget(self.label_7, 0, 2, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox_5)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(1000)

        self.gridLayout_14.addWidget(self.origen_y_spinBox, 0, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_14.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.groupBox_11)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_15 = QGridLayout(self.groupBox_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label = QLabel(self.groupBox_8)
        self.label.setObjectName(u"label")

        self.gridLayout_15.addWidget(self.label, 0, 0, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.groupBox_8)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(1000)

        self.gridLayout_15.addWidget(self.destino_x_spinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_8)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_15.addWidget(self.label_2, 0, 2, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox_8)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(1000)

        self.gridLayout_15.addWidget(self.destino_y_spinBox, 0, 3, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_8, 2, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox_11)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_2 = QGridLayout(self.groupBox_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_9)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox_9)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_9)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox_9)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.green_spinBox, 0, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_9)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox_9)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.blue_spinBox, 0, 5, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_9, 3, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.groupBox_11)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_18 = QGridLayout(self.groupBox_12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.velocidad_spinBox = QSpinBox(self.groupBox_12)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(10000)

        self.gridLayout_18.addWidget(self.velocidad_spinBox, 0, 1, 1, 1)

        self.label_37 = QLabel(self.groupBox_12)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_18.addWidget(self.label_37, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_12, 4, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBox_11)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_5 = QGridLayout(self.groupBox_13)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.salida_plainTextEdit = QPlainTextEdit(self.groupBox_13)
        self.salida_plainTextEdit.setObjectName(u"salida_plainTextEdit")

        self.gridLayout_5.addWidget(self.salida_plainTextEdit, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox_13)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ordenar_velocidad_pushButton = QPushButton(self.groupBox_2)
        self.ordenar_velocidad_pushButton.setObjectName(u"ordenar_velocidad_pushButton")

        self.gridLayout_4.addWidget(self.ordenar_velocidad_pushButton, 2, 0, 1, 1)

        self.ordenar_distancia_pushButton = QPushButton(self.groupBox_2)
        self.ordenar_distancia_pushButton.setObjectName(u"ordenar_distancia_pushButton")

        self.gridLayout_4.addWidget(self.ordenar_distancia_pushButton, 3, 0, 1, 1)

        self.ordenar_id_pushButton = QPushButton(self.groupBox_2)
        self.ordenar_id_pushButton.setObjectName(u"ordenar_id_pushButton")

        self.gridLayout_4.addWidget(self.ordenar_id_pushButton, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.groupBox_13)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout = QGridLayout(self.groupBox_14)
        self.gridLayout.setObjectName(u"gridLayout")
        self.agregar_final_pushButton = QPushButton(self.groupBox_14)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 3, 0, 1, 2)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox_14)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_14, 1, 1, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox_13)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_5.addWidget(self.mostrar_pushButton, 2, 0, 1, 2)


        self.gridLayout_19.addWidget(self.groupBox_13, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_11)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 0, 0, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox_3)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(100000)

        self.gridLayout_13.addWidget(self.id_spinBox, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_3, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.groupBox_11, 0, 0, 3, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1074, 27))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuVer.addAction(self.actionPuntos)
        self.menuVer.addAction(self.actionMostrar_Grafo)
        self.menuAlgoritmos.addAction(self.actionPuntos_mas_cercanos)
        self.menuAlgoritmos.addAction(self.actionRecorrido_de_Grafo)
        self.menuAlgoritmos.addAction(self.actionPrim)
        self.menuAlgoritmos.addAction(self.actionKruskal)
        self.menuAlgoritmos.addAction(self.actionDijkstra)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionPuntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.actionPuntos_mas_cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos mas cercanos", None))
        self.actionMostrar_Grafo.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.actionRecorrido_de_Grafo.setText(QCoreApplication.translate("MainWindow", u"Recorrido de Grafo", None))
        self.actionPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.actionKruskal.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.actionDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.sortDist_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar Distancia", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.id_lineEdit.setText("")
        self.id_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de la particula", None))
        self.sortVel_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar Velocidad", None))
        self.sortId_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar Id", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Gr\u00e1ficar", None))
        self.groupBox_10.setTitle("")
        self.groupBox_11.setTitle("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.groupBox_12.setTitle("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.ordenar_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.ordenar_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.ordenar_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.groupBox_3.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

