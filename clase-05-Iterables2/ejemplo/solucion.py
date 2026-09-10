sigueAgregando = "S"
lista_productos = []
while sigueAgregando == "S":
   nombreProducto = input("Ingresar nombre producto: ")
   precioProducto = input("Ingresar precio producto: ")
   cantidadProducto = input("Ingresar cantidad producto: ")
   producto = {
      "nombre": nombreProducto,
      "precio": precioProducto,
      "cantidad": cantidadProducto
   }
   lista_productos.append(producto)
   sigueAgregando = input("Seguir agregando? S/N: ").upper()
print(lista_productos)