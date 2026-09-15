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


def ordena(datos, campo):
    datos.sort(key=lambda fila: fila[campo])
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
        print("2. Ordenar por ID")
        print("3. Ordenar por marca")
        print("4. Ordenar por modelo")
        print("5. Ordenar por anio")
        print("6. Ordenar por tipo de combustible")
        print("7. Agregar registro")
        print("8. Eliminar registro")
        print("9. Salir")

        op = input("\nESCOJE UNA OPCION: ")

        if op == "1":
            datos, encabezados = lee_archivo(registro_autos)
            mostrar_datos(datos, encabezados)
        elif op == "2":
            datos, encabezados = lee_archivo(registro_autos)
            ordenados = sorted(list(datos), key=lambda fila: int(fila["ID_auto"]))
            mostrar_datos(ordenados, encabezados)
            archivo_ordenado(ordenados, encabezados)
            print("Archivo ordenado por ID.")
        elif op == "3":
            datos, encabezados = lee_archivo(registro_autos)
            ordenados = ordena(list(datos), "Marca")
            mostrar_datos(ordenados, encabezados)
            archivo_ordenado(ordenados, encabezados)
            print("Archivo ordenado por marca.")
        elif op == "4":
            datos, encabezados = lee_archivo(registro_autos)
            ordenados = ordena(list(datos), "Modelo")
            mostrar_datos(ordenados, encabezados)
            archivo_ordenado(ordenados, encabezados)
            print("Archivo ordenado por modelo.")
        elif op == "5":
            datos, encabezados = lee_archivo(registro_autos)
            ordenados = ordena(list(datos), "Ano")
            mostrar_datos(ordenados, encabezados)
            archivo_ordenado(ordenados, encabezados)
            print("Archivo ordenado por anio.")
        elif op == "6":
            datos, encabezados = lee_archivo(registro_autos)
            ordenados = ordena(list(datos), "Tipo_Combustible")
            mostrar_datos(ordenados, encabezados)
            archivo_ordenado(ordenados, encabezados)
            print("Archivo ordenado por tipo de combustible.")
        elif op == "7":
            agregar_auto()
            print("\nAuto agregado.")
        elif op == "8":
            eliminar_auto()
        elif op == "9":
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
