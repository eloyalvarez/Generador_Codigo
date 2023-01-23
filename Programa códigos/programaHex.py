import hashlib

def generar_hash(descripcion):
    hash_object = hashlib.sha256()
    hash_object.update(descripcion.encode())
    return hash_object.hexdigest()

def generar_codigo(hash_hex):
# Eliminar caracteres no deseados
    hash_hex = hash_hex.replace("a", "")
    hash_hex = hash_hex.replace("b", "")
    hash_hex = hash_hex.replace("c", "")
    # Convertir a mayusculas
    hash_hex = hash_hex.upper()
    # Tomar solo los primeros 8 caracteres
    codigo = hash_hex[:8]
    return codigo

def main():
    descripcion = input("Ingrese la descripcion del producto: ")
    hash_hex = generar_hash(descripcion)
    codigo = generar_codigo(hash_hex)
    print("El codigo generado es: ", codigo)

main()