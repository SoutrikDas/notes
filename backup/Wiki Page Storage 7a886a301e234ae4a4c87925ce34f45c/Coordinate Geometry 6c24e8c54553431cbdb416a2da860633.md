# Coordinate Geometry

Child: Breaking%20Pair%20of%20Straight%20Lines%20Equation%20c21617c3d3db4c0d9090b461f3fb931b.md
Column: Aug 30, 2020 1:13 PM
Last edited by: Soutrik das
Parent: Complex%20Numbers%2058520c2afe2a4be2a00a946e780d9af9.md

[Questions in Coordinate Geomtry](Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/Questions%20in%20Coordinate%20Geomtry%20d87a5db27c04474a8cd794af3ea00703.md)

# How to identify what an equation represents ?

---

- What is the general equation of a conic section ?

    $$ax^2+by^2+2hxy+2gx+2fy+c=0$$

Calculate the $h^2-ab$ value and depending on this value , we can distinguish which conic section it is !

1.  If $h^2-ab=0$ Its a **Parabola** 
2. If $h^2-ab > 0$ its a **Hyperbola**
3. If $h^2-ab\le 0$ 
    1. if ( $a=b$ ) **AND** ( $h=0$ )  then its a circle
    2. if ( $a\ne b$ ) **OR** ( $h \ne 0$ )  then its an Ellipse

# Line

---

## Area of a Triangle

---

$$\triangle=\frac 12 \sin \omega
\begin{vmatrix}
x_1 & y_1  & 1 \\
x_2 & y_2 & 1 \\
x_3 & y^3 &1
\end{vmatrix}$$

Where  $\omega$ is the angle between the two axes. Normally , its $=90 \degree$ but for oblique axis , it may change  

## ⭐Distance of a point from a line

---

Suppose our point is at $(x_1,y_1)$ and our line is $ax+by+c=0$ 

Then the Perpendicular Distance of the point from the line is given by 

$$D=\frac{|ax_1+by_1+c|}{\sqrt{a^2+b^2}}$$

## Angle between two straight lines

---

Let two lines be 

- $y=m_1x+c_1$
- $y=m_2x+c_2$

Then the angle between them $\Delta \theta$ is 

$$\Delta \theta=\frac{m_2-m_1}{1+m_1m_2}$$

## Find out on which side of the line a point is

- This kind of position always needs a reference to something else , what is the reference here ?

    The krux is that , you can answer by saying " the point is in the side of origin " OR "the point is not in the side of origin " 

    You cannot just say that , the point is above the line , or the point is on the left side of the line 

    As a matter of fact , you can not only use origin but any other point .

Find a reference point , it maybe origin or some other point , here I am taking  it to be $(x_0,y_0)$

Then take a point which you want to check "which side is it on?" , I am taking that point to be $(x_1,y_1)$

If the lines equation is $ax+by+c=0$ , then in your mind define a new function  $f(x,y)=ax+by+c$ 

Now 

- if $f(x_1,y_1)=0$ then the point $(x_1,y_1)$ is on the line
- if $f(x_1,y_1)$ and $f(x_0,y_0)$ have the **same** signs then $(x_1,y_1)$ is **on** the side of $(x_0,y_0)$
- if $f(x_1,y_1)$ and $f(x_0,y_0)$ have **different** signs then $(x_1,y_1)$ is **NOT** on the side of $(x_0,y_0)$

# Pair of Straight Line

---

[How to break a pair of straight line ?](https://www.youtube.com/watch?v=Uk5kEuT3Vmw)

- How its formed ?

    The general equation is $ax^2+2hxy+by^2+2gx+2fy+c$ 

    $$(y-m_1x)(y-m_2x)=0 \\
    y^2-(m_1+m_2)xy+m_1m_2x=0$$

First empty out the coefficient of B 

So we get to know a few things already 

The coefficient of $xy$ is  $2h$ but its also equal to $-(m_1+m_2)$

$$2h /b=-(m_1+m_2)
\\
h/b=-\frac{m_1+m_2}{2}$$

The coefficient of x $=a/b$ ( if coeff of y= $1$) 

$$\frac ab=m_1m_2$$

$$2h/b=-(m_1+m_2)
\\
h/b=-\frac{m_1+m_2}{2}$$

$$\frac ab=m_1m_2$$

If they are perpendicular then $m_1m_2=-1$ so $\frac ab=-1$ Or   $a+b=0$

## Angle between the two pair of straight lines

---

The angle between two lines whose slopes you know is easy to find 

So if you know that $m_2>m_1$ you can 

$$tan(\theta _2-\theta_1)=\frac{m_2-m_1}{1-m_1m_2} \\
\tan \Delta \theta=$$

![Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/IMG-20200829-212425.jpg](Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/IMG-20200829-212425.jpg)

![Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/Untitled.png](Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/Untitled.png)

## Equation of Pair of Angle Bisectors

---

The idea is to find a locus by the geometrical constraint that the point is equidistant from both the lines

## Homogenising POSL

---

- What is homogenising really ?

    The most weird effect ever. When you take a line and then use it to homogenise a curve , the new equation that forms ( is not the same as the curve ) but its a **group**  of straight lines connecting the intersection points with origin 

To observe homogenising of a curve with a line, go [here](https://www.desmos.com/calculator/0g1vtodbhm) 

- Can we homogenise a curve with another curve ?

    It doesnt seem to always happen , but yeah , you can do it . then the result will be a very wird curve that passess through the intersection points and the origin ( but sometimes very wierd )

    To observe homogenising of a curve with a circle go [here](https://www.desmos.com/calculator/c87wjcltjq)

# Circle

---

General Equation : $x^2+y^2+2gx+2fy+c=0$ 

Radius : $\sqrt{g^2+f^2-c}$

Center : $(-g,-f)$

- 🌟 Some important Notations  (What is $S$ , $S_1$ , $T_1$ ?)

    $S=x^2+y^2+2gx+2fy+c$

    $S_1=x_1^2+y_1^2+2gx_1+2fy_1+c$

    $T=xx_1+yy_1+g(x+x_1) +f(y+y_1)+c$

- What is the equation of a circle using the proper notation?

    $S=0$

- What is an imaginary circle ?

    A circle with negative radius.

- How to know if a point is outside the circle or not ?
    1. Calculate the distance between the point and center of circle , if its $>radius$ then outside
    2. Put the point in the general equation  $S=x^2+y^2+2gx+2fy+c$  ( without $=0$ ) and if the value after calculating comes out to be greater than 0 , then the point is outside circle 
        1. $S_1>0$ means outside the circle
        2. $S_1=0$ means on the circle 
        3. $S_1<0$ means in the circle 
- How to calculate the x and y intercept of a circle ?

    x intercept : $\sqrt{g^2-c}$

    y intercept : $\sqrt{f^2-c}$

    [Here is a desmos graph](https://www.desmos.com/calculator/gmv7zfundz)

- How to know if the circle touches the x axis or y axis ?

    If either x or y intercepts are $0$ then it is touching that axis . If it is less than 0 then it is not . If more than 0 then it is intercepting it

## $T=0$ , The master equation for circle

---

This one equation solves so many problems that its hard to believe .

- But first things first, what does $T$ even mean ?

    $$T=xx_1+yy_1+g(x+x_1)+f(y+y_1)+c$$

    Where 

    - $x$ is the general x ( the one found in equation of line ) ,ie its a variable
    - $y$ is a variable just like $x$
    - $x_1$ is the x coordinate of a point ( eg $x_1=6$ )
    - $y_1$ is the y coordinate of a point ( eg $y_1=5$ )
    - $g,f,c$ have their respective meanings from the general equation

As you can see , we can only write this equation w.r.t a point ( because we need $(x_1,y_1)$ , so we will name this point $P$

So what problems does this one equation solve ? 

Namely , three 

1. Equation of Polar  ( when $P$ is in the circle )  **Fig. I**
2. Equation of Tangent ( when $P$ is on the circle )  **Fig. II**
3. Equation of Chord of Contact  ( when $P$ is outside the circle )   **Fig. III**

Play around with the $T=0$  [here](https://www.desmos.com/calculator/1mewa8ipzf) 

![Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/pole_a56.gif](Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/pole_a56.gif)

# $S-S'=0$  The line that joins intercepts of two circle

Play around with radical axis over [here](https://www.desmos.com/calculator/lqx5b1ocgy)

The radical axis is **NOT** the perpendicular bisector of the two centers 

# Parabola

---

# Ellipse

---

- What is the eccentricity of an ellipse ?

    $$e^2=1-\frac{b^2}{a^2}$$

- What is the semi-major axis of an ellipse ?

    ![Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/260px-Ellipse_semi-major_and_minor_axes.svg.png](Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633/260px-Ellipse_semi-major_and_minor_axes.svg.png)

    Semi major axis : $a$

    Semi minor axis : $b$

    They are related through the eccentricity

# Hyperbola

---

- What is the eccentricity of a hyperbola ?

    $$e^2=1+\frac{b^2}{a^2}$$

# Locus

---

When a point moves so as always to satisfy a given condition, or conditions, the path it traces out is called its Locus under these conditions.