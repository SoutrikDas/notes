# Differential Equation

Child: x%5E2(y-x%20frac%7Bdy%7D%7Bdx%7D)=y(%20frac%7Bdy%7D%7Bdx%7D)%5E2%20b4bfda23f40946ed84e1275236a55064.md
Column: Sep 26, 2020 12:28 PM
Last edited by: Soutrik das
Tags: maths

# Order of a Differential Equation

---

the highest order if the maximum value of n , n being $\frac{d^ny}{dx^n}+\cdots$ 

For example in 

$$\newcommand{\b}[1]{\frac{d^{#1}y}{dx^{#1}}}
\b3+\b2+\b1+\b0=0 \tag{here order is 3}$$

# Degree of a Differential Equation

---

The highest exponent of the highest order term is called the degree 

$$\newcommand{\b}[1]{\frac{d^{#1}y}{dx^{#1}}}
\b3+\left( \b1\right)^3 =0 \tag{order=3 degree=1}$$

# ODE vs PDE

---

![Differential%20Equation%20140b16dfa0854772803fa71633eb3ff2/Untitled.png](Differential%20Equation%20140b16dfa0854772803fa71633eb3ff2/Untitled.png)

ODE - Ordinary Differential Equations is that in which all the differernial coefficients have reference to a single independent variable. Thus the equations (i) to (u) are all ordinary differential equations

PDE - Partial Differential Equations is that in wh ich there a'f'e two or more independent variables and partial differential coefficients with respect to any of them. Thus the equations (vi) and (vii) are partial differential equations.

# Formation of ODE and PDE

---

An ordinary differential equation is formed in an attempt to **eliminate certain arbitrary constant from a relation** 'in the variables and constants. It will, however , be seen later that the partial differential equations may be formed by the **elimination of either arbitrary constants or arbitrary functions**. To applied mathematics, every geometrical or physical problem when translated into mathematical symbols gives rise to a differential equation

ex:

# Solving Differential Equations of 1st Order 1st Degree

---

There are four methods 

- Variable Seperable
- Homogenous Equations
- Linear Equations
- Exact Equations

## Variable Seperable

---

## Homogenous Equations

---

## Linear Equations

---

A differential equation is said to be Linear if the dependent variable and its differential coefficients occur

only in the first degree and not multiplied together

$$\frac{dy}{dx}+yP(x)=Q(x)$$

Remember to make any coefficients of $\frac{dy}{dx}$ into $1$ , otherwise there will be a problem 

Find the integrating factor 

$$IF=e^{\int P(x) dx }$$

Them multiply $IF$ to RHS and LHS 

$$\frac{d y}{d x} \cdot e^{\int P d x}+y\left(e^{\int P d x} P\right)=Q e^{\int P d x}
\\
 \text { i.e., } \frac{d}{d x}\left(y e^{\int P d x}\right)=Q e^{\int P d x}$$

Now you just have ot integrate both side 

$$ye^{\int P(x)dx}=\int Qe^{\int P(x)dx}dx +c$$

And add that c

## Exact Differential Equation

---

If the differential equation is of the form 

$$M(x,y)dx+N(x,y)dy=0$$

and the LHS part of that equation is a differential of some function $u(x,y)$ then it is said to be exact 

The **necessary and sufficient condition** is 

$$\frac{\partial \overbrace M^{\text{one with the dx}} }{\partial y}=\frac{\partial \overbrace N^{\text{one with the dy}}}{\partial y}$$

The solution is 

$$\int_{(y \operatorname{const})} M d x+\int(\text { terms of } N \text { not containing } x) d y=c$$

example 

$$\left(y^{2} e^{x y^{2}}+4 x^{3}\right) d x+\left(2 x y e^{x y^{2}}-3 y^{2}\right) d y=0$$

$$M=\left(y^{2} e^{x y^{2}}+4 x^{3}\right)$$

$$N=\left(2 x y e^{x y^{2}}-3 y^{2}\right) $$

$$\int _{\text{y constant}}Mdx=e^{xy^2}+x^4$$

$$\int _{\text{N without x terms }}-3y^2dy=-y^3$$

Solution=

$$e^{xy^2}+x^4-y^3=c$$

## Reducible to Exact Differential

---

Given a non exact differential equation we can multiply a function $f(x,y)$ such that the non exact function becomes exact , then this factor is known as **Integrating Factor**

example 

$$(x^2y-2xy^2)dx+(-x^3+3x^2y)dy=0$$

$$M=x^2y-2xy^2 \\
N=-x^3+3x^2y$$

$$\frac{\partial M}{\partial y}=x^2-4xy \\
\frac{\partial N}{\partial x}=-3x^2+6xy$$

Since $\frac{\partial \overbrace M^{\text{one with the dx}} }{\partial y}\ne \frac{\partial \overbrace N^{\text{one with the dy}}}{\partial y}$ therefore we can say that its non exact .

But upon multiplying the initial non exact differential with $\cfrac 1{x^2y^2}$ on both sides 

we get a new differential equation ( which is exact ) 

$$\left( \frac 1y - \frac 2x\right)dx + \left(- \frac {x}{y^2}+\frac 3y \right)dy$$

Now if you check you can find that  $\frac{\partial \overbrace M^{\text{one with the dx}} }{\partial y}= \frac{\partial \overbrace N^{\text{one with the dy}}}{\partial y}$

### Type 1 - Homogenous

$$(x^{\colorbox{red}{2}}y^{\colorbox{red}{1}}-2x^{\colorbox{orange}{1}}y^{\colorbox{orange}{2}})dx+(-x^{\colorbox{blue}{3}}+3x^{\colorbox{green}{2}}y^{\colorbox{green}{1}})dy=0$$

If even one term of this equation were of a different degree then this wouldnt be called a **"Homogenous Equation"** 

In this type the Integrating Factor is 

$$IF=\frac{1}{\underbrace{Mx+Ny}_{\text{after cutting this should be a single term}}}$$

After Multiplying it becomes an Exact Differential 

### Type 2

If the Differential Equation is of the form $Mdx+Ndy$ and 

- you can take $y$ common from $M$
- you can take $x$ common from $N$

That is 

$$Mdx+Ndy=0
\\
\implies yM'dx+xN'dy=0$$

[Here](https://www.notion.so/Differential-Equation-140b16dfa0854772803fa71633eb3ff2#923fa504f1904bc2b7fbee592bc1c7cf)  By $M'$ I dont mean the differetial of $M$ but rather i mean a changed function . 

For example if the equation is like  

$$\overbrace{(x^2y-2xy^2)}^{\text{M}}dx+(-x^3+3x^2y)dy=0$$

We can write it as 

$$y(\overbrace{x^2-2xy}^{\text{M}'})dx+x(-x^2+3xy)dy=0$$

then the Integrating factor is :

$$IF=\frac{1}{Mx-Ny}$$

### Type 3

Calculate the following 

$$\frac{\frac{\partial M}{ \partial y}-\frac{\partial N }{ \partial x}}{N} \\ \text{if this is a function of x then Type 3}$$

If the result is only a function of $x$ , then the question is of type 3 and the integrating factor is d

$$IF =e^{\int f(x) dx}$$

⭐ Where $f(x)$ is the function that you got over [here](https://www.notion.so/Differential-Equation-140b16dfa0854772803fa71633eb3ff2#6f06dc136d0a4e4ea4e4fbc5c67fc148) 

### Type 4

This is the opposite of Type 3

$$\frac{\frac{\partial N}{ \partial x}-\frac{\partial M }{ \partial y}}{M} \\ \text{if this is a function of y then Type 4}$$

$$IF =e^{\int g(y) dx}$$

Where $g(y)$ is the  final function of y that you get in [this step](https://www.notion.so/Differential-Equation-140b16dfa0854772803fa71633eb3ff2#ea1e090f37b84b6b9fe81f0edf2a0bd7) 

# Solving Differential Equations of 1st Order $n^{th}$ Degree (oos)

---

This is out of syllabus probably for JEE advanced 

In Higher Degrees to simplify things we will denote $\cfrac{dy}{dx}$ as $p$ or $\dot{y}$ or $y'$

So a general form of a 1st Order but nth Degree differential Equation is of the form 

$$p^{n}+P_{1} p^{n-1}+P_{2} p^{n-2}+\ldots+P_{n}=0 \tag1$$

Where $P_1,P_2 \cdots$ are functions of $x$ and $y$

To solve this , we split the LHS into factors just like how we would split $x^2-5x+6$ as $(x-3)(x-2)$ , Similarly we factorize the [general equation](https://www.notion.so/Differential-Equation-140b16dfa0854772803fa71633eb3ff2#c68de6fe35ea49629b7b3ce654eaaf38) above , 

$$\left[p-f_{1}(x, y)\right]\left[p-f_{2}(x, y)\right] \ldots\left[p-f_{n}(x, y)\right]=0$$

So we get multiple First order First Degree Differential Equations 

Ie 

$$p=f_1(x,y)$$

$$p=f_2(x,y)$$

$$p=f_n(x,y)$$

Each of these is one First Degree Differential Equations  , which we need to solve . And on solving one , we get one solution . 

So for $n^{th}$ Degree Diff Eq , we get $n$ First Degree Diff Eq , Which gives us $n$ general solution

## Examples of N Degree Diff Equation

---

Q: $\frac{d y}{d x}-\frac{d x}{d y}=\frac{x}{y}-\frac{y}{x}$

$$\frac{d y}{d x}-\frac{d x}{d y}=\frac{x}{y}-\frac{y}{x}$$

Taking $p=\frac{dy}{dx}$ we get 

$$p-\frac1p=\frac{x^2-y^2}{xy}$$

$$xy(p^2-1)=p\frac{x^2-y^2}{1}$$

$$p^2xy-xy=px^2-py^2$$

$$(xy)p^2+(y^2-x^2)p -xy=0$$

So we treat this as quadratic equation in $p$ and try to break the middle term So that its product is $-x^2y^2$,  OH! We already have it broken 

$$(xy)p^2+y^2p-x^2p -xy=0$$

$$yp(xp+y) -x(xp+y)=0$$

$$(yp-x)(xp+y)=0$$

So our two First Degree diff equations are 

- $y\frac{dy}{dx}=x$ → $y^2=x^2+2c$

    $$ydy=xdx \\
    \implies y^2/2=x^2/2+c
    \\
    \implies x^2-y^2+2c=0$$

- $x\frac{dy}{dx}=-y$ → $xy=c$

    $$\frac {dy}y=-\frac{dx}{x} \\
    \implies \ln y=-\ln x + \ln c \\
    \implies xy=c$$

Both of them can be solved using variable seperation.

And the required solution can be written as 

$$(xy-c)(x^2-y^2+2c)=0$$