import random
import numpy as np

N = 10 #NxN GRID
NUM_DAYS = 100
NUM_ITERATIONS = 10 #In a day

#INITIAL POPULATION
M_HELPFUL = 10
M_UNGRATEFUL = 10
M_TIT_FOR_TAT = 10
M = M_HELPFUL + M_UNGRATEFUL + M_TIT_FOR_TAT 

K = 10 #CANTEENS

FOOD_CANTEEN = 2
FOOD = 2

REPRODUCTION_THRESHOLD = 4

TYPES = ["Helpful", "Ungrateful", "Tit-for-Tat"]

GHOST_GANG = 1

class Macpen():
    def __init__(self, x, y, food, type):
        self.x = x
        self.y = y
        self.food = food
        self.type = type

    def move(self):
        min_dist = N
        direction = -1 #L = 0, R = 1, U = 2, D = 3, Stay = 10
        for x in range(N):
            if (grid[x][self.y] > 0):
                if (abs(self.x - x) < min_dist):
                    min_dist = abs(self.x - x)
                    if x < self.x:
                        direction = 0
                    elif x > self.x:
                        direction = 1
                    else:
                        direction = 10
        for y in range(N):
            if (grid[self.x][y] > 0):
                if (abs(self.y - y) < min_dist):
                    min_dist = abs(self.y - y)
                    if y < self.y:
                        direction = 2
                    elif y > self.y:
                        direction = 3
                    else:
                        direction = 10
        if direction == -1:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            dx, dy = random.choice(directions)
            if (0 <= self.x + dx < N and 0 <= self.y + dy < N):
                self.x += dx
                self.y += dy
        elif direction == 0:
            if self.x > 0:
                self.x-=1
        elif direction == 1:
            if self.x < N-1:
                self.x+=1
        elif direction == 2:
            if self.y > 0:
                self.y-=1
        elif direction == 3:
            if self.y < N-1:
                self.y+=1
        elif direction == 10:
            pass

    def reproduce(self):
        if self.food >= REPRODUCTION_THRESHOLD:
            self.food //= 2
            new_macpens = [Macpen(self.x, self.y, self.food, self.type), Macpen(self.x, self.y, self.food, self.type)]
            if self.type == TYPES[0]:
                M_HELPFUL+=1
            elif self.type == TYPES[1]:
                M_UNGRATEFUL+=1
            elif self.type == TYPES[2]:
                M_TIT_FOR_TAT+=1
            
            #NEW CANTEEN
            grid[self.x][self.y] = 0
            x, y = random.randint(0, N-1), random.randint(0, N-1)
            grid[x][y] = FOOD_CANTEEN

            return new_macpens
        return [self]

    #def share_food(self):





#ENVIRONMENT-SETUP
grid = np.zeros((N, N), dtype=int) #Stores the number of macpen on each cell
for i in range(K):
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    grid[x][y] = FOOD_CANTEEN
#print(grid)

#MACPEN
population = []
for i in range(M_HELPFUL):
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    population.append(Macpen(x, y, FOOD, TYPES[0]))
for i in range(M_UNGRATEFUL):
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    population.append(Macpen(x, y, FOOD, TYPES[1]))
for i in range(M_TIT_FOR_TAT):
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    population.append(Macpen(x, y, FOOD, TYPES[2]))

def simulate():
    for day in range(NUM_DAYS):
        print("DAY 0:\nPopulation: Helpful - ", M_HELPFUL, ", Ungrateful - ", M_UNGRATEFUL, ", Tit-for-Tat - ", M_TIT_FOR_TAT)
        #Each day things
        for i in range(NUM_ITERATIONS):
            for macpan in population:
                #Reproduce
                population.append(macpan.reproduce())
                population.remove(macpan)

                #Canteen
                if (grid[macpan.x][macpan.y] > 0):
                    macpan.food += FOOD_CANTEEN

            #Share Food


            for macpan in population:
                #Move
                macpan.move()

        #Ghost Gang
        for macpan in population:
            macpan.food -= GHOST_GANG
            if (macpan.food <= 0):
                population.remove(macpan)

        print("DAY ", day, ":\nPopulation: Helpful - ", M_HELPFUL, ", Ungrateful - ", M_UNGRATEFUL, ", Tit-for-Tat - ", M_TIT_FOR_TAT)
