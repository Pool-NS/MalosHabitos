def calcular(valor1, valor2, valor3):
    operacion = valor1 * valor2 + valor3
    return operacion

def principal():
    multiplicando = float(input("multiplicando: "))
    multiplicador = float(input("multiplicador: "))
    sumando = float(input("sumando: "))
    resultado = calcular(multiplicando, multiplicador, sumando)
    print(f" el resultado de :{multiplicando} * {multiplicador} + {sumando}  es := {resultado}")
    

principal()
