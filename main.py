from getpass import getpass
from producto import registrar_producto, editar_producto, mostrar_producto
from cliente import registrar_cliente


def main():
    usuario = str(input("ingrese usuario: "))
    contraseña = getpass("ingrese contraseña: ")
    if usuario == "admin" and contraseña == "contraseña":
        menu_principal()
    else:
        print("usuario o contraseña incorrecta \n ingrese otra ves los datos ")
        main()


def menu_principal():
    print("***************************")
    print("******MENU PRINCIPAL*******")
    print("***********MENU************")
    print("  -> 1 Ingresar cliente")
    print("  -> 2 Editar cliente")
    print("  -> 3 Eliminar cliente")
    print("  -> 4 Ingresar producto")
    print("  -> 5 Editar producto")
    print("  -> 6 mostrar producto")
    print("  -> 7 Salir       ")
    print("")

    print("ingrese una opcion ")
    opcion = str(input(">>> "))

    match opcion:
        case "1":
            registrar_cliente()
        case "2":
            None
        case "3":
            None
        case "4":
            registrar_producto()
        case "5":
            editar_producto()
        case "6":
            mostrar_producto()
        case "7":
            exit()
        case _:
            print("opcion invalida...")
            menu_principal()


if __name__ == '__main__':
    menu_principal()
    main()
