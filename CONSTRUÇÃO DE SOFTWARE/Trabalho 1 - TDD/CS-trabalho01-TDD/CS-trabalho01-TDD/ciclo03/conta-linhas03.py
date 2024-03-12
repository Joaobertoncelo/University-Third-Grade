# Nome: João Pedro Peres Bertoncelo
# RA: 112650

# 2o passo (green): copie a última versão do código aqui e escreva novo código para fazer o novo caso de teste passar
def conta_linhas(arquivo):
	file = open(arquivo, "r")
	texto = file.read()
	separaTexto = texto.split("\n")
	contadorLinhas = 0
	for i in separaTexto:
		if i != "":
			contadorLinhas += 1

	return contadorLinhas

# 1o passo (red): copie aqui os casos de teste 01 e 02 e escreva o novo caso de teste 		
def test_03():
	# formato do caso de teste automatizado
	# assert conta_linhas(entrada) == saida_esperada
	assert conta_linhas("teste.txt") == 1
	assert conta_linhas("teste2.txt") == 2
	assert conta_linhas("teste3.txt") == 2

if __name__ == "__main__":
	test_03()
	print("Passou em todos os testes!")
	
# 3o passo (refactor): precisa refatorar o código?
# Caso a resposta seja sim, crie o arquivo conta-linhas03a.py com o código refatorado
