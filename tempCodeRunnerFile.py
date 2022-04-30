from pprint import pprint, pformat
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import SLOT,Slot
from PySide2.QtGui import QClipboard, QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from particula.adminparticula import AdminParticula
from particula.particula import Particula
from particula.algoritmos import puntos_mas_cercanos
from random import randint
from particula.arista import AristaNoDirigidaPonderada
from particula.nodo import Nodo
from particula.grafo import Grafo



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
   
        self.adminparticula = AdminParticula()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.puntos = []

        self.ui.agregar_final_pushButton.clicked.connect(self.agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar)
        
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_titulo)

        self.ui.limpiar.clicked.connect(self.limpiar)
        self.ui.dibujar.clicked.connect(self.dibujar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        #Table Widget
        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.ordenar_dis)
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.ordenar_vel)

        #Plain Text Widget
        self.ui.sortDist_pushButton.clicked.connect(self.sort_id)
        self.ui.sortVel_pushButton.clicked.connect(self.sort_vel)
        self.ui.sortDist_pushButton.clicked.connect(self.sort_dis)

        #ActionButton
        self.ui.actionPuntos.triggered.connect(self.dibujar_puntos)
        self.ui.actionPuntos_mas_cercanos.triggered.connect(self.mostrar_puntos_cercanos)
        self.ui.actionMostrar_Grafo.triggered.connect(self.action_mostrar_grafo)
        self.ui.actionRecorrido_de_Grafo.triggered.connect(self.recorrido_grafo)
        self.ui.actionPrim.triggered.connect(self.prim)
    
    
    @Slot()
    def prim(self):
        grafo = Grafo()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        inicio = Nodo((origen_x,origen_y))
        for particula in self.adminparticula:
            arista = AristaNoDirigidaPonderada(Nodo((particula.origen_x, particula.origen_y)), Nodo((particula.destino_x, particula.destino_y)), particula.distancia)
            grafo.agregar_arista(arista)
        if inicio not in grafo.get_lista_ady():
            QMessageBox.critical(
                self, "Error:", "No es posible leer los valores"
            )
        else:
            prim = grafo.prim(inicio)
            pen = QPen()
            pen.setWidth(2)
            for key in prim.keys():
                for value in prim[key]:
                    color = QColor(255, 51, 205)
                    pen.setColor(color)
                    x_origen = key.dato[0]
                    y_origen = key.dato[1]
                    x_destino = value[0].dato[0]
                    y_destino = value[0].dato[1]

                    self.scene.addEllipse(x_origen, y_origen, 6, 6, pen)
                    self.scene.addEllipse(x_destino, y_destino, 6, 6, pen)
                    self.scene.addLine(x_origen+3, y_origen+3, x_destino+3, y_destino+3, pen)
 
    @Slot()
    def recorrido_grafo(self):
        origen_x = self.ui.origen_x_spinBox.value() #Sacamos lo que está ahí
        origen_y = self.ui.origen_y_spinBox.value()
        origen = (origen_x, origen_y)
        

        profundidad = self.adminparticula.recorrido_profundidad(origen)
        recorrido_profundidad = self.adminparticula.recorrido_toString(profundidad)
        print("Origen: " + str(origen))
        print("Profundidad: ")
        print(recorrido_profundidad)
        self.ui.salida_plainTextEdit.clear()
        self.ui.salida_plainTextEdit.insertPlainText("Origen: " + str(origen) + "\n" + "\n")
        self.ui.salida_plainTextEdit.insertPlainText("Profundidad: \n")
        self.ui.salida_plainTextEdit.insertPlainText(recorrido_profundidad)
        
        amplitud = self.adminparticula.recorrido_amplitud(origen)
        recorrido_amplitud = self.adminparticula.recorrido_toString(amplitud)
        print("Amplitud: ")
        print(recorrido_amplitud)
        self.ui.salida_plainTextEdit.insertPlainText("\n")
        self.ui.salida_plainTextEdit.insertPlainText("Anchura: \n")
        self.ui.salida_plainTextEdit.insertPlainText(recorrido_amplitud)





    @Slot()
    def action_mostrar_grafo(self):
        self.ui.salida_plainTextEdit.clear()
        self.ui.salida_plainTextEdit.insertPlainText(self.adminparticula.ver_grafo())
        self.dibujar()


    @Slot()
    def mostrar_puntos_cercanos(self):
        resultado = puntos_mas_cercanos(self.puntos)
        pen = QPen()
        pen.setWidth(2)
        pprint(resultado)

        for punto1, punto2 in resultado:
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]
            
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            
            color = QColor(r,g,b)
            pen.setColor(color)



            self.scene.addLine(x1+3,y1+3,x2+3,y2+3,pen)
            





    
    @Slot()
    def dibujar_puntos(self):
        self.limpiar()
        self.puntos = []
        pen = QPen()
        pen.setWidth(2)

        for particula in self.adminparticula:
            x1 = particula.origen_x
            x2 = particula.origen_y
            punto = (x1,x2)
            self.puntos.append(punto)
            y1 = particula.destino_x
            y2 = particula.destino_y
            punto = (y1,y2)
            self.puntos.append(punto)
        for punto in self.puntos:
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)

            x1 = punto[0]
            x2 = punto[1]
            y1 = punto[0]
            y2 = punto[1]

            color = QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(x1,x2, 6,6, pen)
            self.scene.addEllipse(x1, x2, 6,6, pen)
    
    @Slot()
    def action_abrir_archivo(self):
        #print('abrir_archivo')
        ubicacion=  QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.adminparticula.abrir(ubicacion):
            QMessageBox.information(
            self,
            "Exito",
            "Se abrio el archivo" + ubicacion
            )

        else: 
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo" + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'

            )[0]
        print(ubicacion)
        if self.adminparticula.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion

            )
        else: 
            QMessageBox.critical(+
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )


    @Slot()
    def mostrar(self):
        self.adminparticula.mostrar()
        self.ui.salida_plainTextEdit.clear()
        self.ui.salida_plainTextEdit.insertPlainText(str(self.adminparticula))

    @Slot()
    def agregar_final(self):
        identificador = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value() #Sacamos lo que está ahí
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(identificador, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

        self.adminparticula.agregar_final(particula)
    
    @Slot()
    def agregar_inicio(self):
        identificador = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value() #Sacamos lo que está ahí
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(identificador, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

        self.adminparticula.agregar_inicio(particula)

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.adminparticula))

        row = 0

        for p in self.adminparticula:
            id_widget = QTableWidgetItem(str(p.id))
            origenX_widget = QTableWidgetItem(str(p.origen_x))
            origenY_widget = QTableWidgetItem(str(p.origen_y))
            destinoX_widget = QTableWidgetItem(str(p.destino_x))
            destinoY_widget = QTableWidgetItem(str(p.destino_y))
            velocidad_widget = QTableWidgetItem(str(p.velocidad))
            red_widget = QTableWidgetItem(str(p.red))
            green_widget = QTableWidgetItem(str(p.green))
            blue_widget = QTableWidgetItem(str(p.blue))
            distancia_widget = QTableWidgetItem(str(p.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origenX_widget)
            self.ui.tabla.setItem(row, 2, origenY_widget)
            self.ui.tabla.setItem(row, 3, destinoX_widget)
            self.ui.tabla.setItem(row, 4, destinoY_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1
    
    @Slot()
    def buscar_titulo(self):
        p_id = self.ui.id_lineEdit.text()
        
        encontrado = False

        for p in self.adminparticula:
            if p_id == str(p.id):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(p.id))
                origenX_widget = QTableWidgetItem(str(p.origen_x))
                origenY_widget = QTableWidgetItem(str(p.origen_y))
                destinoX_widget = QTableWidgetItem(str(p.destino_x))
                destinoY_widget = QTableWidgetItem(str(p.destino_y))
                velocidad_widget = QTableWidgetItem(str(p.velocidad))
                red_widget = QTableWidgetItem(str(p.red))
                green_widget = QTableWidgetItem(str(p.green))
                blue_widget = QTableWidgetItem(str(p.blue))
                distancia_widget = QTableWidgetItem(str(p.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenX_widget)
                self.ui.tabla.setItem(0, 2, origenY_widget)
                self.ui.tabla.setItem(0, 3, destinoX_widget)
                self.ui.tabla.setItem(0, 4, destinoY_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención!",
                f'La partícula con ID "{p_id}" no fue encontrado'
            )
   
    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for p in self.adminparticula:
            r = p.red
            g = p.green
            b = p.blue
            color = QColor(r, g, b)
            pen.setColor(color)

            origen_x = p.origen_x
            origen_y = p.origen_y
            destino_x = p.destino_x
            destino_y = p.destino_y

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x+3, origen_y+3, destino_x, destino_y, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def ordenar_id(self):
        self.adminparticula.ordenar_por_id()
        self.mostrar_tabla()
    
    @Slot()
    def ordenar_dis(self):
        self.adminparticula.ordenar_por_distancia()
        self.mostrar_tabla()
    
    @Slot()
    def ordenar_vel(self):
        self.adminparticula.ordenar_por_velocidad()
        self.mostrar_tabla()

    @Slot()
    def sort_id(self):
        self.adminparticula.ordenar_por_id()
        self.mostrar()
    
    @Slot()
    def sort_dis(self):
        self.adminparticula.ordenar_por_distancia()
        self.mostrar()
    
    @Slot()
    def sort_vel(self):
        self.adminparticula.ordenar_por_velocidad()
        self.mostrar()