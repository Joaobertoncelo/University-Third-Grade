# Nome: João Pedro Peres Bertoncelo
# RA: 112650

# 2o passo (green): escreva o código para fazer o caso de teste passar
def conta_linhas(arquivo):
	file = open(arquivo, "r")
	texto = file.read()
	separaTexto = texto.split("\n")
	contadorLinhas = 0
	for i in separaTexto:
		if i != "":
			contadorLinhas += 1

	return contadorLinhas

# 1o passo (red): escreva um caso de teste 	
def test_01():
	# formato do caso de teste automatizado
	# assert conta_linhas(entrada) == saida_esperada
	assert conta_linhas("teste.txt") == 1

if __name__ == "__main__":
	test_01()
	print("Passou em todos os testes!")