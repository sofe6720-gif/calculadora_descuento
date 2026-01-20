calculadora_descuento.py
def aplicar_descuento(precio, descuento):
    precio_final = precio - (precio * descuento / 100)
    return precio_final


def calcular_descuento():
    precio_original = float(input("Ingrese el precio original del producto: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

    precio_final = aplicar_descuento(precio_original, porcentaje_descuento)

    def mostrar_resultado(monto_final):
        print("El monto final a pagar después del descuento es:", monto_final)

    mostrar_resultado(precio_final)


calcular_descuento()
