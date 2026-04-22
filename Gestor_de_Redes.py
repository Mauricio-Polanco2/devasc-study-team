import os

def borrar():
    os.system("clear")

sucursales = [
    "Campus Uno", 
    "Campus Matriz", 
    "Zona Core / VPN", 
    "Sector Outsourcing", 
    "Data Center Externo"
]

while True:
    borrar()
    print("==========================================")
    print("   SISTEMA DE GESTION DE RED - INACAP    ")
    print("==========================================")
    print("1. Ver dispositivos por sucursal")
    print("2. Registrar nuevo dispositivo")
    print("3. Listar sucursales activas")
    print("4. Salir")
    
    opcion = input("\nSelecciona una opcion (1-4): ")

    if opcion == "1":
        borrar()
        print("--- SELECCIONE UNA SUCURSAL PARA VER ---")
        for i, sucursal in enumerate(sucursales):
            print(f"{i+1}. {sucursal}")
        
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
                    print("No hay registros guardados para esta sucursal.")
            else:
                print("Ese numero de sucursal no existe.")
        except ValueError:
            print("Error: Debes ingresar un numero.")
        
        input("\nPresiona Enter para volver...")

    elif opcion == "2":
        borrar()
        print("--- REGISTRO DE DISPOSITIVO ---")
        for i, sucursal in enumerate(sucursales):
            print(f"{i+1}. {sucursal}")
            
        try:
            seleccion_suc = input("\n¿A que sucursal pertenece el equipo? (Numero): ")
            indice = int(seleccion_suc) - 1
            
            if 0 <= indice < len(sucursales):
                
                archivo = sucursales[indice].replace(" ", "_").replace("/", "_") + ".txt"
                
                borrar()
                print(f"--- Nueva entrada para: {sucursales[indice]} ---")
                
                
                nombre_equipo = input("- Nombre del dispositivo (ej: R-ORIENTE): ")
                ip_equipo = input("- Direccion IP (ej: 172.16.1.1): ")
                
                print("\nCapa del Modelo Jerarquico:")
                print("1. Nucleo (Core)")
                print("2. Distribucion")
                print("3. Acceso")
                capa_sel = input("- Seleccione capa (1, 2 o 3): ")
                
                if capa_sel == "1":
                    capa_texto = "Nucleo"
                elif capa_sel == "2":
                    capa_texto = "Distribucion"
                else:
                    capa_texto = "Acceso"
                
                vlan = input("- VLANs configuradas (Si no tiene, ponga N/A): ")
                servicios = input("- Servicios de red (ej: VPN, OSPF, DHCP): ")

                
                with open(archivo, "a") as f:
                    f.write(f"Dispositivo: {nombre_equipo}\n")
                    f.write(f"IP: {ip_equipo} | Capa: {capa_texto}\n")
                    f.write(f"VLAN: {vlan} | Servicios: {servicios}\n")
                    f.write("------------------------------------------\n")
                
                print(f"\n¡Exito! Datos guardados en {archivo}")
            else:
                print("Numero de sucursal fuera de rango.")
                
        except ValueError:
            print("\nError: Ingresaste letras en lugar de un numero.")
            
        input("\nPresiona Enter para continuar...")

    elif opcion == "3":
        borrar()
        print("--- SUCURSALES CONFIGURADAS EN EL SISTEMA ---")
        for s in sucursales:
            print(f"-> {s}")
        input("\nPresiona Enter para volver...")

    elif opcion == "4":
        print("Cerrando sistema...")
        break
