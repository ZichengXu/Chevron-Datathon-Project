# Chevron-Datathon-Project

## Inspiration
The multilayer perceptron is a fully connected class feedforward artificial neural network ANN. The rationale we apply MLPs contributes to their capability for solving sophisticated problems stochastically. 	Interpreting regression prediction in which real-valued quantities are collectively presented through concise sets of values makes it possible for us to generate approximation solutions. 


## What it does
Our model takes in 16 independent variables that we parsed from 29 given MSN variables. Within the 16 variables, five come from the outer sources, which are GDP, total energy consumption (by the state in a year), Population, average energy price within a year, and the state government's total expenditure. It will predict the state government’s annual assistance to private renewable energy companies. 

## How we built it
We have no prior knowledge of any of the models, so we started with the most basic linear regression model and went further. The linear regression model has a huge loss with the data but it also gives us important information about the data, which suggests the correlation between variables. In the next step, we searched and found MLP, which is a more complex neural network model. We then test the model with different layers and different neurons in each layer. At first, we choose hundreds of neurons in each layer and we found that it is too complex for 250 data points we move to fewer neurons with fewer layers which improves the model significantly.

## Challenges we ran into
We were initially solely considering the 29 given MSN parameters, which gave us a rooted MSE of 170,000,000. We then tried multiple other models, such as linear regression. But neither gave us a significant improvement in the rotted MSE. So we switch our attention to mining data from other sources. After integrating five outside sources into our model, we successfully reduced the rooted MSE to 29,000,000. 

## Accomplishments that we're proud of
We utilized the keras package in python and built our neural network model. We also reduce the size of data from 7595x8 to 250x38, which is an 85 percent reduction, so the model can handle the training data more efficiently. 

## What's next for Three with One
We will continue to check on other neural network algorithms and find a model that fits the data better. We also believe that with more data, we will be able to reduce the rooted mean square area. The neural network is a powerful machine learning prediction model, and we see its application in many other fields, such as COVID tracking, stock market prediction, and so on. We are interested in applying our knowledge to all these fields.
