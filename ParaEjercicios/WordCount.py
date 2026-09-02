from Emulador import Job
from datetime import date

inputDir = "C:/Users/Mar/Desktop/PracticaBigData/Data/Inversionistas"
outputDir = "C:/Users/Mar/Desktop/PracticaBigData/Output/"

## El nombre del inversionista más joven 
## El total del importe invertido por todos los inversionistas 
## El promedio de edad 

def calcularMinimo(inversionista, edad, nombre, nuevaEdad):
    if(nuevaEdad<edad):
        edad= nuevaEdad
        inversionista= nombre
    return inversionista, edad

def CalcularEdad(year , month, day):
    hoy = date.today()
    edad = hoy.year - year - ((hoy.month, hoy.day) < (month, day))
    return edad

def fmap(key, value, context):
    words = value.split()
    nombre= words[0]
    anio= int(words[3])
    mes= int(words[2])
    dia= int(words[1])
    aporte= float(words[4])
    context.write("GLOBAL", (nombre, anio, mes, dia, aporte))
        
def fred(key, values, context):
    totalAportes=0
    cantidadInversionistas=0
    edades=0
    inversionistaMasJoven=""
    edadMasJoven=100
    for v in values:
        cantidadInversionistas+=1
        totalAportes+=v[4]
        edadAux= CalcularEdad(v[1], v[2], v[3])
        edades+= edadAux
        inversionistaMasJoven, edadMasJoven = calcularMinimo(inversionistaMasJoven, edadMasJoven, v[0], edadAux)

    promedio=edades/cantidadInversionistas
    context.write(key, ("Inversionista más joven: "+inversionistaMasJoven, "Total aportes: "+str(totalAportes), "Promedio de edad: "+str(promedio)))


job = Job(inputDir, outputDir, fmap, fred)
success = job.waitForCompletion()
