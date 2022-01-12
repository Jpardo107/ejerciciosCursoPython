#FUNCIONES ANIDADAS
def calculadora(a,b, opc = 'sumar'):
    if opc == 'sumar':
        def sumar(a,b):
            return a+b
        print(sumar(a,b))
    elif opc == 'restar':
        def restar(a,b):
            return a-b
        print(restar(a,b))

calculadora(5,6, 'sumar')