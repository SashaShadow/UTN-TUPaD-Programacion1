def fusionar (izq, der):
    resultado = []
    i = 0
    j = 0

    while i < len(izq) and j < len(der):
        print(izq[i])
        print(der[j]) 
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    print("###")
    print(resultado)
    print("###\n")

    resultado += izq[i:]
    resultado += der[j:]
    print("aft")
    print(resultado)
    print("aft\n")

    return resultado

def merge_sort(vector):
    if len(vector) <= 1:
        return vector

    medio = len(vector) // 2
    izquierda = merge_sort(vector[:medio])
    derecha = merge_sort(vector[medio:])

    print("izq", izquierda)
    print("der", derecha)

    return fusionar(izquierda, derecha)

numeros = [8, 4, 5, 2, 9, 1]
ordenado = merge_sort(numeros)
print("Vector ordenado: ", ordenado)