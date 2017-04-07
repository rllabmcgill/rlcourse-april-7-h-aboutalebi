# Performance Of Different SARSA methods on Non-Stationary Environment

In this work, I tried to check the performance of SARSA, Expected SARSA, Double Q-Learning and Q-Learning in a nonstationary environment.


The environment I am considering here is a square grid with length 10. We start at cell [1,1] and our goal is to reach the cell [10,10]. Each cell in the maze has different reward, the reward is a gaussian distribution random variable with mean equal to -10 and variance equal to 1.5. We chose these numbers to assure that each additional step we take is going to cost and difference between the cells of the grid is noticeable. The goal has reward zero. In the following, we have tested different SARSA methods individually based on the different alpha parameter. Finally, we will compare all of them together assuming that the alpha is equal to 1.

##SARSA
