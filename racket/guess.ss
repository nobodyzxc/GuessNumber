;#lang racket/base
(#%require racket/vector) ; vector
(#%require racket/list) ; remove-duplicates

(define (vector-del v pos)
  (vector-append
    (vector-take v pos)
    (vector-drop v (add1 pos))))

(define (number->list n)
  (define (char->digit ch)
    (apply - (map char->integer (list ch #\0))))
  (map char->digit (string->list (number->string n))))

(define (make-cmpv init-seq)
  (define init-idx 1)
  (define cmpv (make-vector 10))
  (let loop ((idx init-idx)
             (seq init-seq))
    (if (not (null? seq))
      (begin
        (vector-set! cmpv (car seq) idx)
        (loop (add1 idx) (cdr seq)))
      cmpv)
    )
  )

(define (number->cmpv number)
  (make-cmpv (number->list number)))

(define (vector-zip . args)
  (apply vector-map (cons list args)))

(define (make-prob)
  (let loop ((prob '())
             (cand #(0 1 2 3 4 5 6 7 8 9)))
    (define pos (random 0 (vector-length cand)))
    (if (< (length prob) 4)
      (loop
        (cons (vector-ref cand pos) prob)
        (vector-del cand pos))
      prob)))

(define (count-ab va vb)
  (let ((a 0) (b 0))
    (for-each
      (lambda (x)
        (let ((ea (car x)) (eb (cadr x)))
          (when (and (> ea 0) (> eb 0))
            (cond
              ((= ea eb) (set! a (add1 a)))
              (else (set! b (add1 b)))))))
      (vector->list (vector-zip va vb)))
    (list a b)
    ))

(define (show-msg msg)
  (begin (display msg)
         (newline) (flush-output)))

(define (illegal-guess guess)
  (not (and
         (= (length (remove-duplicates guess)) 4)
         (= (length guess) 4))))

(define (game-loop)
  (begin
    (define guess (read))
    (cond
      ((equal? guess 'exit) (show-msg "bye"))
      ((number? guess)
       (begin
         (let*
           ((guessv (number->cmpv guess))
            (result (count-ab answer guessv)))
           (cond
             ((illegal-guess (number->list guess))
              (show-msg "illegal guess")
              (game-loop))
             ((= (car result) 4)
              (show-msg "WIN"))
             (else
               (apply printf (cons "~vA~vB" result))
               (show-msg "")
               (game-loop))
             ))))
      (else (show-msg "illegal guess") (game-loop)))
    ))

(define prob (make-prob))
(show-msg prob)
(define answer (make-cmpv prob))
(game-loop)
