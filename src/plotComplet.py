import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


# Defineix les llistes per emmagatzemar els valors de x i y
x_values = []
y_values = []

# Valors arbre relaxed
x_valuesR = []
y_valuesR = []

# Valors arbre squarish
x_valuesS = []
y_valuesS = []

variances = []

# Create a subplot with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(12, 12), gridspec_kw={'hspace': 0.75})  # Adjust the figure size as needed (fig es tot el conjunt i axs es cada bloc per separat)

# Get the number from the user
numero_dimensio = int(input("Entra el numero de la dimensio del fitxer de dades: ")) 

nom_fitxer1 = f'dadesK{numero_dimensio}.txt'   
nom_fitxer2 = f'dadesK{numero_dimensio}R.txt'
nom_fitxer3 = f'dadesK{numero_dimensio}S.txt'


# Obre el fitxer per llegir
with open(nom_fitxer1, 'r') as file:
    # Llegeix les línies del fitxer
    lines = file.readlines()

    for i in range(0, len(lines), 3):
        x = float(lines[i].strip())
        costos_per_query = list(map(int, lines[i + 1].strip().split()))
        y = float(lines[i + 2].strip())
 
        x_values.append(x)  #afegir al final de la llista
        y_values.append(y)
    
        aux = 0
        for x in costos_per_query:
            aux += pow(x-y, 2)
        variances.append(np.sqrt(aux/499))



# Obre el fitxer Relaxed
with open(nom_fitxer2, 'r') as file:
    # Llegeix les línies del fitxer
    lines = file.readlines()

    for i in range(0, len(lines), 3):
        x = float(lines[i].strip())
        y = float(lines[i + 2].strip())
 
        x_valuesR.append(x)  
        y_valuesR.append(y)

# Obre el fitxer Squarish
with open(nom_fitxer3, 'r') as file:
    # Llegeix les línies del fitxer
    lines = file.readlines()

    for i in range(0, len(lines), 3):
        x = float(lines[i].strip())
        y = float(lines[i + 2].strip())
 
        x_valuesS.append(x) 
        y_valuesS.append(y)



# PLOT 1 ------------------

axs[0, 0].plot(x_values, y_values, label='standard k-d tree', marker='o', linestyle='-')
axs[0, 0].set_title(f'Creixement del cost vs num nodes amb la variància i K={numero_dimensio}')
axs[0, 0].legend()
axs[0, 0].set_xlabel('n (numero nodes arbres)')
axs[0, 0].set_ylabel('Cn (mitjana cost)')  
axs[0, 0].grid(color='black', linestyle='--', linewidth=1, alpha=0.3)



errpos = [] 
errneg = []
for i in range(len(y_values)):
    errpos.append(y_values[i] + variances[i])
    errneg.append(y_values[i] - variances[i])

axs[0, 0].fill_between(x_values, errpos, errneg, color = 'blue', alpha=0.2)

axs[0, 0].set_ylim(0, max(errpos) + 1)


# PLOT 2 ------------------  Tots els tipus de arbres
 # Arbres estandard
# Calcula el logaritme neperia ln als valors de x i y 
ln_x_values = np.log(x_values)  
ln_y_values = np.log(y_values - np.log2(x_values))  


axs[0, 1].plot(ln_x_values, ln_y_values, label='Standard k-d tree', color='blue')
axs[0, 1].set_ylim(0, max(ln_y_values) + 0.6 ) # perque hi hagi un marge a la part superior

slope, intercept, r_value, p_value, std_err = linregress(ln_x_values, ln_y_values)

fitted_line = slope * ln_x_values + intercept

axs[0, 1].plot(ln_x_values, fitted_line, color='r', linestyle='--')
axs[0, 1].set_title(f'Transformació Logarítmica i Regressió Lineal (discontinua)\n K={numero_dimensio}')
axs[0, 1].set_xlabel('ln(n)')
axs[0, 1].set_ylabel('ln(Cn - log2(n))')
axs[0, 1].legend()
axs[0, 1].grid(color='black', linestyle='--', linewidth=1, alpha=0.8)
                                       
regression_eq = f'Equació de la recta Standard: ln(Cn - log2(n)) = {slope:.4f} * ln(n) + b, R-squared = {r_value**2:.4f}'   # valor de la b:  {intercept:.4f} 
axs[0, 1].text(1.70, 1.48, regression_eq, fontsize=10, verticalalignment='center', horizontalalignment='center', transform=axs[1, 0].transAxes, bbox=dict(facecolor='white', alpha=0.8))


 # Arbres Relaxed:
ln_x_valuesR = np.log(x_valuesR) 
ln_y_valuesR = np.log(y_valuesR - np.log2(x_valuesR))  


axs[0, 1].plot(ln_x_valuesR, ln_y_valuesR, label='Relaxed k-d tree', color='orange')
axs[0, 1].legend()

slopeR, interceptR, r_valueR, p_valueR, std_errR = linregress(ln_x_valuesR, ln_y_valuesR)

fitted_lineR = slopeR * ln_x_valuesR + interceptR

axs[0, 1].plot(ln_x_valuesR, fitted_lineR, color='r', linestyle='--')
                                       
regression_eqR = f'Equació de la recta Relaxed: ln(Cn - log2(n)) = {slopeR:.4f} * ln(n) + b, R-squared = {r_valueR**2:.4f}'  
axs[0, 1].text(1.70, 1.33, regression_eqR, fontsize=10, verticalalignment='center', horizontalalignment='center', transform=axs[1, 0].transAxes, bbox=dict(facecolor='white', alpha=0.8))


 # Arbres Squarish:
ln_x_valuesS = np.log(x_valuesS) 
ln_y_valuesS = np.log(y_valuesS - np.log2(x_valuesS))  


axs[0, 1].plot(ln_x_valuesS, ln_y_valuesS, label='Squarish k-d tree', color='green')
axs[0, 1].legend()

slopeS, interceptS, r_valueS, p_valueS, std_errS = linregress(ln_x_valuesS, ln_y_valuesS)

fitted_lineS = slopeS * ln_x_valuesS + interceptS

axs[0, 1].plot(ln_x_valuesS, fitted_lineS, color='r', linestyle='--')
                                       
regression_eqS = f'Equació de la recta Squarish: ln(Cn - log2(n)) = {slopeS:.4f} * ln(n) + b, R-squared = {r_valueS**2:.4f}'  
axs[0, 1].text(1.70, 1.18, regression_eqS, fontsize=10, verticalalignment='center', horizontalalignment='center', transform=axs[1, 0].transAxes, bbox=dict(facecolor='white', alpha=0.8))



# PLOT 3 ------------------


# Fit a logarithmic curve to the data
log_fit_params = np.polyfit(np.log(x_values), y_values, 1)
logarithmic_curve = np.poly1d(log_fit_params)

x_fit = np.linspace(min(x_values), max(x_values), 100)
y_fit = logarithmic_curve(np.log(x_fit))

axs[1, 0].plot(x_values, y_values, label='Standard k-d tree', marker='o', linestyle='-',  color='blue')

# Plot the logarithmic curve fit in the second subplot (axs[1, 0])
axs[1, 0].plot(x_fit, y_fit, color='red')
axs[1, 0].set_title(f'Regressio Logarítmica i K={numero_dimensio}')
axs[1, 0].set_xlabel('n (numero nodes arbres)')
axs[1, 0].set_ylabel('Cn (mitjana cost)')

axs[1, 0].legend()
axs[1, 0].grid(color='black', linestyle='--', linewidth=1, alpha=0.3)

 # extra plot 2, regressio corva logaritmica:
eq_reg_log = f'Equació corva logarítmica: Cn = b * log2(n)' 
axs[1, 0].text(0.5, -0.27, eq_reg_log, fontsize=10, verticalalignment='center', horizontalalignment='center', transform=axs[1, 0].transAxes, bbox=dict(facecolor='white', alpha=0.8))



# Relaxed
log_fit_paramsR = np.polyfit(np.log(x_valuesR), y_valuesR, 1)
logarithmic_curveR = np.poly1d(log_fit_paramsR)

x_fitR = np.linspace(min(x_valuesR), max(x_valuesR), 100)
y_fitR = logarithmic_curveR(np.log(x_fitR))

axs[1, 0].plot(x_valuesR, y_valuesR, label='Relaxed k-d tree', marker='o', linestyle='-',  color='orange')


axs[1, 0].plot(x_fitR, y_fitR, color='red')
axs[1, 0].legend()
axs[1, 0].grid(color='black', linestyle='--', linewidth=1, alpha=0.3)


# Squarish
log_fit_paramsS = np.polyfit(np.log(x_valuesS), y_valuesS, 1)
logarithmic_curveS = np.poly1d(log_fit_paramsS)

x_fitS = np.linspace(min(x_valuesS), max(x_valuesS), 100)
y_fitS = logarithmic_curveS(np.log(x_fitS))

axs[1, 0].plot(x_valuesS, y_valuesS, label='Squarish k-d tree', marker='o', linestyle='-',  color='green')

axs[1, 0].plot(x_fitS, y_fitS, label='Fit Corva Logarítmica', color='red')
axs[1, 0].legend()
axs[1, 0].grid(color='black', linestyle='--', linewidth=1, alpha=0.3)



# PLOT 4 ------------------ 

#veure que les dades tenen una relacio constant
#  dividir les dades originals per n^exponent
x_amb_constant = np.array(x_values) / (np.array(x_values) ** slope) 
y_amb_constant = np.array(y_values) / (np.array(x_values) ** slope)


axs[1, 1].plot(x_amb_constant, y_amb_constant, marker='o', linestyle='-', color='purple')
axs[1, 1].set_xlabel('n / n^constant')
axs[1, 1].set_ylabel('Cn / n^constant')
axs[1, 1].set_title(f'Dades originals dividides per n^{slope:.4f} (la constant)')
# Set the axis limits and equal aspect ratio
axs[1, 1].set_xlim(0, max(x_amb_constant))
axs[1, 1].set_ylim(0, max(y_amb_constant)+max(y_amb_constant))
axs[1, 1].grid(color='black', linestyle='--', linewidth=1, alpha=0.3)


# Mostra la gràfica
plt.show()