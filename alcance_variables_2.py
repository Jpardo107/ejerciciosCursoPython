#MAS DE FUNCIONES ANIDADAS Y ALCANCE DE VARIABLES

def funcionExterna():
    var_local_externa = 'Variable local externa'
    def funcionAnidada():
        var_local_anidada = 'Variable local anidada'
        nonlocal var_local_externa
        var_local_externa = 'Nuevo valor variable local externa'
        print(f'Variable local anidada: {var_local_anidada}')
    funcionAnidada()
    print(f'Valor variable local externa: {var_local_externa}')
funcionExterna()