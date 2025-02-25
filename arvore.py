#a = '*'

#while a == '*':
    #print(a)
    #a = a + '*'
###############################################
# Definição da altura da árvore
altura = 10
# Declarando o que a é
a = '*'

# Loop para cada linha
for i in range(1, altura + 1):
    # Centralizar cada asterísco
    print(a.center(altura * 2 - 1))
    # Somar dois * para crescer a árvore
    a = a + '**'