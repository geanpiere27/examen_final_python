"""
crear un diccionario que tenga dos registros de un alumno
1. crear una funcion que me imprima los registro,
2. crear una funcion que me permita editar uno de los campos del registro
"""
alumnos = {
    "nombre": "Juan",
    "apellido":"altamirano",
    "edad": 20,
    "carrera": "Enfermeria Informática"
    ,
    "nombre": "jose",
    "apellido":"gonzales",
    "edad":21,
    "carrera":"ASTIP"
}
def imprimir_alumnos(alumnos):
    print("Registro del alumno:")
    for clave, valor in alumnos.items():
        print(f"{clave}: {valor}")
def editar_registro(alumnos, edad, nuevo_valor):
    if edad in alumnos:
        alumnos[edad] = nuevo_valor
        print(f"apellido '{edad}' actualizado correctamente.")
    else:
        print(f"El campo '{edad}' no existe en el registro del alumno.")
print("Registro inicial del alumno:")
imprimir_alumnos(alumnos)
campo_a_editar = 'edad'
nuevo_valor = 30
editar_registro(alumnos, campo_a_editar, nuevo_valor)
print("\nRegistro actualizado del alumno:")
imprimir_alumnos(alumnos)
