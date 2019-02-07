def cargarArchivo():
    return[linea.split(" ") for linea in [y.strip("\n") for y in open ("Matriz(5).txt").readlines()]]

def rec_pfila(matriz):
    return matriz[0]

def rec_ufila(matriz):
    return list (reversed(matriz[-1]))

def rec_pcol(matriz):
    return list(reversed([x[0] for x in matriz]))

def rec_ucol(matriz):
    return [x[-1] for x in matriz]

def recorrerCaracol(matriz):
    if(len(matriz)>0):
        print( rec_pfila(Lista) + (rec_ucol(Lista)) + (rec_ufila(Lista)) + (rec_pcol(Lista)))
        matriz1 = [matriz[1:]]
        matriz1 = [matriz[:-1]] 
        matriz1 = [x[1:] for x in matriz]
        matriz1 = [x[:-1] for x in matriz]
        recorrerCaracol(matriz1)
#    return ListaFinal

Lista = cargarArchivo()

recorrerCaracol(Lista)

#for x in recorrerCaracol(Lista):
#    print(x, end=" ")
