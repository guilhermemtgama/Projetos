a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor: '))
soma = a+b
subt = a-b
multip = a*b
divisao = a/b
resto = a%b

Resultado = ('Soma: {soma}. '
      '\nSubtração: {sub}. '
      '\nMultiplicação: {mult}. '
      '\nDivisão: {div}.'
      '\n resto: {resto}'.format(soma=soma,
                                sub=subt,
                                mult=multip,
                                div=int(divisao),
                                resto=resto))

print(Resultado)
