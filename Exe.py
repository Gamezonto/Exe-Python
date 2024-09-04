def is_fibonacci(n):
    
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n


numero = int(input("Informe um número: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

/

def count_a_in_string(s):
    count = s.lower().count('a')
    return count


texto = input("Informe uma string: ")

contagem = count_a_in_string(texto)

if contagem > 0:
    print(f"A letra 'a' aparece {contagem} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")

/

INDICE = 12
SOMA = 0
K = 1
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
