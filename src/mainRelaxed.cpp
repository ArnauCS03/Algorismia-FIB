#include "relaxed.hh"

using namespace std;

int main() {

    srand(time(nullptr)); 

    int T = 5;          // num_arbres

    int ni = 5000;      // increment del nombre de nodes 

    int k ;             // dimensio

    // Introduïr la dimensio dels arbres Relaxed
    cin >> k;

    int midaQ = 100;    // num_queries 
    vector<vector<double> > Q(midaQ, vector<double> (k, 0.0));  // 100 punts de k dimensions cada un

    double mitjana_nodes_total = 0.0;

    // Generar uns punts random a buscar
    for (int j = 0; j < midaQ; ++j) {
        for (int p = 0; p < k; ++p) Q[j][p] = double(rand()) / double(RAND_MAX);   
    }

    int num_punts_grafica = 20; // amb la primera iteracio en fem 21 en total

    //bucle on fem 100 querris en 5 arbres diferents per cada mida 
    for (int m = 0; m <= num_punts_grafica; ++m) {
        
        int n;          // nombre de nodes de l'arbre actual
        if (m == 0) n = 500;
        else n = ni * m;

        cout << n << endl;

        mitjana_nodes_total = 0.0;

        for (int i = 0; i < T; ++i) {

            RelaxedKdTree a;
            a.assig_k(k);
        
            a.generar_arbre(n);

            double mitjana_nodes_queries = 0.0;

            int contNodesVisitats = 0;
            
            for (int z = 0; z < midaQ; ++z) {

                // Distancia minima provisional d'un punt candidat al punt Q, i les coordanades del candidat
                pair<double, vector<double>> min = make_pair(100, vector<double>(k));    

                a.nearestNeighbour(Q[z], min, contNodesVisitats);

                cout << contNodesVisitats << " ";

                mitjana_nodes_queries += contNodesVisitats;

                contNodesVisitats = 0;
            }

            double mitjana_nodes_arbre = mitjana_nodes_queries/midaQ;

            mitjana_nodes_total += mitjana_nodes_arbre;

            a.borra_arbre();
        }

        double mitjanaTotal = mitjana_nodes_total/T;
        cout << endl << mitjanaTotal << endl;
    }
}