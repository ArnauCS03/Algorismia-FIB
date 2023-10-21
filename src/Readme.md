Projecte d'Algorisimia: Consulta pel vei mes proper en arbres k-dimensionals aleatoris
Creadors: Arnau Claramunt, Ferriol Falip, Giancarlo Morales, Marti Puerta
18/10/2023

===============================================================================================================================================

Instruccions de com generar i executar els fitxers de la practica i una breu descripcio dels fitxers


Els tres tipus d'arbres estan implementats per separat en fitxers .hh i cada tipus d'arbre te el seu propi programa principal .cpp


Per compilar els fitxers principals:

$ make mainEstandar
$ make mainRelaxed
$ make mainSquarish

(cada main, conte la creacio dels T arbres d'un tipus concret, amb la Q, la n, el contador de nodes visitats i fa cout de les dades)

Tots de cop:
$ make mains



Per executar el fitxer mainEstandar.exe:
$ ./mainEstandar.exe
  (i a més a més introduïr el numero de la dimensió k quan ha començat a executar-se)
   
    Per guardar els resultats experimentals dels costos, redirigir la sortida a un fitxer de text:
$ ./mainEstandar.exe > dadesK2.txt 
  (i introduïr la dimensio)



Un cop les dades ja estan recollides als fitxers dadesK...txt aquestes estan en format: (hi ha un total de 15 fitxers de dades ja recollides)

  Exemple de 3 línies del fitxer:

    500 		        // (número de nodes dels arbres)
    21 17 .... 14   // (500 valors separats per espais, que son el cost mitjà obtingut de cada una de les 100 queries fetes en 5 arbres)
    18.985		      // (cost mitjà)



Per tractar i graficar les dades s'utilitzen 2 python scripts, cada un amb el seu executable ja generat independentment, perque es puguin 
executar sense intpret i sense tenir instalades les dependencies de les llibreries.

compararKs.py:
  Grafica del creixement del cost mitja respecte el nombre de nodes per cada k en els arbres estandar.

  Per executar:
  $ ./compararKs.exe

plotComplet.py:
  4 gràfiques en un requadre 2x2 com una matriu. A la posicio [0][0] hi ha la grafica Cn vs n amb la variancia dels arbres estandar.
  Al [0][1] la tranformacio logaritmica a les dades i la regressio lineal als tres tipus d'arbres.
  Al [1][0] la regressio logaritmica als tres tipus d'arbres.
  Al [1][0] dividir les dades per n^exponent per veure que la relacio es constant, nomes amb els arbres estandar.

  Per executar:
  $ ./plotComplet.exe
  (un cop executat, esperar uns 10 segons a que carregui Matplotlib i introduir el numero de la dimensio de les dades que es vol mirar, 
  apareix un missatge per pantalla demanant a l'usuari la k)
