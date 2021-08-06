
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALMAIOREQMAIORMENOREQMENORleftPLUSMINUSleftVEZESDIVIDEATE ATRIBUICAO COMENTARIO COMENTARIO_INCOMPLETO DIF DIVIDE DOISPONTOS ELOGICO ENTAO ESCREVA FIM FLUTUANTE ID IGUAL INTEIRO LCOLCH LEIA LPAREN MAIOR MAIOREQ MENOR MENOREQ MINUS NEGACAO NUM_CIENTIFICA NUM_FLUTUANTE NUM_INTEIRO OULOGICO PLUS RCOLCH REPITA RETORNA RPAREN SE SENAO VEZES VIRGULA\n        programa : lista_declaracoes\n        \n        lista_declaracoes : lista_declaracoes declaracao\n                            | declaracao\n        \n        declaracao : declaracao_variaveis\n                     | inicializacao_variaveis\n                     | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOISPONTOS lista_variaveis\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : lista_variaveis VIRGULA var\n                          | var\n        \n        var : ID\n              | ID indice\n        \n        indice : indice LCOLCH expressao RCOLCH\n                 | LCOLCH expressao RCOLCH\n        \n        tipo : INTEIRO\n            | FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                            | cabecalho\n        \n        cabecalho : ID LPAREN lista_parametros RPAREN corpo FIM\n        \n        lista_parametros : lista_parametros VIRGULA parametro\n                           | parametro\n                           | vazio\n        \n        parametro : tipo DOISPONTOS ID\n                    | ID\n        \n        parametro :  parametro LCOLCH RCOLCH\n        \n        corpo : corpo acao\n                | vazio\n        \n        acao : expressao\n               | declaracao_variaveis\n               | se\n               | repita\n               | leia\n               | escreva\n               | retorna\n               | error\n        \n        se : SE expressao ENTAO corpo FIM\n             | SE expressao ENTAO corpo SENAO corpo FIM\n        \n        repita : REPITA corpo ATE expressao\n        \n        atribuicao : var ATRIBUICAO expressao\n        \n        leia : LEIA LPAREN ID RPAREN\n        \n        escreva : ESCREVA LPAREN expressao RPAREN\n        \n        retorna : RETORNA LPAREN expressao RPAREN\n        \n        expressao : expressao_simples\n                    | atribuicao\n        \n        expressao_simples : expressao_aditiva\n                            | expressao_simples operador_relacional expressao_aditiva\n        \n        expressao_aditiva : expressao_multiplicativa\n                            | expressao_aditiva operador_soma expressao_multiplicativa\n        \n        expressao_multiplicativa : expressao_unaria\n                                   | expressao_multiplicativa operador_multiplicacao expressao_unaria\n        \n        expressao_unaria : fator\n                           | operador_unario fator\n        \n        operador_relacional : MENOR\n                              | MAIOR\n                              | IGUAL\n                              | DIF\n                              | MENOREQ\n                              | MAIOREQ\n                              | ELOGICO\n                              | OULOGICO\n        \n        operador_soma : PLUS\n                        | MINUS\n        \n        operador_unario : PLUS\n                          | MINUS\n                          | NEGACAO\n        \n        operador_multiplicacao : VEZES\n                                 | DIVIDE\n        \n        fator : LPAREN expressao RPAREN\n                | var\n                | chamada_funcao\n                | numero\n        \n        numero : NUM_INTEIRO\n                 | NUM_FLUTUANTE\n                 | NUM_CIENTIFICA\n        \n        chamada_funcao : ID LPAREN lista_argumentos RPAREN\n        \n        lista_argumentos : lista_argumentos VIRGULA expressao\n                           | expressao\n                           | vazio\n        \n        vazio :\n        '
    
_lr_action_items = {'INTEIRO':([0,2,3,4,5,6,8,9,14,16,19,20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,72,76,77,78,79,80,84,85,86,90,91,93,94,95,96,97,98,99,100,101,102,105,111,115,120,121,122,123,124,125,126,127,128,],[10,10,-3,-4,-5,-6,-8,-18,-2,-17,10,-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,10,-14,-9,-46,-48,-50,-68,10,-27,-13,-75,-19,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,10,-79,10,-38,-40,-41,-42,-36,-79,10,-37,]),'FLUTUANTE':([0,2,3,4,5,6,8,9,14,16,19,20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,72,76,77,78,79,80,84,85,86,90,91,93,94,95,96,97,98,99,100,101,102,105,111,115,120,121,122,123,124,125,126,127,128,],[11,11,-3,-4,-5,-6,-8,-18,-2,-17,11,-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,11,-14,-9,-46,-48,-50,-68,11,-27,-13,-75,-19,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,11,-79,11,-38,-40,-41,-42,-36,-79,11,-37,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,76,77,78,79,80,84,85,86,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,111,112,113,114,115,116,120,121,122,123,124,125,126,127,128,],[13,13,-3,-4,-5,-6,17,-8,-18,-15,-16,-2,24,-17,31,44,-12,31,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,31,31,-70,-71,-63,-64,-65,-72,-73,-74,31,24,31,-53,-54,-55,-56,-57,-58,-59,-60,31,-61,-62,31,-66,-67,31,-52,-69,-79,44,89,-14,-9,-46,-48,-50,-68,31,-27,-13,-75,31,-19,-26,-28,-29,-30,-31,-32,-33,-34,-35,31,-79,31,117,31,31,-79,31,31,-38,-40,-41,-42,-36,-79,31,-37,]),'$end':([1,2,3,4,5,6,8,9,14,16,20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,76,77,78,79,80,84,90,91,93,],[0,-1,-3,-4,-5,-6,-8,-18,-2,-17,-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-9,-46,-48,-50,-68,-13,-75,-19,]),'DOISPONTOS':([7,10,11,48,103,],[15,-15,-16,74,15,]),'ATRIBUICAO':([12,13,20,25,31,76,90,],[18,-11,-12,18,-11,-14,-13,]),'LPAREN':([13,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,76,77,78,79,80,84,85,86,90,91,92,94,95,96,97,98,99,100,101,102,104,105,106,107,108,111,113,114,115,116,120,121,122,123,124,125,126,127,128,],[19,19,35,-12,35,-7,-10,-11,-69,-39,-43,-44,-45,-47,67,-49,-51,35,35,-70,-71,-63,-64,-65,-72,-73,-74,35,35,-53,-54,-55,-56,-57,-58,-59,-60,35,-61,-62,35,-66,-67,35,-52,-69,-79,-14,-9,-46,-48,-50,-68,35,-27,-13,-75,35,-26,-28,-29,-30,-31,-32,-33,-34,-35,35,-79,112,113,114,35,35,35,-79,35,35,-38,-40,-41,-42,-36,-79,35,-37,]),'LCOLCH':([13,20,24,31,44,46,76,87,88,89,90,],[21,49,21,21,-24,73,-14,73,-25,-23,-13,]),'PLUS':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,41,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,76,77,78,79,80,84,85,86,90,91,92,94,95,96,97,98,99,100,101,102,104,105,111,113,114,115,116,120,121,122,123,124,125,126,127,128,],[38,-12,38,-7,-10,-11,-69,-39,-43,-44,62,-47,-11,-49,-51,38,-70,-71,-72,-73,-74,38,38,-53,-54,-55,-56,-57,-58,-59,-60,38,-61,-62,38,-66,-67,38,-52,-69,-79,-14,-9,62,-48,-50,-68,38,-27,-13,-75,38,-26,-28,-29,-30,-31,-32,-33,-34,-35,38,-79,38,38,38,-79,38,38,-38,-40,-41,-42,-36,-79,38,-37,]),'MINUS':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,41,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,76,77,78,79,80,84,85,86,90,91,92,94,95,96,97,98,99,100,101,102,104,105,111,113,114,115,116,120,121,122,123,124,125,126,127,128,],[39,-12,39,-7,-10,-11,-69,-39,-43,-44,63,-47,-11,-49,-51,39,-70,-71,-72,-73,-74,39,39,-53,-54,-55,-56,-57,-58,-59,-60,39,-61,-62,39,-66,-67,39,-52,-69,-79,-14,-9,63,-48,-50,-68,39,-27,-13,-75,39,-26,-28,-29,-30,-31,-32,-33,-34,-35,39,-79,39,39,39,-79,39,39,-38,-40,-41,-42,-36,-79,39,-37,]),'NEGACAO':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,41,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,76,77,78,79,80,84,85,86,90,91,92,94,95,96,97,98,99,100,101,102,104,105,111,113,114,115,116,120,121,122,123,124,125,126,127,128,],[40,-12,40,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,40,-70,-71,-72,-73,-74,40,40,-53,-54,-55,-56,-57,-58,-59,-60,40,-61,-62,40,-66,-67,40,-52,-69,-79,-14,-9,-46,-48,-50,-68,40,-27,-13,-75,40,-26,-28,-29,-30,-31,-32,-33,-34,-35,40,-79,40,40,40,-79,40,40,-38,-40,-41,-42,-36,-79,40,-37,]),'NUM_INTEIRO':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,76,77,78,79,80,84,85,86,90,91,92,94,95,96,97,98,99,100,101,102,104,105,111,113,114,115,116,120,121,122,123,124,125,126,127,128,],[41,-12,41,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,41,41,-70,-71,-63,-64,-65,-72,-73,-74,41,41,-53,-54,-55,-56,-57,-58,-59,-60,41,-61,-62,41,-66,-67,41,-52,-69,-79,-14,-9,-46,-48,-50,-68,41,-27,-13,-75,41,-26,-28,-29,-30,-31,-32,-33,-34,-35,41,-79,41,41,41,-79,41,41,-38,-40,-41,-42,-36,-79,41,-37,]),'NUM_FLUTUANTE':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,76,77,78,79,80,84,85,86,90,91,92,94,95,96,97,98,99,100,101,102,104,105,111,113,114,115,116,120,121,122,123,124,125,126,127,128,],[42,-12,42,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,42,42,-70,-71,-63,-64,-65,-72,-73,-74,42,42,-53,-54,-55,-56,-57,-58,-59,-60,42,-61,-62,42,-66,-67,42,-52,-69,-79,-14,-9,-46,-48,-50,-68,42,-27,-13,-75,42,-26,-28,-29,-30,-31,-32,-33,-34,-35,42,-79,42,42,42,-79,42,42,-38,-40,-41,-42,-36,-79,42,-37,]),'NUM_CIENTIFICA':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,76,77,78,79,80,84,85,86,90,91,92,94,95,96,97,98,99,100,101,102,104,105,111,113,114,115,116,120,121,122,123,124,125,126,127,128,],[43,-12,43,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,43,43,-70,-71,-63,-64,-65,-72,-73,-74,43,43,-53,-54,-55,-56,-57,-58,-59,-60,43,-61,-62,43,-66,-67,43,-52,-69,-79,-14,-9,-46,-48,-50,-68,43,-27,-13,-75,43,-26,-28,-29,-30,-31,-32,-33,-34,-35,43,-79,43,43,43,-79,43,43,-38,-40,-41,-42,-36,-79,43,-37,]),'RPAREN':([19,20,25,26,27,28,29,30,31,32,33,36,37,41,42,43,44,45,46,47,67,68,69,70,76,78,79,80,81,82,83,84,87,88,89,90,91,109,117,118,119,],[-79,-12,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-24,71,-21,-22,-79,-52,-69,84,-14,-46,-48,-50,91,-77,-78,-68,-20,-25,-23,-13,-75,-76,122,123,124,]),'VIRGULA':([19,20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,44,45,46,47,67,68,69,76,77,78,79,80,81,82,83,84,87,88,89,90,91,109,],[-79,-12,51,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-24,72,-21,-22,-79,-52,-69,-14,-9,-46,-48,-50,92,-77,-78,-68,-20,-25,-23,-13,-75,-76,]),'FIM':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,76,77,78,79,80,84,85,86,90,91,94,95,96,97,98,99,100,101,102,115,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,-14,-9,-46,-48,-50,-68,93,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,125,-38,-40,-41,-42,-36,-79,128,-37,]),'error':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,76,77,78,79,80,84,85,86,90,91,94,95,96,97,98,99,100,101,102,105,111,115,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,-14,-9,-46,-48,-50,-68,102,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,102,-79,102,-38,-40,-41,-42,-36,-79,102,-37,]),'SE':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,76,77,78,79,80,84,85,86,90,91,94,95,96,97,98,99,100,101,102,105,111,115,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,-14,-9,-46,-48,-50,-68,104,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,104,-79,104,-38,-40,-41,-42,-36,-79,104,-37,]),'REPITA':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,76,77,78,79,80,84,85,86,90,91,94,95,96,97,98,99,100,101,102,105,111,115,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,-14,-9,-46,-48,-50,-68,105,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,105,-79,105,-38,-40,-41,-42,-36,-79,105,-37,]),'LEIA':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,76,77,78,79,80,84,85,86,90,91,94,95,96,97,98,99,100,101,102,105,111,115,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,-14,-9,-46,-48,-50,-68,106,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,106,-79,106,-38,-40,-41,-42,-36,-79,106,-37,]),'ESCREVA':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,76,77,78,79,80,84,85,86,90,91,94,95,96,97,98,99,100,101,102,105,111,115,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,-14,-9,-46,-48,-50,-68,107,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,107,-79,107,-38,-40,-41,-42,-36,-79,107,-37,]),'RETORNA':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,71,76,77,78,79,80,84,85,86,90,91,94,95,96,97,98,99,100,101,102,105,111,115,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-79,-14,-9,-46,-48,-50,-68,108,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,108,-79,108,-38,-40,-41,-42,-36,-79,108,-37,]),'ATE':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,76,77,78,79,80,84,86,90,91,94,95,96,97,98,99,100,101,102,105,111,121,122,123,124,125,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-9,-46,-48,-50,-68,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,116,-38,-40,-41,-42,-36,-37,]),'SENAO':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,76,77,78,79,80,84,86,90,91,94,95,96,97,98,99,100,101,102,115,120,121,122,123,124,125,128,],[-12,-7,-10,-11,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-9,-46,-48,-50,-68,-27,-13,-75,-26,-28,-29,-30,-31,-32,-33,-34,-35,-79,126,-38,-40,-41,-42,-36,-37,]),'VEZES':([20,25,30,31,32,33,36,37,41,42,43,68,69,76,79,80,84,90,91,],[-12,-69,65,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,65,-50,-68,-13,-75,]),'DIVIDE':([20,25,30,31,32,33,36,37,41,42,43,68,69,76,79,80,84,90,91,],[-12,-69,66,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,66,-50,-68,-13,-75,]),'MENOR':([20,25,27,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,],[-12,-69,53,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,]),'MAIOR':([20,25,27,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,],[-12,-69,54,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,]),'IGUAL':([20,25,27,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,],[-12,-69,55,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,]),'DIF':([20,25,27,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,],[-12,-69,56,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,]),'MENOREQ':([20,25,27,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,],[-12,-69,57,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,]),'MAIOREQ':([20,25,27,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,],[-12,-69,58,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,]),'ELOGICO':([20,25,27,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,],[-12,-69,59,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,]),'OULOGICO':([20,25,27,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,],[-12,-69,60,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,]),'RCOLCH':([20,25,26,27,28,29,30,31,32,33,36,37,41,42,43,50,68,69,73,75,76,78,79,80,84,90,91,],[-12,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,76,-52,-69,88,90,-14,-46,-48,-50,-68,-13,-75,]),'ENTAO':([20,25,26,27,28,29,30,31,32,33,36,37,41,42,43,68,69,76,78,79,80,84,90,91,110,],[-12,-69,-39,-43,-44,-45,-47,-11,-49,-51,-70,-71,-72,-73,-74,-52,-69,-14,-46,-48,-50,-68,-13,-75,115,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'lista_declaracoes':([0,],[2,]),'declaracao':([0,2,],[3,14,]),'declaracao_variaveis':([0,2,85,111,120,127,],[4,4,96,96,96,96,]),'inicializacao_variaveis':([0,2,],[5,5,]),'declaracao_funcao':([0,2,],[6,6,]),'tipo':([0,2,19,72,85,111,120,127,],[7,7,48,48,103,103,103,103,]),'atribuicao':([0,2,18,21,35,49,67,85,92,104,111,113,114,116,120,127,],[8,8,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'cabecalho':([0,2,7,],[9,9,16,]),'var':([0,2,15,18,21,34,35,49,51,52,61,64,67,85,92,104,111,113,114,116,120,127,],[12,12,23,25,25,69,25,25,77,69,69,69,25,25,25,25,25,25,25,25,25,25,]),'indice':([13,24,31,],[20,20,20,]),'lista_variaveis':([15,],[22,]),'expressao':([18,21,35,49,67,85,92,104,111,113,114,116,120,127,],[26,50,70,75,82,95,109,110,95,118,119,121,95,95,]),'expressao_simples':([18,21,35,49,67,85,92,104,111,113,114,116,120,127,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'expressao_aditiva':([18,21,35,49,52,67,85,92,104,111,113,114,116,120,127,],[29,29,29,29,78,29,29,29,29,29,29,29,29,29,29,]),'expressao_multiplicativa':([18,21,35,49,52,61,67,85,92,104,111,113,114,116,120,127,],[30,30,30,30,30,79,30,30,30,30,30,30,30,30,30,30,]),'expressao_unaria':([18,21,35,49,52,61,64,67,85,92,104,111,113,114,116,120,127,],[32,32,32,32,32,32,80,32,32,32,32,32,32,32,32,32,32,]),'fator':([18,21,34,35,49,52,61,64,67,85,92,104,111,113,114,116,120,127,],[33,33,68,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'operador_unario':([18,21,35,49,52,61,64,67,85,92,104,111,113,114,116,120,127,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'chamada_funcao':([18,21,34,35,49,52,61,64,67,85,92,104,111,113,114,116,120,127,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'numero':([18,21,34,35,49,52,61,64,67,85,92,104,111,113,114,116,120,127,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'lista_parametros':([19,],[45,]),'parametro':([19,72,],[46,87,]),'vazio':([19,67,71,105,115,126,],[47,83,86,86,86,86,]),'operador_relacional':([27,],[52,]),'operador_soma':([29,78,],[61,61,]),'operador_multiplicacao':([30,79,],[64,64,]),'lista_argumentos':([67,],[81,]),'corpo':([71,105,115,126,],[85,111,120,127,]),'acao':([85,111,120,127,],[94,94,94,94,]),'se':([85,111,120,127,],[97,97,97,97,]),'repita':([85,111,120,127,],[98,98,98,98,]),'leia':([85,111,120,127,],[99,99,99,99,]),'escreva':([85,111,120,127,],[100,100,100,100,]),'retorna':([85,111,120,127,],[101,101,101,101,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','AnaliseSintatica.py',30),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','AnaliseSintatica.py',36),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','AnaliseSintatica.py',37),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','AnaliseSintatica.py',46),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','AnaliseSintatica.py',47),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','AnaliseSintatica.py',48),
  ('declaracao_variaveis -> tipo DOISPONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','AnaliseSintatica.py',54),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','AnaliseSintatica.py',60),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','AnaliseSintatica.py',66),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','AnaliseSintatica.py',67),
  ('var -> ID','var',1,'p_var','AnaliseSintatica.py',76),
  ('var -> ID indice','var',2,'p_var','AnaliseSintatica.py',77),
  ('indice -> indice LCOLCH expressao RCOLCH','indice',4,'p_indice','AnaliseSintatica.py',86),
  ('indice -> LCOLCH expressao RCOLCH','indice',3,'p_indice','AnaliseSintatica.py',87),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','AnaliseSintatica.py',96),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','AnaliseSintatica.py',97),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','AnaliseSintatica.py',103),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','AnaliseSintatica.py',104),
  ('cabecalho -> ID LPAREN lista_parametros RPAREN corpo FIM','cabecalho',6,'p_cabecalho','AnaliseSintatica.py',113),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','AnaliseSintatica.py',119),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','AnaliseSintatica.py',120),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','AnaliseSintatica.py',121),
  ('parametro -> tipo DOISPONTOS ID','parametro',3,'p_parametro','AnaliseSintatica.py',130),
  ('parametro -> ID','parametro',1,'p_parametro','AnaliseSintatica.py',131),
  ('parametro -> parametro LCOLCH RCOLCH','parametro',3,'p_parametro2','AnaliseSintatica.py',140),
  ('corpo -> corpo acao','corpo',2,'p_corpo','AnaliseSintatica.py',146),
  ('corpo -> vazio','corpo',1,'p_corpo','AnaliseSintatica.py',147),
  ('acao -> expressao','acao',1,'p_acao','AnaliseSintatica.py',156),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','AnaliseSintatica.py',157),
  ('acao -> se','acao',1,'p_acao','AnaliseSintatica.py',158),
  ('acao -> repita','acao',1,'p_acao','AnaliseSintatica.py',159),
  ('acao -> leia','acao',1,'p_acao','AnaliseSintatica.py',160),
  ('acao -> escreva','acao',1,'p_acao','AnaliseSintatica.py',161),
  ('acao -> retorna','acao',1,'p_acao','AnaliseSintatica.py',162),
  ('acao -> error','acao',1,'p_acao','AnaliseSintatica.py',163),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','AnaliseSintatica.py',169),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','AnaliseSintatica.py',170),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','AnaliseSintatica.py',179),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','AnaliseSintatica.py',185),
  ('leia -> LEIA LPAREN ID RPAREN','leia',4,'p_leia','AnaliseSintatica.py',191),
  ('escreva -> ESCREVA LPAREN expressao RPAREN','escreva',4,'p_escreva','AnaliseSintatica.py',197),
  ('retorna -> RETORNA LPAREN expressao RPAREN','retorna',4,'p_retorna','AnaliseSintatica.py',203),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','AnaliseSintatica.py',209),
  ('expressao -> atribuicao','expressao',1,'p_expressao','AnaliseSintatica.py',210),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','AnaliseSintatica.py',216),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','AnaliseSintatica.py',217),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','AnaliseSintatica.py',226),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','AnaliseSintatica.py',227),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','AnaliseSintatica.py',236),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','AnaliseSintatica.py',237),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','AnaliseSintatica.py',246),
  ('expressao_unaria -> operador_unario fator','expressao_unaria',2,'p_expressao_unaria','AnaliseSintatica.py',247),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','AnaliseSintatica.py',256),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','AnaliseSintatica.py',257),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','AnaliseSintatica.py',258),
  ('operador_relacional -> DIF','operador_relacional',1,'p_operador_relacional','AnaliseSintatica.py',259),
  ('operador_relacional -> MENOREQ','operador_relacional',1,'p_operador_relacional','AnaliseSintatica.py',260),
  ('operador_relacional -> MAIOREQ','operador_relacional',1,'p_operador_relacional','AnaliseSintatica.py',261),
  ('operador_relacional -> ELOGICO','operador_relacional',1,'p_operador_relacional','AnaliseSintatica.py',262),
  ('operador_relacional -> OULOGICO','operador_relacional',1,'p_operador_relacional','AnaliseSintatica.py',263),
  ('operador_soma -> PLUS','operador_soma',1,'p_operador_soma','AnaliseSintatica.py',269),
  ('operador_soma -> MINUS','operador_soma',1,'p_operador_soma','AnaliseSintatica.py',270),
  ('operador_unario -> PLUS','operador_unario',1,'p_operador_unario','AnaliseSintatica.py',276),
  ('operador_unario -> MINUS','operador_unario',1,'p_operador_unario','AnaliseSintatica.py',277),
  ('operador_unario -> NEGACAO','operador_unario',1,'p_operador_unario','AnaliseSintatica.py',278),
  ('operador_multiplicacao -> VEZES','operador_multiplicacao',1,'p_operador_multiplicacao','AnaliseSintatica.py',284),
  ('operador_multiplicacao -> DIVIDE','operador_multiplicacao',1,'p_operador_multiplicacao','AnaliseSintatica.py',285),
  ('fator -> LPAREN expressao RPAREN','fator',3,'p_fator','AnaliseSintatica.py',291),
  ('fator -> var','fator',1,'p_fator','AnaliseSintatica.py',292),
  ('fator -> chamada_funcao','fator',1,'p_fator','AnaliseSintatica.py',293),
  ('fator -> numero','fator',1,'p_fator','AnaliseSintatica.py',294),
  ('numero -> NUM_INTEIRO','numero',1,'p_numero','AnaliseSintatica.py',303),
  ('numero -> NUM_FLUTUANTE','numero',1,'p_numero','AnaliseSintatica.py',304),
  ('numero -> NUM_CIENTIFICA','numero',1,'p_numero','AnaliseSintatica.py',305),
  ('chamada_funcao -> ID LPAREN lista_argumentos RPAREN','chamada_funcao',4,'p_chamada_funcao','AnaliseSintatica.py',311),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','AnaliseSintatica.py',317),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','AnaliseSintatica.py',318),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','AnaliseSintatica.py',319),
  ('vazio -> <empty>','vazio',0,'p_vazio','AnaliseSintatica.py',328),
]
