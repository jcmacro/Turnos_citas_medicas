# Juan Carlos Macias 6to. nivel TICs UTM
# Practica 1: Sistema de turnos médicos

# La cola de pacientes representada en forma de lista
cola_pacientes = []

# Se define la función agregar_paciente para ponerlos al final de la cola
def agregar_paciente():
    nombre= input("Ingrese el nombre del paciente: ")
    edad= int(input("Ingrese la edad del paciente: "))
    especialidad= input("Ingrese el especialidad del paciente: ")
    paciente = (nombre, edad, especialidad) # La variable pacienta guarda la informacion
    cola_pacientes.append(paciente)  #Se van agregando pacientes en la lista
    print(f"Paciente agregado: {paciente}") #Muestra en consola los datos del paciente

# Se define la función para atender al primer paciente en la cola
def atender_paciente():
    if cola_pacientes:
        paciente = cola_pacientes.pop(0) #Selecciona al primer paciente
        print(f"Atendiendo a: {paciente}") # Muestra al paciente que se esta atendiendo
    else:
        print("No hay pacientes en espera.") #En caso de que no haya ningun paciente en espera

# Se define la función para mostrar todos los pacientes en espera
def mostrar_pacientes():
    if cola_pacientes:
        print("Pacientes en espera:") #Muestra a los pacientes espera, ya no a los que han sido atendidos
        for i, paciente in enumerate(cola_pacientes, start=1):
            print(f"{i}. Nombre: {paciente[0]}, Edad: {paciente[1]}, Especialidad: {paciente[2]}")
    else:
        print("No hay pacientes en la cola.")

# Secuencia de la atencion con las funciones
#Primer paciente
agregar_paciente()
# Segundo paciente
agregar_paciente()
#Muestra al primer paciente en atencion
atender_paciente()
#Muestra al paciente que esta en espera
mostrar_pacientes()
# Agrega un nuevo paciente
agregar_paciente()
# Muestra al paciente que estaba esperando y ahora esta siendo atendido
atender_paciente()
# Muestra al paciente en espéra de atencion
mostrar_pacientes()
# Muestra al paciente que estaba esperando y ahora esta siendo atendido
atender_paciente()
# Muestra al paciente en espéra de atencion
mostrar_pacientes()