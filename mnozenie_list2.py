def mnozenie_list(lista1, lista2):
    if len(lista1) > 0 and len(lista2) > 0:
        lista = [(lista1[0]*lista2[0])]
        lista.extend(mnozenie_list(lista1[1:], lista2[1:]))
        return lista
    else:
        return []
string = "Jeszcze jak!"

lista_pierwsza = [100, 250, 67, 19, 55]
pierwsza_lista = [1,2,3,4,5]
druga_lista = [68,44,21,56,33]
lista_druga = [14, 23, 44, 99, 66]

print(mnozenie_list(pierwsza_lista, druga_lista))
print(mnozenie_list(pierwsza_lista, lista_pierwsza))
print(mnozenie_list(lista_pierwsza, druga_lista))
