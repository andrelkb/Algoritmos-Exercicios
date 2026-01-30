def buscaMenor(arr):
    menor = arr[0] #estipula a variavel menor como sendo a do indice 0
    menor_indice = 0 #estipula o indice da variavel menor
    for i in range(1, len(arr)): #percorre o array do indice 1 ate o fim
        if arr[i] < menor: #se o elemento de indice i for menor que a variavel menor
            menor = arr[i]  # este elemento de indice i sera o novo menor
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print (ordenacaoporSelecao([5, 3, 6, 2, 10]))
