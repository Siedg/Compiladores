# coding=UTF-8
import ply.lex as lex
import sys

class AnaliseLexica(object):
    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    pr = {
        u'até' : 'ATE',
        u'se' : 'SE',
        u'senão' : 'SENAO',
        u'então' : 'ENTAO',
        u'fim' : 'FIM',
        u'repita' : 'REPITA',
        u'flutuante' : 'FLUTUANTE',
        u'retorna' : 'RETORNA',
        u'leia' : 'LEIA',
        u'escreva' : 'ESCREVA',
        u'inteiro' : 'INTEIRO',

    }
    

    tokens = [
        'PLUS',
        'MINUS',
        'VEZES',
        'DIVIDE',
        'IGUAL',
        'VIRGULA',
        'DOISPONTOS',
        'LCOLCH',
        'RCOLCH',
        'NEGACAO',
        'LPAREN',
        'RPAREN',
        'MAIOR',
        'MENOR',
        'MENOREQ',
        'MAIOREQ',
        'ATRIBUICAO',
        'ELOGICO',
        'OULOGICO',
        'DIF',
        'ID',
        'NUM_FLUTUANTE',
        'COMENTARIO',
        'NUM_CIENTIFICA',
       'NUM_INTEIRO',
        'COMENTARIO_INCOMPLETO',

    ] + list(pr.values())


    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_VEZES   = r'\*'
    t_DIVIDE  = r'/'
    t_IGUAL   = r'\='
    t_VIRGULA = r','
    t_DOISPONTOS = r'\:'
    t_LCOLCH = r'\['
    t_RCOLCH = r'\]'
    t_NEGACAO = r'\!'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_MAIOR = r'\>'
    t_MENOR = r'\<'
    t_MENOREQ = r'\<='
    t_MAIOREQ = r'\>='
    t_ATRIBUICAO = r'(\?<\!<|>|:|=)=(?!=)'
    t_ELOGICO = r'&&'
    t_OULOGICO = r"\|\|"
    t_DIF = r'<>'

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_COMENTARIO(self, t):
        r'\{[^}]*[^{]*\}'

    def t_COMENTARIO_INCOMPLETO(self, t):
        r'({)'

    def t_PR(self, t):
        r'se\b|então\b|senão\b|fim\b|repita\b|flutuante\b|retorna\b|até\b|leia\b|escreva\b|inteiro\b'
        t.type = self.pr.get(t.value)
        return t

    def t_ID(self, t):
        r'[a-zA-Z][a-zA-Z_0-9]*'
        t.type = self.pr.get(t.value, 'ID')
        return t

    def t_NUM_CIENTIFICA(self, t):
        r'([+-]?(\d+)(.\d+)([eE][+|-]?(\d+)))'
        return t

    def t_NUM_FLUTUANTE(self, t):
        r'([+-]?\d+)?(\.(\d)+)|((\d)\.)'
        return t

    def t_NUM_INTEIRO(self, t):
        r'([+-]?\d+)'
        return t

    t_ignore = ' \t'

    def t_error(self, t):
        print("Illegal character '%s', linha %d" % (t.value[0], t.lineno))
        t.lexer.skip(1)


    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

if __name__ == '__main__':
    import sys
    codigo = open(sys.argv[1], 'r', encoding='utf-8')
    r = codigo.read()
    lexerTest = AnaliseLexica()
    lexerTest.build()
    lexerTest.lexer.input(r)

    while True:
        tok = lexerTest.lexer.token()
        if not tok:
            break
        print("<" + tok.type + ", " + tok.value + ">")