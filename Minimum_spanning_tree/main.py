import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from Home import Ui_MainWindow
from Prim import prim
from Kruskal import kruskal_algo
from DrawGraph import draw_graph


class MainWindow:
    def __init__(self):
        self.main_win = QtWidgets.QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.btnKruscal.clicked.connect(self.dokruscal)
        self.uic.btnPrim.clicked.connect(self.doprim)
        self.uic.btnInfo.clicked.connect(self.showInfo)
        self.uic.btnNext.clicked.connect(self.donext)
        self.uic.btnPrev.clicked.connect(self.doPrev)
        self.count = 0
        self.length = 0
        self.arrayDraw = []

    def showInfo(self, m, n):
        self.uic.tblMaTran.setRowCount(m)
        self.uic.tblMaTran.setColumnCount(m)
        lstMaTran = n.split("\n")
        for i in range(m):
            lstMaTran[i] = lstMaTran[i].split(", ")
        for x in range(m):
            self.uic.tblMaTran.setRowHeight(x,1)
            self.uic.tblMaTran.setColumnWidth(x,1)
            for y in range(m):
                self.uic.tblMaTran.setItem(x, y, QtWidgets.QTableWidgetItem(lstMaTran[x][y]))
        print("end")


    def donext(self):
        if self.length >= self.count + 1:
            self.count = self.count + 1
            draw_graph(self.arrayDraw[:self.count:])
            qpixMap = QPixmap("graph.png")
            self.uic.image_label.setPixmap(qpixMap)


    def doPrev(self):
        if self.count - 1 >= 0:
            self.count = self.count - 1
            draw_graph(self.arrayDraw[:self.count:])
            qpixMap = QPixmap("graph.png")
            self.uic.image_label.setPixmap(qpixMap)

    def dokruscal(self):
        a = int(self.uic.txtSoDinh.text())
        b = self.uic.txtMaTran.toPlainText()
        rs = ""
        kruskal = kruskal_algo(a, b)
        for u, ver, weight in kruskal:
            rs = rs + ("%d - %d : %d \n" % (u, ver, weight))
        self.uic.txtResult.setPlainText(rs)
        self.length = len(kruskal)
        self.arrayDraw = kruskal
        self.count = 1
        self.showInfo(a, b)
        qpixMap = QPixmap()
        self.uic.image_label.setPixmap(qpixMap)

    def doprim(self):
        rs = ""
        a = int(self.uic.txtSoDinh.text())
        b = self.uic.txtMaTran.toPlainText()
        arrPrim = prim(a, b)
        for u, ver, weight in arrPrim:
            rs = rs + ("%d - %d : %d \n" % (u, ver, weight))
        self.uic.txtResult.setPlainText(rs)
        self.length = len(arrPrim)
        self.count = 1
        self.arrayDraw = arrPrim
        self.showInfo(a, b)
        qpixMap = QPixmap()
        self.uic.image_label.setPixmap(qpixMap)


    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

