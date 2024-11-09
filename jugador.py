

import random


class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0

    def atacar(self):
        return random.randint(10,20) * self.nivel
    
    def recibir_dano(self, dano):
        self.salud = self.salud - dano
        print(f"Te quedan {self.salud} puntos de salud")
        if (self.salud) <= 0:
            print("Game Over")
    
    def ganar_experiencia(self, experiencia):
        self.experiencia = self.experiencia + experiencia
        print(f"{self.nombre} has ganado {experiencia} puntos de experiencia!!")
        if self.experiencia >= 100:
            self.nivel = self.nivel + 1
            self.experiencia = 0
            print(f"{self.nombre} ha subido de nivel a {self.nivel}")