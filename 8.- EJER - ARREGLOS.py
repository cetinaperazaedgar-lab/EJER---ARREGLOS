import pandas as pd

# Definir meses y departamentos
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
departamentos = ["Ropa", "Deportes", "Juguetería"]

# Crear matriz de 12x3 inicializada en 0
ventas = [[0 for _ in range(len(departamentos))] for _ in range(len(meses))]

# Método para insertar venta
def insertar_venta(mes, depto, valor):
    i = meses.index(mes)
    j = departamentos.index(depto)
    ventas[i][j] = valor

# Método para buscar venta
def buscar_venta(mes, depto):
    i = meses.index(mes)
    j = departamentos.index(depto)
    return ventas[i][j]

# Método para eliminar venta (poner en 0)
def eliminar_venta(mes, depto):
    i = meses.index(mes)
    j = departamentos.index(depto)
    ventas[i][j] = 0

# Método para mostrar tabla
def mostrar_tabla():
    df = pd.DataFrame(ventas, index=meses, columns=departamentos)
    print("\nTabla de Ventas:\n")
    print(df)

# Menú interactivo
while True:
    print("\n" + "="*30)
    print("\n--- MENÚ DE VENTAS ---")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar tabla")
    print("5. Salir")
    print("\n" + "="*30)

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        mes = input("\nIngrese el mes (Ejemplo: Enero): ")
        depto = input("\nIngrese el departamento (Ropa/Deportes/Juguetería): ")
        valor = int(input("\nIngrese la venta: "))
        insertar_venta(mes, depto, valor)
        print("\nVenta insertada con éxito.")

    elif opcion == "2":
        mes = input("\nIngrese el mes: ")
        depto = input("\nIngrese el departamento: ")
        print(f"🔎 Venta encontrada: {buscar_venta(mes, depto)}")
    
    elif opcion == "3":
        mes = input("\nIngrese el mes: ")
        depto = input("\nIngrese el departamento: ")
        eliminar_venta(mes, depto)
        print("\nVenta eliminada con éxito.")

    elif opcion == "4":
        mostrar_tabla()

    elif opcion == "5":
        print("\nSaliendo del programa...")
        break

    else:
        print("\nOpción no válida, intenta de nuevo.")