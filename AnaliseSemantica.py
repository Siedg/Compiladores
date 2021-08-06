# -*- coding: utf-8 -*-
from AnaliseSintatica import AnaliseSintatica

class Semantica:

    def __init__(self, code):
        self.tabelaSimbolos = {}
        self.escopo = "global"
        self.tree = AnaliseSintatica(code).ast
        self.tipo_aux = None
        self.start(self.tabelaSimbolos)

    def start(self, tabelaSimbolos):
        self.lista_declaracoes(self.tree.child[0])

        if "principal" not in tabelaSimbolos.keys():
            print("ERRO: funcao principal nao declarada")

        for k, v in tabelaSimbolos.items():
            if v[0] == "variavel" and v[2] is False:
                escopo = k.split("-")
                if escopo[0] == "global":
                    print("WARNING: variavel [" + v[1] + "] nunca é utilizada")
                else:                        
                    print("WARNING: variavel [" + v[1] + "] no escopo [" + escopo[0] + "] declarada e nao utilizada")
            elif v[0] == "funcao":
                if k != "principal":
                    if v[3] is False:
                        print("WARNING: a funcao [" + k + "] nunca é utilizada ")


    def lista_declaracoes(self, node):
        if len(node.child) == 1:
            self.declaracao(node.child[0])

        else:
            self.lista_declaracoes(node.child[0])
            self.declaracao(node.child[1])


    def declaracao(self, node):
        if node.child[0].type == "declaracao_variaveis":
            self.declaracao_variaveis(node.child[0])

        elif node.child[0].type == "inicializacao_variaveis":
            self.inicializacao_variaveis(node.child[0])

        else:
            if len(node.child[0].child) == 1:
                self.escopo = node.child[0].child[0].value

            else:
                self.escopo = node.child[0].child[1].value

            self.declaracao_funcao(node.child[0])
            self.escopo = "global"

    
    def declaracao_variaveis(self, node):
        tipo = node.child[0].type

        for child in self.lista_variaveis(node.child[1]):
            if ("global-" + child in self.tabelaSimbolos.keys()) or (self.escopo + "-" + child in self.tabelaSimbolos.keys()):
                print("ERRO: variavel [" + child + "] já foi declarada")

            if child in self.tabelaSimbolos.keys():
                print("WARNING: funcoes com nomes iguais: " + node.value)
                                                    
            self.tabelaSimbolos[self.escopo + "-" + child] = ["variavel", child, False, False, tipo, self.escopo]

    def inicializacao_variaveis(self, node):
        self.atribuicao(node.child[0])


    def lista_variaveis(self, node):
        list_var = []
        if len(node.child) == 1:
            if len(node.child[0].child) == 1:
                list_var.append(node.child[0].value + self.indice(node.child[0].child[0]))

            else:
                list_var.append(node.child[0].value)

            return list_var
        else:
            list_var = self.lista_variaveis(node.child[0])
            list_var.append(node.child[1].value)

            return list_var


    def var(self, node):
        name_var = self.escopo + "-" + node.value
        if name_var not in self.tabelaSimbolos:
            name_var = "global" + "-" + node.value

            if name_var not in self.tabelaSimbolos:
                print("ERRO: variavel [" + node.value + "] nao foi declarada")

        if self.tabelaSimbolos[name_var][3] is False:
            #print("ERRO: variavel [" + node.value + "] nao possui atribuicao")
            print()

        self.tabelaSimbolos[name_var][2] = True

        return self.tabelaSimbolos[name_var][4]


    def indice(self, node):
        if len(node.child) == 1:
            tipo = self.expressao(node.child[0])
            if tipo != "inteiro":
                print("ERRO: somente vetores do tipo inteiro são aceitos")

            return "[]"
        else:
            var = self.indice(node.child[0])
            tipo = self.expressao(node.child[1])
            if tipo != "inteiro":
                print("ERRO: somente vetores do tipo inteiro são aceitos")

            return "[]" + var

    def tipo(self, node):
        if node.type == "inteiro" or node.type == "flutuante":
            return node.type

        else:
            print("ERRO: tipo não suportado: [" + node.type + "]")


    def declaracao_funcao(self, node):
        if len(node.child) == 1:
            tipo = "void"
            if node.child[0].value in self.tabelaSimbolos.keys():
                print("ERRO: a função [" + node.child[0].value + "] ja foi declarada")

            elif "global-" + node.child[0].value in self.tabelaSimbolos.keys():
                print("ERRO: a variavel [" + node.child[0].value + "] ja foi declarada")

            self.tabelaSimbolos[node.child[0].value] = ["funcao", node.child[0].value, [], False, tipo]
            self.cabecalho(node.child[0])
        else:
            tipo = self.tipo(node.child[0])

            self.tabelaSimbolos[node.child[1].value] = ["funcao", node.child[1].value, [], False, tipo]
            self.cabecalho(node.child[1])


    #funcao, nome, lista parametros, usada, tipo
    def cabecalho(self, node):
        params = self.lista_parametros(node.child[0])
        self.tabelaSimbolos[node.value][2] = params
        corpo = self.corpo(node.child[1])

        if corpo != self.tabelaSimbolos[node.value][4]:
            if node.value == "principal":
                print("WARNING: a funcao [" + repr(node.value) + "] deveria retornar [" + repr(self.tabelaSimbolos[node.value][4]) + "] mas retorna ["  + repr(corpo) + "]")                

            else:
                print("ERRO: a funcao [" + node.value + "] deveria retornar [" + self.tabelaSimbolos[node.value][4] + "] mas retorna [" + corpo + "]")


    def lista_parametros(self, node):
        params = []

        if len(node.child) != 1:
            params = self.lista_parametros(node.child[0])
            params.append(self.parametro(node.child[1]))
            return params
            
        else:
            if node.child[0] is not None:
                params.append(self.parametro(node.child[0]))
                return params
            else:
                return "void"
            

    def parametro(self, node):
        if len(node.child) > 0 and node.child[0].type == "parametro":
            return self.parametro(node.child[0])

        else:
            if len(node.child) != 0:
                tipo = self.tipo(node.child[0])

            else:
                tipo = self.tipo_aux

            self.tabelaSimbolos[self.escopo + "-" + node.value] = ["variavel", node.value, False, True, tipo, self.escopo]
            self.tipo_aux = tipo
            return tipo

    def corpo(self, node):
        if len(node.child) != 1:
            self.corpo(node.child[0])
            return self.acao(node.child[1])

        else:            
            return "void"

    def acao(self, node):
        if node.child[0].type == "expressao":
            return self.expressao(node.child[0])

        elif node.child[0].type == "declaracao_variaveis":
            return self.declaracao_variaveis(node.child[0])

        elif node.child[0].type == "se":
            return self.se(node.child[0])

        elif node.child[0].type == "repita":
            return self.repita(node.child[0])

        elif node.child[0].type == "leia":
            return self.leia(node.child[0])

        elif node.child[0].type == "escreva":
            return self.escreva(node.child[0])

        elif node.child[0].type == "retorna":
            return self.retorna(node.child[0])



    def se(self, node):
        expr = self.expressao(node.child[0])

        if expr != "logico":
            print("ERRO: a expressao [" + expr + "] nao e valida")

        if len(node.child) == 2:
            return self.corpo(node.child[1])

        else:
            c1 = self.corpo(node.child[1])
            c2 = self.corpo(node.child[2])
            if c1 != c2:
                if c1 == "void":
                    return c2

                else:
                    return c1

            return c1

    def repita(self, node):
        expr = self.expressao(node.child[1])
        if expr != "logico":
            print("ERRO: a expressao [" + expr + "] nao e valida")

        return self.corpo(node.child[0])


    def atribuicao(self, node):
        escopo = self.escopo + "-" + node.child[0].value

        if self.escopo + "-" + node.child[0].value not in self.tabelaSimbolos.keys():
            escopo = "global-" + node.child[0].value

            if "global-" + node.child[0].value not in self.tabelaSimbolos.keys():
                print("ERRO: a variavel [" + node.child[0].value + "] nao foi declarada")

        t1 = self.tabelaSimbolos[escopo][4]
        t2 = self.expressao(node.child[1])

        if t1 == "inteiro[]":
            t1 = t1[:-2]

        self.tabelaSimbolos[escopo][2] = True
        self.tabelaSimbolos[escopo][3] = True

        if t1 != t2:
            print("WARNING: atribuicao na variavel [" + node.child[0].value + "] com tipos diferentes [" + t1 + "] e [" + t2 + "]")

        return "void"

    def leia(self, node):
        if self.escopo + "-" + node.value not in self.tabelaSimbolos.keys():
            if "global-" + node.value not in self.tabelaSimbolos.keys():
                print("ERRO: a variavel [" + node.value + "] nao foi declarada")

        return "void"

    def escreva(self, node):
        expr = self.expressao(node.child[0])

        if expr == "logico":
            print("ERRO: expressao invalida [" + expr + "]")

        return "void"

    def retorna(self, node):
        expr = self.expressao(node.child[0])

        if expr == "logico":
            print("ERRO: expressao invalida [" + expr + "]")
        return expr

    def expressao(self, node):
        if node.child[0].type == "expressao_simples":
            return self.expressao_simples(node.child[0])

        else:
            return self.atribuicao(node.child[0])

    def expressao_simples(self, node):
        if len(node.child) == 1:
            return self.expressao_aditiva(node.child[0])

        else:
            self.operador_relacional(node.child[1])

            if self.expressao_simples(node.child[0]) != self.expressao_aditiva(node.child[2]):
                print("WARNING: operacao com dois tipos diferentes: [" + self.expressao_simples(node.child[0]) + "] e [" + self.expressao_aditiva(node.child[2]) + "]")
            return "logico"

    def expressao_aditiva(self, node):
        if len(node.child) != 1:
            t1 = self.expressao_aditiva(node.child[0])
            self.operador_soma(node.child[1])
            t2 = self.expressao_multiplicativa(node.child[2])

            if t1 != t2:
                print("WARNING: operacao com tipos diferentes [" + t1 + "] e [" + t2 + "]")

            if (t1 != "flutuante") and (t2 != "flutuante"):
                return "inteiro"
                
            else:
                return "flutuante"
           
        else:
            return self.expressao_multiplicativa(node.child[0])

    def expressao_multiplicativa(self, node):
        if len(node.child) != 1:
            t1 = self.expressao_multiplicativa(node.child[0])
            self.operador_multiplicacao(node.child[1])
            t2 = self.expressao_unaria(node.child[2])

            if t1 != t2:
                print("WARNING: operacao com tipos diferentes [" + t1 + "] e [" + t2 + "]")

            if (t1 != "flutuante") and (t2 != "flutuante"):
                return "inteiro"
                
            else:
                return "flutuante"
            
        else:
            return self.expressao_unaria(node.child[0])

    def expressao_unaria(self, node):
        if len(node.child) == 1:
            return self.fator(node.child[0])

        elif (self.operador_soma(node.child[0]) != "SOMA"):
            self.operador_negacao(node.child[0])
            return self.fator(node.child[1])

        else:
            self.operador_soma(node.child[0])
            return self.fator(node.child[1])

    def operador_relacional(self, node):
        return node.value

    def operador_soma(self, node):
        return node.value

    def operador_multiplicacao(self, node):
        return node.value

    def operador_negacao(self, node):
        return node.value

    def fator(self, node):
        if node.child[0].type == "var":
            return self.var(node.child[0])

        if node.child[0].type == "chamada_funcao":
            return self.chamada_funcao(node.child[0])

        if node.child[0].type == "numero":
            return self.numero(node.child[0])

        else:
            return self.expressao(node.child[0])

    def numero(self, node):
        var = repr(node.value)
        if ("e" in var) or ("E" in var):
            return "cientifico"

        if "." in var:
            return "flutuante"

        else:
            return "inteiro"


    def chamada_funcao(self, node):
        if node.value == "principal" and self.escopo == "principal":
            print("WARNING: chamada recursiva para a funcao principal")

        if node.value == "principal" and self.escopo != "principal":
            print("ERRO: a funcao [" + self.escopo + "] faz uma chamada para a funcao principal")

        if node.value not in self.tabelaSimbolos.keys():
            print("ERRO: a funcao [" + node.value + "] nao foi declarada")

        args_chamada = []
        args_chamada.append(self.lista_argumentos(node.child[0]))

        if args_chamada[0] is "void":
            args_chamada = []

        elif type(args_chamada[0]) != str:
            args_chamada = args_chamada[0]

        args_def = self.tabelaSimbolos[node.value][2]

        if type(args_def) is str:
            args_def = []

        if len(args_chamada) != len(args_def):
            print("ERRO: quantidade de argumentos invalida para a funcao [" + node.value + "], esperado [" + repr(len(args_def)) + "] mas a chamada foi feita com [" + repr(len(args_chamada)) + "]")

        for i in range(len(args_chamada)):
            if (args_chamada[i] == "inteiro" and args_def[i] == "flutuante"):
                print("WARNING: a chamada da função [" + node.value + "] faz uma conversão implícita de tipos [" + repr(args_chamada[i]) + "] -> [" + repr(args_def[i]) + "]")
            elif args_chamada[i] != args_def[i]:
                print("ERRO: tipo de argumento invalido para a funcao [" + node.value + "], esperado [" + repr(args_def[i]) + "] mas a chamada foi feita com [" + repr(args_chamada) + "]")

        self.tabelaSimbolos[node.value][3] = True

        return self.tabelaSimbolos[node.value][4]

    def lista_argumentos(self, node):
        args = []

        if len(node.child) != 1:
            args.append(self.lista_argumentos(node.child[0]))

            if not (type(args[0]) is str):
                args = args[0]

            args.append(self.expressao(node.child[1]))
            return args
            
        else:
            if node.child[0] is None:
                return "void"

            if node.child[0].type == "expressao":
                return self.expressao(node.child[0])

            else:
                return []
            

def print_tabelaSimbolos(simbolos):
    print("\n")
    print("===================== TABELA DE SÍMBOLOS =====================")
    print("[var|func][nome][usada][atribuida][tipo][escopo]")
    for key, values in simbolos.items():
        print(values)
    print("==============================================================")


if __name__ == '__main__':
    import sys
    #print_tree(x.tree)
    code = open(sys.argv[1], 'r', encoding='utf-8')
    print("\n")
    x = Semantica(code.read())
    print_tabelaSimbolos(x.tabelaSimbolos)
    
    
