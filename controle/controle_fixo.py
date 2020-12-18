import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from telas.tela_fixo import *
from model.aluminio import *
from model.conexao_vidro import *

### Classe do Menu Orçamento -> Fixos
class TelaFixo(QMainWindow):
	def __init__(self):
		super().__init__()
		self.tela_fixo = Ui_Tela_fixo()
		self.tela_fixo .setupUi(self)
		self.aluminio = PerfilAluminio()

		### CONEXÃO COM BANCO ###
		self.conexao_vidro = ConexaoVidro()
		self.event_preenche_combobox_vidro()
		### AÇÃO ###
		# Menu Orçamento -> Fixos
		# Botão Cancelar - Fecha a tela de Orçamento de Fixos
		self.tela_fixo.pushButton_cancelar.clicked.connect(self.event_bt_cancelar)

		### AÇÃO ###
		# Menu Orçamento -> Fixos
		# Botão Calcular - Retorna o valor calculado em Total Unitário
		self.tela_fixo.pushButton_calcular.clicked.connect(self.event_bt_calcular)

	def event_preenche_combobox_vidro(self):
		### PREENCHE O COMBOBOX COM OS ITENS DO BANCO ###
		resultado_busca = self.conexao_vidro.preenche_combobox_vidro()
		# precisa 2 for porque o banco retorna uma lista de túplas
		for itens in resultado_busca:
			for i in itens:
				self.tela_fixo.comboBox_vidro.addItem(i)


	### BOTÃO CANCELAR ###
	def event_bt_cancelar(self):
		self.close()

	### BOTÃO CALCULAR ###
	def event_bt_calcular(self):

		### TODO
		### FAZER LOGICA PARA QUANDO CLICAR NO BOTÃO CALCULAR E OS CAMPOS ESTIVEREM VAZIOS
		### APARECER POPUP OU DEIXAR CAMPOS VAZIOS EM VERMELHO
		largura = None
		altura = None
		quantidade = None
		margem = None
		valor_unitario = None
		valor_total = None

		try:
			largura = int(self.tela_fixo.lineEdit_largura.text())
			altura = int(self.tela_fixo.lineEdit_altura.text())
			quantidade = int(self.tela_fix8.lineEdit_quantidade.text())
			margem = int(self.tela_fixo.lineEdit_margem.text())
		except ValueError:
			print('Campos com valores incorretos!')
		else:
			valor_total = self.aluminio.calcular_fixo_total_geral(largura, altura, quantidade, margem)
			valor_unitario = self.aluminio.calcular_fixo_total_unitario(largura, altura, margem)

		self.tela_fixo.label_valor_total_unitario.setText(str(valor_unitario))
		self.tela_fixo.label_valor_total_geral.setText(str(valor_total))

