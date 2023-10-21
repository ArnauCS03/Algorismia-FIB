import matplotlib.pyplot as plt
import numpy as np

#------------------K2------------------
# Obrir l'arxiu en mode lectura
with open("dadesK2.txt", "r") as file:
    lines = file.readlines()

index = 0

# Bucle lectura

x_valuesK2 = []
y_valuesK2 = []
variancesK2 = []
while index < len(lines):
    # Llegir el valor de N y convertir-lo a enter
    N = int(lines[index].strip())
    index += 1


    # Llegir els 500 números enters i posar-los a una llista
    # Son 500 queries en total (de 5 arbres), cada query amb el seu cost.
    costos_per_query = list(map(int, lines[index].strip().split()))
    index += 1 

    # Llegir el valor de M y convertir-lo a enter
    M = float(lines[index].strip())
    index += 1 
    
    aux = 0
    for x in costos_per_query:
        aux += pow(x-M,2)

    x_valuesK2.append(N)
    y_valuesK2.append(M)
    variancesK2.append(np.sqrt(aux/499))

# Fi bucle

#------------------K3------------------

with open("dadesK3.txt", "r") as file:
    lines = file.readlines()

index = 0

x_valuesK3 = []
y_valuesK3 = []
variancesK3 = []
while index < len(lines):
    N = int(lines[index].strip())
    index += 1

    costos_per_query = list(map(int, lines[index].strip().split()))
    index += 1

    M = float(lines[index].strip())
    index += 1
    
    aux = 0
    for x in costos_per_query:
        aux += pow(x-M,2)

    x_valuesK3.append(N)
    y_valuesK3.append(M)
    variancesK3.append(np.sqrt(aux/499))

#------------------K4------------------

with open("dadesK4.txt", "r") as file:
    lines = file.readlines()

index = 0

x_valuesK4 = []
y_valuesK4 = []
variancesK4 = []
while index < len(lines):
    N = int(lines[index].strip())
    index += 1

    costos_per_query = list(map(int, lines[index].strip().split()))
    index += 1 

    M = float(lines[index].strip())
    index += 1 
    
    aux = 0
    for x in costos_per_query:
        aux += pow(x-M,2)

    x_valuesK4.append(N)
    y_valuesK4.append(M)
    variancesK4.append(np.sqrt(aux/499))

#------------------K5------------------

with open("dadesK5.txt", "r") as file:
    lines = file.readlines()

index = 0

x_valuesK5 = []
y_valuesK5 = []
variancesK5 = [] 
while index < len(lines):
    N = int(lines[index].strip())
    index += 1 

    costos_per_query = list(map(int, lines[index].strip().split()))
    index += 1

    M = float(lines[index].strip())
    index += 1
    
    aux = 0
    for x in costos_per_query:
        aux += pow(x-M,2)

    x_valuesK5.append(N)
    y_valuesK5.append(M)
    variancesK5.append(np.sqrt(aux/499))

#------------------K6------------------

with open("dadesK6.txt", "r") as file:
    lines = file.readlines()

index = 0

x_valuesK6 = []
y_valuesK6 = []
variancesK6 = [] 
while index < len(lines):
    N = int(lines[index].strip())
    index += 1 

    costos_per_query = list(map(int, lines[index].strip().split()))
    index += 1 

    M = float(lines[index].strip())
    index += 1 
    
    aux = 0
    for x in costos_per_query:
        aux += pow(x-M,2)

    x_valuesK6.append(N)
    y_valuesK6.append(M)
    variancesK6.append(np.sqrt(aux/499))

#----------------------------------------------------

#Crear gràfica
plt.grid(color='black', linestyle='--', linewidth=1, alpha=0.3)

plt.plot(x_valuesK2, y_valuesK2, marker = 'o', linestyle = '-')
plt.plot(x_valuesK3, y_valuesK3, marker = 'o', linestyle = '-')
plt.plot(x_valuesK4, y_valuesK4, marker = 'o', linestyle = '-')
plt.plot(x_valuesK5, y_valuesK5, marker = 'o', linestyle = '-')
plt.plot(x_valuesK6, y_valuesK6, marker = 'o', linestyle = '-')

plt.legend(['k = 2','k = 3', 'k = 4', 'k = 5', 'k = 6'])

plt.ylim(0)

# Títols
plt.title('Gràfica del cost segons k')
plt.xlabel('nodes de l\'arbre')
plt.ylabel('nodes visitats')

# Mostra la gràfica
plt.show()
