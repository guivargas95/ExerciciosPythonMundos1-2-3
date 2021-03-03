def maior(*valores):
    print('-='*30)
    print('Analisando os valores passados...')
    m = cont = 0
    for c in valores:
        print(f'{c}',end=' ')
        cont += 1
        if c > m:
            m = c
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {m}')
    print('-='*30)
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
