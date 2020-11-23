# Matplotlib

Column: Oct 9, 2020 9:33 PM
Last edited by: Soutrik das
Parent: Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0.md, Libraries%20Frameworks%203ca2a70d57044c5f9f825e715002487c.md, Python%20py%2037f8f5b26a314016a6c73e8e8340af98.md

The idea here is to learn a bit , to see the gradient descent in one variable 

# Graphing a Quadratic

---

Coming From Deep learning , the formula of the error  $(y)$ in terms of the weight $(x)$ is 

$$y=(ix-g)^2$$

where 

- $y$ is error ( for our case squared error )
- $i$ is input ( for us , thats a constant )
- $g$ is the goal prediction ( the answer that the Network tries to predict )

    $$y=i^2x^2+g^2-2ixg$$

```python
import numpy as np 
from matplotlib import pyplot as plt 
# create 1000 equally spaced points between -10 and 10
x = np.linspace(-1, +1, 1000)

weight = 0.5
goal_pred = 0.8
input = -0.5
# calculate the y value for each element of the x vector
y = (input**2)*(x**2) +goal_pred**2-2 * input * goal_pred*weight
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

And it works , but now for the hard part ,how do I make it so that I can get the gradient descent points 

After ever for loop I want to add a point $(w,error)$ 

# Animation with matplotlib

---

It was pretty difficult 

![Matplotlib%203b87d785ac084fa8b00de436bb24b41d/newanimationerror1.gif](Matplotlib%203b87d785ac084fa8b00de436bb24b41d/newanimationerror1.gif)

[matplotlibrough.py](Matplotlib%203b87d785ac084fa8b00de436bb24b41d/matplotlibrough.py)

## Show an array graphically using colours

![Matplotlib%203b87d785ac084fa8b00de436bb24b41d/Untitled.png](Matplotlib%203b87d785ac084fa8b00de436bb24b41d/Untitled.png)

This is a randomized 100 x 100 numpy array created with `np.random.rand(100,100)`

```python
plt.imshow(a,interpolation="nearest")
# where a is the  numpy array name 
```