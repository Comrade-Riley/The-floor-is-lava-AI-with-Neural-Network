cy = 400
y = 4
import pygame
from pygame import *
import time
import os
import numpy as np
from numpy import exp, array, random, dot
#The input of the sets the AI trains with
training_set_inputs = array([[4, 0, 0], [2, 0, 0], [5, 0, 0], [3, 0, 0]])
#The output of the sets the AI trains with
training_set_outputs = array([[1, 0, 1, 0]]).T
random.seed(1)
synaptic_weights = 2 * random.random((3, 1)) - 1
#Trains with the sets
print('Learning...')
for iteration in range(9999):
    output = 1 / (1 
    + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
os.system('clear')
screen = pygame.display.set_mode([300,525])
running=True
pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
while running:
  if pygame.event.poll().type == pygame.QUIT:
    running = False
  pygame.display.flip()
  screen.fill([255,255,255])
  pygame.draw.rect(screen,(255,0,0),(0,430,500,600))
  pygame.draw.circle(screen, (255,255,0), (90, cy), 25)
  Y = y
  s = 1 / (1 + exp(-(dot(array([Y,0,0]), synaptic_weights))))
  output = np.around(1 / (1 + exp(-(dot(array([Y,0,0]), synaptic_weights)))))
  time.sleep(2)
  os.system('clear')
  if output == 1:
    s = s/.5
    s = int(s*100)
    c = 'UP'
    cy -= 100
    y -= 1
  elif output == 0:
    s = s*.5
    s = int(s*100)
    c = 'DOWN'
    cy += 100
    y += 1  
  if s > 100:
    s = 100
  s = 'The AI is ' + str(s) + '% sure'
  textsurfacec = myfont.render(c, False, (0, 0, 0))
  screen.blit(textsurfacec,(0,0))
  textsurfaces = myfont.render(s, False, (0, 0, 0))
  screen.blit(textsurfaces,(0,20))
pygame.quit()