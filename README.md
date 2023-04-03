<!-- # BCS-Takneek-PS-2023
This is a repo containing the code and the documentation for the BCS PS, Takneek 2023.
 -->
# NEUROECONOMICS:

### _~Submission by Shauryas_

## INTRODUCTION

This project aims to analyze the effect of small individual decisions on the population of a grid world inhabited by Pacman-like creatures called Macpen. We will study the population growth and development based on the behavior of three types of Macpen: Helpful, Ungrateful, and Tit-for-Tat. The Macpen must collect food from random canteens in the grid world to reproduce. However, their food supply will be reduced by the Ghost Gang, which takes away a certain amount of food from each Macpen every day. If any Macpen's food level falls below zero, it will die. We will use Python to implement the environment and strategies of the Macpen and visualize their population development graphically.


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

2. On the basis of number of canteens in the area:

![image](https://user-images.githubusercontent.com/123170794/229429408-892c952a-b6d3-4ceb-ab4b-0090296835e9.png)![image](https://user-images.githubusercontent.com/123170794/229429425-142f7a12-8c62-4605-97ed-d90ab8b26717.png)

![image](https://user-images.githubusercontent.com/123170794/229429453-c9709f94-9ebc-40f2-b867-7c5fc0beaba4.png)![image](https://user-images.githubusercontent.com/123170794/229429649-851d75cc-379c-47a6-9114-d53cccc92f6f.png)

![image](https://user-images.githubusercontent.com/123170794/229429706-4f9cb6fb-7be2-4cc5-948d-0ba1bb144baa.png)![image](https://user-images.githubusercontent.com/123170794/229429735-50a6b2ec-7bf6-47da-9f41-1408591466ac.png)



On decreasing the number of canteens the ungrateful one starts winning

#

3. On decreasing the initial food of the macpen 

![image](https://user-images.githubusercontent.com/123170794/229429166-a8a83692-5f09-4f07-80ad-04e186a75a16.png)![image](https://user-images.githubusercontent.com/123170794/229429198-0d01cf16-6c4b-4c36-b8c6-57958cfab927.png)

![image](https://user-images.githubusercontent.com/123170794/229429210-e923ad87-eee4-4ace-8c46-ef0409a276fe.png)![image](https://user-images.githubusercontent.com/123170794/229429228-731b50d3-01cd-46c1-b8c2-9ea89d15ad4a.png)

![image](https://user-images.githubusercontent.com/123170794/229429254-fa8f0a2a-4a51-4250-ac0a-376f7e0ea03b.png)![image](https://user-images.githubusercontent.com/123170794/229429274-acfe776f-e06b-4c14-84ae-ae1ddeef6a63.png)

![image](https://user-images.githubusercontent.com/123170794/229429296-83ab5938-83ff-4ba8-97e6-5364d7f9faf7.png)

#

4. On decreasing the threshold of reproduction

![image](https://user-images.githubusercontent.com/123170794/229428468-78a840ec-fb61-454b-9879-c36e7f73a55e.png)![image](https://user-images.githubusercontent.com/123170794/229428622-8464c069-cd7e-468c-97a6-4a3991d2c817.png)



There are a lot of variation post the above change.



## CONCLUSION
In conclusion, this project aims to simulate a grid world with Macpen, canteens, and the Ghost gang to analyze the effect of small individual decisions on the population. By implementing the environment in Python, defining the strategies of Macpen, and analyzing the population development over time, we can gain insights into how different types of behavior can affect the survival and growth of a population. The project requires a combination of programming skills, analytical skills, and creativity to come up with effective strategies and visualize the data.

