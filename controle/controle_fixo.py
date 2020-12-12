import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from telas.tela_fixo import *

### Classe do Menu Orçamento -> Fixos
class TelaFixo(QMainWindow):
	def __init__(self):
		super().__init__()
		self.tela_fixo = Ui_Tela_fixo()
		self.tela_fixo.setupUi(self)

		### AÇÃO ###
		# Menu Orçamento -> Fixos
		# Botão Cancelar - Fecha a tela de Orçamento de Fixos
		self.tela_fixo.pushButton_cancelar.clicked.connect(self.event_bt_cancelar)

		### AÇÃO ###
		# Menu Orçamento -> Fixos
		# Botão Calcular - Retorna o valor calculado em Total Unitário
		self.tela_fixo.pushButton_calcular.clicked.connect(self.event_bt_calcular)

	def event_bt_cancelar(self):
		self.close()

	def event_bt_calcular(self):
		largura = int(self.tela_fixo.lineEdit_largura.text()) / 1000
		altura = int(self.tela_fixo.lineEdit_altura.text()) / 1000
		quantidade = int(self.tela_fixo.lineEdit_quantidade.text())

		total_unitario = (largura * altura)
		total_geral = total_unitario * quantidade
		self.tela_fixo.label_valor_total_unitario.setText(str(total_unitario))
		self.tela_fixo.label_valor_total_geral.setText(str(total_geral))
