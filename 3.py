'''3. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd'; '''

lista_estado_civil = ['s', 'c', 'v', 'd']
lista_sexo = ['f', 'm']

while True:
    nome = input("nome: ")
    while len(nome) <= 3:
        nome = input("insira nome com mais de 3 caracteres: ")
        if len(nome) > 3:
            break
    idade = int(input("idade: "))
    while idade < 0 or idade > 150:
        idade = int(input("idade invalida, insira nova idade: "))
        if 0 > idade <= 150:
            break
    salario = int(input("salario: "))
    while salario <= 0:
        salario = int(input("insira salario novamente: "))
        if salario > 0:
            break
    sexo = input("sexo: ")
    while sexo not in lista_sexo:
        sexo = input("insira sexo novamente: ")
        if sexo in lista_sexo:
            break
    estado_civil = input("insira estado civil: ")
    while estado_civil not in lista_estado_civil:
        estado_civil = input("insira estado civil valido: ")
        if estado_civil in lista_estado_civil:
            break
    break
