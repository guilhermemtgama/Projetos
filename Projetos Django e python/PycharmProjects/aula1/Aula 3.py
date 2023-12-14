# a = int(input('Primeira bimestre: '))
# while a > 10:
#     a = int(input('você digitou errado. Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# while b > 10:
#     b = int(input('você digitou errado. Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# while c > 10:
#     c = int(input('você digitou errado. Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))
# while d > 10:
#     d = int(input('você digitou errado. Quarto bimestre: '))
#
# media = (a + b + c + d)/4
#
# print('media: {}'.format(media))









# nota = int(input('Digite a nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida. Digite a nota: '))
# print(nota)


# a = 0
# while a<=10:
#     print(a)
#     a+=1




a = int(input('Entre com um Valor: '))
for num in range(a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        # print(x, resto)
        if resto == 0:
            div +=1

    if div == 2:
        print(num)








# a = int(input('Entre com um número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div +=1
#
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))