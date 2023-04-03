<!-- # BCS-Takneek-PS-2023
This is a repo containing the code and the documentation for the BCS PS, Takneek 2023.
 -->
# NEUROECONOMICS:

### _~Submission by Shauryas_

## INTRODUCTION

We will start by creating a grid world of size NxN and placing random canteens in it. We will then initialize the population of each type of Macpen and assign them a starting position on the grid. We will then create functions for the movement of Macpen and food collection. The Macpen will move towards the nearest canteen and collect food. After collecting enough food, they will reproduce which results in two new Macpen with an equal share of food from the parent Macpen. We will also create functions for the Ghost Gang's daily visit and its reduction of the Macpen's food supply. We will then implement the behavior of the three types of Macpen: Helpful, Ungrateful, and Tit-for-Tat. We will run the simulation for a fixed number of days and record the population of each type of Macpan on each day. Finally, we plotted the population graphs of each type of Macpan for all the days.

## APPROACH

We will start by creating a grid world of size NxN and placing random canteens in it. We will then initialize the population of each type of Macpen and assign them a starting position on the grid. We will then create functions for the movement of Macpen and food collection. The Macpen will move towards the nearest canteen and collect food. After collecting enough food, they will reproduce which results in two new Macpen with an equal share of food from the parent Macpen. We will also create functions for the Ghost Gang's daily visit and its reduction of the Macpen's food supply. We will then implement the behavior of the three types of Macpen: Helpful, Ungrateful, and Tit-for-Tat. We will run the simulation for a fixed number of days and record the population of each type of Macpan on each day. Finally, we plotted the population graphs of each type of Macpan for all the days.

## RESULTS

We ran the simulation for 1000 days with 1000 macpen in the grid world, out of which 30% were Helpful, 30% were Ungrateful, and 40% were Tit-for-tat. The ghost gang took away 20% of the food every day. The initial food level of each macpan was randomly assigned between 0 and 10. The canteens were randomly placed in the grid world with a fixed amount of food.

From the below graphs, we can observe that the population of all three types of Pacman initially grows but then stabilizes after some time. The most ideal case is if the population of Helpful Macpan is always the highest, followed by Tit-for-tat Macpan and then Ungrateful Macpan. This is because Helpful Macpan shares its food with other Macpan and helps them survive, whereas Ungrateful Macpan does not share food. However, variations in the parameters result into vagaries in the data and the graphs. Certain parameters also result in overlapping of all the three graphs.


## GRAPHICAL RESULTS

No matter how we change the parameters, the grateful one and the tit for tat one behave in a similar manner.

The following changes were made in order to analyse the results:

1. Change in the number of iterations.

![image](https://user-images.githubusercontent.com/123170794/229425902-a4488b4c-8ab7-4ac0-8762-4e55187d1990.png)![image](https://user-images.githubusercontent.com/123170794/229425957-34498985-1a83-4b7f-9ee5-fd6608cb35c5.png)

![image](https://user-images.githubusercontent.com/123170794/229426220-69ab5782-80a9-4d44-b223-4a78361287a3.png)![image](https://user-images.githubusercontent.com/123170794/229426243-acc874f9-5e3f-4542-abc7-9005193d53b4.png)

On decreasing the number of iteration the population starts dying as the arrival of ghost gang overpowers the population growth

# 
#
2. On the basis of number of canteens in the area:

![image](https://user-images.githubusercontent.com/123170794/229426477-b9cbb96c-9009-466a-b3fd-b2554c032c83.png)![image](https://user-images.githubusercontent.com/123170794/229426493-123d6d30-665b-4dfa-a491-0f6e7c964c24.png)

![image](https://user-images.githubusercontent.com/123170794/229426501-a2e16b78-aeb5-4820-98cc-ec4afeb43955.png)![image](https://user-images.githubusercontent.com/123170794/229426526-18cac48d-6709-465d-b1b8-87450cfafca9.png)

![image](https://user-images.githubusercontent.com/123170794/229426653-e14dd75f-c816-43c2-985f-372bf4d6047b.png)![image](https://user-images.githubusercontent.com/123170794/229426670-460d59d7-45d5-4f97-b7ce-a587644c179f.png)

On decreasing the number of canteens the ungrateful one starts winning

#
#
3. On decreasing the initial food of the macpen 

![image](https://user-images.githubusercontent.com/123170794/229426777-1a5e3d70-9f43-4a51-9319-98036408d8ba.png)![image](https://user-images.githubusercontent.com/123170794/229426805-ab412f22-9ffd-4b6f-a018-752672bc2f69.png)

![image](https://user-images.githubusercontent.com/123170794/229426862-bdc0e505-e725-4a46-b3a9-c6813b8e8a59.png)![image](https://user-images.githubusercontent.com/123170794/229426874-3f2c06fb-f88b-4f9e-9e3f-675f7827e68e.png)

![image](https://user-images.githubusercontent.com/123170794/229426938-b05e5ed2-a433-4b0c-b08f-654db7c37ad4.png)![image](https://user-images.githubusercontent.com/123170794/229426947-b2d0a82b-ebb7-4529-90fe-b552229ce4fa.png)

![image](https://user-images.githubusercontent.com/123170794/229426969-3a8173b0-2202-40f7-a352-29b58a00cd12.png)

#
#
4. On decreasing the threshold of reproduction

![image](https://user-images.githubusercontent.com/123170794/229427040-dabbd8f5-1e77-45f1-bc2b-bed476cd62cb.png)![image](https://user-images.githubusercontent.com/123170794/229427053-3089e21b-56af-45b8-ba2b-f0d599cddd88.png)


There are a lot of variation post the above change.



## Conclusion
In conclusion, this project aims to simulate a grid world with Macpen, canteens, and the Ghost gang to analyze the effect of small individual decisions on the population. By implementing the environment in Python, defining the strategies of Macpen, and analyzing the population development over time, we can gain insights into how different types of behavior can affect the survival and growth of a population. The project requires a combination of programming skills, analytical skills, and creativity to come up with effective strategies and visualize the data.

