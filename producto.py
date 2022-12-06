from models import Producto

archivo = "./archivo_producto/producto.txt"


def registrar_producto():
    codigo = input("CODIGO: ")
    nombre = input("NOMBRE: ")
    precio = input("PRECIO: ")

    fuente = Producto(codigo, nombre, precio)
    archivo_fuente = open(archivo, "a")
    archivo_fuente.write(str(fuente))
    archivo_fuente.close()


def mostrar_producto():
    ruta_archivo = open(archivo, "r")
    for linea in ruta_archivo.readlines():
        atributo = linea.split(";")
        print("{} \t {} \t {}".format(
            atributo[0], atributo[1], atributo[2]), end="")


def editar_producto():
    cadena = ""
    ruta_archivo = open(archivo, "r")
    buscar_codigo = str(input("Ingrese el codigo: "))

    for linea in ruta_archivo.readlines():

        aux = []
        atributo = linea.split(";")
        aux.append(linea)
        if buscar_codigo == atributo[0]:
            print("existe")
            codigo = input("CODIGO: ")
            nombre = input("NOMBRE: ")
            precio = input("PRECIO: ")

            fuente = "{};{};{}\n".format(codigo, nombre, precio)
            aux = [fuente]
        print(aux)
        for c in aux:
            cadena += str(c)
    archivo_fuente = open(archivo, "w")
    archivo_fuente.write(str(cadena))
    archivo_fuente.close()
