def quick_sort(lista):
    if len(lista)<=1:
        return lista
    else:
        pivote=lista[len(lista)//2]
        izquierda=[x for x in lista if x<pivote]
        centro=[x for x in lista if x== pivote]
        derecha=[x for x in lista if x>pivote]
        return quick_sort(izquierda)+centro+quick_sort(derecha)
    
lista=[10,7,8,9,1,5]
print(f"Lista ordenada: {quick_sort(lista)}")