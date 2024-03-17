from main import Relogio24Horas



def test_tique():
    relogio = Relogio24Horas()
    
    relogio.tique()
    assert relogio.horas == 0
    assert relogio.minutos == 0
    assert relogio.segundos == 1

    
    relogio.segundos = 59
    relogio.tique()
    assert relogio.horas == 0
    assert relogio.minutos == 1
    assert relogio.segundos == 0

    
    relogio.minutos = 59
    relogio.segundos = 59
    relogio.tique()
    assert relogio.horas == 1
    assert relogio.minutos == 0
    assert relogio.segundos == 0

    relogio.horas = 23
    relogio.minutos = 59
    relogio.segundos = 59
    relogio.tique()
    assert relogio.horas == 0
    assert relogio.minutos == 0
    assert relogio.segundos == 0

    relogio.horas = 24
    relogio.minutos = 30
    relogio.segundos = 0
    relogio.tique()
    assert relogio.horas == 0
    assert relogio.minutos == 30
    assert relogio.segundos == 1

def test_compare():
    relogio1 = Relogio24Horas()
    relogio2 = Relogio24Horas()
    assert relogio1.compare(relogio2) == 0

    relogio1.horas = 12
    relogio1.minutos = 30
    relogio2.horas = 12
    relogio2.minutos = 30
    assert relogio1.compare(relogio2) == 0

    #B>A
    relogio1.horas = 12
    relogio1.minutos = 30
    relogio1.segundos = 20
    relogio2.horas = 13
    relogio2.minutos = 50
    relogio2.segundos = 33
    assert relogio1.compare(relogio2) == -1

    #A>B
    relogio1.horas = 16
    relogio1.minutos = 30
    relogio1.segundos = 26
    relogio2.horas = 13
    relogio2.minutos = 50
    relogio2.segundos = 49
    assert relogio1.compare(relogio2) == 1

def test_add():
    relogio1 = Relogio24Horas()
    relogio2 = Relogio24Horas()
    result = relogio1.add(relogio2)
    assert  result.horas == 0
    assert  result.minutos == 0
    assert  result.segundos == 0

    #Sem rollover
    relogio1.horas = 12
    relogio1.minutos = 30
    relogio1.segundos = 20
    relogio2.horas = 00
    relogio2.minutos = 20
    relogio2.segundos = 00
    result = relogio1.add(relogio2)
    assert  result.horas == 12
    assert  result.minutos == 50
    assert  result.segundos == 20

    #Com rollover nos segundos
    relogio1.horas = 00
    relogio1.minutos = 00
    relogio1.segundos = 20
    relogio2.horas = 00
    relogio2.minutos = 00
    relogio2.segundos = 40
    result = relogio1.add(relogio2)
    assert  result.horas == 00
    assert  result.minutos == 1
    assert  result.segundos == 00

    #Com rollover nos minutos
    relogio1.horas = 12
    relogio1.minutos = 30   
    relogio1.segundos = 00
    relogio2.horas = 00
    relogio2.minutos = 30
    relogio2.segundos = 0
    result = relogio1.add(relogio2)
    assert  result.horas == 13
    assert  result.minutos == 0
    assert  result.segundos == 00

    #Com rollover nas horas
    relogio1.horas = 12
    relogio1.minutos = 30   
    relogio1.segundos = 00
    relogio2.horas = 12
    relogio2.minutos = 00
    relogio2.segundos = 0
    result = relogio1.add(relogio2)
    assert  result.horas == 00
    assert  result.minutos == 30
    assert  result.segundos == 00

def test_subtraction():
    relogio1 = Relogio24Horas()
    relogio2 = Relogio24Horas()
    result = relogio1.subtraction(relogio2)
    assert  result.horas == 0
    assert  result.minutos == 0
    assert  result.segundos == 0

    #A>B
    relogio1.horas = 12
    relogio1.minutos = 30
    relogio1.segundos = 00
    relogio2.horas = 12
    relogio2.minutos = 20
    relogio2.segundos = 00
    result = relogio1.subtraction(relogio2)
    assert  result.horas == 00
    assert  result.minutos == 10
    assert  result.segundos == 00

    #B>A
    relogio1.horas = 00
    relogio1.minutos = 40
    relogio1.segundos = 00
    relogio2.horas = 1
    relogio2.minutos = 00
    relogio2.segundos = 00
    result = relogio1.subtraction(relogio2)
    assert  result.horas == 23
    assert  result.minutos == 40
    assert  result.segundos == 00

    #B=A
    relogio1.horas = 12
    relogio1.minutos = 30   
    relogio1.segundos = 00
    relogio2.horas = 12
    relogio2.minutos = 30
    relogio2.segundos = 0
    result = relogio1.subtraction(relogio2)
    assert  result.horas == 0
    assert  result.minutos == 0
    assert  result.segundos == 00
