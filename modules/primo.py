def primo(numero):
    if numero > 1:
        for x in range(1, numero):
            if (numero % x) == 0:
                return "Esse não é um numero primo! "
            else:
                return "Esse é um numero primo!" 
    else:
        print('Esse número não é primo: Numero menor ou igual à 1')