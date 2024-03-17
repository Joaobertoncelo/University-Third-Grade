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


# 1o passo (red): copie aqui os casos de teste 01 a 07 e escreva o novo caso de teste 		
def test_08():
	# formato do caso de teste automatizado
	# assert conta_linhas(entrada) == saida_esperada
	assert conta_linhas("teste.txt") == 1
	assert conta_linhas("teste2.txt") == 2
	assert conta_linhas("teste3.txt") == 2
	assert conta_linhas("teste4.txt") == 2
	assert conta_linhas("teste5.txt") == 3
	assert conta_linhas("teste6.txt") == 4
	assert conta_linhas("teste7.txt") == 6
	assert conta_linhas("teste8.txt") == 1

if __name__ == "__main__":
	test_08()
	print("Passou em todos os testes!")
	
# 3o passo (refactor): precisa refatorar o código?
# Caso a resposta seja sim, crie o arquivo conta-linhas08a.py com o código refatorado
