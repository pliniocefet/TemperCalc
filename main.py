import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from telas.tela_principal import *
from controle.controle_fixo import *


class TelaPrincipal(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui_tela_fixo = TelaFixo()


		### AÇÃO ###
		# Menu Arquivo -> Sair
		# Fecha o Sistema
		self.ui.actionSair.triggered.connect(self.event_menu_sair)

		### AÇÃO ###
		# Menu Orçamento -> Fixos
		# Chama a tela para orçamento de fixos
		self.ui.actionVidros_Fixos.triggered.connect(self.event_menu_fixo)


	@QtCore.pyqtSlot()
	def event_menu_sair(self):
		sys.exit()

	@QtCore.pyqtSlot()
	def event_menu_fixo(self):
		self.ui_tela_fixo.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	principal = TelaPrincipal()
	principal.show()
	sys.exit(app.exec_())