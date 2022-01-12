# scope de variables o alcance

var_global = 'Variable global'
def imprimir():
    global var_global
    print(f'Variable global desde una funcion: {var_global}')
    var_local = 'Variable local'
    print(f'Variable local desde su funcion: {var_local}')
    var_global = 'nuevo valor dado en la funcion'
    def imprimir2():
        print(f'Variable local dentro de una funcion anidada: {var_local}')
    imprimir2()
imprimir()
print(f'Reasignacion de valor a variable global dentro de la funcion: {var_global}')
