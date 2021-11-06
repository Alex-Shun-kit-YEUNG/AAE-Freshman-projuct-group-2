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
After running the code, cost values o part 1 to 3, as well as the total cost will be shown.

We can find the total cost of each aircraft model by runnung the code with modified number factor. It would be clearest to show all related cost numbers for each model at the same to for easy comparison. However, we found it difficult to write a code for such operation together with the code for finding the shortest path. Thus we decided to make a separate code just to show all the relavent numbers and compare the values to find the model with the lowest cost by using the list function in the code.

Here is the link to the code for comparing the numbers:

[comparison code](AAE-Freshman-projuct-group-2)

![Task1 numbers](https://github.com/Alex-Shun-kit-YEUNG/AAE-Freshman-projuct-group-2/blob/0ee9bf5ed7224fc73bed4743379536dc401045f9/task1%20numbers.png)

Therefore, we found the A380 is the model with the lowest cost when travelling through our designated map.

This is the map for our group. The red line represents the shortest distance from the start to the goal found using the a star path finding code.
![week6 task figure](https://github.com/Alex-Shun-kit-YEUNG/AAE-Freshman-projuct-group-2/blob/main/week6%20task%20figure.png)


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

In this freshmen project, I have learnt how to use programming and python for the first time. Programming has amazed me that by typing simple characters and symbols solely using the keyboard, almost all functions can be done, like coding for a calculator, plotting a path planning graph by matplotlib and inserting an image in a project report. 

Working on this project requires self-learning at the same time since python is a completely new language. We learnt the new programming language by searching for information on the internet and trying on our own repeatedly. When we were working on the compulsory task 1, difficulties were encountered in editing the fuel-consuming area and time-consuming area. We do not understand the function of  “for i / j in range”. Therefore we  took a photo of the original graph for record, then changed the data in each section accordingly and observed the difference in the graph so as to analyse what each data is representing. Finally we are able to conclude that the range for i is the start and end point on the x-axis while the range for j is the start and end point on the y-axis. During the process of searching for the use of different programming functions from the internet and Youtube videos, I have found that I become more motivated in learning things actively by myself and many obstacles faced when doing the project can be solved easily and quickly. It is believed that self-motivation is an important key to work efficiently.

Other than the knowledge on the technical side, I have also widened my horizon about GitHub and readme. GitHub is a platform where everyone in the world can share their programming work and collaborate with others. Readme is also one of the new things I have learnt to use. Usually we used to type a project report on google document or microsoft word file. However, readme is completely different from them. For example, inserting an image by typing a specific function and the link of the image, linking the table of contents with the heading of each sections by adding anchors, and bolding the text using “**”. These functions are all very interesting that we no longer depend on the buttons at the tool bar, but typing out the formatting and functions on our own instead.

In overall, I had a great experience working on the path planning project by programming.

- Yeung Shun Kit

I am glad that I chose the AAE freshmen project, as I realized I had gained some formidable learning experience.

First, I learned a lot about programming. Before entering university, I had rarely tried anything related to programming. With this freshmen project, it gave me a good purpose and opportunity to really dig deeper into to world of coding. Although at the end of this project, I have only acquired some very basic ideas about coding, the process still gave me a lot of insights and raised my interest in the software side of engineering. I will definitely try more on coding in the future and hopefully develop some useful programming skills for learning and career purposes.

Second, this project made me realize the importance of self-learning. I was so used to the secondary education system in which I was fed with information from teachers. It took me quite some time to adapt to the self-learning method. When the tutors gave us the tasks, they rarely showed us how to actually do them. I was confused and had to find the solution together with my groupmates. Although the process was tough, because I didn’t know where to start, as the time goes on, I get the hang of self-learning methods and made some good process. From the learning experience, I realized that from this point on, more learning will be done in self-learning, thus I will make sure to be more proactive in learning on my own.

Lastly, I have acquired more experience on being a leader of a team. I volunteered as the leader at the beginning of the workshop. And throughout the project, I have realised the importance of the leader of a team. As the team leader, not only do you have to assign proper work to team member with the corresponding abilities, but you also need to understand the concept and flow of the project such that you can monitor the progress. Although I did not understand a lot about programming, coordinating the team and asking member with respective knowledge to help with the task makes up my limitations. 



- Zeng Muxi

--- 
### <a name="references"></a> References
