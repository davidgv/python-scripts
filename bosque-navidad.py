# Bosque navideño usando módulo turtle (Logo)

import turtle
import random
import time

turtle.setup(800, 800, 0, 0)
turtle.title("Bosque navideño usando módulo turtle (Logo)")

def pinta_arbol(x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  # hojas
  turtle.fillcolor("green")
  turtle.begin_fill()
  turtle.goto(x+100, y)
  turtle.goto(x, y+200)
  turtle.goto(x-100, y)
  turtle.goto(x, y)
  turtle.end_fill()
  # tronco
  turtle.fillcolor("brown")
  turtle.begin_fill()
  turtle.goto(x+10, y)
  turtle.goto(x+10, y-50)
  turtle.goto(x-10, y-50)
  turtle.goto(x-10, y)
  turtle.goto(x, y)
  turtle.end_fill()

for i in range(12):
  alea_x = random.randint(-400, 400)
  alea_y = random.randint(-400, 400)
  pinta_arbol(alea_x, alea_y)

time.sleep(3) # segundos de pausa antes de salir
