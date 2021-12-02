import time
import random
from operator import add

from PIL import Image, ImageColor


WIDTH, HEIGHT = 15,15

def multiply(direction, n):
    return [value * n for value in direction]


def getNextCell(currentCell, direction):
    direction = multiply(direction, 2)
    return list(map(add, currentCell, direction))


def removeWall(currentCell, direction):
    return list(map(add, currentCell, direction))


def drawCell(im, cell, color):
    x, y = cell[0], cell[1]
    im.putpixel((x,y), ImageColor.getcolor(color, '1'))
    im.save('maze.png')

def generateMaze(WIDTH, HEIGHT):
    directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

    startCell = [1, 1]
    visitedCells = []
    track = []

    currentCell = startCell
    visitedCells.append(currentCell)
    track.append(currentCell)

    im = Image.new('1', (WIDTH, HEIGHT))
    # maze = generateMaze(WIDTH, HEIGHT)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            im.putpixel((x,y), ImageColor.getcolor('black', '1'))

    drawCell(im, currentCell, 'white')

    for i in range(5000000):
        nextDirection = random.choice(directions)
        nextCell = getNextCell(currentCell, nextDirection)

        if nextCell[0] <= 0 or nextCell[0] >= WIDTH:
            continue
        if nextCell[1] <= 0 or nextCell[1] >= HEIGHT:
            continue

        if not nextCell in visitedCells:
            wall = removeWall(currentCell, nextDirection)
            visitedCells.append(wall)
            track.append(wall)

            currentCell = nextCell
            visitedCells.append(currentCell)
            track.append(currentCell)

            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            
            time.sleep(0.2)
            drawCell(im, wall, 'white')
            
            time.sleep(0.2)
            drawCell(im, currentCell, 'white')

            continue

        directions.remove(nextDirection)
    
        if not directions:
            currentCell = track[-3]
            track.pop()
            track.pop()

            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        
        # if len(track) == 0:
        #     break

    # return visitedCells

# im = Image.new('1', (WIDTH, HEIGHT)) # create the Image of size 1 pixel
# maze = generateMaze(WIDTH, HEIGHT)

#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             im.putpixel((x,y), ImageColor.getcolor('black', '1')) # or whatever color you wish

# for cell in maze:
#     x, y = cell[0], cell[1]
#     im.putpixel((x,y), ImageColor.getcolor('white', '1')) # or whatever color you wish

# im.save('maze.png') # or any image format

generateMaze(WIDTH, HEIGHT)

