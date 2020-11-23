# Multivariable Calculus

Column: Sep 30, 2020 4:36 PM
Last edited by: Soutrik das
Parent: three%20js%202046713f87c64c2da1812a98f8cc20ce.md
Tags: chapter, maths

All these notes are based on Grant's videos from Khan academy ( [link](https://www.youtube.com/playlist?list=PLSQl0a2vh4HC5feHa6Rc5c0wbRTx56nF7) )

 

From What I have learnt it seems that mutlivariable functions can be visualised and thought of in different ways , not just graph. And the different ways are actually important because Later in higher dimensions it will be a problem if we only think of funtions as graphs , because there wont be any graphs in higher dimensions 

# Gradient

---

## How to compute it ?

---

For example if we have a function

$$f(x,y)=x^2 \sin y$$

How do we find the gradient ? 

Lets first find the partial derivatives wrt x and wrt y 

$$\frac{\partial f}{\partial y}=x^2\cos y$$

$$\frac{\partial f}{\partial x}=2x\sin y$$

then the gradient , represented  by $\nabla f$ , and here since there are two inputs , $\nabla f(x,y)$ 

$$\nabla f(x,y)=
\left[ 
\begin{matrix}
2x\sin y \\
x^2\cos y
\end{matrix}
\right]$$

And that is it !

In general

$$\nabla f(x,y)=
\left[ 
\begin{matrix}
\frac{\partial f}{\partial x_1} \\ \\
\frac{\partial f}{\partial x_2} \\
\\ \frac{\partial f}{\partial x_3}\\ \\
\vdots
\end{matrix}
\right]$$

But Gradient as a operator has a bit of different definition ( atleast rigorously )

$$\nabla
\left[ 
\begin{matrix}
\frac{\partial }{\partial x_1} \\ \\
\frac{\partial }{\partial x_2} \\
\\ \frac{\partial }{\partial x_3}\\ \\
\vdots
\end{matrix}
\right]$$

You can dot or cross this operator To get either Divergence or Curl

## Its Geometrical Meaning ?

---

> The direction of the steepest Ascent

The Direction indeed is Always towards the steepest ascent at that point , but what about the magnitude ? 

> the magnitude tells you about the steepness of that place

## Directional Derivatives

---

We know that partial derivative means ,

![Multivariable%20Calculus%206ce8e7f50891492bad2c6a31d0dbb7e1/Untitled.png](Multivariable%20Calculus%206ce8e7f50891492bad2c6a31d0dbb7e1/Untitled.png)

How much would the $f$ nudge when we nudge the inputs in the $x$ ( keeping others constant ) 

That is partial derivative of $f$ wrt $x$  Similarly for $y$ we would nudge the input in the $y$ direction to see the effect it causes of the $f$ numberline 

But a Directional Derivative is when instead of nudging only one input , we nudge them together ( in some ratio ) 

Another way to say it : In the case of partial derivatives , we were only moving along x axis or y axis to get $\frac{\partial f}{\partial x}$ or $\frac{\partial f}{\partial y}$ , but now we are going to move according to a vector ( some combination of $x$ and $y$ ) and see the effect of that movement on $f$ 

![Multivariable%20Calculus%206ce8e7f50891492bad2c6a31d0dbb7e1/Untitled%201.png](Multivariable%20Calculus%206ce8e7f50891492bad2c6a31d0dbb7e1/Untitled%201.png)

But $\vec v$ in this picture is rather big , in reality out vector would be multiplied by a very very small number $h$ (maybe) 

Its denoted by 

$$\nabla _{\vec v}=\frac{\partial }{\partial \vec v}$$

Lets try to calculate the directional derivative of an example sum

$$f(x,y)=x^2y$$

So when we write 

$$\nabla_{\vec v}f=\text{Directional Derivative} \ne Gradient $$

We dont mean Gradient , we just mean directional Derivative 

If the vector is given $\vec v=- \hat i +2 \hat j$ then the directional derivative is just 

$$\nabla _{\vec v}f=-\frac{\partial f}{\partial x}+2\frac{\partial f}{\partial y}$$

Why that specific combination ? Because we are taking that step ( one small step in -x direction and 2 small step in y direction )

$$\nabla _{\vec v}f=-2xy+2(x^2)$$

In a more general sense 

$$\nabla_{\vec v}f=\vec v\cdot\nabla f$$