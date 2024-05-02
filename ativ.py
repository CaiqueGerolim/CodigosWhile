contador = 0
n =int(input("Quantas notas vai ter? "))
while n in range(contador):
    contador += n
    n2 = int(input("Qual a nota do aluno? "))
    media = (n2 * n)/2
print(media)
