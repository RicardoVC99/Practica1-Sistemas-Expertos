# -*- coding: utf-8 -*-
# -----------------------------------------------------------
class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der
        
         
    def __str__(self):
        return str(self.carga)
 
# -----------------------------------------------------------
 
def si(preg):
    resp = input(preg)
    return (resp == 'si')
 
# -----------------------------------------------------------
 
def main():
    bucle = True

    subARBOL1_1 = Arbol(("Es un super sayayin"),Arbol("Goku"),Arbol("Piccolo"))
    subARBOL1_2 = Arbol(("Pelea"),Arbol("Krillin"),Arbol("Bulma"))
    
    subARBOL1 = Arbol(("Es un Alienigena"),subARBOL1_1,subARBOL1_2)

    subARBOL2_1 = Arbol(("Tiene cabello Amarillo"),Arbol("Naruto"),Arbol("Sasuke"))
    subARBOL2_2 = Arbol(("Es de Shingeky"),Arbol("Eren"),Arbol("El Chapulin Colorado"))
    
    subARBOL2 = Arbol(("Es de naruto"),subARBOL2_1,subARBOL2_2)

    raiz = Arbol(("Es un personaje de Dragon Ball"),subARBOL1,subARBOL2)

    while bucle:
        arbol = raiz
        while arbol.izquierda != None:
            if si(arbol.carga + "? "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha
         
        #adivinar
        personaje = arbol.carga
        if si("Es " + personaje + "? "):
            print("Logre Adivinarlo!!")
            continue
         
        #obtener informacion
        nuevo = input("Qué personaje era? ")
        info = input("Qué diferencia a " + personaje + " de " + nuevo + "? ")
        indicador = "Si el personaje fuera " + personaje + " cual seria la respuesta? "
        arbol.carga = info
        if si(indicador):
            arbol.izquierda = Arbol(personaje)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(personaje)
            arbol.izquierda = Arbol(nuevo)
 
    return 0
 
if __name__ == '__main__':
    main()