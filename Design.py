from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def showdialog(self,window_title,title,content):
       msg = QtWidgets.QMessageBox()
       msg.setIcon(QtWidgets.QMessageBox.Information)
    
       msg.setText(title)
       msg.setInformativeText(content)
       msg.setWindowTitle(window_title)
       msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
       msg.exec_()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 675)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 780, 751))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setProperty("background", QtGui.QColor(255, 255, 255))
        self.frame.setObjectName("frame")
        self.img_viewer = QtWidgets.QGraphicsView(self.frame)
        self.img_viewer.setGeometry(QtCore.QRect(30, 120, 381, 211))
        self.img_viewer.setObjectName("img_viewer")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(29, 15, 330, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 141, 16))
        self.label_2.setObjectName("label_2")
        self.btn_img_upload = QtWidgets.QPushButton(self.frame)
        self.btn_img_upload.setGeometry(QtCore.QRect(30, 350, 71, 31))
        self.btn_img_upload.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.btn_img_upload.setObjectName("btn_img_upload")
        self.bnt_camera_show = QtWidgets.QPushButton(self.frame)
        self.bnt_camera_show.setGeometry(QtCore.QRect(110, 350, 81, 31))
        self.bnt_camera_show.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.bnt_camera_show.setAutoDefault(False)
        self.bnt_camera_show.setDefault(False)
        self.bnt_camera_show.setFlat(False)
        self.bnt_camera_show.setObjectName("bnt_camera_show")
        self.btn_camera_capture = QtWidgets.QPushButton(self.frame)
        self.btn_camera_capture.setGeometry(QtCore.QRect(200, 350, 31, 31))
        self.btn_camera_capture.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.btn_camera_capture.setObjectName("btn_camera_capture")
        self.btn_face = QtWidgets.QPushButton(self.frame)
        self.btn_face.setGeometry(QtCore.QRect(350, 350, 61, 31))
        self.btn_face.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.btn_face.setObjectName("btn_face")
        self.cmb_classes = QtWidgets.QComboBox(self.frame)
        self.cmb_classes.setGeometry(QtCore.QRect(430, 350, 91, 31))
        self.cmb_classes.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.cmb_classes.setObjectName("cmb_classes")
        self.btn_classes_list = QtWidgets.QPushButton(self.frame)
        self.btn_classes_list.setGeometry(QtCore.QRect(530, 350, 91, 31))
        self.btn_classes_list.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.btn_classes_list.setObjectName("btn_classes_list")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 410, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(430, 90, 141, 16))
        self.label_4.setObjectName("label_4")
        self.btn_run = QtWidgets.QPushButton(self.frame)
        self.btn_run.setGeometry(QtCore.QRect(650, 350, 101, 31))
        self.btn_run.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"border-color: red;\n"
"color: red;\n"
"padding: 4px;")
        self.btn_run.setObjectName("btn_run")
        self.listView_class = QtWidgets.QTableWidget(self.frame)
        self.listView_class.setGeometry(QtCore.QRect(430, 120, 321, 211))
        self.listView_class.setStyleSheet("")
        self.listView_class.setObjectName("listView_class")
        self.listView_class.setColumnCount(0)
        self.listView_class.setRowCount(0)
        self.listView_result = QtWidgets.QTableWidget(self.frame)
        self.listView_result.setGeometry(QtCore.QRect(30, 440, 721, 181))
        self.listView_result.setObjectName("listView_result")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(470, 630, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lbl_toplam_kayit = QtWidgets.QLabel(self.frame)
        self.lbl_toplam_kayit.setGeometry(QtCore.QRect(550, 630, 31, 16))
        self.lbl_toplam_kayit.setObjectName("lbl_toplam_kayit")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(590, 630, 41, 16))
        self.label_8.setObjectName("label_8")
        self.lbl_tanimli = QtWidgets.QLabel(self.frame)
        self.lbl_tanimli.setGeometry(QtCore.QRect(640, 630, 21, 16))
        self.lbl_tanimli.setObjectName("lbl_tanimli")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(675, 630, 51, 16))
        self.label_9.setObjectName("label_9")
        self.lbl_tanimsiz = QtWidgets.QLabel(self.frame)
        self.lbl_tanimsiz.setGeometry(QtCore.QRect(735, 630, 21, 16))
        self.lbl_tanimsiz.setObjectName("lbl_tanimsiz")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 50, 601, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.chk_SSIM = QtWidgets.QRadioButton(self.frame)
        self.chk_SSIM.setGeometry(QtCore.QRect(110, 631, 50, 17))
        self.chk_SSIM.setObjectName("chk_SSIM")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(30, 630, 71, 16))
        self.label_12.setObjectName("label_12")
        self.chk_MSE = QtWidgets.QRadioButton(self.frame)
        self.chk_MSE.setGeometry(QtCore.QRect(170, 631, 50, 17))
        self.chk_MSE.setObjectName("chk_MSE")
        self.chk_PSNR = QtWidgets.QRadioButton(self.frame)
        self.chk_PSNR.setGeometry(QtCore.QRect(230, 631, 50, 17))
        self.chk_PSNR.setObjectName("chk_PSNR")
        self.chk_all = QtWidgets.QRadioButton(self.frame)
        self.chk_all.setEnabled(True)
        self.chk_all.setGeometry(QtCore.QRect(290, 631, 50, 17))
        self.chk_all.setChecked(True)
        self.chk_all.setObjectName("chk_all")
        self.cmb_cascade = QtWidgets.QComboBox(self.frame)
        self.cmb_cascade.setGeometry(QtCore.QRect(260, 350, 81, 31))
        self.cmb_cascade.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"\n"
"")
        self.cmb_cascade.setObjectName("cmb_cascade")
        self.img_person = QtWidgets.QGraphicsView(self.frame)
        self.img_person.setGeometry(QtCore.QRect(660, 230, 91, 101))
        self.img_person.setVisible(False)
        self.img_person.setObjectName("img_person")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Y Ü Z </span><span style=\" font-size:12pt; color:#ffffff;\">- </span><span style=\" font-size:12pt;\">T A N I M A </span><span style=\" font-size:12pt; color:#ffffff;\">-</span><span style=\" font-size:12pt;\"> İ L E</span><span style=\" font-size:12pt; color:#ffffff;\"> -</span><span style=\" font-size:12pt;\"> Y O K L A M A</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Karşılaştırma Resmi :"))
        self.btn_img_upload.setText(_translate("MainWindow", "Yükle"))
        self.bnt_camera_show.setText(_translate("MainWindow", "Kamera"))
        self.btn_camera_capture.setText(_translate("MainWindow", "[ ]"))
        self.btn_face.setText(_translate("MainWindow", "Algıla"))
        self.btn_classes_list.setText(_translate("MainWindow", "Getir"))
        self.label_3.setText(_translate("MainWindow", "Yoklama Sonucu :"))
        self.label_4.setText(_translate("MainWindow", "Sınıf Listesi :"))
        self.btn_run.setText(_translate("MainWindow", "B A Ş L A T"))
        self.label_5.setText(_translate("MainWindow", "Toplam Kayıt :"))
        self.lbl_toplam_kayit.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Tanımlı :"))
        self.lbl_tanimli.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Tanımsız :"))
        self.lbl_tanimsiz.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "OpenCv kütüphanesi kullanılarak, algılanan yüzlerin sınıflara ait yüzler ile  çeşitli algoritmalar ile karşılaştırılması."))
        self.chk_SSIM.setText(_translate("MainWindow", "SSIM"))
        self.label_12.setText(_translate("MainWindow", "Algoritmalar :"))
        self.chk_MSE.setText(_translate("MainWindow", "MSE"))
        self.chk_PSNR.setText(_translate("MainWindow", "PSNR"))
        self.chk_all.setText(_translate("MainWindow", "ALL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

