# E_s=-\frac{dV}{ds} where E_s is the component of electric field in the direction of ds. But if given the potential and position of two points what can we get ?

Column: Oct 9, 2020 9:40 PM
Last edited by: Soutrik das
Parent: Electric%20Potential%206271e75f33a14a86a800bca3330eebb2.md
Tags: doubt, doubt cleared, physics

Lets suppose there are two people in a room , A and B . 

Now **A** knows that there is a certain electric field in an area 

$$\vec E=x \hat i +y\hat j+z\hat k$$

But he takes two points P $( 0,0,0)$ and Q $(1,1,0)$ and then finds the potential difference $V_Q-V_P$ 

$$V_Q-V_P=-\int _P^Q (x \hat i+y \hat j +z\hat k)\cdot (dx \hat i +dy\hat j+dz \hat k)$$

$$V_Q-V_P= -\frac {x^2}{2} \Big|^1_0-\frac {y^2}{2} \Big|^1_0-\frac {z^2}{2} \Big|^0_0+$$

$$V_Q-V_P= -1$$

Now **A**  gives two pieces of information to **B**

- P $( 0,0,0)$ and Q $(1,1,0)$
- $V_Q-V_P= -1$

> Now the question is : What can **B** get to know about the electric field through these pieces of information ? ( along with $E_s=-\frac{dV}{ds}$ )

Using $E_s=-\frac{dV}{ds}$ we get that 

$$\underset{\text{in the direction of displacement}}{E_{\hat i +\hat j}}=-\frac{\overbrace{-1}^{dV}}{\sqrt 2} \times \vec v$$

Where $\vec v$ is the unit vector from $P$ to $Q$

Do we take $ds$ as $\sqrt 2$ ~~or $\hat i+\hat j$~~ 

> Our book says you can get the ( component ) of Electric field in a particular direction by using $E_s=-\frac{dV}{ds}$ but here the actual component should have been $x \hat i +y \hat j$ , but **B**  got it to be $1\hat i + 1\hat j$

# Conclusion

if we do take $ds$ as $\sqrt 2$ then **B** will say to A that " The electric field is $E=\frac 12$ in the direction $\frac{\hat i +\hat j}{\sqrt 2}$

 ****

If we had the Potential function $V(x,y,z)$ then using $E_s=-\frac{dV}{ds}$ we could have found the exact Electric field at any point