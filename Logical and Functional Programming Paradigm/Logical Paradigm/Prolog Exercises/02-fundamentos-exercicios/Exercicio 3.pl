pai(adao, abel).
pai(adao, caim).
pai(adao, sete).
pai(caim, enoque).
pai(enoque, irad).
pai(irad, meujael).
pai(meujael, metusael).
pai(metusael, lameque).
pai(lameque, jabal).
pai(lameque, jubal).
pai(lameque, tubalcaim).
pai(lameque, naama).

mae(eva, abel).
mae(eva, caim).
mae(eva, sete).
mae(ada, jabal).
mae(ada, jubal).
mae(zila, tubalcaim).
mae(zila, naama).

homem(sete).
homem(caim).
homem(jabal).
homem(jubal).
homem(tubalcaim).

mulher(naama).

homem(X) :- pai(X,Y).
mulher(X) :- mae(X,Y).
mesmo_pai(X,Y) :- pai(Z,X),pai(Z,Y).
mesma_mae(X,Y) :- mae(Z,X),mae(Z,Y).
irmaos(X,Y) :- mesmo_pai(X,Y);mesma_mae(X,Y).
casados(X,Y) :- pai(X,Z),mae(Y,Z);mae(X,Z),pai(Y,Z).
avo(X,Y) :- pai(X,Z),pai(Z,Y);mae(Z,Y).
irma(X,Y) :- mulher(x),irmaos(X,Y).
