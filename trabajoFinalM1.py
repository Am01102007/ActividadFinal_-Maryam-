#Sistema de Registro de Productos en Inventario
# Crear una aplicación modular que permita gestionar el inventario básico de una tienda pequeña.
#Funcionalidades requeridas:

#1.Registrar productos.
#2.Mostrar todos los productos registrados.
#3.Buscar producto por nombre.
#4.Calcular valor total del inventario.
#5.Validar entradas y salidas.

# Definimos la lista de productos
productos = []
#1.Registrar productos.
def registrar_productos():
    print("\n ---Registro de productos----")
    nombre=input("Ingrese el nombre del producto: ").strip().title()
        
    while True:
        try:
            precio=float(input("Ingrese el precio del producto: "))
            if precio<=0:
                print("Error: debe ingresar un precio válido")
            else:
                break
        except ValueError:
            print("Error: debe ingresar un precio numérico válido")
        
    while True:
        try:
            cantidad=int(input("Ingrese la cantidad del producto: "))
            if cantidad<=0:
                print("Error: debe ingresar una cantidad válida")
            else:
                break
        except ValueError:
            print("Error: debe ingresar una cantidad numérica válido")
            
    
    #se crea un diccionario a partir de los valores anteriores relación clave - valor
    producto={"nombre":nombre,"precio":precio,"cantidad":cantidad}
    #Agregamos el objeto producto 
    productos.append(producto)
    print("Producto registrado satisfactoriamente.")
    
#2.Mostrar todos los productos registrados.
def mostrar_productos():
    print("\n---Lista de productos registrados---")
    if not productos:
        print("No hay productos registrados")
    else:
        for i , p in enumerate(productos,1):
            print (f"{i}.{p['nombre']} - {p['precio']} precio - {p['cantidad']}")
            
#3. Buscar producto por nombre.
def buscar_producto():
   print("\n---Buscar un producto---") 
   nombre=input("Ingrese el nombre a buscar: ").strip().lower()
   
   encontrados = [p for p in productos if nombre in p["nombre"].lower()]
   if encontrados:
       for p in encontrados:
           print (f"{p['nombre']} - {p['precio']} precio - {p['cantidad']}")
   else:
         print("No se encontraron productos con ese nombre.")
         
#4.Calcular valor total del inventario.
def calcular_valor_inventario():
    print("\n---Valor total del inventario---")
    if not productos:
        print("No hay productos registrados")
        return 
    valores_inventario=[p ["precio"]*p["cantidad"] for p in productos]
    total_precio_inventario= sum(valores_inventario)
    print (f"Total de precios inventario= {total_precio_inventario:.2f}")

def menu():
    while True:
        print("\n === SISTEMA DE INVENTARIO ===")
        print("1. Registrar productos")
        print("2. Mostrar productos registrados")
        print("3. Buscar producto por nombre")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        opcion= input("Seleccione una opcion (1-5):")
        if opcion=="1":
            registrar_productos()
        elif opcion=="2":
            mostrar_productos()
        elif opcion=="3":
            buscar_producto()
        elif opcion=="4":
            calcular_valor_inventario()
        elif opcion=="5":
            print("Saliendo del sistema de inventario. ¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Por favor, intente otra vez seleccionando una opción del 1 al 5.")
def main():
    menu()

if __name__ == "__main__":
    main()