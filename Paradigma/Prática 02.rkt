#lang racket

;; InteiroPositivo -> Boolean
;;
;; Produz #t se uma pessoa com idade id é isento da
;; tarifa de transporte público, isto é, menor ou igual a
;; 18 anos ou maior ou igual a 65 anos. Produz #f caso contrário.

(require examples)

(examples
 (check-equal? (isento-tarifa? 17) #t)
 (check-equal? (isento-tarifa? 18) #t)
 (check-equal? (isento-tarifa? 50) #f)
 (check-equal? (isento-tarifa? 65) #t)
 (check-equal? (isento-tarifa? 70) #t))

(define (isento-tarifa? id) 
  (or (<= id 18) (>= id 65)))