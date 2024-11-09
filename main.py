
import random
from jugador import Jugador
from enemigo import Enemigo



def main():
    nombre_jugador = input("Ingrese nombre: ")
    jugador = Jugador(nombre_jugador) #Aca ya directamente llamamos a la instancia de Jugador


    enemigos = [
        Enemigo("Alien",50,10),
        Enemigo("Simio",15,30),
        Enemigo("Mounstro",10,10)
    ]

    enemigos_derrotados = []

    print("Comienza la aventura")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue #Lo hacemos saltearse todo lo de abajo, que no lo haga, que vuelve a hacer la pregunta del if
        print(f"Te encuentras con un {enemigo_actual.nombre}, debes pelear con el")

        while enemigo_actual.salud > 0:
            accion = input(" Que deseas hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de daño")
                enemigo_actual.recibir_dano(dano_jugador)
                jugador.ganar_experiencia(2)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"El {enemigo_actual.nombre} te atacó y te causo {dano_enemigo}")
                    jugador.recibir_dano(dano_enemigo)

                elif enemigo_actual.salud <=0:
                    enemigos_derrotados.append(enemigo_actual)
                    enemigos.remove(enemigo_actual)
                    print(f"Has destrozado a pedazos a {enemigo_actual.nombre}, ve por los demas mientras puedas")
    
            elif accion == "huir":
                print("Has decidido huir del combate, soldado que huye sirve para otra guerra dice el dicho")
                break
        if jugador.salud <= 0:
            print("Perdiste")
            break
        
        continuar = input("Quieres seguir explorando (s/n): ")

        if continuar != "s":
            print("Gracias por haber jugado")
            break

    if not enemigos:
        print("Felicidades no te queda ninguna por destruir")

if __name__ == "__main__":
    main()
