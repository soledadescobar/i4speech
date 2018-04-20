# -*- coding: utf-8 -*-
import legibilidad


def c(texto):
    # Muestra la lecturabilidad
    L = legibilidad.fernandez_huerta(texto)
    print(L)
    print(legibilidad.interpretaL(L))
    # Índice de perspicuidad de Szigriszt-Pazos
    P=legibilidad.szigriszt_pazos(texto)
    print(" Índice de perspicuidad de Szigriszt-Pazos:")
    print(P)
    print(legibilidad.interpretaP(P))
    # Interpretación Inflesz
    print("Interpretación Inflesz:")
    print(legibilidad.inflesz(P))
    # Índice de comprensibilidad de Gutiérrez de Polini
    G=legibilidad.gutierrez(texto)
    print(G)
    print(legibilidad.gutierrez_interpret(G))
    # Índice de comprensibilidad de Crawford
    C=legibilidad.crawford(texto)
    print("Años de escolaridad necesarios para la comprensión del texto:")
    print(C)
    # Legibilidad µ
    U=legibilidad.mu(texto)
    print("Legibilidad U:")
    print(U)
    print(legibilidad.mu_interpret(U))
    return 0
