public class Nodo {
    int valor;
    Nodo izquierda;
    Nodo derecha;

    public Nodo(int valor) {
        this.valor = valor;
        izquierda = null;
        derecha = null;
    }
}

public class ArbolBinario {
    Nodo raiz;

    public ArbolBinario() {
        raiz = null;
    }

    public boolean vacio() {
        return raiz == null;
    }

    public void insertar(int valor) {
        if (vacio()) {
            raiz = new Nodo(valor);
        } else {
            insertarNodo(valor, raiz);
        }
    }

    private void insertarNodo(int valor, Nodo nodoActual) {
        if (valor < nodoActual.valor) {
            if (nodoActual.izquierda == null) {
                nodoActual.izquierda = new Nodo(valor);
            } else {
                insertarNodo(valor, nodoActual.izquierda);
            }
        } else if (valor > nodoActual.valor) {
            if (nodoActual.derecha == null) {
                nodoActual.derecha = new Nodo(valor);
            } else {
                insertarNodo(valor, nodoActual.derecha);
            }
        }
    }

    public void imprimirArbol() {
        imprimir(raiz);
    }

    private void imprimir(Nodo nodoActual) {
        if (nodoActual != null) {
            imprimir(nodoActual.izquierda);
            System.out.print(nodoActual.valor + " ");
            imprimir(nodoActual.derecha);
        }
    }

    public static void main(String[] args) {
        ArbolBinario arbol = new ArbolBinario();
        System.out.println(arbol.vacio());
        arbol.insertar(5);
        arbol.insertar(10);
        arbol.insertar(12);
        arbol.insertar(3);
        arbol.insertar(1);
        arbol.imprimirArbol();
    }
}
