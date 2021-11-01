# PolyU Eng1003 AAE Freshman Project
### Group 2 Report

### Overview   
Recently, thousands of aircrafts are operating for the aviation industry. Finding the most efficient path for the aircrafts is an essential task to achieve. In this project, we are assigned to design a flight path for an aircraft using python and different tools with some data researches.

---
### Table of content

1. [Background of Path Planning to Aviation Engineering](#background-of-path-planning-to-aviation-engineering)

2. [Theory of Path Planning Algorithm](#theory-of-path-planning-algorithm)

3. [Introduction of the Engineering Tools](#introduction-of-the-engineering-tools)
   3.1 [Python](#python)
   3.2 [GitHub](#github)

4. [Task 1: Methodology, Results and Discussion](#task1)

5. [Task 2.1: Methodology, Results and Discussion](#task2.1)

6. [Task 2.2: Methodology, Results and Discussion](#task2.2)

7. [Task 3: Methodology, Results and Discussion](#task3)

8. [Task 4: Methodology, Results and Discussion](#task4)
   
9. [Reflective Essay](#reflective-essay)

10. [References](#references)
   
---
### <a name="background-of-path-planning-to-aviation-engineering"></a> Background of Path Planning to Aviation Engineering

---
### <a name="theory-of-path-planning-algorithm"></a> Theory of Path Planning Algorithm

---
### <a name="introduction-of-the-engineering-tools"></a> Introduction of the Engineering Tools

### <a name="python"></a> Python
### <a name="github"></a> Github
---
### <a name="task1"></a> Task 1: Methodology, Results and Discussion

Task 1 aims to find the aircraft model with the minimum total cost flying through the designated zone.
We were given a 70 by 70 square zone template. We changed the position of the start, goal, aditional cost areas and barriers by editing the sample code.

![Task1 numbers](https://github.com/Alex-Shun-kit-YEUNG/AAE-Freshman-projuct-group-2/blob/0ee9bf5ed7224fc73bed4743379536dc401045f9/task1%20numbers.png)

![week6 task figure](https://github.com/Alex-Shun-kit-YEUNG/AAE-Freshman-projuct-group-2/blob/main/week6%20task%20figure.png)

The minimum cost is model A380

---
### <a name="task2.1"></a> Task 2.1: Methodology, Results and Discussion

We know that C = Cf * delta F + Ct * delta T + Cc , delta F = delta T = 5

So C = (Cf + Ct) * 5 + Cc

Let Cf be y and Ct be x.

And we can simply transfer the constraints to:

y-x-30=<0

-0.5y-x+30=<0

2y-x-20>=0

-4y-x+220>=0

We can input these functions into one plane.

Just like this

![B2326E68-26A9-4BF3-8333-EE0A5ACDF009_1_201_a.jpeg](https://github.com/Alex-Shun-kit-YEUNG/AAE-Freshman-projuct-group-2/blob/main/B2326E68-26A9-4BF3-8333-EE0A5ACDF009_1_201_a.jpeg)

So we can find the area under the constraints.

Let y + x = z

So the minimum of z is 40 when it across the point (20 , 20).

So the answer of the task 2 question 1 is 210.

---
### <a name="task2.2"></a> Task 2.2: Methodology, Results and Discussion
C:\Users\Alex\Desktop\Untitled-1.py start the A star algorithm demo !!
min_x: -10

min_y: -10

max_x: 60

max_y: 60

x_width: 70

y_width: 70

1 9 1 16

1 10 1 15

1 11 1 14

1 12 1 13

1 13 1 12

1 14 1 11

1 15 1 10

1 16 1 9

9 1 16 1

10 1 15 1

11 1 14 1

12 1 13 1

13 1 12 1

14 1 11 1

15 1 10 1

16 1 9 1

35

PolyU-A380 cost part1->  364.8

PolyU-A380 cost part2->  364.8

PolyU-A380 cost part3->  10

---
### <a name="task3"></a> Task 3: Methodology, Results and Discussion

This task aims to design a new cost area that can reduce the cost of the route. The additional minus cost area should be at a maximum of 16 grip points and located at the best location.

Firstly of all, a new minus costarea is decided to be located at the place which cover a longer route, so the cost can be reduced at a higher rate. Besides, the maximum area of 16 grid points has to be taken into consideration. After the decision of location, a new code has to be inserted to the original one so as to create the area at the planned location. The new code is inserted under the fuel consuming area and time consuming area and the area is located by inputting the x-axis and y-axis.

Other than the locating the area by inputting a new code, the two new elements data of the additional minus cost area has to be added, while the equation for the cost in the original code has to be amended according to the given one, so that the designated minus cost area can be used to reduce the cost. 

For the result, the location of minus cost area is selected at i in range(16,20) and j in range(53,57), forming a square of 16 grid points.

![Task3 figure](https://github.com/Alex-Shun-kit-YEUNG/AAE-Freshman-projuct-group-2/blob/main/task3-figure.png)

---
### <a name="task4"></a> Task 4: Methodology, Results and Discussion

---
### <a name="reflective-essay"></a> Reflective Essay
- Chan Kai Hin
- Pu Yuxuan
- Sim Ji Tong
- Yeung Shun Kit
- Zeng Muxi

--- 
### <a name="references"></a> References
