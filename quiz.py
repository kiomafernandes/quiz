import anexo
print('Seja bem vindo ao Quiz!')
answer_user = input('Quer começar? (S/N) ').upper()

if answer_user != 'S':
    quit()

score = 0

print('Começando...')
print('\n')
print('--------------Primeira pergunta--------------------------')
print('Qual o nome da estrela mais brilhante? '
      '\n (A) Alpha Centauri (Rigil Kentaurus)'
      '\n (B) Alpha Canis Majori (Sirius ou Sirius A)'
      '\n (C) Alpha Orionis (Betelgeuse)'
      '\n (D) Zeta Oriones')
answer = input('Resposta ').upper()
if answer == 'B':
    print('---------------------------------------------------')
    print('Correto!')
    print(anexo.sirius)
    score = score + 1
else:
    print('---------------------------------------------------')
    print('Incorreto!')

print('-------------Segunda pergunta---------------------------')

print('Quem é o pai da Física Quantica? '
      '\n (A) Max Planck'
      '\n (B) Carl Jonhson'
      '\n (C) Albert Einstein'
      '\n (D) Carl Seigan')
answer = input('Resposta ').upper()
if answer == 'A':
    print('---------------------------------------------------')
    print('Correto!')
    print(anexo.max_planck)
    score = score + 1
else:
    print('---------------------------------------------------')
    print('Incorreto!')

print('--------------terceira pergunta-------------------------')

print('Quantas copas a argentina ganhou? '
      '\n (A) 2'
      '\n (B) 1'
      '\n (C) 3'
      '\n (D) Nenhuma')
answer = input('Resposta ').upper()
if answer == 'C':
    print('---------------------------------------------------')
    print('Correto!')
    print(anexo.argentina)
    score = score + 1
else:
    print('---------------------------------------------------')
    print('Incorreto!')

print('O quiz acabou... '
      f'\n Pontuação: {score}/3')
print('\n')
print('-----------------------------------------------------')
print('\n')