# The maximum electric field at a point on the axis of a uniformly charged ring is E_0. At how many points on the axis will the magnitude of the electric field be E_0/2

Column: Sep 6, 2020 8:54 AM
Last edited by: Soutrik das
Parent: Cengage%20BM%20Sharma%209c189c7938ba426db954efeea20531ef.md
Tags: physics, question

# Electric Field of a Ring at a point $x$ distance from its center on its axis

$$E=\frac{kqx}{(x^2+R^2)^{\frac32}}$$

# Where is the field maximum ?

To know this , lets differentiate 

$$0=\frac{kqx}{(x^2+R^2)^{\frac32}}$$

- Usign division rule we cannot get the result , its pretty difficult

    $$0=kq \times \frac{(1)(x^2+R^2)^{\frac32}-(\frac 32\{ x^2+R^2 \}^{\frac12})(x)}{(x^2+R^2)^3}$$

    $$(x^2+R^2)^{\frac32}=\frac32 x\{ x^2+R^2\}^{\frac12}$$

    Squaring it we get 

    $$(x^2+R^2)^3=\frac 94x^2\{x^2+R^2 \}$$

    $$ 4x^6+4R^6+3x^2R^4+3x^4R^2
    =9x^4+9x^2R^2
    $$

    $$ 4x^6+4R^6+12x^2R^4+12x^4R^2
    =9x^4+9x^2R^2$$

Lets use the product rule to see 

Ignore the coefficients 

$$\begin{aligned}
\text{simple product rule}\ f(x) &= u(x)\times v(x); \quad u(x) = x;\quad v(x) = \frac1{(x^2 + r^2)^{3/2}}\\
f'(x) &= u'(x)\times v(x) + u(x)\times v'(x)\\
f'(x) &= \frac1{(x^2 + r^2)^{3/2}} + \frac{\left(-\frac32\right)2x^2}{(x^2 + r^2)^{5/2}}
\end{aligned}$$

$$\frac1{(x^2 + r^2)^{3/2}} = \frac{3x^2}{(x^2 + r^2)^{5/2}}$$

$$x^2+r^2=3x^2$$

$$x=\pm\frac{R}{\sqrt2}$$

# Graph of electric field

[https://www.desmos.com/calculator/l1n2vgjoro](https://www.desmos.com/calculator/l1n2vgjoro)

Click [here](https://www.desmos.com/calculator/l1n2vgjoro) to go to the desmos page 

We can see from the graph that there are 4 points , but we could also conclude from the fact that field strength will decrease on both sides of $\pm \frac {R}{\sqrt2}$

$$ x^6+R^6+3x^2R^4+3x^4R^2
=\frac 14\{9x^4+9x^2R^2 \}
$$