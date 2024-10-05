def merge_sort(lista):
    if len(lista)>1:
        mid=len(lista)//2
        izquierda=lista[:mid]
        derecha=lista[mid:]
        
        merge_sort(izquierda)
        merge_sort(derecha)
        
        i=j=k=0
        
        while i<len(izquierda) and j<len(derecha):
            if izquierda[i]<derecha[j]:
                lista[k]=izquierda[i]
                i+=1
            else:
                lista[k]=derecha[j]
                j+=1
            k+=1
        
        while i < len(izquierda):
            lista[k]=izquierda[i]
            i+=1
            k+=1
            
        while j < len(derecha):
            lista[k]=derecha[j]
            j+=1
            k+=1
            
lista=[12,11,13,5,6,7]
merge_sort(lista)
print(f"Lista ordenada: {lista}")