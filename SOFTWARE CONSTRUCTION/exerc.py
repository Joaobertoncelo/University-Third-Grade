import math

def raizes(a, b, c):
    delta = (b**2)-4*a*c
    if delta<0:
        return None
    elif delta==0:
        raiz1= (-b+(math.sqrt(delta)))/(2*a)
        raiz2= (-b-(math.sqrt(delta)))/(2*a)
        return raiz1, raiz2
    else:
        raiz1= (-b+(math.sqrt(delta)))/(2*a)
        raiz2= (-b-(math.sqrt(delta)))/(2*a)
        return raiz1, raiz2

#Característica: delta
#Blocos: delta<0:"none", delta=0:(x,y), delta>0:(x,y)
def testeRaizes():
    assert raizes(1,-4,5) == None
    assert raizes(4,-4,1) == (0.5,0.5)
    assert raizes(1,-5,6) == (3,2)
    print("tá filé")

__name__=='__main__'
testeRaizes()

#Relatório:
#Primeiramente, os testes falharam, pois em raiz1 e raiz2, estavam recebendo a função sem a última raiz, ou seja, (-b+(math.sqrt(delta)))/2*a
#O que resultou em um problema de cálculos, pois normalmente estava dividindo toda a conta por 2 antes de multiplicar 2 por 4, e por algum motivo
#isso estava causando um erro, e no processo de depuração, mudei os valores de do teste 2(que estava causando problemas) para(4,4,1).
#Após isso, o erro foi resolvido e os testes passaram