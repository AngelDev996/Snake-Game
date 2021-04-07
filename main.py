from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.tracer(0)
pantalla.title("Juego de la serpiente")

record = Scoreboard()
snake = Snake()
food = Food()

pantalla.listen()
pantalla.onkey(snake.up, "Up")
pantalla.onkey(snake.down, "Down")
pantalla.onkey(snake.left, "Left")
pantalla.onkey(snake.right, "Right")

juego_On = True

while juego_On:
    pantalla.update()
    time.sleep(0.1)
    snake.mover_serpiente()

    #Detectar colision con la comida
    if snake.cabeza.distance(food) < 15:
        food.new_food_location()
        record.incrementar_puntaje()
        snake.extender_serpiente()
    if snake.cabeza.xcor() > 280 or snake.cabeza.ycor() > 280 or snake.cabeza.xcor() < -280 or snake.cabeza.ycor() < -280:
        record.game_over()
        juego_On = False

    for segmento in snake.segmentos[1:]: #Aplicando slicing al arreglo (se evade el primer elemento con esta notacion, y hay muchas mas)
        if snake.cabeza.distance(segmento) < 10:
            record.game_over()
            juego_On = False









pantalla.exitonclick()
