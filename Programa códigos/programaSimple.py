import hashlib

def generar_codigo(descripcion):
    descripcion = descripcion.upper()
    descripcion = descripcion.replace(" ","")
    codigo = descripcion[:12]
    return codigo

def main():
    descripcion = input("Ingrese la descripcion del producto: ")
    codigo = generar_codigo(descripcion)
    print("El codigo generado es: ", codigo)

main()