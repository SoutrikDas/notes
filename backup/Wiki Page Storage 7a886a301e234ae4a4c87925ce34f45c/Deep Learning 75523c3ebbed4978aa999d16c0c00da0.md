# Deep Learning

Child: NumPy%20e8320948215b4ffeb824a8756c7f33cc.md, Numerical%20Analysis%20d3653cd8f5d34935bd07cd197e0d9a8e.md, Matplotlib%203b87d785ac084fa8b00de436bb24b41d.md, Diagnosing%20Neural%20Networks%2017b2dfe8c703496fb9ba83180f8baaf1.md, Think%20Stats%20e488afe492224725ae4c64c54a2b052e.md
Column: Oct 1, 2020 8:07 PM
Last edited by: Soutrik das
Parent: Deep%20Learning%20(%20Nielsons%20Book%20)%203b2b8d76d53748e78e6d6c9708b11ea9.md
Tags: aiml, data science

Supervised Learning is when you have questions and also answers ( that you keep to yourself , and when the machine answers , you check , and if there is a difference in two answers , you tell the machine , hey , the error is this much , please try not to do this again ) 

Unsupervised learning is when even you dont have the answer. For example if you tell the AI to find structure or clusters in data ( which you did not know )  

Parametric v/s non parametric is just trial and error v/s  Probability and counting 

> As an example, let’s say the problem is to fit a square peg into the correct (square) hole. Some humans (such as babies) just jam it into all the holes until it fits somewhere (parametric). A teenager, however, may count the number of sides (four) and then searchfor the hole with an equal number (nonparametric). Parametric models tend to use trial and error, whereas nonparametric models tend to count.

Supervised parametric learning is turning the knobs to find the best knob configuration , The number of knobs remain fixed , and that is by themselves the parameter part ( the parametric models have a fixed number of parameters) 

While the non parametric adjust the number of parameters depending on the data they are working on . 

# Using vectors in python

---

Create an array in python using `numpy` like so 

```python
weights=np.array([1,2,3])
```

Dot products in numpy 

```python
inputs.dot(weights) 
numpyarray1.dot(numpyarray2) 
```

Here is example code for doing dot product and neural network 

```python
import numpy as np
weights = np.array([0.1, 0.2, 0])
def neural_network(input, weights):
	pred = input.dot(weights)
	return pred
toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])
input = np.array([toes[0],wlrec[0],nfans[0]])
pred = neural_network(input,weights)
print(pred)
```

# Reading Weights

---

When the weight is like `[1,0,1]` it means `if input[0] OR input[2]`  because only then it would give a high result  or something like that ?  ( The conditions are basically conditions to activate or fire a neuron ) 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled.png)

# Prediction Basics

---

## Multiple Inputs

---

```python
import numpy as np
weights = np.array([0.1, 0.2, 0])
def neural_network(input, weights):
	**pred = input.dot(weights)**
	return pred
toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])
input = np.array([toes[0],wlrec[0],nfans[0]])
pred = neural_network(input,weights)
print(pred)
```

## Multiple Outputs

---

Here we will have three predictions . 

Before this , out prediction was just a simple value 

But after this , even our predictions are vectors 

```python
import numpy as np 
weights=np.array([0.1,0.2,0])
input=5
def neural_network(input,weights):
    return np.array(
        [weights[0]*input,
        weights[1]*input,
        weights[2]*input]
        )
```

We can make a function that multiplies  our input to different weights 

```python
import numpy as np 
weights=np.array([0.1,0.2,0])
input=5 
def neural_network(input,weights):
    return ele_mul(input, weights)

def ele_mul ( number,vector):
    output =np.zeros(len( vector))
	 //creates a zero array of length len(v)
    for i in range( len vector):
        output[i]=input*vector[i]
    return output
```

## Multiple inputs and multiple outputs

---

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%201.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%201.png)

This is where the array notations started and where from I really lost it 

So for every prediction there are 3 weights ( the number of inputs ) 

and there are 3 predictions 

Q: If there are $n$ inputs and $m$ predictions , how many weights are there ? 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%202.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%202.png)

Every prediction will have $n$ weights ,and since there are $m$ predictions , there will be $n\times m$ weights 

But how will we handle the weights ? more than that how will we even name them ? 

How many weights are there even ? Oh we calculated $m n$

This is how Andrew Trask does this 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%203.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%203.png)

If we number it like this 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%204.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%204.png)

Then it will be something like this : 

$$w=\left[\def\arraystretch{1.5}
   \begin{array}{c:c:c:c}
\text{toes}&\text{wins}&\text{fans} \\\hline
   w_{11} & w_{12} & w_{13}& \text{hurt?} \\ \hline
   w_{21} & w_{22} & w_{23} &\text{win?}\\
  \hdashline
   w_{31} & w_{32} & w_{33} & \text{sad?}
\end{array} \right]$$

Looks okay , but I do not know how it would look if we were to add more layers on top of it 

Here is how 3b1b does it 

[Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/vlc-record-2020-09-29-10h11m39s-1-But_what_is_a_Neural_Network___Deep_learning_chapter_1.mp4-.mp4](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/vlc-record-2020-09-29-10h11m39s-1-But_what_is_a_Neural_Network___Deep_learning_chapter_1.mp4-.mp4)

So one row of weights is basically weights of a single prediction 

And indeed it is , even in my way of doing this , one row is for one prediction ( for example `hurt?` ) 

$$w=\left[\def\arraystretch{1.5}
   \begin{array}{c:c:c:c}
\text{toes}&\text{wins}&\text{fans} \\\hline
   w_{11} & w_{12} & w_{13}& \text{hurt?} \\ \hline
   w_{21} & w_{22} & w_{23} &\text{win?}\\
  \hdashline
   w_{31} & w_{32} & w_{33} & \text{sad?}
\end{array} \right]$$

Now how do I dot product ? Actually matrix multiplication 

```python
>>> weights=np.arange(9).reshape(3,3)
>>> weights
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> input=np.arange(3).reshape(3,1)
>>> input
array([[0],
       [1],
       [2]])
>>> pred=weights.dot(input)
>>> pred
array([[ 5],
       [14],
       [23]])
```

- How to define a 2D numpy array

    You can do it the hard way 

    ```python
    a=np.array([[0,1,2],
    						[3,4,5],
    						[6,7,8]])
    ```

    Or if you just want to test something , you can use a simple array

    ```python
    a=np.arange(9) # this creates a 9 memeber linear array from 1 to 8
    a=np.arange(9).reshape(3,3) # this reshapes the linear to 3 x 3 matrix 
    ```

Here is a small neural network built with  random weights and input ( not really random ) 

```python
import numpy as np
weights = np.arange(9).reshape(3, 3)
inpt = np.arange(1,4,1).reshape(3, 1)
def neural_network( inpt , weights):
	pred=weights.dot(inpt)
	return pred 

print( neural_network(inpt,weights))
```

## A three layer neural network ?

---

Here is the one im trying to make 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%205.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%205.png)

And here is the code , this time I used `random.rand(r,c)` 

```python
import numpy as np
weight1 = np.random.rand(3,3)
weight2 = np.random.rand(3,3)
weights=[weight1,weight2]
inpt = np.random.rand(3, 1)
def neural_network( inpt ,weights ):
	temp=weights[0].dot(inpt)
	pred=weights[1].dot(temp)
	return pred 

print( neural_network(inpt,weights))
```

# Compare and Learn Basics

---

## Error

---

There are many ways of measuring error , but we will look at the mean squarred error 

$$E=\sum (x-\bar x)^2$$

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%206.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%206.png)

So how are we going to find the error ? we obviously need some pre known result , from which we can get the error. If there is no bulls eye , how will the archer know  how much he has missed ? 

For us  that bulls eye is the `goal_pred`

I think this code does it pretty well  

```python
import numpy as np
weight=np.random.rand(1,1)
input=np.random.rand(1,1)
goal_pred=np.random.rand(1,1)

def neural_network(input,weight):
	pred=weight.dot(input)
	error=goal_pred-pred
	print(error)
	se=error**2
	print(se)
	return pred

pred=neural_network(input,weight)
```

## Learning  Hot and Cold

---

At the end of the day learning is just adjusting the knobs so that the average error goes near to zero 

> How do you know whether to turn the knob up or down? Well, you try both up and down and see which one reduces the error! Whichever one reduces the error is used to update `knob_weight`.

So we are gonna do if else 

```python
import numpy as np
weight=0.2
input=6
goal_pred=2
step=0.01

def neural_network(input,weight):
	pred=weight*(input)
	error=goal_pred-pred
	
	se=error**2
	
	return pred

pred=neural_network(input,weight)
for i in range(10):
	pred=neural_network(input,weight)
	error=goal_pred-pred
	se=error**2
	se1=(goal_pred-neural_network(input,weight+step))**2
	se2=(goal_pred-neural_network(input,weight-step))**2
	print(se)
	print(se1)
	print(se2)
	print("-------")
	if (se1<se2):
		weight=weight+step
	if se1>se2 :
		weight=weight-step
```

This reduces or increases the weight by `step` everytime 

This is an improvement to the logic 

```python
if se>se1 or se>se2:
        if (se1<se2):
            weight=weight+step
        if se1>se2 :
            weight=weight-step
```

> What if you had a way to compute both direction and amount for each weight without having to
repeatedly make predictions?

Right now , we arent doing this ? 

We are doing the direction by checking with if 

However the amount we have to correct each weight is constant `step` , we could use help with that 

## Gradient Descent ( Grant )

---

 Grant says to put all the weights  into a vector 

$$\vec V=\begin{bmatrix}
w_1 \\
w_2 \\
w_3 \\
\vdots \\
w_n

\end{bmatrix}$$

Find 

$$\nabla \vec V= ?$$

## Gradient Descent ( Adnrew Trask)

---

He says to 

```python
direction_and_amount= (pred - goal_pred) * input 
weight=weight-direction_and_amount
```

This in contrast to just hot and cold learning has three significances 

 

> These three attributes have the combined effect of translating the pure error into the absolute amount you want to change weight. They do so by addressing three major edge cases where the pure error isn’t sufficient to make a good modification to weight.

With hot or cold learning , you were checking at every point , if its better to increase the weight or to decrease it . But that took huge computations , but here , in gradient descent 

$$\nabla \cdot \vec a$$

the gradient is the direction of steepest ascent , that means , engative of gradient is the steepest descent 

$$-\nabla \cdot \vec a$$

So we know which way to move , instead of checking both ways ( that was still feasable in single dimension , it would get more and more impossible as the weights/dimensions increase ) 

Actually , since out error function is 

$$y=(g-ix)^2$$

$$y=i^2x^2+g^2-2igx$$

the slope at any point is 

$$\dot y(x)=2i^2x-2ig=2i(\overbrace{ix-g}^{delta})$$

So how do we use this ?

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%207.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%207.png)

At any point , if the slope is negative , we want to increase the weight , 
If the slope is positive we want to decrease the weight 

So what do we do with the slope ? 

$$w=w-\dot y$$

if $\dot y$ is negative , $w$ increases 

and if $\dot y$ is positive , $w$ decreases 

So that is how andrew was able to use the gradient descent without any differentiation. He quietly slipped this formula in  just after gradient descent

### Stopping

---

It basically only adjusts weight when the input is non zero , when the input is zero  , then why should it adjust its weight ? Because that input didnt contribute to the error at all 

### Scaling

---

And it also reduces the step as we come near and near a minima 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%208.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%208.png)

As you can see, the step size changes ( as the colour changes from red to blue ) 

But this often goes out of control pretty quickly 

For example this curve 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%209.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%209.png)

And this is out starting point ( by starting point I mean the initial error value )

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2010.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2010.png)

Initially the difference(error) is only this big . 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2011.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2011.png)

But suppose you took a step  corresponding to that error 

And the error increased. Now your next step length is going to be even more ( because step lengths $\propto \text{ error}$

 

$$\text{step}= \text{ input } \times \text{ error }$$

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2012.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2012.png)

And it goes out of bounds with flying colours 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2013.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2013.png)

### Negative Reversal

---

The thing is , 

- if input is `positive`
- increasing weight results in increased prediction

But if 

- input is `negative` (sometimes it happens )
- increasing weight results in decreased prediction

to counter this , our step includes the sign of the input 

But this is still a bit difficult to understand 

Why does it matter at all ? What would happen if we didnt have negative reversal with us 

that is , instead of 

```python
direction_and_amount= (pred - goal_pred) * input 
weight=weight-direction_and_amount
```

what would happen if we were to use this ?

```python
direction_and_amount= (pred - goal_pred) *  abs(input)
weight=weight-direction_and_amount
```

- lets experiment

    When using this code 

    ```python
    import numpy as np 
    weight = 0.5
    goal_pred = 0.8
    input = 0.5
    for iteration in range(20):
        pred = input * weight
        error = (pred - goal_pred) ** 2
        direction_and_amount = (pred - goal_pred) * input
        weight = weight - direction_and_amount
        print("Error:" + str(error) + " Prediction:" + str(pred))
    ```

    The log is such : 

    ```python
    Error:0.30250000000000005 Prediction:0.25
    Error:0.17015625000000004 Prediction:0.3875
    Error:0.095712890625 Prediction:0.49062500000000003
    Error:0.05383850097656251 Prediction:0.56796875
    Error:0.03028415679931642 Prediction:0.6259765625
    Error:0.0170348381996155 Prediction:0.669482421875
    Error:0.00958209648728372 Prediction:0.70211181640625
    Error:0.005389929274097089 Prediction:0.7265838623046875
    Error:0.0030318352166796153 Prediction:0.7449378967285156
    Error:0.0017054073093822882 Prediction:0.7587034225463867
    Error:0.0009592916115275371 Prediction:0.76902756690979
    Error:0.0005396015314842384 Prediction:0.7767706751823426
    Error:0.000303525861459885 Prediction:0.7825780063867569
    Error:0.00017073329707118678 Prediction:0.7869335047900676
    Error:9.603747960254256e-05 Prediction:0.7902001285925507
    Error:5.402108227642978e-05 Prediction:0.7926500964444131
    Error:3.038685878049206e-05 Prediction:0.7944875723333098
    Error:1.7092608064027242e-05 Prediction:0.7958656792499823
    Error:9.614592036015323e-06 Prediction:0.7968992594374867
    Error:5.408208020258491e-06 Prediction:0.7976744445781151
    ```

    Now lets try with `abs(input)` 

    ```python
    import numpy as np 
    weight = 0.5
    goal_pred = 0.8
    input = 0.5
    for iteration in range(20):
        pred = input * weight
        error = (pred - goal_pred) ** 2
        direction_and_amount = (pred - goal_pred) * abs(input)
        weight = weight - direction_and_amount
        print("Error:" + str(error) + " Prediction:" + str(pred))
    ```

    ```python
    Error:0.30250000000000005 Prediction:0.25
    Error:0.17015625000000004 Prediction:0.3875
    Error:0.095712890625 Prediction:0.49062500000000003
    Error:0.05383850097656251 Prediction:0.56796875
    Error:0.03028415679931642 Prediction:0.6259765625
    Error:0.0170348381996155 Prediction:0.669482421875
    Error:0.00958209648728372 Prediction:0.70211181640625
    Error:0.005389929274097089 Prediction:0.7265838623046875
    Error:0.0030318352166796153 Prediction:0.7449378967285156
    Error:0.0017054073093822882 Prediction:0.7587034225463867
    Error:0.0009592916115275371 Prediction:0.76902756690979
    Error:0.0005396015314842384 Prediction:0.7767706751823426
    Error:0.000303525861459885 Prediction:0.7825780063867569
    Error:0.00017073329707118678 Prediction:0.7869335047900676
    Error:9.603747960254256e-05 Prediction:0.7902001285925507
    Error:5.402108227642978e-05 Prediction:0.7926500964444131
    Error:3.038685878049206e-05 Prediction:0.7944875723333098
    Error:1.7092608064027242e-05 Prediction:0.7958656792499823
    Error:9.614592036015323e-06 Prediction:0.7968992594374867
    Error:5.408208020258491e-06 Prediction:0.7976744445781151
    ```

    There is almost no problem at all !? Maybe thats because negative reversal fixes things when inputs are negative , but here the inputs arent negative at all 

    So lets make the inputs negative 

    The following code 

    ```python
    import numpy as np 
    weight = 0.5
    goal_pred = 0.8
    input = -0.5
    for iteration in range(20):
        pred = input * weight
        error = (pred - goal_pred) ** 2
        direction_and_amount = (pred - goal_pred) * abs(input)
        weight = weight - direction_and_amount
        print("Error:" + str(error) + " Prediction:" + str(pred))
    ```

    ```python
    Error:1.1025 Prediction:-0.25
    Error:1.72265625 Prediction:-0.5125
    Error:2.691650390625 Prediction:-0.840625
    Error:4.2057037353515625 Prediction:-1.25078125
    Error:6.571412086486816 Prediction:-1.7634765625
    Error:10.26783138513565 Prediction:-2.404345703125
    Error:16.043486539274454 Prediction:-3.20543212890625
    Error:25.067947717616335 Prediction:-4.206790161132813
    Error:39.16866830877552 Prediction:-5.458487701416016
    Error:61.201044232461754 Prediction:-7.02310962677002
    Error:95.62663161322149 Prediction:-8.978887033462524
    Error:149.41661189565858 Prediction:-11.423608791828155
    Error:233.46345608696654 Prediction:-14.479510989785194
    Error:364.7866501358852 Prediction:-18.299388737231492
    Error:569.9791408373206 Prediction:-23.074235921539366
    Error:890.5924075583135 Prediction:-29.042794901924207
    Error:1391.5506368098647 Prediction:-36.50349362740526
    Error:2174.297870015414 Prediction:-45.82936703425658
    Error:3397.340421899084 Prediction:-57.48670879282072
    Error:5308.344409217319 Prediction:-72.0583859910259
    ```

    My god , it overshoots , and keeps doing so 

    Lets now try it with negative reversal 

    ```python
    import numpy as np 
    weight = 0.5
    goal_pred = 0.8
    input = -0.5
    for iteration in range(20):
        pred = input * weight
        error = (pred - goal_pred) ** 2
        direction_and_amount = (pred - goal_pred) * (input)
        weight = weight - direction_and_amount
        print("Error:" + str(error) + " Prediction:" + str(pred))
    ```

    Wowo

    ```python
    Error:1.1025 Prediction:-0.25
    Error:0.6201562500000002 Prediction:0.012500000000000011
    Error:0.3488378906249999 Prediction:0.20937500000000003
    Error:0.19622131347656252 Prediction:0.35703125
    Error:0.11037448883056644 Prediction:0.4677734375
    Error:0.062085649967193644 Prediction:0.550830078125
    Error:0.034923178106546424 Prediction:0.61312255859375
    Error:0.019644287684932357 Prediction:0.6598419189453125
    Error:0.011049911822774457 Prediction:0.6948814392089844
    Error:0.006215575400310641 Prediction:0.7211610794067382
    Error:0.0034962611626747353 Prediction:0.7408708095550537
    Error:0.001966646904004536 Prediction:0.7556531071662903
    Error:0.0011062388835025535 Prediction:0.7667398303747177
    Error:0.0006222593719701891 Prediction:0.7750548727810382
    Error:0.0003500208967332314 Prediction:0.7812911545857787
    Error:0.00019688675441244187 Prediction:0.7859683659393341
    Error:0.00011074879935699914 Prediction:0.7894762744545005
    Error:6.22961996383129e-05 Prediction:0.7921072058408754
    Error:3.5041612296551e-05 Prediction:0.7940804043806565
    Error:1.971090691680969e-05 Prediction:0.7955603032854924
    ```

    It actually still reached the minima ! 

Conclusion: It is very important if the inputs are negative ( it helps to prevent overshooting ) 

But if the input is positive , it doesnt really help much 

## Using alpha ( modifying Gradient Descent )

He redefines the direction and amount using delta 

$$\text{direction and amount}= (\overbrace{\text{pred} - \text{goalpred}}^{\text{delta}}) *  \text{input}$$

His new code is

```python
number_of_toes = [8.5]
win_or_lose_binary = [1] # (won!!!)
input = number_of_toes[0]
goal_pred = win_or_lose_binary[0]
pred = neural_network(input,weight)
error = (pred - goal_pred) ** 2
delta = pred - goal_pred
weight_delta = input * delta
alpha = 0.01
weight -= weight_delta * alpha
```

## Revisiting Gradient Descent in One Dimension

---

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2014.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2014.png)

$$\frac{\partial C_0}{\partial w^{(L)}}=\frac{\partial z^{(L)}}{\partial w^{(L)}}\frac{\partial a^{(L)}}{\partial z^{(L)}}\frac{\partial C_0}{\partial a^{(L)}}$$

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2015.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2015.png)

So since our cost function is 

$$C_0=(a^{(L)}-y)^2$$

Where

- $y$ is the target
- $a^{(L)}$ is the output of layer $L$ ( which happens to be our last layer ) hence it is the final output
- $z^{(L)}=a^{(L-1)}w^{(L)}+b^{(L)}$

$$\frac{\partial C_0}{\partial w^{(L)}}=\frac{\partial z^{(L)}}{\partial w^{(L)}}\frac{\partial a^{(L)}}{\partial z^{(L)}}\times 2(a^{(L)}-y)$$

So since $a^{(L)}=\sigma (z^{(L)})$

$$\frac{\partial a^{(L)}}{\partial z^{(L)}}=\sigma^\prime(z^{(L)})=\sigma(z)(1-\sigma (z))$$

And the last one is 

$$\frac{\partial z^{(L)}}{\partial w^{(L)}}=a^{(L-1)}$$

So our Gradient is going to be 

$$\frac{\partial C_0}{\partial w^{(L)}}
=
a^{(L-1)} 
\phantom{a}
\sigma(z)(1-\sigma (z))
\phantom{a}
 2(a^{(L)}-y)$$

So what is this and how does this fit into the bigger picture ? 

The bigger picture is to find the gradient and to walk in the direction that is opposite to it 

so what exactly is the gradient ?

$$\nabla C(w^{(L)},w^{(L-1)}\cdots)=
\left[ 
\begin{matrix}
\frac{\partial C}{\partial w^{(L)}} \\ \\
\frac{\partial f}{\partial w^{(L-1)}} \\
\\ \frac{\partial f}{\partial w^{(L-2)}}\\ \\
\vdots
\end{matrix}
\right]$$

and what did we find ? 

$$\nabla C(w^{(L)},w^{(L-1)}\cdots)=
\left[ 
\begin{matrix}
\colorbox{red}{\boxed{\frac{\partial C}{\partial w^{(L)}}}} \\ \\
\frac{\partial f}{\partial w^{(L-1)}} \\
\\ \frac{\partial f}{\partial w^{(L-2)}}\\ \\
\vdots
\end{matrix}
\right]$$

We only found the red part , But did we really find it ? 

$$\frac{\partial C_0}{\partial w^{(L)}}
=
a^{(L-1)} 
\phantom{a}
\sigma(z)(1-\sigma (z))
\phantom{a}
 2(a^{(L)}-y)$$

I mean are there any variables here or we have a value like 

$$\frac{\partial C_0}{\partial w^{(L)}}
= -2.5 ?$$

For that we must revise what we know 

- We know $y$ because thats our target value
- We know $a^{(L)}$ because we found it during forward propagation
- $z$ is just the `final_inputs` as I call it in my mnist neural network , and that too we calculated during forward propagation
- $a^{(L-1)}$ is the output of the previous layer , we did that too in the forward propagation

So we have the value for

$$\frac{\partial C_0}{\partial w^{(L)}}
=
a^{(L-1)} 
\phantom{a}
\sigma(z)(1-\sigma (z))
\phantom{a}
 2(a^{(L)}-y)$$

and we can find it for any layer ie we can find $\frac{\partial C}{\partial w^{(L-2)}}$ or even $\frac{\partial C}{\partial w^{(L-1)}}$

~~Lets move on to more nodes~~ 

Before we move on , how do we actually find the gradient ? We need to find 

$$\frac{\partial C}{\partial w^{(L-1)}}$$

and this 

$$ \frac{\partial C}{\partial w^{(L-2)}}$$

I guess we can find it for every layer , because we have the values for its previous layer , the only problem would have been the error of that layer , but Tariq has solved that and taught us how to find error of previous nodes ( by distributing it ) but in this case there are no more weights so full error will fall back on the previous node 

## Revisiting Gradient Descent for multiple nodes

---

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2016.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2016.png)

We use $k$ for the whole of Layer $(L-1)$ , and $j$ to index the whole of $(L)$

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2017.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2017.png)

What does this $C_0$ mean in the below picture ? 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2018.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2018.png)

its the sum of individual cost functions 

Now the 

$$z_{j}^{(L)}=w_{j 0}^{(L)} a_{0}^{(L-1)}+w_{j 1}^{(L)} a_{1}^{(L-1)}+w_{j 2}^{(L)} a_{2}^{(L-1)}+b_{j}^{(L)}$$

$$C_{0}=\sum_{j=0}^{n_{L}-1}\left(a_{j}^{(L)}-y_{j}\right)^{2}$$

The cost function iterates and adds error from each node 

so this time how do we actually use this fact 

We again try to find the 

$$\frac{\partial C}{\partial w_{jk}^{(L)}}$$

and here we see that 

$$\frac{\partial C_{0}}{\partial w_{j k}^{(L)}}=\frac{\partial z_{j}^{(L)}}{\partial w_{j k}^{(L)}} \frac{\partial a_{j}^{(L)}}{\partial z_{j}^{(L)}} \frac{\partial C_{0}}{\partial a_{j}^{(L)}}$$

which we can find piece by piece from LHS 

$$\frac{\partial z_{j}^{(L)}}{\partial w_{j k}^{(L)}}=?$$

Lets bring the equation here

$$z_{j}^{(L)}=w_{j 0}^{(L)} a_{0}^{(L-1)}+w_{j 1}^{(L)} a_{1}^{(L-1)}+w_{j 2}^{(L)} a_{2}^{(L-1)}+b_{j}^{(L)}$$

From this we can see that for $w_{jk}$ the the term in $z_j$ will be $w_{jk} \times a_k$

$$\frac{\partial z_{j}^{(L)}}{\partial w_{j k}^{(L)}}=a_k$$

Remember $k$ corresponds to $(L-1)$ and $j$ corresponds to $(L)$ 

Moving on to the second term

$$\frac{\partial a_{j}^{(L)}}{\partial z_{j}^{(L)}} =?$$

We know that $a_j=\sigma ( z_j)$

So this part is just going to be the derivative of the Sigmoid function  which we know 

$$\frac{d(\sigma (x))}{dx}=\sigma (x)\times (1-\sigma (x) )$$

Using that here we get 

$$C_{0}=\sum_{j=0}^{n_{L}-1}\left(a_{j}^{(L)}-y_{j}\right)^{2}$$

$$\frac{\partial a_{j}^{(L)}}{\partial z_{j}^{(L)}} =\sigma(z_j)\times (1-\sigma(z_j))$$

Now the third term 

$$\frac{\partial C_{0}}{\partial a_{j}^{(L)}}$$

We know that the cost function is 

$$C_{0}=\sum_{j=0}^{n_{L}-1}\left(a_{j}^{(L)}-y_{j}\right)^{2}$$

But here $j$ is just an arbitrary number , it can be $0$ or $1$ or anything ( within some limits ). 

$$\frac{\partial C_{0}}{\partial a_{j}^{(L)}}=\frac{\partial \left( \sum_{j=0}^{n_{L}-1}\left(a_{j}^{(L)}-y_{j}\right)^{2}\right)}{\partial a_{j}^{(L)}}$$

But actually if we expand that sum term 

$$\newcommand{\a}[1]{\left( a_{#1}-y_{#1} \right)^2}
\frac{\partial C_{0}}{\partial a_{j}^{(L)}}=\frac{\partial \left(\a1+\a2+\cdots\a{j}+\cdots  \right)}{\partial a_{j}^{(L)}}$$

From this we can see that all the other terms with respect to $a_j$ is constant 

$$\frac{\partial C_{0}}{\partial a_{j}^{(L)}}=2\left( a_{j}-y_{j} \right)$$

Now putting them all together we get 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/WhatsApp_Image_2020-10-01_at_19.28.19.jpeg](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/WhatsApp_Image_2020-10-01_at_19.28.19.jpeg)

$$\frac{\partial C_{0}}{\partial w_{j k}^{(L)}}=a_k\times \sigma(z_j) (1-\sigma(z_j))\times 2\left( a_{j}-y_{j} \right)$$

We can also write it as

if converted to the variables used in Tariq Rashids neural net we get 

$$\frac{\partial C_{0}}{\partial w_{j k}^{(L)}}=\left( \text{hidden\_outputs[k]}\right)\times \left( \text{final\_outputs[j]}\right) (1-\left( \text{final\_outputs[j]}\right))\times 2\left( \text{output\_errors[j]}\right)$$

~~But the problem is how do i vectorise it ? You probably do not have to do it~~ 

Oh and dont forget the learning rate 

$$\text{change} =\alpha \times  a_k\times \sigma(z_j) (1-\sigma(z_j))\times 2\left( a_{j}-y_{j} \right)$$

But WHY is there a dot product in there , I cant understand that , [Here is the official repo](https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork/blob/master/part2_neural_network_mnist_data.ipynb)

```python
self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
```

How is he vectorising it ?

OKay so I have progressed a bit , 

The actual change that we are making to each weight is this : 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2019.png](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/Untitled%2019.png)

Now the question is how do we write it in matrix form ?Maybe something like this 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/WhatsApp_Image_2020-10-01_at_19.27.24.jpeg](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/WhatsApp_Image_2020-10-01_at_19.27.24.jpeg)

Now we need to find that matrix on the right , how do we find it ? We can use a for loop and then calculate the gradient for each individually using the following formula

$$\frac{\partial C_{0}}{\partial w_{j k}^{(L)}}=a^{(L-1)}_k\times a^L_j (1-a_j^{(L)})\times 2\left( a_{j}-y_{j} \right)$$

But we have two certain matrices that , if , we can use intelligently , we can form the matrix in the blue 

![Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/InkedWhatsApp_Image_2020-10-01_at_19.27.24_LI.jpg](Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0/InkedWhatsApp_Image_2020-10-01_at_19.27.24_LI.jpg)

and those two matrix are 

$$A=\newcommand{\a}[1]{a^{(L-1)}_{#1}\\ \\}
\text{hidden\_output}=
\left[
\begin{matrix}
\a0 \a1 \a2 \cdots 
\end{matrix} \right]$$

$$B=\left( \text{final\_output}\right)\left( 1-\text{final\_output}\right)\left( \text{output\_errors}\right)=
\newcommand{\a}[1]{a^{(L)}_{#1}\left(1-a^{(L)}_{#1} \right)\left(a^{(L)}_{#1}-y_{#1} \right) \\ \\}
\left[
\begin{matrix}
\a0 \a1 \a2 \cdots 
\end{matrix} \right]
$$

The matrix we need to make is 

$$\newcommand{\a}[2]{a^{(L-1)}_{#1}\times a^{(L)}_{#2}\left(1-a^{(L)}_{#2} \right)\left(a^{(L)}_{#2}-y_{#2} \right)}
\left[ 
\begin{matrix}
\a00 &\a10 \cdots 
\\
\\
\a01 & \a11 \cdots
\\
\\
\vdots & \vdots
\end{matrix}
\right]$$

---

Basically the problem boils down to 

You have a matrix $A$ and matrix $B$ , what operations do you do to make matrix $C$ 

$$A=\left[
\begin{matrix}
a_1 \\ a_2\\a_3 \\ \vdots \\ a_m
\end{matrix} \right]$$

$$B=\left[
\begin{matrix}
b_1 \\ b_2\\b_3 \\ \vdots \\ b_n
\end{matrix} \right]$$

$$C=\left[
\begin{matrix}
a_1b_1 & a_2b_1 &\cdots & a_mb_1 
\\
a_1b_2 & a_2b_2 &\cdots & a_mb_2
\\
\vdots &\vdots & \ddots & \vdots
\\
a_1b_n & a_2b_n &\cdots & a_mb_n
\end{matrix} \right]$$

Which we can simply do by 

$$B \times A^T$$

Why because $B$ is $n \times 1$ and $A^T$ is $1\times m$ , so we can multiply them and get $C$ 

> This operation is called outer product

And this kind of multiplication can be done very simply 

```python
a=np.random.rand(1,3)
b=np.random.rand(3,1)
>>>b*a
array([[0.01838683, 0.03246115, 0.07185034],
[0.07381603, 0.13031901, 0.28845143],
[0.12245251, 0.2161846 , 0.47850852]])

>>>np.dot(b,a)

array([[0.01838683, 0.03246115, 0.07185034],
[0.07381603, 0.13031901, 0.28845143],
[0.12245251, 0.2161846 , 0.47850852]])
```

Going back to our original $A$ and $B$ , this means we can use the following code 

$$A=\newcommand{\a}[1]{a^{(L-1)}_{#1}\\ \\}
\text{hidden\_output}=
\left[
\begin{matrix}
\a0 \a1 \a2 \cdots 
\end{matrix} \right]$$

$$B=\left( \text{final\_output}\right)\left( 1-\text{final\_output}\right)\left( \text{output\_errors}\right)=
\newcommand{\a}[1]{a^{(L)}_{#1}\left(1-a^{(L)}_{#1} \right)\left(a^{(L)}_{#1}-y_{#1} \right) \\ \\}
\left[
\begin{matrix}
\a0 \a1 \a2 \cdots 
\end{matrix} \right]
$$

$$B*A^T=\text{np.dot(B,A.T)}$$

$$B*A^T=\text{np.dot(}\left( \text{final\_output}\right)\left( 1-\text{final\_output}\right)\left( \text{output\_errors}\right)\text{,A.T)}$$

$$B*A^T=\text{np.dot(}\left( \text{final\_output}\right)\left( 1-\text{final\_output}\right)\left( \text{output\_errors}\right)\text{, \text{hidden\_output}.T)}$$

Yes! I have finally made sense of this line of code 

```python
self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
```

The only pieces remaining are the learning rate which frankly didnt ever pose a problem in the understanding 

Oh , and why are we adding here ?Shouldnt we be substracting ?