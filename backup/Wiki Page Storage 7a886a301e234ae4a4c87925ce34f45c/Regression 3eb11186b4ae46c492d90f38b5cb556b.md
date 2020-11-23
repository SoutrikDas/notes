# Regression

Column: Sep 28, 2020 7:53 AM
Last edited by: Soutrik das
Tags: aiml, data science

# Simple Linear Regression

---

It allows us to model mathematically the realtion between variables 

The best fit line for only one variable is the mean 

> with only one variable, and no other information, the best prediction for the next measurement is the mean of the sampe itself. The variability in the tips can only be explained by the tips themselves

![Regression%203eb11186b4ae46c492d90f38b5cb556b/Untitled.png](Regression%203eb11186b4ae46c492d90f38b5cb556b/Untitled.png)

Goodness of the fit 

We can measure the distance of the point from the line 

 These are called Residuals or error ( the distance from the best fit line to the points )

![Regression%203eb11186b4ae46c492d90f38b5cb556b/Untitled%201.png](Regression%203eb11186b4ae46c492d90f38b5cb556b/Untitled%201.png)

The sum of the residual is always $0$ 

But we can square the residual 

![Regression%203eb11186b4ae46c492d90f38b5cb556b/Untitled%202.png](Regression%203eb11186b4ae46c492d90f38b5cb556b/Untitled%202.png)

Sum of Squared Errors (SSE) = 120 

The goal of simple linear regression is to create a  linear model that minimizes the sum of squares of the residuals / error ( SSE) 

So when we do Linear Regression , we will compare ( " the fir " ) to this model , where the second variable doesnt even exist 

![Regression%203eb11186b4ae46c492d90f38b5cb556b/Untitled%203.png](Regression%203eb11186b4ae46c492d90f38b5cb556b/Untitled%203.png)

 

Simple Linear regression is really a comparison of two models 

one is where the independent variable does not even exist

And the other uses the best fit regression line ( where we use the independent variable ) 

 

A SLR equation is just like a straight line equation 

$$y=mx+b$$

$$y=\beta_0+\beta_1x+\overbrace{\epsilon}^{\text{error}}$$

The $y=\beta_0 +\beta_1 x$ part explains the points through regression and the error helps explain the unexplained variation 

If your linear regression passes through all the points , there wont be any error  , hence our linear regression perfectly explains every variation ( and hence we dont need another term to explain anything , $\epsilon=0$ ) 

We write this like 

$$E(y)=\beta_0 +\beta_1 x$$

Where $E(y)$ is the mean or expected value of $y$, for a given value of $x$