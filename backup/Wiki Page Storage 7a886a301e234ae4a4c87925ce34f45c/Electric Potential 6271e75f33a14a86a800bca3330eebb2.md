# Electric Potential

Child: E_s=-%20frac%7BdV%7D%7Bds%7D%20where%20E_s%20is%20the%20component%20of%20e%20c2b325bf29a646c29cf20e1fb5079e60.md, If%20we%20have%20a%20conducting%20sphere%20and%20a%20charge%20in%20vic%2088108bfeb3cd4866b2fda221c0a83bb8.md, When%20does%20zero%20electric%20flux%20mean%20that%20the%20electri%20957b1366aee94166a88f597a6ade8fdd.md, Capacitance%20caeded92469e47e098a21d1ef36e2d0c.md
Column: Sep 11, 2020 3:11 PM
Last edited by: Soutrik das
Tags: chapter, physics

[$E_s=-\frac{dV}{ds}$ where $E_s$ is the component of electric field in the direction of $ds$. But if given the potential and position of two points what can we get ?](E_s=-%20frac%7BdV%7D%7Bds%7D%20where%20E_s%20is%20the%20component%20of%20e%20c2b325bf29a646c29cf20e1fb5079e60.md) 

It is defined like 

$$V_A-V_B=\frac{W_{\text{external }B \to A}}{q} \tag{speed shoudl be 0}$$

The work you put inside , is the potential 

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Wext.gif](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Wext.gif)

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/ezgif-4-9174ce9b5572.gif](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/ezgif-4-9174ce9b5572.gif)

Potential at point 2 is the work ext done per unit charge to bring the charge from infinity to 2

$$V=-\int_\infin^P \vec E \cdot d\vec l$$

---

Note when asked where potential is zero ( and given two opposite charges seperated by d ) then there maybe two points where potential is zero , one between them and one outside . This did not happen in electric field 

# Problems

## Problems Requiring you to find the Potential Difference by specifying the Electric field ( eg $\vec E=3x^2y \hat i +x^3 \hat j$ )

---

We have to use 

$$V_2-V_1=\frac {W_{ext\text{ 1 $\to$ 2}}}{q}=-\int_1^2 \vec E_{el}\cdot d \vec r$$

Suppose the points are A( 0,0,0) and B(1,1,1) and they want us to find $V_A-V_B$ and given 

$$⁍$$

Then 

$$V_A-V_B=-\int_B^A \overbrace{(3x^2y \hat i +x^3 \hat j)}^{\vec E} \cdot (\overbrace{dx\hat i +dy\hat j+ dz\hat k}^{d\vec r}) $$

$$V_A-V_B=-\int_B^A 3x^2ydx+x^3dy$$

Now this is an [exact differential equatio](https://www.notion.so/Differential-Equation-140b16dfa0854772803fa71633eb3ff2#2fbc1baf917a47acbf192717a89a18a8)n ([Differential Equation ](Differential%20Equation%20140b16dfa0854772803fa71633eb3ff2.md)) (since $\frac{\partial \overbrace M^{\text{one with the dx}} }{\partial y}=\frac{\partial \overbrace N^{\text{one with the dy}}}{\partial y}$ ), of which the method to solving is [given here](https://www.notion.so/Differential-Equation-140b16dfa0854772803fa71633eb3ff2#a42498158ddd4cc4901ef97dc3af1c57)

We can also use the fact that $d(x^3y)=3x^2ydx+x^3dy$  to make out problem from $\boxed{V_A-V_B=-\int_B^A 3x^2ydx+x^3dy}$ to this $\boxed{V_A-V_B=-\int_B^A d(x^3y)}$

So on solving we get 

$$-\int^A _{B} \underset{\text{ taking y as constant}}{3x^2y}-\int_B^A \overbrace{0dy}^{\text{because no term without x}}$$

$$-x^3y \Big|^{(0,0,0)}_{(1,1,1)}=1$$

$$V_A-V_B=1$$

## Problems requiring you to find Equation of $\vec E (x,y,z)$ when $\vec V (x,y,z)$ is given

---

Example 
 

$$V=x(y^2-4x^2)$$

We have to use the fact that 

$$E_x=-\frac{\partial V}{\partial x} =-y^2+12x^2$$

$$E_y=-\frac{\partial V}{\partial y} =-2xy$$

$$E_z=-\frac{\partial V}{\partial z} =0$$

$$E=(-y^2+12x^2) \hat i + (-2xy) \hat j +0 \hat k $$

# Ring

---

### Potential along any point on the axis

$$\frac{kQ}{\sqrt{R^2+x^2}}$$

# Non conducting Plate

---

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled.png)

Now this Gaussian surface ( the circular ) is absolutely perpendicular to the electric field , hence we can say 

$$E\times 2\pi R^2=\frac{\pi R^2\times \sigma }{\epsilon_0}$$

$$E=\frac{\sigma }{2\epsilon_0}$$

# Infinite Conducting Sheet

---

In fact , a conducting plate also wouldnt differ much 

For a **infinite** Conductor like this 

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%201.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%201.png)

If you paint one side with Q charge 

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%202.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%202.png)

Then the conductor being a conductor will redistribute the charge very quickly 

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%203.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%203.png)

Now the electric field Formula may change depending on what we mean by $\sigma$ because it can have two meanings 

- $\sigma =\cfrac{Q}{2A}$

    ![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%204.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%204.png)

    For this kind of notation , the electric field is $\sigma / \epsilon_o$

- $\sigma =\cfrac {Q}A$

    ![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%205.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%205.png)

    For this guy the electric field is just like a non conducting sheet $\sigma /2\epsilon_0$

# Sphere ( Hollow non conducting / conducting )

---

### Potential

- Outside $\frac{kQ}{r}$
- On surface $\frac{kQ}{R}$
- Inside  $\frac{kQ}{R}$

- But why is the potential inside constant ? Answer : There is no Electric field . But why is there no Electric Field ?

    Because Gauss Law says that if there is no charge , there will not be Flux , hence no Electric field

### Self Potential of a Sphere

This is nothing but the work done to bring together this whole sphere from small pieces kept at infinity. So how do you get that work ?

You can also think of this shape ( if it is a conductor ) as a capacitor and then try to find out its energy , like [this](https://doubtnut.com/question-answer-physics/calculate-the-self-potential-energy-of-charge-q-distributed-over-the-surface-of-a-hollow-sphere-of-r-17238105)

[Summary](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Summary%2097c25cc302a442cbb248b72fb986a507.md)

# Electric Field and Potential of induced Charges ( induced charge on a conductor due to external charge )

---

Suppose we give a conducting shell a charge $Q$ , when its alone , isolated , all the charge will try to move to the surface ( Why ? Because if it doesnt , there will be some electric field inside the conductor , and some electrons will flow , and the flow will stop only when the electric field inside is 0 , ( which will happen at some time ) ) 

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%206.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%206.png)

But as soon as we bring in the charge q near to the sphere , the charge density's symmetry gets destroyed 

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%207.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%207.png)

But the goal of this new charge distribution is to always keep electric field inside 0

But even then , the electric field at any point is going to be 0 ( at equilibrium ) 

But the opposing electric field , is it only caused by induced charges ? or also by $Q$ , the charge that was already present on the sphere ?

- The charges  ( induced and/or $Q$ ) Do indeed exert some electric field all over the area , then does that mean that some charge has seeped inside the sphere ? ( meaning , all the charges are not on the surface ) . Because if the were to be on the surface , they wouldnt be able to exert electric field INSIDE ?

But then you can also change the gaussian surface 

![Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%208.png](Electric%20Potential%206271e75f33a14a86a800bca3330eebb2/Untitled%208.png)