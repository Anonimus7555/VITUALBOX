suma = 0
print("----------------------EVALUACION DE TRABAJOS--------------------------")

print("---------------ALUMNOS A EVALUAR-------------------- ")

lista = ("Marco Pisco", f"{22} años", "Ingenieria Sistemas" )
print(lista)

lista2 = ("Marcelo Moreno", f"{21} años", "Ingenieria Electronica" )
print(lista2)

lista3 = ("Carlos Morales", f"{25} años", "Derecho" )
print(lista3)

print("CUANTAS TAREAS VA A PRESENTAR( SON 5 TAREAS EN TOTAL)")

numero = int(input("Tareas a presentar: "))
while numero > 5:
    print("SOLO SE DEJARON 5 TAREAS OE MONGOL!!!!!!!!")
    numero = int(input("Tareas a presentar: "))

for i in range(1, numero + 1):
    nota = int(input(f"Tarea {i}: "))
    while nota > 20:
        print("LA NOTA SE EVALUA DESDE (0 - 20) OE MONGOL")
        nota = int(input(f"Tarea {i}: "))
    suma = suma + nota
    
print(f"LA SUMA DE SUS NOTAS ES DE: {suma}")
    
prom = suma / 5

print(f"SU PROMEDIO FINAL DEL CURSO ES DE: {prom}")
    
if prom >= 14 :
    print("FELICITACIONES, OBTUVO SU CERTIFICADO!!!!!!!!!!!!!!!")

else :
    print("VETE A SUSTITUTORIO NOMAS CALICHIN ")


