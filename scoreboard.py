from turtle import Turtle
from snake import Snake

from food import Food
PUNTOS = 0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.puntos = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.actualizar_banner()

    def actualizar_banner(self):

        self.write(f"Puntaje = {self.puntos} ", align="center", font=("Arial", 10, "normal"))



    def incrementar_puntaje(self):
        self.puntos += 1
        self.clear()
        self.actualizar_banner()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over ",align= "center" ,font=("Arial", 20, "normal"))
        self.goto(0, -30)
        self.write("Salir (s)  Reiniciar (r)", align="center", font=("Arial", 10, "normal"))










