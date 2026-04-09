nome = str(input('Digite seu nome completo: ')).strip()

dividido = nome.split()

print('Analisando seu nome...')
print('seu nome em maíusculas é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {}'.format(len(nome)- nome.count('')))
print('seu primeiro no é {} e tem {} letras'.format(dividido[0],len(dividido[0])))
