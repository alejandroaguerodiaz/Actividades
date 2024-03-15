funcionalidades = ["agregar", "eliminar", "mostrar", "salir"]
def seleccion():
    # No sale del loop hasta que se ingresen los datos de manera correcta
    while True:
        mensaje = str(input("Ingrese el tipo de accion que desea realizar, agregar, eliminar, mostrar o salir: ")).lower()
        if mensaje in funcionalidades:
            return mensaje
        else: 
            print("Valor incorrecto. Recuerde que por ahora la aplicacion solo cuenta con las funcionalidades", funcionalidades)
            
# Creacion del dict, sleecciona la funcion y la ejecuta
inventario = {}
while True:
    # Asigna a funcion lo que haya seleccionado el usuario
    funcion = seleccion()
    if funcion == "salir":
        break
    elif funcion == "mostrar":
        print(inventario)
        continue

    # Si se quiere eliminar o agregar se tiene que ingresar el nombre producto
    nombre_producto = str(input("Ingrese el nombre del producto: "))

    # Si el producto se encuentra dentro del inventario entonces solo suma el stock
    if funcion == "agregar":
        stock = int(input("Ingrese la cantidad de stock: "))
        if nombre_producto in inventario:
            inventario[nombre_producto] += stock
        else:
            inventario[nombre_producto] = stock

    # Si el producto se encuentra en el inventario, se elimina, sino se lanza un error y se vuelve al loop
    elif funcion == "eliminar":
        if nombre_producto in inventario:
            del inventario[nombre_producto]
        else:
            print("No se encuentra tal producto en el inventario, intente de nuevo con otro producto")
            continue    
        