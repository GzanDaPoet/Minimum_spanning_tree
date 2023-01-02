import sys
from PyQt5 import QtWidgets
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
        # self.uic.btnInfo.clicked.connect(self.)
        # self.uic.btnNext.clicked.connect(self.)
        # self.uic.btnPrev.clicked.connect(self.)

    # def showInfo(self):

    # def donext(self):


    def dokruscal(self):
        a = int(self.uic.txtSoDinh.text())
        b = self.uic.txtMaTran.toPlainText()
        rs = ""
        kruskal = kruskal_algo(a, b)
        print(kruskal)
        for u, ver, weight in kruskal:
            rs = rs + ("%d - %d : %d \n" % (u, ver, weight))
        self.uic.txtResult.setPlainText(rs)
        draw_graph(kruskal)

    def doprim(self):
        a = int(self.uic.txtSoDinh.text())
        b = self.uic.txtMaTran.toPlainText()
        prim(a, b)
        self.uic.txtResult.setPlainText(prim(a, b))


    # def showinfo(self):
    #     self.uic.pushButton.setEnabled(False)
    #     a = self.uic.lineEdit.text()

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     ui.pushButton_2.clicked.connect(ui.lineEdit.setText(self="S123"))
#     sys.exit(app.exec_())
