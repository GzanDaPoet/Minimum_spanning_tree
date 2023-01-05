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
        self.uic.btnKruscal.clicked.connect(self.doKruscal)
        self.uic.btnPrim.clicked.connect(self.doPrim)
        self.uic.btnInfo.clicked.connect(self.checkInput)
        self.uic.btnNext.clicked.connect(self.doNext)
        self.uic.btnPrev.clicked.connect(self.doPrev)
        self.uic.btnClear.clicked.connect(self.clear)
        self.count = 0
        self.length = 0
        self.arrayDraw = []

    def draw_root_graph(self, textArr):
        a = list(textArr.split('\n'))
        lst = []
        graph = []
        for x in a:
            test = x.split(", ")
            tmp = [int(b) for b in test]
            lst.append(tmp)
        for i in range(0, len(lst)):
            for j in range(0, len(lst[i])):
                if lst[i][j] > 0:
                    graph.append([i, j, lst[i][j]])
        draw_graph(graph, "root_graph.png")
        qpixMapRoot = QPixmap("root_graph.png")
        self.uic.lblMaTranGoc.setPixmap(qpixMapRoot)
        qpixMap = QPixmap("graph.png")
        self.uic.image_label.setPixmap(qpixMap)

    def clear(self):
        self.uic.tblMaTran.setRowCount(0)
        self.uic.tblMaTran.setColumnCount(0)
        self.uic.txtSoDinh.setText("")
        self.uic.txtChuY1_2.setText("")
        self.uic.txtChuY1.setText("")
        self.uic.txtMaTran.setPlainText("")
        self.uic.txtResult.setPlainText("")
        qpixMapRoot = QPixmap()
        self.uic.lblMaTranGoc.setPixmap(qpixMapRoot)
        qpixMap = QPixmap()
        self.uic.image_label.setPixmap(qpixMap)

    def checkInput(self, m, n):
        tmp = 0
        if not m.isnumeric():
            self.uic.txtChuY1.setText("Đỉnh nhập vào phải là số nguyên dương")
            self.uic.txtChuY1_2.setText("")
            print("Dinh nhap vao phai la so duong")
            return False
        else:
            self.uic.txtChuY1.setText("")
        m = int(m)
        lstMaTran = n.split("\n")
        for i in range(m):
            lstMaTran[i] = lstMaTran[i].split(", ")
        for x in range(m):
            for y in range(m):
                if lstMaTran[x][y].isnumeric():
                    tmp = tmp + 1
                else:
                    self.uic.txtChuY1_2.setText("Vui lòng kiểm tra lại ma trận!")
                    return False
        if tmp != m * m:
            self.uic.txtChuY1_2.setText("Ma trận và số đỉnh chưa khớp!")
            return False
        else:
            self.uic.txtChuY1_2.setText("")
            return True


    def setup_draw_graph(self, arr):
        self.length = len(arr)
        self.arrayDraw = arr
        self.count = 1
        draw_graph(self.arrayDraw[:self.count:], "graph.png")
        qpixMap = QPixmap("graph.png")
        self.uic.image_label.setPixmap(qpixMap)


    def showInfo(self, m, n):
        self.uic.tblMaTran.setRowCount(m)
        self.uic.tblMaTran.setColumnCount(m)
        lstMaTran = n.split("\n")
        for i in range(m):
            lstMaTran[i] = lstMaTran[i].split(", ")
        for x in range(m):
            self.uic.tblMaTran.setRowHeight(x, 1)
            self.uic.tblMaTran.setColumnWidth(x, 1)
            for y in range(m):
                self.uic.tblMaTran.setItem(x, y, QtWidgets.QTableWidgetItem(lstMaTran[x][y]))

    def doNext(self):
        if self.length >= self.count + 1:
            self.count = self.count + 1
            draw_graph(self.arrayDraw[:self.count:], "graph.png")
            qpixMap = QPixmap("graph.png")
            self.uic.image_label.setPixmap(qpixMap)

    def doPrev(self):
        if self.count - 1 >= 0:
            self.count = self.count - 1
            draw_graph(self.arrayDraw[:self.count:], "graph.png")
            qpixMap = QPixmap("graph.png")
            self.uic.image_label.setPixmap(qpixMap)

    def doKruscal(self):
        a = self.uic.txtSoDinh.text()
        b = self.uic.txtMaTran.toPlainText()
        rs = ""
        if (self.checkInput(a, b)):
            a = int(a)
            kruskal = kruskal_algo(a, b)
            for u, ver, weight in kruskal:
                rs = rs + ("%d - %d : %d \n" % (u, ver, weight))
            self.uic.txtResult.setPlainText(rs)
            self.showInfo(a, b)
            self.setup_draw_graph(kruskal)
            self.draw_root_graph(b)

    def doPrim(self):
        rs = ""
        a = self.uic.txtSoDinh.text()
        b = self.uic.txtMaTran.toPlainText()
        if self.checkInput(a, b):
            a = int(a)
            arrPrim = prim(a, b)
            for u, ver, weight in arrPrim:
                rs = rs + ("%d - %d : %d \n" % (u, ver, weight))
            self.uic.txtResult.setPlainText(rs)
            self.showInfo(a, b)
            self.setup_draw_graph(arrPrim)
            self.draw_root_graph(b)

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
