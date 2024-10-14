#Questão 1 - com lista
def fib(n, fibo=None):
    if fibo is None:
        fibo = [0, 1]  

    fibo.append(soma(fibo[-2], fibo[-1]))  

    if n in fibo:
        return "O número pertence a sequência de fibonate"
    
    elif n > fibo[-1]:
        return fib(n, fibo)  
    
    else:
        return "O número NÂO pertence a sequência de fibonate"  


def soma(a, b):
    return a + b  

#Questão 1 -  com pilhas

class No:
    def __init__(self,valor,prox):
        self.info = valor
        self.prox = prox

class Pilha:
    def __init__(self):
        self.topo = None
        self.quant = 0

    def pop(self):
        if self.quant == 1:
            self.topo = None
        elif self.esta_vazia():
            pass
        else:
            self.topo = self.topo.prox
        self.quant -= 1
            
    def push(self,valor):
        if self.esta_vazia():
            self.topo = No(valor,None)    
        else:    
            novo_topo = No(valor,self.topo)
            self.topo = novo_topo
        self.quant +=1

    def show(self):
        aux = self.topo
        while aux != None:
            print(aux.info,end=' ') 
            aux = aux.prox
    
    def esta_vazia(self):
        return self.quant == 0

    def ver_topo(self):
        return self.topo.info
        
    def qtItens(self):
        return self.quant
    
class fibonate:
    def __init__(self):
        self.pilha = Pilha()
        self.pilha.push(0)
        self.pilha.push(1)

    def fibo(self, n):
        a = self.pilha.ver_topo()
        self.pilha.pop()
        b = self.pilha.ver_topo()
        self.pilha.push(a)
        self.pilha.push(a+b)


        if n == a or n == b:
            return "O número pertence a sequência de fibonate"
        elif n> a:
            return self.fibo(n)
        else:
            return "O número NÂO pertence a sequência de fibonate" 
        

#Questão 2 - simples

def verificarStringA(string):
    qt = sum(1 for i in string if i in ['a', 'A'])
    
    if qt>0:
        return f"Existe letra(s) 'a' na string fornecida. \nQuantidade: {qt}"
    else:
        return 'Não existe letra a na string'
    
#Questão 2 - estruturado em classe

class verificarString:
    def __init__(self,letra):
        self.qt =0
        self.letraUp = letra.upper()
        self.letraMin = letra.lower()
        self.qtUp = 0
        self.qtMin = 0
        self.stri = None

    def string(self, string):
        self.stri = string
        self.analise()

    def analise(self):
        for i in self.stri:
            if i == self.letraUp:
                self.qtUp += 1
                self.qt += 1
            elif i ==  self.letraMin:
                self.qtMin += 1
                self.qt += 1

    def getDados(self):
        return f'Quantidades de {self.letraUp}: {self.qtUp} \nQuantidade de {self.letraMin}: {self.qtMin} \nQuantidade de total: {self.qt}'
    



            


    
        
        




        



