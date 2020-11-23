# A large open tank has two small holes in the wall. One is square hole of side L at depth y from the top and the other is a circular hole of radius R at a depth 4y from the top. When the tank is completely filled with water, the quantities of water flowing out per second from both holes are the same. Then what is the value of R?

Column: Sep 14, 2020 10:07 AM
Last edited by: Soutrik das
Tags: doubt, physics, question

![A%20large%20open%20tank%20has%20two%20small%20holes%20in%20the%20wall%20%20de9f84da87c54bcfac957066803c19f4/Untitled.png](A%20large%20open%20tank%20has%20two%20small%20holes%20in%20the%20wall%20%20de9f84da87c54bcfac957066803c19f4/Untitled.png)

![A%20large%20open%20tank%20has%20two%20small%20holes%20in%20the%20wall%20%20de9f84da87c54bcfac957066803c19f4/Untitled%201.png](A%20large%20open%20tank%20has%20two%20small%20holes%20in%20the%20wall%20%20de9f84da87c54bcfac957066803c19f4/Untitled%201.png)

There are three labellings , O , A ,B

Writing the Bernoulli equation for O and A ( but can we write them seperately ? )

$$\rho gh_o+\frac 12 \rho v_o^2=\rho gh_a+\frac 12 \rho v_a^2$$

From this we get 

$$v_a^2-v_o^2=2gy \tag 1$$

Writing the Bernoulli equation for O and B we get 

$$\rho gh_o+\frac 12 \rho v_o^2=\rho gh_b+\frac 12 \rho v_b^2$$

$$v_b^2-v_o^2=2g(4y) \tag 2$$

Writing the equation of continuity , Inflow = Outflow 

Now we know the areas 

- $A_a$ = $L^2$
- $A_b=\pi R^2$

~~And we also know the fact that $\sout{v_a=v_b=v}$~~ this is not true !

So from equation of continuity we get 

$$v_oA_o=v_aL^2+v_b\pi R^2$$

Now if the Area of the opening at O is very very large compared to L and R 

then 

$$\frac {v_o } 1=\frac{v_aL^2+v_b\pi R^2}{A_o}$$

as $A_o \to \infin$ , $v_o \to 0$

 Hence we can use this fact in equations 1 and 2 

$$v_a^2=2gy $$

$$v_b^2=2g(4y)$$

~~And now using $\sout {v_a=v_b=v}$ on these two equations we get~~ 

$$\sout {v^2=2gy }$$

$$\sout {v^2=2g(4y)}$$

~~but how can one variable be of two values , what is wrong ?~~

Since the Rate of flow is same we can say that $A_av_a=A_bv_b$

$$L^2\times (\sqrt {2gy})=\pi R^2\times (2\sqrt{2gy})$$

From this we get that 

$$R=L\sqrt{\frac{1}{2\pi}}$$

But the answer is given as 

$$R=\frac{L}{2\sqrt \pi}$$