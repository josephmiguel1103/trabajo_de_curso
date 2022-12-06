
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return "{};{};{}\n". format(
            self.codigo, self.nombre, self.precio
        )


class Usuario:
    def __init__(self, dni, nombre_apellido, dirrecion, gmail):
        self.dni = dni
        self.nombre_apellido = nombre_apellido
        self.dirreccion = dirrecion
        self.gamil = gmail

    def __str__(self) -> str:
        return "{};{};{};{}\n". format(
            self.dni, self.nombre_apellido, self.dirreccion, self.gamil
        )
