

def generar_codigo(descripcion):
    descripcion = descripcion.replace(" ","")
    descripcion = descripcion.replace("Nano","NAN")
    descripcion = descripcion.replace("Samsung","SAM")
    descripcion = descripcion.upper()
    codigo = descripcion[:15]
    return codigo

def main():
    descripcion = input("Ingrese la descripcion del producto: ")
    codigo = generar_codigo(descripcion)
    print("El codigo generado es: ", codigo)

main()