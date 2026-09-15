import csv

registro_autos = "registro_autos.csv"
autos_ordenados = "autos_ordenados.csv"


def mostrar_datos(datos, encabezados):
    print(" | ".join(encabezados))
    print("-" * 80)
    for fila in datos:
        print(" | ".join(fila[campo] for campo in encabezados))


def agregar_auto():
    id_auto = input("ID del auto: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    combustible = input("Tipo de combustible: ")

    nuevo_auto = {
        "ID_auto": id_auto,
        "Marca": marca,
        "Modelo": modelo,
        "Ano": ano,
        "Tipo_Combustible": combustible
    }

    with open(registro_autos, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=nuevo_auto.keys())
        escritor.writerow(nuevo_auto)


def lee_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        datos = list(lector)
        encabezados = lector.fieldnames
    return datos, encabezados


def ordena_marca(datos):
    datos.sort(key=lambda fila: fila["Marca"])
    return datos


def ordena_modelo(datos):
    datos.sort(key=lambda fila: fila["Modelo"])
    return datos


def ordena_ano(datos):
    datos.sort(key=lambda fila: fila["Ano"])
    return datos


def ordena_combustible(datos):
    datos.sort(key=lambda fila: fila["Tipo_Combustible"])
    return datos


def eliminar_auto():
    id_auto = input("ID del auto a eliminar: ")
    with open(registro_autos, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        encabezados = lector.fieldnames
        datos = list(lector)

    nuevos_datos = [fila for fila in datos if fila["ID_auto"] != id_auto]

    with open(registro_autos, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(nuevos_datos)

    print(f"Auto con ID {id_auto} eliminado.")


def archivo_ordenado(datos, encabezados):
    with open(autos_ordenados, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(datos)


def main():
    while True:
        print("\n=== SISTEMA DE REGISTROS DE AUTOS ===\n")
        print("1. Mostrar datos")
        print("2. Ordenar por marca")
        print("3. Ordenar por modelo")
        print("4. Ordenar por anio")
        print("5. Ordenar por tipo de combustible")
        print("6. Agregar registro")
        print("7. Eliminar registro")
        print("8. Salir")

        op = input("\nESCOJE UNA OPCION: ")

        if op == "1":
            try:
                datos, encabezados = lee_archivo(registro_autos)
                mostrar_datos(datos, encabezados)
            except FileNotFoundError:
                print("No se encontro el archivo de registro.")
        elif op == "2":
            try:
                datos, encabezados = lee_archivo(registro_autos)
                ordenados = ordena_marca(list(datos))
                mostrar_datos(ordenados, encabezados)
                archivo_ordenado(ordenados, encabezados)
                print("Archivo ordenado por marca.")
            except FileNotFoundError:
                print("No se encontro el archivo de registro.")
        elif op == "3":
            try:
                datos, encabezados = lee_archivo(registro_autos)
                ordenados = ordena_modelo(list(datos))
                mostrar_datos(ordenados, encabezados)
                archivo_ordenado(ordenados, encabezados)
                print("Archivo ordenado por modelo.")
            except FileNotFoundError:
                print("No se encontro el archivo de registro.")
        elif op == "4":
            try:
                datos, encabezados = lee_archivo(registro_autos)
                ordenados = ordena_ano(list(datos))
                mostrar_datos(ordenados, encabezados)
                archivo_ordenado(ordenados, encabezados)
                print("Archivo ordenado por anio.")
            except FileNotFoundError:
                print("No se encontro el archivo de registro.")
        elif op == "5":
            try:
                datos, encabezados = lee_archivo(registro_autos)
                ordenados = ordena_combustible(list(datos))
                mostrar_datos(ordenados, encabezados)
                archivo_ordenado(ordenados, encabezados)
                print("Archivo ordenado por tipo de combustible.")
            except FileNotFoundError:
                print("No se encontro el archivo de registro.")
        elif op == "6":
            agregar_auto()
            print("\nAuto agregado.")
        elif op == "7":
            eliminar_auto()
        elif op == "8":
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
