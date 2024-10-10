#Variables globales
host = ""
path = ""
#Funciones
def run(smb_path: str) -> tuple:
    # TODO
    global host, path
    #Variable local
    host = smb_path[2:15]
    path= smb_path[15:]

    #Otra forma de hacerlos es:
    # ruta = smb_path.strip("/")
    # ruta = smb_path.lstrip("/") te elimina la de las izquierda

    # caracter = ruta.find("/")
    return host, path

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(host)
    print(path)