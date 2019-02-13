# Conjuntos em python

# Declaração de um conjunto
s = {1, 2, 3, 4}
print(s)

# Existem operações disponíveis nos conjuntos através
# de métodos, como as operações mais conhecidas de
# teoria dos conjuntos, como união, interseção e diferença
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Operação de união de conjuntos em python entre os conjuntos A e B
# Resultado: {1, 2, 3, 4, 5, 6}
print(a.union(b))

# Operação de interseção entre os conjuntos A e B
# Resultado: {3, 4}
print(a.intersection(b))

# Operação de diferença entre o conjunto A e B
# Resultado: {1, 2}
print(a.difference(b))

# Operação da diferença simétrica
# Resultado: {1, 2, 5, 6}
print(a.symmetric_difference(b))

# Operação de pertinência
# Resultado: True
print(1 in a)

# É possível verificar se um conjunto é um subconjunto de outro
c = {1, 2}
# Verificando se o conjunto C é subconjunto do conjunto A
# Resultado: True
print(c.issubset(a))

# Também é possível verificar se um conjunto e superconjunto de outro
# Resutlado: True
print(a.issuperset(c))

# Outra relação importante que é possível verificar através de uma função pronta em python é a disjunção entre dois
# conjuntos. Dois conjuntos são disjuntos se tiverem interseção nula. Exemplo:
c = {1, 2}
d = {3, 4}
# Resultado: True
print(c.isdisjoint(d))

# Função set funciona como um construtor de conjunto. Ela pode receber uma lista ou tupla, e seu retorno é um conjunto dos elementos recebidos
lista = [1, 2, 3, 4, 5, 6]
conjunto = set(lista)
print(conjunto)

# interação sob um conjunto
for i in conjunto:
    print(i)
