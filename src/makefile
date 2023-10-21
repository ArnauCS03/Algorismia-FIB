mainEstandar: mainEstandar.cpp arbre.hh
	g++ -o mainEstandar.exe mainEstandar.cpp arbre.hh

mainRelaxed: mainRelaxed.cpp relaxed.hh
	g++ -o mainRelaxed.exe mainRelaxed.cpp relaxed.hh

mainSquarish: mainSquarish.cpp squarish.hh
	g++ -o mainSquarish.exe mainSquarish.cpp squarish.hh


mains: mainEstandar mainRelaxed mainSquarish



# no elimina els .exe dels python scipt (ja venen compilats independentment)
clean:
	rm -f *.o
	rm -f mainEstandar.exe mainRelaxed.exe mainSquarish.exe
