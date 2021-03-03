print('\033[0:30:41mTESTE\033[m')



print('\033[1;31mOlá, mundo!')
print('\033[1;32mOlá, mundo!')
print('\033[1;33mOlá, mundo!')
print('\033[1;35mOlá, mundo!')


print('{}Olá, mundo!{}'.format('\033[1;31m','\033[m'))




print('Muito prazer em te conhecer, {}Guilherme{}!'.format('\33[1;35m','\033[m'))



cores = {'limpa':'\033[m',
         'vermelha':'\033[1;31m',
         'verde':'\033[1;32m'}

print('{}Seja bem vindo.{} Obrigado até o momento.{} Até breve.'.format(cores['vermelha'],cores['verde'],cores['limpa']))

