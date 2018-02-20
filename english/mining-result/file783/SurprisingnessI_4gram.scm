;Interesting Pattern Mining results for 4 gram patterns. Total pattern number: 143

;p = 2/23 = 0.0869565

; { [0]=
; { [1]=
; { [2]=
; { [3]=
; { [01]=2/23=0.0869565 [23]=D 
; { [02]=2/23=0.0869565 [13]=2/23=0.0869565, expect = 0.00756144x23 = 0.173913, nDiff = 10.5}
; { [03]=2/23=0.0869565 [12]=2/23=0.0869565, expect = 0.00756144x23 = 0.173913, nDiff = 10.5}
; { [0]=
; { [0]=
; { [0]=
; { [1]=
; { [1]=
; { [2]=
; { [0]=

;Pattern: Frequency = 2, SurprisingnessI = 10.5, SurprisingnessII = 0
(EvaluationLink
  (LinkGrammarRelationshipNode "A")
  (ListLink
    (PatternVariableNode "$var_1")
    (PatternVariableNode "$var_2")
  )
)
(EvaluationLink
  (LinkGrammarRelationshipNode "D")
  (ListLink
    (PatternVariableNode "$var_3")
    (PatternVariableNode "$var_2")
  )
)
(EvaluationLink
  (LinkGrammarRelationshipNode "PH")
  (ListLink
    (PatternVariableNode "$var_3")
    (PatternVariableNode "$var_1")
  )
)
(EvaluationLink
  (LinkGrammarRelationshipNode "W")
  (ListLink
    (PatternVariableNode "$var_4")
    (PatternVariableNode "$var_2")
  )
)


