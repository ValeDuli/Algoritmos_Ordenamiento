def selection_sort(lista):
    n=len(lista)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if lista[j]<lista[min_idx]:
                min_idx=j
        lista[i],lista[min_idx]=lista[min_idx],lista[i]
        
        
lista=[64,25,12,22,11]
selection_sort(lista)
print(f"Lista ordenada: {lista}")