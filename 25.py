'''25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. '''

while True:
    try:
        idades = input("Insira as idades: ").split()
        soma = 0
        for i in idades:
            i = int(i)
            soma += i
        media = soma//len(idades)
        
        if 0 <= media <= 25:
            anos = "jovens"
        elif 26 <= media <= 60:
            anos = "adultos"
        else:
            anos = "idosos"
            
        resultado = f'A media das idades é {media}, majoritariamente {anos}.'
        print(resultado)
        
    except EOFError:
        break
