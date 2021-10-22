# PolyU Eng1003 AAE Freashman Project
### Group 2 Report

### Overview   
Recently, thousands of aircrafts are operating for the aviation industry.  Finding the most efficient path for the aircrafts is an essential task to achieve. In this  project , we are assigned to design a flight path for an aircraft using python and different tools with some data researches.

---
### Table of content

---
### Background of Path Planning to Aviation Engineering

---
### Task 1

Task 1 aims to find the aircraft model with the minimum total cost flyin through the designated zone.
We were given a 70 by 70 square zone template. We changed the position of the start, goal, aditional cost areas and barriers by editing the sample code.

![Task1 numbers](https://github.com/Alex-Shun-kit-YEUNG/AAE-Freshman-projuct-group-2/blob/0ee9bf5ed7224fc73bed4743379536dc401045f9/task1%20numbers.png)


![week6 task figure](https://github.com/Alex-Shun-kit-YEUNG/AAE-Freshman-projuct-group-2/blob/main/week6%20task%20figure.png)


The minimum cost is model A380

---


Task 2 

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



Task 2 question 2
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
