cont = 0
def mostrar_cont():

    print(cont)

def modificar_cont(c):
    global cont
    cont = c

modificar_cont(5)
mostrar_cont()