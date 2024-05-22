# usuário informa os números
x = str(input('Informe o primeiro número')).replace(',', '.')
y = str(input('Informe o segundo número')).replace(',', '.')

# converte para números decimais
x = float(x)
y = float(y)

print('Informe a operação que deseja fazer: \n')
print('"+" para somar.')
print('"-" para subtrair.')
print('"*" para multiplicar.')
print('"/" para dividir.')
print('"%" para encontrar o resto da divisão.')

op = input('Operação desejada: ')
