
def arearectangulo(largo, ancho):
    operacion = largo * ancho
    return operacion


def areatriangulo(base, altura):
    respuesta = 0.5 * base * altura
    return respuesta

# Función principal
if __name__=="__main__":
    largo=float(input("Introduce el largo del rectangulo: "))
    ancho = float(input("Introduce el ancho del rectangulo: "))
    rect_area = arearectangulo(largo, ancho)
    print(f"el Area del rectangulo es: {largo} *{ancho} = {rect_area}")

    base = float(input("Introduce la base del rectangulo: "))
    altura = float(input("Introduce la altura del rectangulo: "))
    tri_area=areatriangulo(base, altura)
    print(f"Area del triangulo:{0.5} * {base} * {altura} ={tri_area}")