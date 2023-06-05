# The 100 Prisoners Riddle

The original riddle was proposed by computer scientist Peter Bro Miltersen in a 2003 paper. The riddle presents a challenge for 100 convicts who are numbered from 1 to 100. They must enter a room with 100 labeled boxes and find the box containing their respective numbers. The catch is that they can only communicate and devise a strategy before the challenge begins. If all the prisoners succeed in locating their numbers by opening at most 50 boxes each, they will be freed. The riddle asks us to determine the chances of success for the convicts.

## Solution Description

### The Naive Approach

The naive approach, where each convict opens random boxes, leads to a very low probability of success. Each prisoner has a 50% chance (50 out of 100 boxes) of finding their number with this approach. However, the games of the prisoners are independent of each other. Therefore, the overall probability of success is the multiplication of the individual probabilities (50% x 50% x ...). This results in incredibly low odds of winning the challenge, approximately 1 in 2^100. To put this into perspective, the estimated number of sand grains on Earth is 2^60. The probability of winning the game using this strategy is orders of magnitude lower than two people finding the same grain of sand.

### The Counterintuitive Solution

Remarkably, there is a strategy that significantly increases the chances of success for the prisoners. Each prisoner starts by opening the box labeled with their own number. If the box contains their number, they win. Otherwise, they proceed by opening the box labeled with the number found inside the last box. This process continues until the prisoner either finds their number or reaches 50 opened boxes. Surprisingly, this simple strategy significantly increases the probability of winning the challenge.

#### Moving in Circles

The key idea behind this strategy is that the procedure creates circuits of boxes that eventually lead to the prisoner's number. For example, let's consider a prisoner with the number 47. They start by opening box 47 and find the number 23 inside. They then proceed to open box 23, which contains the number 72. Continuing in this manner, they open box 72 and find the number 51. Now, let's consider the number they may find inside the following box. It could be their own number (47), creating a circuit of boxes: 47, 23, 72, 51, and 47 again. However, it could also be other numbers that they have not encountered yet. This is because the procedure only reveals numbers that have not yet been discovered. By applying this reasoning for each box, it becomes clear that the procedure will eventually lead to the prisoner's number. The length of these circuits determines the probability of success, with a maximum length of 50 boxes.

#### Statistical Analysis of Circuits' Length

To analyze the probability of success, we can consider the complementary question: What is the probability of having a circuit longer than 50 boxes? Let's start with the case of circuits of length 100. To create a circuit of length 100, we choose the first number out of the 100 possibilities, then continue choosing from the remaining 99 choices, and so on until there is only one choice left. The total number of unique circular arrangements of length 100 is given by 100! / 100, taking into account that circular arrangements wrap around. The probability of having one of these arrangements inside the room full of boxes is then 1 / 100. This can be generalized for numbers greater than 50, where the probability of having a circuit longer than 50 boxes becomes the sum of the individual probabilities 1 / 51, 1 / 52, and so on. This probability is approximately 0.69. Consequently, the probability of having shorter circuits is 1 - 0.69 = 0.31, which is remarkable.

## Implementation

This Python implementation demonstrates the counterintuitive solution to the 100 Prisoners Riddle. It simulates the challenge by shuffling the boxes randomly and having each prisoner follow the predetermined strategy to find their number within 50 tries. The code tracks the success or failure for each prisoner and provides an estimation of the overall success rate based on multiple iterations.

To run the implementation, execute the provided code in Python. The success rate represents the probability that all prisoners will find their numbers within 50 tries based on the shuffled boxes. You can adjust the number of iterations in the `num_iterations` variable to obtain a more accurate estimation of the success rate.

Have fun exploring the fascinating solution to the 100 Prisoners Riddle!
