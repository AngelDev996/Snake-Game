from turtle import Turtle

POSICIONES_PRINCIPALES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_DE_MOVIMIENTO = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.segmentos = []
        self.crear_serpiente()
        self.cabeza = self.segmentos[0]
    #Funcion que crea la serpiente principal (Se crea con tres segmentos)
    def crear_serpiente(self):
        for posicion in POSICIONES_PRINCIPALES:
            self.anadir_segmento(posicion)
            
    #Funcion que añade mas segmentos 
    def anadir_segmento(self, posicion):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(posicion)
        self.segmentos.append(square)
    
    #Funcion que extiende a la serpiente
    def extender_serpiente(self):
        self.anadir_segmento(self.segmentos[-1].position())
    
    #Funcion que mueve la serpiente de manera contstante
    def mover_serpiente(self):
        for n in range(len(self.segmentos) - 1, 0, -1):
            nueva_coor_x = self.segmentos[n - 1].xcor()
            nueva_coor_y = self.segmentos[n - 1].ycor()
            self.segmentos[n].goto(nueva_coor_x, nueva_coor_y)
        self.cabeza.forward(DISTANCIA_DE_MOVIMIENTO)

    #Mapeo de las teclas arriba, abajo, izquierda, derecha, para controlar la serpiente
    def up(self):
        if self.cabeza.heading() != DOWN:
            self.cabeza.setheading(UP)

    def down(self):
        if self.cabeza.heading() != UP:
            self.cabeza.setheading(DOWN)

    def left(self):
        if self.cabeza.heading() != RIGHT:
            self.cabeza.setheading(LEFT)

    def right(self):
        if self.cabeza.heading() != LEFT:
            self.cabeza.setheading(RIGHT)









