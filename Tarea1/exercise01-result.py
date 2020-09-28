# Se me ocurrio hacerlo pidiendo al vendedor la cantidad de clientes
# que desea insertar, metí ese valor en una variable y la convertí en mi
# condicion del bucle para detenerse


ListaRegistro = []
clientes = 0
cantidad = int(input("Inserte la cantidad de clientes que desea agregar: "))

while clientes < cantidad:
    cliente = input("Inserte el nombre del cliente: ")
    producto = input("Inserte el producto: ")
    costo = float(input("Inserte el costo ($0.00): "))

    registro = dict(cliente=cliente, producto=producto, costo=costo)
    ListaRegistro.append(registro)
    clientes += 1
for registro in ListaRegistro:
    print(registro)
