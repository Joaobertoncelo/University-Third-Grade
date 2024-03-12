;; Função para descobrir os nomes dos times
(define (encontra-times result)
  (foldr (lambda (game acc)
           (append (list (first game) (third game)) acc))
         '()
         result))

;; Função para calcular pontos, número de vitórias e saldo de gols de um time
(define (calcula-desempenho time result)
  (define time-resultados (filter (lambda (game)
                                    (or (equal? (first game) time) (equal? (third game) time)))
                                  result))
  (define pontos (foldr (lambda (game acc)
                          (cond ((equal? (first game) time) (+ acc (if (> (second game) (fourth game)) 3 1)))
                                ((equal? (third game) time) (+ acc (if (> (fourth game) (second game)) 3 1)))
                                (else acc)))
                        0
                        time-resultados))
  (define vitorias (count (lambda (game)
                            (or (and (equal? (first game) time) (> (second game) (fourth game)))
                                (and (equal? (third game) time) (> (fourth game) (second game)))))
                          time-resultados))
  (define saldo-gols (- (foldr (lambda (game acc)
                                  (cond ((equal? (first game) time) (+ acc (- (second game) (fourth game))))
                                        ((equal? (third game) time) (+ acc (- (fourth game) (second game))))
                                        (else acc)))
                              0
                              time-resultados)))
  (list time pontos vitorias saldo-gols))

;; Função para classificar os times
(define (classifica desempenhos)
  (define sorted (insertion-sort desempenhos))
  (reverse sorted))

;; Função auxiliar para ordenação por inserção
(define (insertion-sort lst)
  (cond ((null? lst) '())
        (else (insert (car lst) (insertion-sort (cdr lst))))))

;; Função para transformar a classificação em uma lista de strings
(define (classificacao->strings classificacao)
  (map (lambda (time)
         (apply string-append
                (append (list (first time) " " (number->string (second time)) " " (number->string (third time)) " " (number->string (fourth time)))
                        '())))
       classificacao))

;; Função principal
(define (classifica-times sresultados)
  ;; Transforma a lista de strings da entrada em uma lista de resultados
  (define resultados (map string->resultado sresultados))
  ;; Encontra o nome dos times
  ;; ListaResultado -> ListaString
  (define times (encontra-times resultados))
  ;; Calcula o desempenho de cada time
  ;; ListaString ListaResultado -> ListaDesempenho
  (define desempenhos (map (lambda (time) (calcula-desempenho time resultados)) times))
  ;; Faz a classificação dos times pelo desempenho
  ;; ListaDesempenho -> ListaDesempenho
  (define classificacao (classifica desempenhos))
  ;; Transforma classificação (lista de desempenhos) em uma lista de strings
  (classificacao->strings classificacao))
