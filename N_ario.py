# IMPLEMENTACIÓN DE UN ÁRBOL N-ARIO
print("\nIMPLEMENTACIÓN DE UN ÁRBOL N-ARIO")
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.hijos = []

    def insertarHijo(self,dato):
        hijo = Nodo(dato)
        self.hijos.append(hijo)

    def imprime(self):
        print(f"Mi dato es: {self.dato}")

    def imprimeHijos(self):
        print("Y mis hijos son: ")
        for h in self.hijos:
            h.imprime()

    def imprimeArbol(self):
        self.imprime()
        if self.hijos != None:
            print("Y mi descendencia es: ")
            for h in self.hijos:
                h.imprimeArbol()
        else:
            print("No tengo descendencia")

    def buscarDato(self,dato):
        if self.dato == dato:
            return self
        for h in self.hijos:
            respuesta = h.buscarDato(dato)
            if respuesta != None:
                return respuesta
        return None

    def insertaEn(self,dato,padre):
        papa = self.buscarDato(padre)
        if papa != None:
            papa.insertarHijo(dato)
            return True
        else:
            print("Ese padre se dio a la fuga")
            return False

n = Nodo("Carlos")
n.insertarHijo("Aldo")
n.insertarHijo("Adolfo")
n.imprimeArbol()
n.imprime()
print("Los hijos son:")
n.insertaEn("Isaí","Adolfo")
n.hijos[0].imprime()
n.hijos[1].imprime()

n.imprimeArbol()