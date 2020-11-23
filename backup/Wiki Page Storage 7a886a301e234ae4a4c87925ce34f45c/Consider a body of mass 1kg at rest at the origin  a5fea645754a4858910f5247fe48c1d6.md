# Consider a body of mass 1kg at rest at the origin at time t=0. A force \vec F=(\alpha t\hat i +\beta \hat j) is applied on the body, where \alpha=1Ns^{-1} and \beta=1N. The torque acting on the body about the origin at time t=1s is \vec \tau, Which are true ?

Column: Oct 9, 2020 9:40 PM
Last edited by: Soutrik das
Parent: JEE%20ADV%202018%20paper%201%20156baa1a568144639dd9e5b9a1b32e04.md, Rotational%20Mechanics%204ed592873b3d432b99c2bb7f12e1635e.md
Tags: doubt cleared, physics, question

![Consider%20a%20body%20of%20mass%201kg%20at%20rest%20at%20the%20origin%20%20a5fea645754a4858910f5247fe48c1d6/Untitled.png](Consider%20a%20body%20of%20mass%201kg%20at%20rest%20at%20the%20origin%20%20a5fea645754a4858910f5247fe48c1d6/Untitled.png)

We know 

$$\tau=\vec r\times \vec F$$

We are given 

- $F_x=t$
- $F_y=1$

Acceleration 

- $a_x=t$
- $a_y=1$

Velocity

- $v_x=\frac {t^2}{2}$
- $v_y=t$

Displacement

- $s_x=\frac{t^3}{6}$
- $s_y=\frac{t^2}{2}$

So torque can be found in two ways 

- $\tau =s_x F_y=\frac{t^3}{6}$
- $\tau =s_yF_x=\frac{t^3}{2}$

Why are these two different in magnitude  ? shouldnt they be same ? 

also , they have different directions . 

How to find the actual torque ? 

At any point , the coordinates of the particle are $(\frac{t^3}{6},\frac{t^2}{2})$, when will the be equal ?

$$t^3/6=t^2/2$$

$$t=3$$

At three seconds it will become equal , so who was less than who before it ? putting $t=1$ we get $(1/6,1/2)$ , so $x<y$ before $t=3$, and $x>y$ after that time .

So I was finding the torque due to the components of the forces , therefore I was getting two different torques , one was due to $F_x$ and the other due to $F_y$ 

So $\tau_{net}=\tau_1+\tau_2$ 

If I take the $\hat k$ to be +ve direction then 

$$\tau_{net}=\hat k(t^3/6-t^3/2)$$

$$\tau_{net}=-\hat k \frac {t^3}3$$

But how do I find this without finding the individual components ?

$$F=(t\hat i+\hat j +0\hat k)$$

$$r=(\frac{t^3}6 \hat i +\frac{t^2}{2}\hat j +0\hat k )$$

$$\tau=\vec r \times \vec F$$

$$\def\arraystretch{1.5}
  \begin{array}{c:c:c}
   a & b & c \\ \hline
   d & e & f \\
   \hdashline
   g & h & i
\end{array}$$

$$\def\arraystretch{1.5}
\tau=\begin{vmatrix}
\hat i &\hat j &\hat k  \\
\frac{t^3}{6} & \frac{t^2}{2}& 0 \\
t & 1&0
\end{vmatrix}$$

$$\tau=0\hat i-\hat j(0)+\hat k (\frac{t^3}{6}-\frac{t^3}2)$$

$$\tau_{net}=-\hat k \frac {t^3}3$$

Now for the question we are given $t=1s$ 

$$\tau_{net}=-\hat k \frac {1}3$$

option A is correct 

option C is correct 

option D is wrong because $s_x(1)=1/6$ , and if you take $s_y$  it will be more