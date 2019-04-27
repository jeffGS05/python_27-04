mis_frutas=['fresa', 'manzana','mango', 'pera','naranja','piña']
verduras=['tomates', 'papas','cebolals', 'ajos']
frutas=['piña', 'naraja', 'sandia']
carne=['mortadela', 'pollo', 'costilla de cerdo']
limpieza=['jabon','cloro','shampoo']
lista_del_compras=[verduras,frutas,carne,limpieza]

# Paso 3 cuantos articulos hay en la lista
print(len(lista_del_compras))

# if return is not present the output will be null

#Solucion 1
cantidad=0
for categoria in lista_del_compras:
    print(categoria, len(categoria))
    cantidad+=len(categoria)
print(cantidad)

#Solucion 2

mi_lista=[]
for articulos in lista_del_compras:
    mi_lista.extend(articulos)
    print(mi_lista)
print(len(mi_lista))