# Find Electric Flux when equation of Electric Field is given as E=E_0(\beta x^2\hat i +2\hat j+15 \hat k)

Column: Sep 26, 2020 3:47 PM
Last edited by: Soutrik das
Parent: Electric%20Field%20(%20Gauss%20Law%20)%20d957b7fe60664b469168b278edad7ca0.md
Tags: physics, question

![https://i.imgur.com/kKuDXBj.png](https://i.imgur.com/kKuDXBj.png)

So the surface is a cube 

and the Electric field is defined by 

$E=E_0(\beta x^2\hat i +2\hat j+15 \hat k)$

What causes flux ? 

$$\int \vec E \cdot \vec ds=\frac{Q_{in}}{\varepsilon_0}$$

If constant electric field falls on two opposite faces then they will not contribute to the flux inside 

![Find%20Electric%20Flux%20when%20equation%20of%20Electric%20Field%20d018bab25c6a405a96e94c0d7d9fa1ab/Untitled.png](Find%20Electric%20Flux%20when%20equation%20of%20Electric%20Field%20d018bab25c6a405a96e94c0d7d9fa1ab/Untitled.png)

Because on the first surface the value of th eodt product is $-|ds||E|$ and on the second surface the value of the dot product is $+|ds||E|$ 

Therefore 

$$E=E_0(\beta x^2\hat i +\overbrace{2\hat j}^{\text{will not contribute}}+\overbrace{15\hat k}^{\text{will not contribute}})$$

So our business is only with the electric field in $\hat i$ direction 

and so we are going to only take the x faces 

![Find%20Electric%20Flux%20when%20equation%20of%20Electric%20Field%20d018bab25c6a405a96e94c0d7d9fa1ab/onlyxfaces.gif](Find%20Electric%20Flux%20when%20equation%20of%20Electric%20Field%20d018bab25c6a405a96e94c0d7d9fa1ab/onlyxfaces.gif)

The first face is at $x=-L/2$ and the second one is at $x=+L/2$ 

Flux For the first face 

$$\phi_1=(\beta \frac {L^2}4\hat i)\cdot (L^2\overbrace{-\hat i}^{\text{surface vector }})\\
\phi_1=-\beta L^4/4$$

For second Surface we get 

$$\phi_2=(\beta \frac {L^2}4\hat i)\cdot (L^2\overbrace{+\hat i}^{\text{surface vector }})\\
\phi_1=\beta L^4/4$$

Net flux should be 0 

$$\phi =\phi_1+\phi_2=0$$