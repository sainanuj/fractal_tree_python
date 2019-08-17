import pygame
import math
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (255, 192, 203)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fractal tree")
running = True

def randomRange(min, max):
	return min + random.random()*(max - min)

def line(x1, y1, x2, y2, color=BLACK, width=1, surface=screen):
	pygame.draw.line(surface, color, (x1, y1), (x2, y2), width)

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

p0 = Point(WIDTH/2, HEIGHT-50)
p1 = Point(WIDTH/2, 50)

branchAngle = randomRange(0, math.pi/2)
trunkRatio = randomRange(0.25, 0.75)


def tree(p0, p1, limit):
	dx = p1.x - p0.x
	dy = p1.y - p0.y
	dist = math.sqrt(dx*dx + dy*dy)
	angle = math.atan2(dy, dx)
	branchLength = dist * (1 - trunkRatio)

	pA = Point((p0.x + dx*trunkRatio), (p0.y + dy*trunkRatio))

	pB = Point((pA.x + math.cos(angle+branchAngle)*branchLength),
		(pA.y + math.sin(angle+branchAngle)*branchLength))

	pC = Point((pA.x + math.cos(angle - branchAngle) * branchLength),
		(pA.y + math.sin(angle - branchAngle) * branchLength))

	line(p0.x, p0.y, pA.x, pA.y)

	if (limit > 0):
		tree(pA, pC, limit - 1)
		tree(pA, pB, limit - 1)
	else:
		line(pA.x, pA.y, pB.x, pB.y)
		line(pA.x, pA.y, pC.x, pC.y)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	clock.tick(30)
	screen.fill(PINK)

	tree(p0, p1, 10)
	branchAngle += .005

	pygame.display.flip()

pygame.quit()