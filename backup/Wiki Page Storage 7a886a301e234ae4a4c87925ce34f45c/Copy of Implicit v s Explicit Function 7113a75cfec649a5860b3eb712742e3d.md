# Copy of Implicit v/s Explicit Function

Column: Aug 26, 2020 12:48 PM
Last edited by: Soutrik das
Tags: maths

$$ \begin{aligned}
\frac{d}{dx} \large \left[ \int_{a(x)}^{b(x)}f(x,t)dt \right]=&\large \left[ \int_{a(x)}^{b(x)}\frac{\partial}{\partial x}f(x,t)dt  \right] \\ &+f(x,\overbrace{b(x)}^{\text{instead of t }}) \frac{d}{dx}b(x)-f(x,a(x))\frac{d}{dx}a(x) 
\end{aligned}$$

# Implicit v/s Explicit Function

A function can be explicit or implicit: Explicit: "y = some function of x". ... Implicit: "some function of y and x equals something else". Knowing x does not lead directly to y.

so when two variables like $x=x^2-\log t$ then this is a implicif function $f(x,t)=x^2-\log t$

For explicit function where there is no two variables ( mainly $f(t)$ and $d(t)$ should match , ie there should be only one variable in the function and that too should be accompanying $d(\_\_)$

So in that case the first term will vanish , ie $\Large \left[ \int_{a(x)}^{b(x)}\frac{\partial}{\partial x}f(x,t)dt \right]=0$