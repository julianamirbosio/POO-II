'''6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois
modifique o programa para que ele mostre os números um ao lado do outro. '''

for i in range(0,20):
    num = i + 1
    print(num)
    
lista_num = []
for i in range(0,20):
    lista_num.append(i+1)
lista_a = list(map(str, lista_num))
lista_numero = ' '.join(lista_a)

print(lista_numero)
