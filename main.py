import time
import random
from operator import add

from PIL import Image

WIDTH, HEIGHT = 15,15

DIRECTIONS = [[0, -1], [0, 1], [1, 0], [-1, 0]]

WHITE, BLACK, BLUE = (255, 255, 255), (0, 0, 0), (0, 0, 255)


def multiply(direction, n):
    return [value * n for value in direction]


def getNextCell(cell, direction):
    wall = list(map(add, cell, direction))

    direction = multiply(direction, 2)
    nextCell = list(map(add, cell, direction))

    return wall, nextCell


def getPossibleDirections(cell, visitedCells):
    possibleDirections = []

    for direction in DIRECTIONS:
        wall, nextCell = getNextCell(cell, direction)

        # Check if cell is within maze bounds
        if nextCell[0] <= 0 or nextCell[0] >= WIDTH -1:
            continue
        if nextCell[1] <= 0 or nextCell[1] >= HEIGHT -1:
            continue

        if not nextCell in visitedCells:
            possibleDirections.append(direction)

    return possibleDirections


def createImage(color):
    image = Image.new('RGB', (WIDTH, HEIGHT))
    for x in range(WIDTH):
        for y in range(HEIGHT):
            image.putpixel((x,y), color)
    
    return image


def drawCell(image, cell, color):
    x, y = cell[0], cell[1]
    image.putpixel((x,y), color)
    image.save('maze.png')

    

def generateMaze():
    startCell = [1, 1]
    currentCell = startCell

    stack = []
    visitedCells = []
    visitedCells.append(currentCell)

    
    mazeImage = createImage(BLACK)
    drawCell(mazeImage, currentCell, WHITE)


    while True:
        possibleDirections = getPossibleDirections(currentCell, visitedCells)

        while possibleDirections:
            direction = random.choice(possibleDirections)
            wall, nextCell = getNextCell(currentCell, direction)

            if not nextCell in visitedCells:
                stack.append(currentCell)

                currentCell = nextCell
                visitedCells.append(wall)
                visitedCells.append(currentCell)

                # Update maze image everytime nextCell is found for a simple vizualization
                time.sleep(0.1)
                drawCell(mazeImage, wall, WHITE)

                time.sleep(0.1)
                drawCell(mazeImage, currentCell, WHITE)
                
            break
        
        if not possibleDirections:
            currentCell = stack.pop() # Get previous cell from stack for backtracking

        if currentCell == visitedCells[0]:
            break

    # return visitedCells

generateMaze()


# im = Image.new('1', (WIDTH, HEIGHT))
# maze = generateMaze(WIDTH, HEIGHT)

#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             im.putpixel((x,y), ImageColor.getcolor('black', '1'))

# for cell in maze:
#     x, y = cell[0], cell[1]
#     im.putpixel((x,y), ImageColor.getcolor('white', '1'))

# im.save('maze.png') # or any image format