from llvmlite import ir
from AnaliseSintatica import AnaliseSintatica
from AnaliseSemantica import Semantica
from pprint import pprint

class GenCode:
    def __init__(self, code):
        self.module = ir.Module('compiladorTpp')
        self.tabelaSimbolos = Semantica(code).tabelaSimbolos

        self.escopo = "global"
        self.lista_escopos = ["global"]

        self.builder = None
        self.func = None
        self.bloco = None
        self.tipo_aux = None
        self.posicao_parametro = 0

        self.leia_float = ir.Function(self.module, ir.FunctionType(ir.FloatType(), []), name="leiaFlutuante")
        self.leia_int = ir.Function(self.module, ir.FunctionType(ir.IntType(32), []), name="leiaInteiro")
        self.escreve_float = ir.Function(self.module, ir.FunctionType(ir.IntType(32), [ir.FloatType()]), name="escrevaFlutuante")
        self.escreve_int = ir.Function(self.module, ir.FunctionType(ir.IntType(32), [ir.IntType(32)]), name="escrevaInteiro")

        self.start(AnaliseSintatica(code).ast)

        arquivo = open('./out.ll', 'w')
        arquivo.write(str(self.module))
        arquivo.close()

        with open("out.ll", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if "unknown" not in i:
                    f.write(i)
            f.truncate()

    def find_var(self, name):
        for escopo in reversed(self.lista_escopos):
            for key, value in self.tabelaSimbolos.items():
                if value[0] == "variavel":
                    if value[5] == escopo:
                        if value[1] == name:
                            if value[1] == name:
                                if len(value) >= 7:
                                    return value

        return None

    def find_func(self, name):
        for k, v in self.tabelaSimbolos.items():
            if v[0] == "funcao" and v[1] == name:
                return v

        return None

    def start(self, node):
        self.lista_declaracoes(node.child[0])

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
            self.declaracao_funcao(node.child[0])
            self.lista_escopos.pop()
            self.escopo = self.lista_escopos[-1]

    def declaracao_variaveis(self, node):
        var_type = node.child[0].type
        lista_vars = self.lista_variaveis(node.child[1])

        for varname in lista_vars:
            if self.escopo == "global":
                if var_type == "inteiro":
                    var = ir.GlobalVariable(self.module, ir.IntType(32), varname)
                    var.initializer = ir.Constant(ir.IntType(32), 0)

                else:
                    var = ir.GlobalVariable(self.module, ir.FloatType(), varname)
                    var.initializer = ir.Constant(ir.FloatType(), 0)

            else:
                if var_type == "inteiro":
                    var = self.builder.alloca(ir.IntType(32), name=varname)

                else:
                    var = self.builder.alloca(ir.FloatType(), name=varname)

            var.linkage = "common"
            var.align = 4
            self.tabelaSimbolos[self.escopo + "-" + varname] = ["variavel", varname, False, False, var_type, self.escopo, var]

    def inicializacao_variaveis(self, node):
        self.atribuicao(node.child[0])

    def lista_variaveis(self, node):
        list_var = []

        if len(node.child) == 1:
            list_var.append(self.varname(node.child[0]))
        else:
            for item in self.lista_variaveis(node.child[0]):
                list_var.append(item)
            list_var.append(self.varname(node.child[1]))

        return list_var

    def varname(self, node):
        if len(node.child) == 0:
            return node.value

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

    def declaracao_funcao(self, node):
        offset = 0
        if len(node.child) == 1:
            retorno = None
            llvm_retorno = ir.VoidType()

        else:
            offset = 1
            if node.child[0].value == "inteiro":
                retorno = "inteiro"
                llvm_retorno = ir.IntType(32)

            else:
                retorno = "flutuante"
                llvm_retorno = ir.FloatType()

        cabeca = self.cabecalho(retorno, node.child[offset])
        lista_param = cabeca[0]
        llvm_params = []
        corpo_node = cabeca[1]
        func_nome = cabeca[2]

        for param in lista_param:
            tipo = param[0]

            if tipo == "inteiro":
                llvm_params.append(ir.IntType(32))
            else:
                llvm_params.append(ir.FloatType())

        if func_nome == "principal":
            nome_func = "main"

        else:
            nome_func = func_nome
        llvm_func_type = ir.FunctionType(llvm_retorno, llvm_params)
        self.func = ir.Function(self.module, llvm_func_type, name=nome_func)

        escopo_nome = func_nome
        self.lista_escopos.append(escopo_nome)
        self.escopo = escopo_nome

        entry_block = self.func.append_basic_block('entry')

        self.builder = ir.IRBuilder(entry_block)
        self.bloco = entry_block
        self.tabelaSimbolos[func_nome] = ["funcao", func_nome, lista_param, llvm_retorno, 0, escopo_nome, self.func]
        self.corpo(corpo_node)

    def cabecalho(self, tipo, node):
        self.posicao_parametro = 0
        lista_par = self.lista_parametros(node.child[0])
        #print(node.value)

        return [lista_par, node.child[1], node.value]

    def lista_parametros(self, node):
        if len(node.child) == 1 and node.child[0] is not None:
            return [self.parametro(node.child[0])]

        elif len(node.child) == 2:
            parametros = self.lista_parametros(node.child[0])
            parametros.append(self.parametro(node.child[1]))

            return parametros

        else:
            return []

    def parametro(self, node):
        if len(node.child) == 0:
            tipo = self.tipo_aux

        else:
            tipo = node.child[0].value

        self.tipo_aux = tipo
        name = node.value
        posicao = self.posicao_parametro
        self.posicao_parametro += 1

        return [tipo, name, posicao]

    def corpo(self, node):
        if len(node.child) == 2:
            self.corpo(node.child[0])
            self.acao(node.child[1])

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
        if len(node.child) == 2:
            origem_bloco = self.bloco
            condicao_expr = self.expressao(node.child[0])

            true_bloco = self.func.append_basic_block("SE-VERDADE")
            self.bloco = true_bloco
            self.builder.position_at_end(true_bloco)
            self.corpo(node.child[1])
            outer_true_bloco = self.bloco

            self.bloco = origem_bloco
            self.builder.position_at_end(origem_bloco)
            fim_bloco = self.func.append_basic_block("SE-TERMINO")

            self.builder.cbranch(condicao_expr, true_bloco, fim_bloco)

            self.bloco = outer_true_bloco
            self.builder.position_at_end(outer_true_bloco)

            if not self.bloco.is_terminated:
                self.builder.branch(fim_bloco)

            self.bloco = fim_bloco
            self.builder.position_at_end(fim_bloco)

        else:
            origem_bloco = self.bloco
            condicao_expr = self.expressao(node.child[0])

            true_bloco = self.func.append_basic_block("SE-VERDADE")
            self.bloco = true_bloco
            self.builder.position_at_end(true_bloco)
            self.corpo(node.child[1])
            outer_true_bloco = self.bloco

            false_bloco = self.func.append_basic_block("SE-FALSO")
            self.bloco = false_bloco
            self.builder.position_at_end(false_bloco)
            self.corpo(node.child[1])
            outer_false_bloco = self.bloco

            self.bloco = origem_bloco
            self.builder.position_at_end(origem_bloco)
            fim_bloco = self.func.append_basic_block("SE-TERMINO")

            self.builder.cbranch(condicao_expr, true_bloco, false_bloco)

            self.bloco = outer_true_bloco
            self.builder.position_at_end(outer_true_bloco)

            if not self.bloco.is_terminated:
                self.builder.branch(fim_bloco)

            self.bloco = outer_false_bloco
            self.builder.position_at_end(outer_false_bloco)

            if not self.bloco.is_terminated:
                self.builder.branch(fim_bloco)

            self.bloco = fim_bloco
            self.builder.position_at_end(fim_bloco)

    def repita(self, node):
        origem_bloco = self.bloco

        repita = self.func.append_basic_block("REPITA")
        self.builder.branch(repita)
        self.bloco = repita
        self.builder.position_at_end(repita)
        self.corpo(node.child[0])

        ate_expr = self.expressao(node.child[1])

        self.bloco = origem_bloco
        self.builder.position_at_end(origem_bloco)
        fim_repita = self.func.append_basic_block("FIM-REPITA")

        self.bloco = repita
        self.builder.position_at_end(repita)

        self.builder.cbranch(ate_expr, fim_repita, repita)

        self.bloco = fim_repita
        self.builder.position_at_end(fim_repita)

    def atribuicao(self, node):
        varname = self.varname(node.child[0])
        expr = self.expressao(node.child[1])
        var = self.find_var(varname)

        if var is None:
            return

        var[2] = True
        var[3] = True
        self.builder.store(expr, var[6])

    def leia(self, node):
        var = self.find_var(node.value)

        if var[4] == "inteiro":
            func = self.leia_int

        else:
            func = self.leia_float

        valor = self.builder.call(func, [], "")
        self.builder.store(valor, var[6])

    def escreva(self, node):
        expr = self.expressao(node.child[0])
        tipo_expr = expr.type

        if tipo_expr == ir.IntType(32):
            func = self.escreve_int
        else:
            func = self.escreve_float

        self.builder.call(func, [expr], "")

    def retorna(self, node):
        expr = self.expressao(node.child[0])
        self.builder.ret(expr)

    def expressao(self, node):
        if node.child[0].type == "expressao_simples":
            return self.expressao_simples(node.child[0])

        else:
            return self.atribuicao(node.child[0])

    def expressao_simples(self, node):
        if len(node.child) != 1:
            t1 = self.expressao_simples(node.child[0])
            tipo_op = node.child[1].value
            t2 = self.expressao_aditiva(node.child[2])

            if tipo_op == "=":
                tipo_op = "=="

            if tipo_op == "&&":
                result = self.builder.and_(t1, t2, "")

            elif tipo_op == "||":
                result = self.builder.or_(t1, t2, "")

            else:
                result = self.builder.icmp_signed(tipo_op, t1, t2, "")

            return result

        else:
            return self.expressao_aditiva(node.child[0])

    def expressao_aditiva(self, node):
        if len(node.child) != 1:
            t1 = self.expressao_aditiva(node.child[0])
            tipo_op = node.child[1].value
            t2 = self.expressao_multiplicativa(node.child[2])

            if t1.type is ir.FloatType() or t2.type is ir.FloatType():
                if tipo_op == "+":
                    return self.builder.fadd(t1, t2)

                elif tipo_op == "-":
                    return self.builder.fsub(t1, t2)

            else:
                if tipo_op == "+":
                    return self.builder.add(t1, t2)

                elif tipo_op == "-":
                    return self.builder.sub(t1, t2)

        else:
            return self.expressao_multiplicativa(node.child[0])

    def expressao_multiplicativa(self, node):
        if len(node.child) != 1:
            t1 = self.expressao_multiplicativa(node.child[0])
            tipo_op = node.child[1].value
            t2 = self.expressao_unaria(node.child[2])

            if t1.type is ir.FloatType() or t2.type is ir.FloatType():
                if tipo_op == "*":
                    return self.builder.fmul(t1, t2)

            else:
                return self.builder.mul(t1, t2)

            if tipo_op == "/":
                return self.builder.fdiv(t1, t2)            

        else:
            

            return self.expressao_unaria(node.child[0])

    def expressao_unaria(self, node):
        if len(node.child) == 1:
            return self.fator(node.child[0])

        else:
            tipo_op = node.child[0].value
            expr = self.fator(node.child[1])

            if tipo_op == "-" or tipo_op == "!":
                return self.builder.neg(expr)

            return expr

    def fator(self, node):
        if node.child[0].type == "var":
            return self.var(node.child[0])

        elif node.child[0].type == "chamada_funcao":
            return self.chamada_funcao(node.child[0])

        elif node.child[0].type == "numero":
            return self.numero(node.child[0])
            
        else:
            return self.expressao(node.child[0])

    def var(self, node):
        var = self.find_var(node.value)

        if var is None:
            name_func = self.func.name
            func = self.find_func(name_func)
            params = func[2]

            for p in params:
                if p[1] == node.value:
                    return self.func.args[p[2]]

        return self.builder.load(var[6])

    def numero(self, node):
        var = node.value

        if "e" in var or "E" in var:
            #print("cientifico")
            #exit(1)
            return None

        if "." in var:
            return ir.Constant(ir.FloatType(), float(var))

        else:
            return ir.Constant(ir.IntType(32), int(var))

    def chamada_funcao(self, node):
        func = self.find_func(node.value)        
        return self.builder.call(func[6], self.lista_argumentos(node.child[0]), "")

    def lista_argumentos(self, node):
        if len(node.child) != 1:
            args = self.lista_argumentos(node.child[0])
            args.append(self.expressao(node.child[1]))
            return args

        else:
            if node.child[0] is None:
                return []

            return [self.expressao(node.child[0])]
            


if __name__ == '__main__':
    import sys
    code = open(sys.argv[1], 'r', encoding='utf-8')
    print("\n")
    gen = GenCode(code.read())
    print(gen.module)


    #8, 9, 11, 12, 15