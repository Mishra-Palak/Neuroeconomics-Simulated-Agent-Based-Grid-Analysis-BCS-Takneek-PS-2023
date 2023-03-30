import random

# Define grid size and number of days to simulate
GRID_SIZE = 10
NUM_DAYS = 100

# Define initial number of Macpen of each type
num_helpful = 10
num_ungrateful = 10
num_tit_for_tat = 10

# Define food consumption and reproduction parameters
food_consumed_per_day = 1
food_for_reproduction = 2

# Define ghost gang's food tax
ghost_tax = 1

# Define probability of Macpen moving to a neighboring cell
move_prob = 0.8

# Initialize grid with random locations of canteens
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for i in range(5):
    x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
    grid[x][y] = 1

# Define Macpen classes
class Macpen:
    def __init__(self, food, move_prob):
        self.food = food
        self.move_prob = move_prob
        
    def move(self, x, y):
        if random.random() < self.move_prob:
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
                return new_x, new_y
        return x, y
    
    def collect_food(self, x, y):
        if grid[x][y] > 0:
            self.food += grid[x][y]
            grid[x][y] = 0
            
    def share_food(self, other):
        if self.food > other.food:
            self.food /= 2
            other.food = self.food
            
    def reproduce(self):
        if self.food >= food_for_reproduction:
            self.food /= 2
            return Macpen(food_for_reproduction, self.move_prob)
        else:
            return None

class HelpfulMacpen(Macpen):
    def __init__(self, food, move_prob):
        super().__init__(food, move_prob)
        
    def share_food(self, other):
        super().share_food(other)
        other.food = self.food

class TitForTatMacpen(Macpen):
    def __init__(self, food, move_prob):
        super().__init__(food, move_prob)
        self.history = {}
        
    def share_food(self, other):
        if other in self.history and self.history[other] == 'share':
            super().share_food(other)
        elif self.food > 0:
            self.food -= 1
            other.food += 1
        self.history[other] = 'share' if other in self.history else 'ignore'

# Initialize Macpen of each type
macpen_list = []
for i in range(num_helpful):
    macpen_list.append(HelpfulMacpen(food_consumed_per_day, move_prob))
for i in range(num_ungrateful):
    macpen_list.append(Macpen(food_consumed_per_day, move_prob))
for i in range(num_tit_for_tat):
    macpen_list.append(TitForTatMacpen(food_consumed_per_day, move_prob))

# Define simulation function
def simulate_day(macpen_list):
    # Move Macpen and collect food
    for macpen in macpen_list:
        x, y = macpen.move(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        macpen.collect_food(x, y)
        
    # Share food between Helpful Macpen
    for macpen1 in macpen_list:
        if isinstance(macpen1, HelpfulMacpen) and macpen1.food > 0:
            for macpen2 in macpen_list:
                if macpen1 != macpen2 and isinstance(macpen2, HelpfulMacpen) and macpen2.food < macpen1.food:
                    macpen1.share_food(macpen2)
                    
    # Share food between Tit-for-Tat Macpen based on their history
    for macpen1 in macpen_list:
        if isinstance(macpen1, TitForTatMacpen) and macpen1.food > 0:
            for macpen2 in macpen_list:
                if macpen1 != macpen2 and isinstance(macpen2, TitForTatMacpen):
                    macpen1.share_food(macpen2)
                    
    # Calculate ghost tax and apply it to all Macpen
    for macpen in macpen_list:
        macpen.food -= ghost_tax
        
    # Remove dead Macpen and reproduce Macpen
    new_macpen_list = []
    for macpen in macpen_list:
        if macpen.food <= 0:
            continue
        new_macpen_list.append(macpen)
        new_macpen = macpen.reproduce()
        if new_macpen is not None:
            new_macpen_list.append(new_macpen)
    return new_macpen_list

# Run simulation for specified number of days
population_history = []
for i in range(NUM_DAYS):
    macpen_list = simulate_day(macpen_list)
    population_history.append((len([m for m in macpen_list if isinstance(m, HelpfulMacpen)]),
                               len([m for m in macpen_list if isinstance(m, Macpen)]),
                               len([m for m in macpen_list if isinstance(m, TitForTatMacpen)])))
    
# Print population history
for i, pop in enumerate(population_history):
    print("Day ", i+1, ": Helpful=", pop[0], ", Ungrateful=", pop[1], ", Tit-for-Tat=", pop[2])
    #print(f"Day {i+1}: Helpful={pop[0]}, Ungrateful={pop[1]}, Tit-for-Tat={pop[2]}")
