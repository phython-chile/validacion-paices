def _comprueba_cuit(cuit):
    cuit = str(cuit)
    # Aca removemos guiones, espacios y puntos para poder trabajar
    cuit = cuit.replace("-", "") # Borramos los guiones
    cuit = cuit.replace(" ", "") # Borramos los espacios
    cuit = cuit.replace(".", "") # Borramos los puntos
    # Si no tiene 11 caracteres lo descartamos
    if len(cuit) != 11:
        return False, cuit
    # Solo resta analizar si todos los caracteres son numeros
    if not cuit.isdigit():
        return False, cuit
    # Despues de estas validaciones podemos afirmar
    #   que contamos con 11 numeros
    # Aca comienza la magia
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    aux = 0
    for i in xrange(10):
        aux += int(cuit[i]) * base[i]
    aux = 11 - (aux % 11)
    if aux == 11:
        aux = 0
    elif aux == 10:
        aux = 9
    if int(cuit[10]) == aux:
        return True, cuit
    else:
        return False, cuit

print _comprueba_cuit("20267565393")
