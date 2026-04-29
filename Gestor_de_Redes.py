import os

def borrar():
    os.system("clear")


ARCHIVO_SUCURSALES = "lista_sucursales.txt"

def cargar_sucursales():
   
    if not os.path.exists(ARCHIVO_SUCURSALES):
        lista_base = ["Campus Uno", "Campus Matriz", "Zona Core / VPN", "Sector Outsourcing", "Data Center Externo"]
        guardar_sucursales(lista_base)
        return lista_base

    with open(ARCHIVO_SUCURSALES, "r") as f:
        return [linea.strip() for linea in f.readlines()]

def guardar_sucursales(lista):
    with open(ARCHIVO_SUCURSALES, "w") as f:
        for s in lista:
            f.write(s + "\n")

sucursales = cargar_sucursales()

while True:
    borrar()
    print("==========================================")
    print("   SISTEMA DE GESTION DE RED PRO - INACAP ")
    print("==========================================")
    print("1. Ver dispositivos por sucursal")
    print("2. Registrar nuevo dispositivo")
    print("3. AGREGAR NUEVA SUCURSAL / CAMPUS")
    print("4. Listar todas las sucursales")
    print("5. Salir")
    
    opcion = input("\nSelecciona una opcion (1-5): ")

    if opcion == "1":
        borrar()
        print("--- SELECCIONE UNA SUCURSAL PARA VER ---")
        for i, s in enumerate(sucursales):
            print(f"{i+1}. {s}")
        
        try:
            sel = input("\nNumero de sucursal: ")
            indice = int(sel) - 1
            if 0 <= indice < len(sucursales):
                nombre_archivo = sucursales[indice].replace(" ", "_").replace("/", "_") + ".txt"
                borrar()
                print(f"--- DISPOSITIVOS EN {sucursales[indice].upper()} ---")
                if os.path.exists(nombre_archivo):
                    with open(nombre_archivo, "r") as f:
                        print(f.read())
                else:
                    print("No hay registros en esta sucursal.")
            else:
                print("Numero no valido.")
        except:
            print("Error en la seleccion.")
        input("\nPresiona Enter...")

    elif opcion == "2":
        borrar()
        print("--- REGISTRO DE DISPOSITIVO ---")
        for i, s in enumerate(sucursales):
            print(f"{i+1}. {s}")
            
        try:
            sel = input("\n¿A que sucursal pertenece? (Numero): ")
            indice = int(sel) - 1
            if 0 <= indice < len(sucursales):
                archivo = sucursales[indice].replace(" ", "_").replace("/", "_") + ".txt"
                borrar()
                print(f"--- Nueva entrada para: {sucursales[indice]} ---")
                
                nombre = input("- Nombre del dispositivo: ")
                ip = input("- Direccion IP: ")
                print("\n1. Nucleo | 2. Distribucion | 3. Acceso")
                c_sel = input("- Capa (1-3): ")
                capa = "Nucleo" if c_sel=="1" else "Distribucion" if c_sel=="2" else "Acceso"
                vlan = input("- VLANs: ")
                serv = input("- Servicios: ")

                with open(archivo, "a") as f:
                    f.write(f"Dispositivo: {nombre}\nIP: {ip} | Capa: {capa}\nVLAN: {vlan} | Servicios: {serv}\n")
                    f.write("------------------------------------------\n")
                print(f"\n¡Guardado en {archivo}!")
        except:
            print("Error al ingresar datos.")
        input("\nPresiona Enter...")

    elif opcion == "3":
        borrar()
        print("--- IMPLEMENTAR NUEVA SUCURSAL / CAMPUS ---")
        nueva = input("Nombre de la nueva sucursal (ej: Campus Maipu): ")
        if nueva.strip():
            sucursales.append(nueva)
            guardar_sucursales(sucursales)
            print(f"\n¡Sucursal '{nueva}' implementada con exito!")
        else:
            print("Nombre no valido.")
        input("\nPresiona Enter...")

    elif opcion == "4":
        borrar()
        print("--- SUCURSALES ACTUALES ---")
        for s in sucursales:
            print(f"-> {s}")
        input("\nPresiona Enter...")

    elif opcion == "5":
        print("Saliendo...")
        break
