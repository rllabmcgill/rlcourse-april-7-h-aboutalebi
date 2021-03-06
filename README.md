# Performance Of Different SARSA methods on Non-Stationary Environment

In this work, I tried to check the performance of SARSA, Expected SARSA, Double Q-Learning and Q-Learning in a nonstationary environment.


The environment I am considering here is a square grid with length 10. We start at cell [1,1] and our goal is to reach the cell [10,10]. Each cell in the maze has different reward, the reward is a gaussian distribution random variable with mean equal to -10 and variance equal to 1.5. We chose these numbers to assure that each additional step we take is going to cost and difference between the cells of the grid is noticeable. The goal has reward zero. We repeat each epoch 100 times. At the end we will change the reward of each cell randomly and save the Q values for new epoch. We have donethis reset and run for total of 10 times. In the following, we have tested different SARSA methods individually based on the different alpha parameter. Finally, we will compare all of them together assuming that the alpha is equal to 1. The codes are available in the other folder

## SARSA

First we tried SARSA method for different alpha. As it can be seen, for alpha equal to 1 we get the best result. At the begining we have high variance no matter what alpha we choose. For alpha equal to 0.01, we have high variance.

![sarsa2](https://cloud.githubusercontent.com/assets/5707322/24784325/c672487e-1b1f-11e7-916f-90d40209f18a.png)


## Expected SARSA

As it can be seen, again for alpha equal to 1 we get the best result. At the begining we have high variance no matter what alpha we choose. For alpha equal to 0.01, we have high variance. It seems this graph is better than simple SRSA method, as we have faster learning rate.

![figure2](https://cloud.githubusercontent.com/assets/5707322/24784368/0ebe4e70-1b20-11e7-88d4-ec4a565d44e4.png)


## Q_Learn

As it can be seen, again for alpha equal to 1 we get the best result. At the begining we have high variance no matter what alpha we choose. For alpha equal to 0.01, we have high variance. It seems this graph is better than simple SRSA method, as we have faster learning rate.

![figure_3](https://cloud.githubusercontent.com/assets/5707322/24784420/698b9754-1b20-11e7-8348-c9074ee2b18e.png)


## Double Q_Learn

As it can be seen, again for alpha equal to 1 we get the best result. At the begining we have high variance no matter what alpha we choose. For alpha equal to 0.01, we have high variance. It seems this graph is better than simple SRSA method, as we have faster learning rate. It seems this graph has much more variance than the other graphs in nonstationery environment. Especially, in the beggining of the epoch reset.

![figure_4](https://cloud.githubusercontent.com/assets/5707322/24784447/a0d076bc-1b20-11e7-879e-2f2ddfa7e2ac.png)


Finally here is the graph for comparision of different method when we set alpha equal to 1:

![figure_5](https://cloud.githubusercontent.com/assets/5707322/24784469/d0fa608c-1b20-11e7-8dda-d232668a3a54.png)

 A closer look:
 ![figure_6](https://cloud.githubusercontent.com/assets/5707322/24784465/cc09d80a-1b20-11e7-8d32-1123a2e9249f.png)
 
 If we use log format in axis, the plot becomes even more clear:
 
 ![figure_x](https://cloud.githubusercontent.com/assets/5707322/24798527/648b99b8-1b64-11e7-93a6-272743917021.png)
 
 It seems that here double Q learn and simple sarsa has the worst performance on this synthetic environment while Q Learn SARSA is having better performance and faster learning rate. 



