# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_fixo_teste.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_fixo(object):
    def setupUi(self, Tela_fixo):
        Tela_fixo.setObjectName("Tela_fixo")
        Tela_fixo.resize(490, 242)
        Tela_fixo.setMinimumSize(QtCore.QSize(490, 220))
        self.centralwidget = QtWidgets.QWidget(Tela_fixo)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_fixos = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_fixos.setGeometry(QtCore.QRect(9, 9, 470, 220))
        self.groupBox_fixos.setMinimumSize(QtCore.QSize(470, 220))
        self.groupBox_fixos.setMaximumSize(QtCore.QSize(470, 0))
        self.groupBox_fixos.setObjectName("groupBox_fixos")
        self.label_largura = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_largura.setGeometry(QtCore.QRect(12, 20, 47, 13))
        self.label_largura.setObjectName("label_largura")
        self.lineEdit_largura = QtWidgets.QLineEdit(self.groupBox_fixos)
        self.lineEdit_largura.setGeometry(QtCore.QRect(10, 40, 70, 20))
        self.lineEdit_largura.setObjectName("lineEdit_largura")
        self.label_altura = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_altura.setGeometry(QtCore.QRect(94, 20, 31, 16))
        self.label_altura.setObjectName("label_altura")
        self.lineEdit_altura = QtWidgets.QLineEdit(self.groupBox_fixos)
        self.lineEdit_altura.setGeometry(QtCore.QRect(94, 40, 70, 20))
        self.lineEdit_altura.setObjectName("lineEdit_altura")
        self.label_quantidade = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_quantidade.setGeometry(QtCore.QRect(180, 20, 31, 16))
        self.label_quantidade.setObjectName("label_quantidade")
        self.lineEdit_quantidade = QtWidgets.QLineEdit(self.groupBox_fixos)
        self.lineEdit_quantidade.setGeometry(QtCore.QRect(180, 40, 70, 20))
        self.lineEdit_quantidade.setObjectName("lineEdit_quantidade")
        self.pushButton_calcular = QtWidgets.QPushButton(self.groupBox_fixos)
        self.pushButton_calcular.setGeometry(QtCore.QRect(10, 180, 75, 25))
        self.pushButton_calcular.setObjectName("pushButton_calcular")
        self.pushButton_cancelar = QtWidgets.QPushButton(self.groupBox_fixos)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(90, 180, 75, 25))
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.lineEdit_margem = QtWidgets.QLineEdit(self.groupBox_fixos)
        self.lineEdit_margem.setGeometry(QtCore.QRect(10, 140, 70, 20))
        self.lineEdit_margem.setObjectName("lineEdit_margem")
        self.label_margem = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_margem.setGeometry(QtCore.QRect(12, 120, 47, 13))
        self.label_margem.setObjectName("label_margem")
        self.label_total_unitario = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_total_unitario.setGeometry(QtCore.QRect(280, 9, 171, 31))
        self.label_total_unitario.setObjectName("label_total_unitario")
        self.label_total_geral = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_total_geral.setGeometry(QtCore.QRect(270, 105, 171, 31))
        self.label_total_geral.setObjectName("label_total_geral")
        self.comboBox_vidro = QtWidgets.QComboBox(self.groupBox_fixos)
        self.comboBox_vidro.setGeometry(QtCore.QRect(100, 90, 69, 20))
        self.comboBox_vidro.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_vidro.setObjectName("comboBox_vidro")
        self.label_cifra_unitario = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_cifra_unitario.setGeometry(QtCore.QRect(291, 50, 41, 31))
        self.label_cifra_unitario.setObjectName("label_cifra_unitario")
        self.label_cifra_geral = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_cifra_geral.setGeometry(QtCore.QRect(292, 145, 41, 31))
        self.label_cifra_geral.setObjectName("label_cifra_geral")
        self.label_valor_total_unitario = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_valor_total_unitario.setGeometry(QtCore.QRect(340, 60, 91, 21))
        self.label_valor_total_unitario.setStyleSheet("QLabel {\n"
"    color: red;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"}")
        self.label_valor_total_unitario.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_valor_total_unitario.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_valor_total_unitario.setLineWidth(1)
        self.label_valor_total_unitario.setIndent(-1)
        self.label_valor_total_unitario.setObjectName("label_valor_total_unitario")
        self.label_valor_total_geral = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_valor_total_geral.setGeometry(QtCore.QRect(340, 153, 91, 21))
        self.label_valor_total_geral.setStyleSheet("QLabel {\n"
"    color: red;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"}")
        self.label_valor_total_geral.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_valor_total_geral.setObjectName("label_valor_total_geral")
        self.label_tipo_vidro = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_tipo_vidro.setGeometry(QtCore.QRect(100, 70, 61, 16))
        self.label_tipo_vidro.setObjectName("label_tipo_vidro")
        self.pushButton_inserir = QtWidgets.QPushButton(self.groupBox_fixos)
        self.pushButton_inserir.setGeometry(QtCore.QRect(180, 180, 75, 25))
        self.pushButton_inserir.setObjectName("pushButton_inserir")
        self.label_espessura = QtWidgets.QLabel(self.groupBox_fixos)
        self.label_espessura.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_espessura.setObjectName("label_espessura")
        self.comboBox_espessura = QtWidgets.QComboBox(self.groupBox_fixos)
        self.comboBox_espessura.setGeometry(QtCore.QRect(10, 90, 75, 20))
        self.comboBox_espessura.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_espessura.setObjectName("comboBox_espessura")
        self.comboBox_espessura.addItem("")
        self.comboBox_espessura.addItem("")
        Tela_fixo.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_fixo)
        QtCore.QMetaObject.connectSlotsByName(Tela_fixo)
        Tela_fixo.setTabOrder(self.lineEdit_largura, self.lineEdit_altura)
        Tela_fixo.setTabOrder(self.lineEdit_altura, self.lineEdit_quantidade)
        Tela_fixo.setTabOrder(self.lineEdit_quantidade, self.comboBox_vidro)
        Tela_fixo.setTabOrder(self.comboBox_vidro, self.lineEdit_margem)
        Tela_fixo.setTabOrder(self.lineEdit_margem, self.pushButton_calcular)
        Tela_fixo.setTabOrder(self.pushButton_calcular, self.pushButton_cancelar)

    def retranslateUi(self, Tela_fixo):
        _translate = QtCore.QCoreApplication.translate
        Tela_fixo.setWindowTitle(_translate("Tela_fixo", "Vidro Fixo"))
        self.groupBox_fixos.setTitle(_translate("Tela_fixo", "Vidro Fixo"))
        self.label_largura.setText(_translate("Tela_fixo", "Largura"))
        self.label_altura.setText(_translate("Tela_fixo", "Altura"))
        self.label_quantidade.setText(_translate("Tela_fixo", "Quant"))
        self.pushButton_calcular.setText(_translate("Tela_fixo", "Calcular"))
        self.pushButton_cancelar.setText(_translate("Tela_fixo", "Cancelar"))
        self.label_margem.setText(_translate("Tela_fixo", "Margem"))
        self.label_total_unitario.setText(_translate("Tela_fixo", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Total Unitário:</span></p></body></html>"))
        self.label_total_geral.setText(_translate("Tela_fixo", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Total Geral:</span></p></body></html>"))
        self.comboBox_vidro.setPlaceholderText(_translate("Tela_fixo", "Vidro"))
        self.label_cifra_unitario.setText(_translate("Tela_fixo", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff0000;\">R$</span></p></body></html>"))
        self.label_cifra_geral.setText(_translate("Tela_fixo", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff0000;\">R$</span></p></body></html>"))
        self.label_valor_total_unitario.setText(_translate("Tela_fixo", "0000,00"))
        self.label_valor_total_geral.setText(_translate("Tela_fixo", "0000,00"))
        self.label_tipo_vidro.setText(_translate("Tela_fixo", "Tipo de Vidro"))
        self.pushButton_inserir.setText(_translate("Tela_fixo", "Inserir"))
        self.label_espessura.setText(_translate("Tela_fixo", "Espessura:"))
        self.comboBox_espessura.setCurrentText(_translate("Tela_fixo", "Espessura"))
        self.comboBox_espessura.setPlaceholderText(_translate("Tela_fixo", "Espessura"))
        self.comboBox_espessura.setItemText(0, _translate("Tela_fixo", "08mm"))
        self.comboBox_espessura.setItemText(1, _translate("Tela_fixo", "10mm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_fixo = QtWidgets.QMainWindow()
    ui = Ui_Tela_fixo()
    ui.setupUi(Tela_fixo)
    Tela_fixo.show()
    sys.exit(app.exec_())