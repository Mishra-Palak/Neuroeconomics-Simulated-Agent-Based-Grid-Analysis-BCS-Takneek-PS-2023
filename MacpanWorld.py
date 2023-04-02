import random
import numpy as np
import matplotlib.pyplot as plt
N = 100 #NxN GRID
NUM_DAYS = 50
NUM_ITERATIONS = 10 #In a day

#INITIAL POPULATION
M_HELPFUL = 100
M_UNGRATEFUL = 100
M_TIT_FOR_TAT = 100

CANTEENS = 10

FOOD_CANTEEN =  8
FOOD_INITIAL = 2

REPRODUCTION_THRESHOLD = 2

TYPES = ["Helpful", "Ungrateful", "Tit-for-Tat"]

GHOST_GANG = 1

class Macpen():
    def __init__(self, x, y, food, type, history):
        self.x = x
        self.y = y
        self.food = food
        self.type = type
        self.history = history

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
            if self.type == TYPES[2]:
                new_macpens = [Macpen(self.x, self.y, self.food, self.type, {0 : 0, 1 : 0}), Macpen(self.x, self.y, self.food, self.type, {0 : 0, 1 : 0})]
            else:
                new_macpens = [Macpen(self.x, self.y, self.food, self.type, self.history), Macpen(self.x, self.y, self.food, self.type, self.history)]

            if self.type == TYPES[0]:
                global M_HELPFUL
                M_HELPFUL+=1
            elif self.type == TYPES[1]:
                global M_UNGRATEFUL
                M_UNGRATEFUL+=1
            elif self.type == TYPES[2]:
                global M_TIT_FOR_TAT
                M_TIT_FOR_TAT+=1
            
            #NEW CANTEEN
            if grid[self.x][self.y] > 0:
                grid[self.x][self.y] = 0
                x, y = random.randint(0, N-1), random.randint(0, N-1)
                grid[x][y] = FOOD_CANTEEN

            return new_macpens
        return []

    def share_food(self, other):
        #Each macpan helps only once in a single iteration
        #Goal is to prevent the needfull ones from dying
        self.food-=1
        other.food+=1

#ENVIRONMENT-SETUP
grid = np.zeros((N, N), dtype=int) #Stores the number of macpen on each cell
for i in range(CANTEENS):
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    grid[x][y] = FOOD_CANTEEN
#print(grid)

#MACPEN
population = []
for i in range(M_HELPFUL):
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    population.append(Macpen(x, y, FOOD_INITIAL, TYPES[0], {1 : 1}))
for i in range(M_UNGRATEFUL):
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    population.append(Macpen(x, y, FOOD_INITIAL, TYPES[1], {0 : 1}))
for i in range(M_TIT_FOR_TAT):
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    population.append(Macpen(x, y, FOOD_INITIAL, TYPES[2], {0 : 0, 1 : 0}))

ungrateful_n=[]
grateful_n=[]
tit_for_tat_n=[]
day_n=[]

def simulate():
    global M_HELPFUL
    global M_UNGRATEFUL
    global M_TIT_FOR_TAT
    global population
    global grid
    print("DAY 0:\nPopulation: Helpful - ", M_HELPFUL, ", Ungrateful - ", M_UNGRATEFUL, ", Tit-for-Tat - ", M_TIT_FOR_TAT)
    for day in range(NUM_DAYS):
        #Each day things
        for i in range(NUM_ITERATIONS):
            #Canteen
            for macpan in population:
                if (grid[macpan.x][macpan.y] > 0):
                    macpan.food += FOOD_CANTEEN

            #Reproduce
            new_population = []
            for macpan in population:
                if macpan.food >= REPRODUCTION_THRESHOLD:
                    new_macpens = macpan.reproduce()
                    new_population.append(new_macpens[0])
                    new_population.append(new_macpens[1])
                else:
                    new_population.append(macpan)
            population = new_population
            
            #Move
            for macpan in population:
                macpan.move()

            #Share Food
            macpan_count = [ [{'excess' : [], 'need' : []} for _ in range(N) ] for _ in range(N) ]
            for macpan in population:
                if macpan.food <= GHOST_GANG:
                    macpan_count[macpan.x][macpan.y]['need'].append(macpan)
                elif macpan.food > GHOST_GANG + 1:
                    if macpan.type != TYPES[1]:
                        macpan_count[macpan.x][macpan.y]['excess'].append(macpan)
                #GHOST_GANG+1 are neither in excess nor need food
            for x in range(N):
                for y in range(N):
                    if len(macpan_count[x][y]['excess']) > 0 and len(macpan_count[x][y]['need']) > 0:
                        excess = macpan_count[x][y]['excess']
                        excess.sort(key=lambda x: x.food, reverse=True)
                        need = macpan_count[x][y]['need']
                        need.sort(key=lambda x: x.food)

                        for i in range(min(len(excess), len(need))):
                            if excess[i].type == TYPES[0] and need[i].type == TYPES[0]:
                                excess[i].share_food(need[i])
                            elif excess[i].type == TYPES[0] and need[i].type == TYPES[1]:
                                excess[i].share_food(need[i])
                            elif excess[i].type == TYPES[0] and need[i].type == TYPES[2]:
                                excess[i].share_food(need[i])
                            elif excess[i].type == TYPES[2] and need[i].type == TYPES[0]:
                                excess[i].share_food(need[i])
                                excess[i].history[1]+=1
                            elif excess[i].type == TYPES[2] and need[i].type == TYPES[1]:
                                excess[i].history[0]+=1
                                # excess.remove(excess[i])
                                # i-=1
                            elif excess[i].type == TYPES[2] and need[i].type == TYPES[2]:
                                if need[i].history[1] >= need[i].history[0]: #By default, Tit-for-Tat's are helpful
                                    excess[i].share_food(need[i])
                                    excess[i].history[1]+=1
                                else:
                                    excess[i].history[0]+=1
                                    # excess.remove(excess[i])
                                    # i-=1

        #Ghost Gang - Comes at the end of the day
        for macpan in population:
            macpan.food -= GHOST_GANG
            if macpan.food <= 0:
                population.remove(macpan)
                if macpan.type == TYPES[0]:
                    M_HELPFUL-=1
                elif macpan.type == TYPES[1]:
                    M_UNGRATEFUL-=1
                elif macpan.type == TYPES[2]:
                    M_TIT_FOR_TAT-=1
        
        grid = np.zeros((N, N), dtype=int)
        for i in range(CANTEENS):
            x, y = random.randint(0, N-1), random.randint(0, N-1)
            grid[x][y] = FOOD_CANTEEN
        ungrateful_n.append(M_UNGRATEFUL)
        grateful_n.append(M_HELPFUL)
        tit_for_tat_n.append(M_TIT_FOR_TAT)
        day_n.append(day+1)
        print("DAY", day+1, ":\nPopulation: Helpful - ", M_HELPFUL, ", Ungrateful - ", M_UNGRATEFUL, ", Tit-for-Tat - ", M_TIT_FOR_TAT)

simulate()
plt.plot(day_n, ungrateful_n, label='Ungrateful')

plt.plot(day_n, grateful_n, label='Helpful one')

plt.plot(day_n, tit_for_tat_n, label='Tit for Tat')

plt.title('Population Vs Number of days')
plt.xlabel('Number of days')
plt.ylabel('Pacman Population')

plt.legend()

plt.show()
