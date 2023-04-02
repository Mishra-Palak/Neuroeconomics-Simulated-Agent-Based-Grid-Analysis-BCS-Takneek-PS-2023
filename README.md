# BCS-Takneek-PS-2023
This is a repo containing the code and the documentation for the BCS PS, Takneek 2023.

# NEUROECONOMICS:

### _~Submission by Shauryas_


## OUR UNDERSTANDING OF THE PS:


To begin with, let's correlate the world mentioned in the problem set to a model of the game. We’ll be mentioning a few points from the problem set and also be adding our understanding of the same.

The game is a two-dimensional grid, and the characters can either move left, right, up or down. The game comprises Macpan (Plural: Macpen) and the Ghost Gang. 

There are three types of Macpan, as mentioned below:
1. Yellow (Helpful) - If the Macpan is in the same cell as another Macpan and has excess food, they can give the food to the other individual. 
2. Red (Ungrateful) - The Macpan will not share food at all.
3. Blue (Tit for Tat) - The Macpan will share food with the other pacman based on their history with the grid community

We have assumed that the ghost gang appears once per day and reduces the food of each macpan by one. We have assumed this because if we had assumed that the ghost gang appears every iteration, the net food intake would become negative as it is not necessary that the macpan feeds at every iteration, as it may not be at a canteen. 



The game repeats a particular cycle after every t time. The cycle is further elaborated below:
- Collection of food - Every Macpan either collects food or doesn't. A maximum of one unit can be collected.
Sharing of food- A Macpan can share food on the basis of the type of Macpan it is.
- Reproduction - If there is enough food for reproduction, a Macpan can reproduce, i.e., it can split into two, with the amount of food being distributed equally amongst the two.
- Snatching of food by the Ghost gang - The ghost gang snatches away one unit of food from everyone in every iteration, and if any Macpan’s food level falls below 0, it dies.

All the basic activities like reproduction, sharing of food, and movement happens multiple times each day. We have also assumed that all canteens will have infinite food supply. 

## Implementation and Strategy

### Moving Strategy:

The moving strategy that we have implemented in this code is that we are looking for the closest canteen in the same row and column as the macpan's coordinates. In case there is no canteen in that '+' region, the macpan will choose a random direction and move.

### Reproduction:
We have ourselves set a threshold for the food required for reproduction of a Macpan (due to the fact that it has not been specified by the problem statement, there is randomness in our final data, as the final results depend on the parameters that we supply to the code). If the food that the macpan has is greater than or equal to the reproduction threshold, then it will reproduce and split into 2 new macpen of the same type as the parent macpan, with no previous history with the community grid. The food undergoes integer division, i.e., if the parent food level is n = odd, each offspring gets (n-1)/2 food.

To deal with sharing food among the Tit-for-Tat macpen, their whole sharing history is stored using a hash map with keys 0 and 1, where 0 is for the times a macron didn’t share food during an interaction, while 1 is for the times it did. The values in the dictionary are updated according to the macpan’s history with the grid community. If there are more no. of 1s in the dictionary, then the macpan will be able to receive food from another blue( i.e. tit-for-tat) macpen. However, if the no. of 0s are more, then the macpan will not be able to receive any food from the blue macpen as its history is negative with the grid community. By default, we assume that Tit-for-Tat macpen are helpful.

If the macpan is reproducing in the same cell in which a canteen exists, then the canteen will be removed from that place, and a new canteen will be generated at a random place in the cell. The reason why we do this is that if the canteen’s location is not changed, then the newly formed macpen will keep getting food from the same canteen and will not move, thus resulting in infinite multiplication of the macpan. Note that the no. of canteens remains constant throughout the entire iteration.
