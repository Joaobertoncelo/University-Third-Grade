#lang racket
(require examples)

;; 1 - Descobrir o nome dos times

;; ListaString -> ListaResultado
;; Transforma a lista de strings da entrada em uma lista de resultados
(examples
    (check-equal? (string->resultado "a 1 b 2") (list "a" "1" "b" "2"))
    (check-equal? (string->resultado "c 3 d 4") (list "c" "3" "d" "4")))
(define (string->resultado s)
    (string-split s " "))

;; ListaResultados -> ListaString
;; a partir de uma lista de resultados, retorna uma lista com os nomes dos times
(examples
    (check-equal? (encontra-times (list (make-resultado "a" "1" "b" "2") (make-resultado "c" "3" "d" "4")))
                  (list "a" "b" "c" "d")))
(define (encontra-times resultados)
    (append (first resultados)
            (third resultados)))

(define (make-resultado time1 gols1 time2 gols2)
    (list time1 gols1 time2 gols2))

;; 2 - Calcular os pontos, número de vitórias e saldo de gols

;; ListaString ListaResultado -> ListaDesempenho
;; Calcula o desempenho de cada time
;; sendo o primeiro valor a quantidade de pontos (vitória = 3, empate = 1, derrota = 0)
;; o segundo valor a quantidade de vitórias
;; o terceiro valor o saldo de gols
(examples
    (check-equal? (calcula-desempenhos (list "a" "b" "c" "d") (list (string->resultado "a 1 b 2") (string->resultado "c 3 d 4")))
                  (list (list "a" "0" "0" "-1") (list "b" "3" "1" "1") (list "c" "0" "0" -1) (list "d" 3 1 1)))
    (check-equal? (calcula-desempenhos (list "a" "b" "c" "d") (list (string->resultado "a 1 b 2") (string->resultado "c 3 d 4") (string->resultado "a 2 c 3") (string->resultado "b 4 d 5")))
                  (list (list "a" "0" "0" "-2") (list "b" "3" "1" "0") (list "c" "3" "1" "0") (list "d" "3" "1" "0"))))

(define (calcula-desempenhos times resultados)
    (map (lambda (time) (calcula-desempenho time resultados)) times))

(define (calcula-desempenho time resultados)
    (define pontos (foldl (lambda (r acc) (if (or (equal? (first r) time) (equal? (third r) time))
                                               (+ acc (if (equal? (second r) (fourth r)) 1 3))
                                               acc)) 0 resultados))
    (define vitorias (foldl (lambda (r acc) (if (equal? (first r) time) (+ acc (if (equal? (second r) (fourth r)) 1 0)) acc)) 0 resultados))
    (define saldo-gols (foldl (lambda (r acc) 
           (if (equal? (first r) time) 
               (+ acc (- (second r) (fourth r))) 
               (if (equal? (third r) time) 
                   (+ acc (- (fourth r) (second r))) 
                   acc))) 
         0 
         resultados))
    (list time pontos vitorias saldo-gols))

;; 3 - Classificar os times de acordo com o desempenho

;; ListaDesempenho -> ListaDesempenho
;; Faz a classificao dos times pelo desempenho
;; sendo a ordem alfabética um critério de desempate
(examples
    (check-equal? (classifica (list (list "a" "1" "0" "-1") (list "b" "0" "0" "1") (list "c" "1" "0" "-1") (list "d" "0" "0" "1")))
                  (list (list "a" 1 0 -1) (list "c" 1 0 -1) (list "b" 0 0 1) (list "d" 0 0 1)))
    (check-equal? (classifica (list (list "a" 1 1 0) (list "b" 0 0 -1) (list "c" 1 0 -1) (list "d" 0 0 1)))
                  (list (list "a" 1 1 0) (list "c" 1 0 -1) (list "b" 0 0 -1) (list "d" 0 0 1))))

(define (classifica desempenhos)
    (sort desempenhos (lambda (a b) (if (= (second a) (second b))
                                        (string<? (first a) (first b))
                                        (> (second a) (second b))))))


;; ListaDesempenho -> ListaString
;; Transforma classificação (lista de desempenhos) em uma lista de strings
(examples
    (check-equal? (desempenhos->strings (list (list "a" 1 0 -1) (list "c" 1 0 -1) (list "b" 0 0 1) (list "d" 0 0 1)))
                  (list "a 1 0 -1" "c 1 0 -1" "b 0 0 1" "d 0 0 1"))
    (check-equal? (desempenhos->strings (list (list "a" 1 1 0) (list "c" 1 0 -1) (list "b" 0 0 -1) (list "d" 0 0 1)))
                  (list "a 1 1 0" "c 1 0 -1" "b 0 0 -1" "d 0 0 1")))

(define (desempenhos->strings classificacao)
    (map (lambda (desempenho) (string-join desempenho " ")) classificacao))


;; ListaString -> ListaString
;; Calcula a classificação dos times
(examples
    (check-equal? (classifica-times (list "a 1 b 2" "c 3 d 4"))
                  (list "a 1 0 -1" "c 1 0 -1" "b 0 0 1" "d 0 0 1"))
    (check-equal? (classifica-times (list "a 1 b 2" "c 3 d 4" "a 2 c 3" "b 4 d 5"))
                  (list "a 1 1 0" "c 1 0 -1" "b 0 0 -1" "d 0 0 1"))
    (check-equal? (classifica-times (list "Sao-Paulo 1 Atletico-MG 2"
                                            "Flamengo 2 Palmeiras 1"
                                            "Palmeiras 0 Sao-Paulo 0"
                                            "Atletico-MG 1 Flamengo 2"))
                  (list "Flamengo 6 2 2" "Atletico-MG 3 1 0" "Palmeiras 1 0 -1" "Sao-Paulo 1 0 -1")))

(define (classifica-times sresultados)
  ;; Transforma a lista de strings da entrada em uma lista de resultados
  (define resultados (map string->resultado sresultados))
  ;; Encontra o nome dos times
  ;; ListaResultado -> ListaString
  (define times (encontra-times resultados))
  ;; Calcula o desempenho de cada time
  ;; ListaString ListaResultado -> ListaDesempenho
  (define desempenhos (calcula-desempenhos times resultados))
  ;; Faz a classificao dos times pelo desempenho
  ;; ListaDesempenho -> ListaDesempenho
  (define classificacao (classifica desempenhos))
  ;; Transforma classificação (lista de desempenhos) em uma lista de strings
  (desempenhos->strings classificacao))