

class PerfilAluminio():

	def __init__(self):
		self.PRECO_VIDRO = 100.00
		self.PRECO_ALUMINIO = 27.70

	def calcular_fixo_total_geral(self, largura, altura, quantidade, margem):
		total_vidro = ((largura / 1000) * (altura / 1000)) * self.PRECO_VIDRO
		total_aluminio = (((largura / 1000) + (altura / 1000)) * 2) * self.PRECO_ALUMINIO
		total_unitario = ((total_aluminio + total_vidro) * (margem / 100)) + (total_aluminio + total_vidro)
		total_geral = None
		
		if quantidade == 1:
			total_geral = total_unitario
			return total_geral
		else:
			total_geral = total_unitario * quantidade
			return total_geral

	def calcular_fixo_total_unitario(self, largura, altura, margem):
		
		total_vidro = ((largura / 1000) * (altura / 1000)) * self.PRECO_VIDRO
		total_aluminio = (((largura / 1000) + (altura / 1000)) * 2) * self.PRECO_ALUMINIO
		total_unitario = ((total_aluminio + total_vidro) * (margem / 100)) + (total_aluminio + total_vidro)

		return total_unitario