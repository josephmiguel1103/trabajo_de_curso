from models import Usuario

archivo = "./archivo_cliente/cliente.txt"


def registrar_cliente():
    dni = input("DNI: ")
    nombre_apellido = input("Nombres y apellidos: ")
    dirreccion = input("dirrecion: ")
    gmail = input("Gmail: ")

    cliente = Usuario(dni, nombre_apellido, dirreccion, gmail)
    archivo_cliente = open(archivo, "a")
    archivo_cliente.write(str(cliente))
    archivo_cliente.close()
