<!-- # BCS-Takneek-PS-2023
This is a repo containing the code and the documentation for the BCS PS, Takneek 2023.
 -->
# NEUROECONOMICS:

### _~Submission by Shauryas_

## INTRODUCTION

This project aims to analyze the effect of small individual decisions on the population of a grid world inhabited by Pacman-like creatures called Macpen. We will study the population growth and development based on the behavior of three types of Macpen: Helpful, Ungrateful, and Tit-for-Tat. The Macpen must collect food from random canteens in the grid world to reproduce. However, their food supply will be reduced by the Ghost Gang, which takes away a certain amount of food from each Macpen every day. If any Macpen's food level falls below zero, it will die. We will use Python to implement the environment and strategies of the Macpen and visualize their population development graphically.

## OUR UNDERSTANDING OF THE PS

To begin with, let's correlate the world mentioned in the problem set to a model of the game. We’ll be mentioning a few points from the problem set and also be adding our understanding of the same.

The game is a two-dimensional grid, and the characters can either move left, right, up or down. The game comprises Macpan (Plural: Macpen) and the Ghost Gang. The Macpen are the main characters, while the ghost gang is an antagonist. 

There are three types of Macpan, as mentioned below:
1. Orange (Helpful) - If the Macpan is in the same cell as another Macpan and has excess food, they can give the food to the other individual. 
2. Blue(Ungrateful) - The Macpan will not share food at all.
3. Green(Tit for Tat) - The Macpan will share food with the other pacman based on their history with the grid community


## ASSUMPTIONS

- The game repeats itself after every interval known as an iteration. One day comprises 10 iterations.
- Arrival of the ghost gang is marked as the end of a day.
- The ghost gang snatches one unit of food from every Macpan.
- At every iteration, macpan can either take one unit of food or might fail to if its away from the canteen.
- This is the reason why the ghost gang cannot appear after every iteration as the net food intake would become negative.
- Every canteen has an infinite amount of food.

## Implementation and Strategies

Every iteration comprises of a few basic activities which are elaborated below:

- Collection of food - Every Macpan either collects food or doesn't. A maximum of one unit can be collected.
- Sharing of food- A Macpan can share food on the basis of the type of Macpan it is.
- Reproduction - If there is enough food for reproduction, a Macpan can reproduce, i.e., it can split into two, with the amount of food being distributed equally amongst the two.


### Moving Strategy
The moving strategy implemented in the code is, every Macpan starts by looking for the closest canteen in the same row and column as its coordinates. In case there is no canteen in the respective  '+' region, the macpan will choose a random direction to move.


### Sharing Food
Over the course of a single iteration, each macpan helps only once, giving only one unit of food in an iteration . The primary goal of this is to prevent the macpen that need food the most from dying.

In the simulation, firstly we have sorted the macpen on the basis of whether or not they are in excess or in need.
The macpan with food less than or equal to the food taken away by the ghost gang is considered “needy”, and the macpan with food greater than or equal to ghost gang +2 is considered to be in “excess”.”

The sharing of food is only done if the macpen is in excess. Each ‘excess’ macpan can share only one unit of food, and only once in an iteration. We want to make sure that the macpan that is sharing its food must not die once it shares food, which is why we have written the “ +2”. For eg, if the macpan had only 2 food packets, and gives one of the food packets to a needy macpan, then it will only have one food packet at the end of the day which will be ultimately taken by the ghost gang, rendering it with 0 food packets, and thus it dies. 

After doing the sorting, we have arranged the needy macpen in ascending order and the macpen in excess in descending order and we have matched them one by one, and sharing of food occurs. The reason why we have done this pair-wise sharing is in order to simplify the sharing process.
 
### Reproduction
We have ourselves set a threshold for the food required for reproduction of a Macpan (due to the fact that it has not been specified by the problem statement, there is randomness in our final data, as the final results depend on the parameters that we supply to the code). If the food that the macpan has is greater than or equal to the reproduction threshold, then it will reproduce and split into 2 new macpen of the same type as the parent macpan, with no previous history with the community grid. The food undergoes integer division, i.e., if the parent food level is n = odd, each offspring gets (n-1)/2 food.

To deal with sharing food among the Tit-for-Tat macpen, their whole sharing history is stored using a hash map with keys 0 and 1, where 0 is for the times a macron didn’t share food during an interaction, while 1 is for the times it did. The values in the dictionary are updated according to the macpan’s history with the grid community. If there are more no. of 1s in the dictionary, then the macpan will be able to receive food from another green( i.e. tit-for-tat) macpen. However, if the no. of 0s are more, then the macpan will not be able to receive any food from the green macpen as its history is negative with the grid community. By default, we assume that Tit-for-Tat macpen are helpful.

If the macpan is reproducing in the same cell in which a canteen exists, then the canteen will be removed from that place, and a new canteen will be generated at a random place in the cell. The reason why we do this is that if the canteen’s location is not changed, then the newly formed macpen will keep getting food from the same canteen and will not move, thus resulting in infinite multiplication of the macpan. Note that the no. of canteens remains constant throughout the entire iteration.

### Environmental Setup
We are assuming the game is set on a N x N grid.
Firstly we start by randomly initializing the location of the canteens
Next we initialize the location of all the helpful macpan, again randomly. The same process is repeated for the ungrateful macpen and the tit-for-tat macpen.

### Simulation
Within the simulation, we firstly check if the canteen exists at the position of the macpan. If it exists, then the macpan’s food is appended by 1. Next, if the reproduction criteria is met, the macpan reproduces and forms 2 macpen with equal amount of food (refer to the reproduction unit for further explanation). After this the macpan moves using the moving strategy described above. If there are more than 2 macpen in the same grid cell, and they meet the sharing criteria, sharing of food occurs( refer to the sharing food unit for further details). At the end of the day, the ghost gang arrives and takes away one food particle from each macpan. If the macpan’s food no. becomes 0, then it dies. This is what happens in each iteration. Every iteration, the food in the canteens is replenished. And each day, the canteen locations are changed, and randomised. 

## INFERENCE  AND GRAPHICAL RESULTS

No matter how we change the parameters, the grateful one and the tit for tat one behave in a similar manner.


### Change in the number of iterations.

On decreasing the number of iteration the population starts dying as the arrival of ghost gang overpowers the population growth

![image](https://user-images.githubusercontent.com/123170794/229419346-b68d7bd4-5445-4c87-a3df-ab1adf183e36.png)![image](https://user-images.githubusercontent.com/123170794/229419649-e82b8085-1340-46a4-a770-249e95976932.png)

![image](https://user-images.githubusercontent.com/123170794/229419755-dc77bf18-8442-4804-8763-2807670e0445.png)![image](https://user-images.githubusercontent.com/123170794/229419763-53e98975-c0bd-4aaa-9a92-ff2f320afe93.png)

### On the basis of number of canteens in the area

On decreasing the number of canteens the ungrateful one starts winning 

![image](https://user-images.githubusercontent.com/123170794/229419829-a12433ca-6dec-4efd-ab18-9eb41ded2379.png)![image](https://user-images.githubusercontent.com/123170794/229419849-2a9b6819-462b-422a-beac-415cda30a427.png)


![image](https://user-images.githubusercontent.com/123170794/229419944-7a1130dd-0328-4561-8e12-ee2c75c00646.png)![image](https://user-images.githubusercontent.com/123170794/229419958-e710f49a-817a-4453-99b0-7365758fb206.png)


![image](https://user-images.githubusercontent.com/123170794/229419976-0c79eb97-58f9-4d34-b8be-083d9d44d71f.png)![image](https://user-images.githubusercontent.com/123170794/229419995-b42c750e-7c60-4ae4-900d-3f94314feaa4.png)

### On decreasing the initial food of the macpen 

![image](https://user-images.githubusercontent.com/123170794/229420033-3bbd737d-5530-4784-b6c2-b6c31289ceeb.png)![image](https://user-images.githubusercontent.com/123170794/229420049-06769c39-0042-4297-bc82-a84c9023f079.png)

![image](https://user-images.githubusercontent.com/123170794/229420076-b627295f-e233-4bcd-90df-f51980ea548d.png)![image](https://user-images.githubusercontent.com/123170794/229420085-ebc7d2ce-7bcc-407d-a1fc-65e0604ccac8.png)

![image](https://user-images.githubusercontent.com/123170794/229420103-ff744cac-ebbb-40b1-8e7e-a6813b016a3f.png)![image](https://user-images.githubusercontent.com/123170794/229420119-970984be-53a8-4772-8fcf-3b39016bd7a8.png)

![image](https://user-images.githubusercontent.com/123170794/229420141-7da4aed6-205d-4d34-9a8e-aed82bd8c573.png)

### On decreasing the threshold of reproduction

There is a lot of variation

![image](https://user-images.githubusercontent.com/123170794/229420180-16a945db-9b04-4ef6-b2f8-7bbebc358622.png)![image](https://user-images.githubusercontent.com/123170794/229420204-20c26f90-c981-4662-b96f-421ceed3585d.png)

## CONCLUSION

In conclusion, this project aims to simulate a grid world with Macpen, canteens, and the Ghost gang to analyze the effect of small individual decisions on the population. By implementing the environment in Python, defining the strategies of Macpen, and analyzing the population development over time, we can gain insights into how different types of behavior can affect the survival and growth of a population. The project requires a combination of programming skills, analytical skills, and creativity to come up with effective strategies and visualize the data.
