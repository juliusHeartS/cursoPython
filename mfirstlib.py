# Estoy haciendo un ejemplo de librería de funciones.
def msuma(x,y):
    # Descripción msuma es una función que recibe 2 números  y devuelve su suma
    # x, y son números
    z = x + y
    return(z)

def prueba(x,y):
    # Descripción ...
    # x,y son números
    if x > 10 and y > 10:
        return(x + y)
    elif x < 10 and y < 10:
        return(x - y)
    else:
        return(x*y)
    
def ordenador(x,y):
    # Toma dos números y devuelve la lista ordenada
    if x > y:
        return([y, x])
    else:
        return([x, y])
    

def valor_ordenado(x,y):
    # Descripción ...
    # x, y son listas de números de la misma longitud
    
    # Verificamos que las listas sean de la misma longitud
    nx = len(x)
    ny = len(y)
    if nx == ny:
        lista_ordenada = []
        for i in range(nx):
            lista_ordenada.append(ordenador(x[i],y[i]))
        
        return(lista_ordenada)
        
    else:
        print("No es posible el proceso")
        return([])
    
def mrange(inicio=0,final=10,paso=1):
    # mrange reproduce los resultados de range pero además acepta pasos no enteros.
    # inicio es el valor de inicio de la sucesión
    # final indica el último valor no alcanzado
    # paso es le valor con el cual avanzo o retrocedo de inicio a final

    if inicio <= final and paso > 0:
        mlista = []
        avance = inicio
        while  avance < final:
            mlista.append(avance)
            avance += paso # avance = avance + paso
        return(mlista) 
    elif inicio >= final and paso < 0:
        mlista = []
        retroceso = inicio
        while retroceso > final:
            mlista.append(round(retroceso,4))
            retroceso += paso
        return(mlista)
    else:
        print("Error, revise los parámetros")
        

