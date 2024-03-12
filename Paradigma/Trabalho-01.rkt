#lang racket
(require examples)

;; Definição de tipos
;; game -> String
;; Representa uma lista de jogos no formato "time1 gols1 time2 gols2"
;;
;; resultado -> (list String Number String Number)
;; Representa um jogo no formato (list "time1" gols1 "time2" gols2)
;;
;; Recebe como entrada uma lista de jogos de futebol, e a saída será uma lista de String com o resultado processado
(examples
(check-equal? (classifica-times (list "Sao-Paulo 1 Atletico-MG 2"
"Flamengo 2 Palmeiras 1"
"Palmeiras 0 Sao-Paulo 0"
"Atletico-MG 1 Flamengo 2")) (list "Flamengo 6 2 2"
"Atletico-MG 3 1 0"
"Palmeiras 1 0 -1"
"Sao-Paulo 1 0 -1")))

;; encontra-times -> (list resultado) -> (list String)
;; Dada uma lista de resultados, retorna uma lista com os nomes dos times
(define (encontra-times resultados)
  (foldr (lambda (game acc)
           (append (list (first game) (third game)) acc))
         '()
         resultados))

;; calcula-desempenhos -> (list String) (list resultado) -> (list Number)
;; Deve calcular o desempenho de cada time, um por vez, a partir da diferença de gols em cada jogo
(define (calcula-desempenhos times resultados)
  (map (lambda (times)
         (foldr (lambda (game acc)
                  (cond
                    [(equal? times (first game)) (+ acc (- (second game) (fourth game)))]
                    [(equal? times (third game)) (+ acc (- (fourth game) (second game)))]
                    [else acc]))
                0
                resultados))
       times)) 

;; ordena -> (list Number) -> (list Number)
;; Deve ordenar a lista de desempenhos
(examples
  (check-equal? (ordena (list 3 1 2 4 5)) (list 1 2 3 4 5))
  (check-equal? (ordena (list 3 1 2 4 5 0)) (list 0 1 2 3 4 5)))

(define (ordena lst)
  (cond
  [(empty? lst) empty]
  [else
    (insere-ordenado (first lst)
      (ordena (rest lst)))]))

;; Insere-ordenado -> Number (list Number) -> (list Number)
;; Dado um número e uma lista ordenada, insere o número na lista de forma ordenada
(examples
  (check-equal? (insere-ordenado 0 empty) (list 0))
  (check-equal? (insere-ordenado 3 (list 1 2 4 5)) (list 1 2 3 4 5))
  (check-equal? (insere-ordenado 3 (list 1 2 4 5 0)) (list 0 1 2 3 4 5)))

(define (insere-ordenado n lst)
  (cond
    [(empty? lst) (list n)]
    [else
      (cond
        [(<= n (first lst)) (cons n lst)]
        [else (cons (first lst) (insere-ordenado n (rest lst)))] )]))


;; classifica -> (list Number) -> (list Number)
;; Deve classificar os times pelo desempenho, do maior para o menor
(examples
  (check-equal? (classifica (list 3 1 2 4 5)) (list 1 2 3 4 5))
  (check-equal? (classifica (list 3 1 2 4 5 0)) (list 0 1 2 3 4 5)))

(define (classifica desempenhos)
  (ordena desempenhos))


;; desempenho->string -> Number -> String
;; Dado um desempenho, retorna uma string no formato "time: desempenho  Número de vitórias  Saldo de gols"
(examples
  (check-equal? (desempenho->string "Flamengo" 6 2 2) "Flamengo 6 2 2")
  (check-equal? (desempenho->string "Atletico-MG" 3 1 0) "Atletico-MG 3 1 0")
  (check-equal? (desempenho->string "Palmeiras" 1 0 -1) "Palmeiras 1 0 -1"))

(define (desempenho->string time desempenho vitórias saldo)
  (string-append time " " (number->string desempenho) " " (number->string vitórias) " " (number->string saldo)))


;; string->resultado -> String -> resultado
;; Dada uma string no formato "time1 gols1 time2 gols2", retorna um resultado
(define (string->resultado s)
  (let ([lst (string-split s " ")])
    (list (first lst) (string->number (second lst)) (third lst) (string->number (fourth lst)))))  

;; ListaNumber -> ListaString
;; "Função auxiliar" para garantir a saída de string ao invés de uma lista de números
(define (desempenhos->strings desempenhos)
  (map desempenho->string desempenhos))

;; ListaString -> ListaString
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
