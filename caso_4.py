mis_frutas=['fresa', 'manzana','mango', 'pera','naranja','piña']
verduras=['tomates', 'papas','cebolals', 'ajos']
frutas=['piña', 'naraja', 'sandia']
carne=['mortadela', 'pollo', 'costilla de cerdo']
limpieza=['jabon','cloro','shampoo']
lista_del_compras=[verduras,frutas,carne,limpieza]
print(lista_del_compras)
# Caso 4 agregar  item a la lista verdura, fruta
verduras.append('chile')
frutas.append('mango')
#lista_del_compras.extend(verduras.append('chile'),frutas.append('mango'))
print(lista_del_compras)

mi_lista=[]
for articulos in lista_del_compras:
    mi_lista.extend(articulos)
    print(mi_lista)
print(len(mi_lista))