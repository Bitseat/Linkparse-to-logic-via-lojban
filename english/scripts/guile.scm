(define x '"newfile1158.scm")
;(display x)
(load "/home/bitseat/setup.scm")
(clear)
(use-modules (opencog patternminer))
;(let ((y (string-append "hello " "world")))
(define y (string-append "/home/bitseat/Desktop/edited/" x))
;(display y)
(load-scm-from-file y)
(pm-run-patternminer)