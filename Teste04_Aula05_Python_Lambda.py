quadrado = lambda x : x**2
print(quadrado(5))
##############################
par = lambda x : x % 2 == 0
print(par(10))
###############################
name_upperCase = lambda n : n.upper()
print(name_upperCase('Tiago'))
#################################
par_impar = lambda x : "par" if x % 2 == 0 else "ímpar"
print(par_impar(5))
print(par_impar(-2))
##################################
valida_usuario = lambda user: "Erro:usuario precisa ser definido" if user == "" else ("usuario não pode ter menos de 4 digitos" if len(user) < 4 else "usuario definido com sucesso")
print(valida_usuario(""))
print(valida_usuario("zé"))
print(valida_usuario("josé"))
####################################
numeros = [1, 2, 3, 4, 5]
quadrado = list(map(lambda x : x**2, numeros))
print(quadrado)
########################################
from functools import reduce
numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x,y : x + y, numeros)
print(soma)
######################################