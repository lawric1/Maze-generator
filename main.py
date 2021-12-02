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
    im.putpixel((x,y), color)
    im.save('maze.png')


def generateMaze(WIDTH, HEIGHT):
    directionList = [[0, -1], [0, 1], [1, 0], [-1, 0]]

    startCell = [1, 1]
    currentCell = startCell

    visitedCells = []
    visitedCells.append(currentCell)

    WHITE, BLACK, BLUE = (255, 255, 255), (0, 0, 0), (0, 0, 255)
    
    im = Image.new('RGB', (WIDTH, HEIGHT))
    for x in range(WIDTH):
        for y in range(HEIGHT):
            im.putpixel((x,y), BLACK)

    drawCell(im, currentCell, WHITE)


    for i in range(5000000):
        direction = random.choice(directionList)
        nextCell = getNextCell(currentCell, direction)

        if nextCell[0] <= 0 or nextCell[0] >= WIDTH:
            continue
        if nextCell[1] <= 0 or nextCell[1] >= HEIGHT:
            continue

        if not nextCell in visitedCells:
            wall = removeWall(currentCell, direction)
            currentCell = nextCell
            visitedCells.append(wall)
            visitedCells.append(currentCell)

            directionList = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            

            time.sleep(0.2)
            drawCell(im, wall, WHITE)
            
            time.sleep(0.2)
            drawCell(im, currentCell, WHITE)

            continue


        directionList.remove(direction)    
        if not directionList:
            drawCell(im, currentCell, BLUE)

            index = visitedCells.index(currentCell) - 2
            currentCell = visitedCells[index]
            
            drawCell(im, visitedCells[index - 1], BLUE)
            drawCell(im, currentCell, BLUE)

            directionList = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        
    # return visitedCells

generateMaze(WIDTH, HEIGHT)


# im = Image.new('1', (WIDTH, HEIGHT))
# maze = generateMaze(WIDTH, HEIGHT)

#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             im.putpixel((x,y), ImageColor.getcolor('black', '1'))

# for cell in maze:
#     x, y = cell[0], cell[1]
#     im.putpixel((x,y), ImageColor.getcolor('white', '1'))

# im.save('maze.png') # or any image format