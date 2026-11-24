"""#EJERCICIO 1 - IMPORTACION MODULS
Disposem de les edats d'un grup de persones:
edats = [25, 30, 22, 35, 28, 30, 40, 27, 30, 24]

Utilitzant el mòdul statistics de Python:
1. Calcula la mitjana de les edats.
2. Calcula la mediana.
3. Identifica la moda.
4. Calcula la desviació estàndard mostral.
5. Mostra els resultats amb dos decimals.

#EJERCICIO 2 - CREACIÓN DE UN MODULO
1. Crea un fitxer anomenat estadistiques.py.
2. Implementa les funcions següents:
   - calcular_mitjana(dades): retorna la mitjana d'una llista.
   - calcular_maxim(dades): retorna el valor màxim.
3. Crea un segon fitxer anomenat main.py.
4. Importa les funcions del mòdul estadistiques.
5. Aplica-les al conjunt de dades següent:
dades = [10, 20, 30, 40, 50, 60, 70]
6. Mostra els resultats obtinguts.

#EJERCICIO 3 - LECTURA DE sales_data.csv Y ESCRITURA en un nuevo archivo 
# con una nueva columna con el cálculo TOTAL = importe * cantidad """


# EJERCICIO 1 - IMPORTACION MODULS
import statistics
edats = [25, 30, 22, 35, 28, 30, 40, 27, 30, 24]

MEDIANA = statistics.mean(edats)
MEDIANA = statistics.median(edats)
MODA = statistics.mode(edats)
DESVIACIO = statistics.stdev(edats)

print(f"Mitjana: {MEDIANA:.2f}")
print(f"Mediana: {MEDIANA:.2f}")
print(f"Moda: {MODA:.2f}")
print(f"Desviació estàndard: {DESVIACIO:.2f}")  

# EJERCICIO 2 - CREACIÓN DE UN MODULO

