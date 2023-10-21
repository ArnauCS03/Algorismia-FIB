#ifndef RELAXED_HH
#define RELAXED_HH

#include <iostream>
#include <cassert>
#include <vector>
#include <cmath>
#include <utility>

using namespace std;


// Implamentacio d'un arbre k-dimensional binari relaxat on cada node té les coordenades k-dimensionals
class RelaxedKdTree {

    int k; // dimensio

    struct Node {

        int disc;
        
        vector<double> coordenades;

        Node* left;
        Node* right;
    };

    Node* primer_node;  // primer node


    // Allibera espai de tots els nodes de la jerarquia que te el node apuntat per m com a arrel (Fa de destructora)
    static void esborra_node_arbre(Node* & m) {
        if (m != NULL) {
            esborra_node_arbre(m->left);
            esborra_node_arbre(m->right);
            delete m;
        }
    }


public:

    // Constructora: crea un relaxed k-d tree buit
    RelaxedKdTree () {
        primer_node = NULL;
    }
    

    // Constructora d'un arbre relaxed amb un node
    RelaxedKdTree (Node* node) {
        primer_node = node;
    }
    

    // Afegir la dimensio de l'arbre
    void assig_k(int d) {
        this->k = d;
    }


    void insertRec(Node* & current, vector<double> & coords_node, int discrim) {       
        
        if (current == nullptr) {   
            Node* nou_node = new Node;
            nou_node->disc = discrim;
            nou_node->coordenades = coords_node;
            nou_node->left = nullptr;
            nou_node->right = nullptr;
            current = nou_node;
        } 
        // si les coordenades que volem inserir mirant al discriminant son menors, insertir-les al subarbre inforior esquerra
        else if (current->coordenades[current->disc] >= coords_node[current->disc]) {     
            insertRec(current->left, coords_node, rand() % k); 
        } 
        else {        
            insertRec(current->right, coords_node, rand() % k); 
        }
    }

    // Inserir un nou node amb les coordenades k-dimensionals 
    void insert(vector<double> & coords_node) { 
        int d = rand() % k; // primer discriminant aleatori
        insertRec(primer_node, coords_node, d); 
    }


    // Destructora de l'arbre k-dimensional, elimina completament l'arbre
    void borra_arbre() {  
        esborra_node_arbre(primer_node);
    }


    // Retorna true si l'arbre és buit
    bool empty() const { 
        return not primer_node; 
    }


    // Retorna el subarbre esquerra
    RelaxedKdTree left() const {
        assert(not empty());
        return RelaxedKdTree(primer_node->left);
    }

    // Retorna el subarbre dret
    RelaxedKdTree right() const {
        assert(not empty());
        return RelaxedKdTree(primer_node->right);
    }


    // Retorna totes les coordenades del node actual
    vector<double> info() const {
        assert(not empty());
        return primer_node->coordenades;
    }


    // Escriu el contingut del vector separat per espais
    void escriure_vector(vector<double> v) const {
        for (uint i = 0; i < v.size(); ++i) cout << v[i] << " ";
    }


    // Escriu el recorregut en preordre de l'arbre k-dimensional 
    void escriure_arbre() const {
   
        if (not empty()) {
            vector<double> coords = info();
            cout << "(";
            escriure_vector(coords);
            cout << "  [" << primer_node->disc << "] "; // remarcar el discriminant

            RelaxedKdTree a1 = left();
            RelaxedKdTree a2 = right();
            a1.escriure_arbre(); 
            a2.escriure_arbre();
            cout << ")";
        }
    }
    

    // Crea arbre k-dimensional amb n nodes, omplerts amb valors entre 0 i 1 generats aleatoriament
    void generar_arbre(int n) {

        for (int i = 0; i < n; ++i) {
            vector<double> coord(k);
            for (int j = 0; j < k; ++j) {
                double x = double(rand()) / double(RAND_MAX);
                coord[j] = x;
            }
            insert(coord); 
        }
    }


    // Funcio que calcula la distancia euclidiana entre dos coordenades, la retona al quadrat perque es mes eficient que calculant-li l'arrel quadrada
    double distancia(const vector<double> coordenadesNode, const vector<double> coordenadesQ) const { 
        double total = 0.0;

        for (int i = 0; i < k; ++i) {   
            double diferencia = coordenadesNode[i] - coordenadesQ[i];
            total += diferencia * diferencia;  // acumular al total la diferencia de components al quadrat
        }
        return total; // tenim la distancia al quadrat   
    }


    // La variable min te el valor minim provisional d'un punt candidat al punt Q, i les coordanades del candidat. 
    // Al final, conte el valor minim definitiu i les coordenades del punt que es el vei de Q
    void findNeighbour(Node* & current, const vector<double> & coordsQ, pair<double, vector<double>>& min, int& contNod) {
        
        // Hem trobat on aniria el node de Q, o en el backtrack una fulla buida
        if (current == nullptr) return; 

        ++contNod; // augmentem el contador de nodes visitats


        double dist = distancia(coordsQ, current->coordenades); // distancia entre les coords de Q i les del node actual

        // Si la distancia de les coordenades del node actual es menor que la minima trobada fins ara, actualitzar el valor de min
        if (dist < min.first) { 
            min.first = dist;  
            min.second = current->coordenades;  
        }

        
        Node* subarbreQueFaltaExplorar = nullptr;

        // La coord pel discriminant de Q es menor que la del node actual, hauria d'anar cap al subarbre inferior esquerra
        if (coordsQ[current->disc] < current->coordenades[current->disc]) {
            
            subarbreQueFaltaExplorar = current->right; // en el backtrack, encara ens queda aquesta branca per explorar

            findNeighbour(current->left, coordsQ, min, contNod);
        }
        else {

            subarbreQueFaltaExplorar = current->left; // en el backtrack, encara ens queda aquesta branca per explorar

            findNeighbour(current->right, coordsQ, min, contNod);
        }

        // Backtrack
        // Evitant recorrer alguna de les sub branques del node actual. 
        //      Mirant que es compleixi que la distancia entre discriminants del node actual i Q sigui mes petita que la dist minima provisional (estigui dins el radi)
        // Estem anant de les fulles als pares i d'aquests visitant branques no explorades que encara poden contenir distancies mes petites
        

        // distancia nomes entre components del discriminant
        double distDiscriminant = coordsQ[current->disc] - current->coordenades[current->disc];
        // la elevem al quadrat perque treballem amb totes les distances al quadrat
        distDiscriminant *= distDiscriminant;

        // Continuem buscant si estem dins del radi que forma el punt Q amb la minima distancia trobada fins el moment
        if (distDiscriminant < min.first) { 
           
            // Els subarbres del node actual son candidats a tenir la distancia minima, mirar al subarbre que li queda explorar per veure si pot trobar una millor distancia
            //  Buscara a la branca contraria de la que ha baixat en el primer recorregut, començant des de la fulla buida on hipoteticament aniria Q
            //      Exemple: soc un node a un subarbre dret i el meu node pare primer ha baixat per la branca dreta on estic, ara haura de busar per la branca esquerra que li quedava mirar
            findNeighbour(subarbreQueFaltaExplorar, coordsQ, min, contNod);
        }
    }

    // 1r Fer recorregut simulant un insert, i pel cami calcular la distancia minima candidata al punt Q.
    // 2n Backtrack des d'on hauria d'anar Q i anar vistant les altres branques, buscant encara el punt mes proper 
    //    descartant branques gracies a la desigualtat trangular si la distancia no pot millorar-se mes
    void nearestNeighbour(const vector<double>& coordenadesQ, pair<double, vector<double>>& min, int& contNod) { 
        
        findNeighbour(primer_node, coordenadesQ, min, contNod);
    }

};
#endif