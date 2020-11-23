# Copy of Consider a spherical gaseous cloud of mass density p(r) in free space where r is the radial
distance from its center.

Column: Aug 26, 2020 12:33 PM
Last edited by: Soutrik das
Tags: question

![Copy%20of%20Consider%20a%20spherical%20gaseous%20cloud%20of%20mass%20e9d8e0a95b7040919b276b41e4b29771/Untitled.png](Copy%20of%20Consider%20a%20spherical%20gaseous%20cloud%20of%20mass%20e9d8e0a95b7040919b276b41e4b29771/Untitled.png)

Consider a spherical gaseous cloud of mass density p(r) in free space where r is the radial
distance from its center. The gaseous cloud is made of particles of equal mass m moving in
circular orbits about the common center with the same kinetic energy K. The force acting
on the particles is their mutual gravitational force. If p(r) is constant in time, the particle
number density n(r) = p(r)/m is
[ G is universal gravitational constant]

So basically select r and R (R is not the radius of the sphere ) like this

![https://cdn.discordapp.com/attachments/536995799859724309/732428910213726230/JPEG_20200714_082049.jpg](https://cdn.discordapp.com/attachments/536995799859724309/732428910213726230/JPEG_20200714_082049.jpg)

and then the force due to all the inner spheres on a particle at R ( Basically R is variable but we want to see the force on a particle at R)

$$dm=4\pi r^2 \cdot d r \cdot\rho(r)$$

$$\overbrace{dF}^{\text{ Force due to one shell at $r$}}= \frac{G \overbrace{m}^{\text{mass of particle at R }}\left( 4\pi r^2 \cdot d r \cdot\rho(r)\right)}{R^2}$$

$$F= \int_0^R \frac{G \overbrace{m}^{\text{mass of particle at R }}\left( 4\pi r^2 \cdot d r \cdot\rho(r)\right)}{R^2}$$

force on particle at R is equal to centrifugal

$$\frac{2K}{R}=\frac{mv^2}{R}=F $$

$$\frac{2K}{R}=\int_0^R \frac{G \overbrace{m}^{\text{mass of particle at R }}\left( 4\pi r^2 \cdot d r \cdot\rho(r)\right)}{R^2}$$

Now Comes the hard part , you have to differentiate this because you want to get rid of the Integration ( because you want a direct relation of $\rho(r)$ with other things but it is currently in the integral . Also you cannot just take $\rho(r)$ out of the integral because the integral is $\text{w.r.t $r$}$ ,so the only method is to differentiate using [Leibnitz Theorem](https://www.notion.so/Leibnitz-Theorem-8df60005fd574e39b183e8fa6aa0a98e) 

$$ \begin{aligned}
\frac{d}{dx} \large \left[ \int_{a(x)}^{b(x)}f(x,t)dt \right]=& \overbrace{\cancel{ \large \left[ \int_{a(x)}^{b(x)}\frac{\partial}{\partial x}f(x,t)dt  \right] }}^{\text{=0 for explicit functions }} \\ &+f(x,\overbrace{b(x)}^{\text{instead of t }}) \frac{d}{dx}b(x)-f(x,a(x))\frac{d}{dx}a(x) 
\end{aligned}$$

Okay Okay lets slow down , a lot of things are happening together . First Lets write our current equation 

$$\frac{2K}{R}=\int_0^R \frac{G \overbrace{m}^{\text{mass of particle at R }}\left( 4\pi r^2 \cdot d r \cdot\rho(r)\right)}{R^2}$$

On differentiating the left side we get $0$ but we cannot do the right side easily , why ? because the right side has two variables 

Just converting $R \to x$ and $r \to t$ in our previous problem we get

$$\int_0^x \frac{G \overbrace{m}^{\text{mass of particle at x }}\left( 4\pi t^2 \cdot d t \cdot \rho(t)\right)}{x^2}$$

Now this has two variables in one integral , If we define a function $f(x,t)$ as 

$$f(x,t)=\int_0^x \frac{G \overbrace{m}^{\text{mass of particle at x }}\left( 4\pi t^2 \cdot d t \cdot \rho(t)\right)}{x^2}$$

Then this function $f(x,t)$ would be an implicit(as two variables in) function and we would have to do some more work for it ( why? because in Leibnitz formula , if the function is explicit there is one less term)

So we can make the RHS of (1) by making it into (2)

$$\frac{2K}{x}=\int_0^x \frac{G \overbrace{m}^{\text{mass of particle at x }}\left( 4\pi t^2 \cdot d t \cdot \rho(t)\right)}{x^2} \tag 1$$

$$\frac{2Kx}{1}=\int_0^x G \overbrace{m}^{\text{mass of particle at x }}\left( 4\pi t^2 \cdot d t \cdot \rho(t)\right) \tag 2$$

We can furthermore bring the $m \times G\times 4 \pi$ to left hand side

$$\frac{2Kx}{mG4 \pi}=\int_0^x  \left(  t^2 \cdot d t \cdot \rho(t)\right) \tag 2$$

Now this is a beautiful implicit function which we can use leibnitz theorem on . But remember we are not Differentiating wrt r , But we are doing it wrt R , ie $\text{wrt x}$

$$\frac{2K}{mG4 \pi}=x^2\rho (x)\frac{d(x)}{dx}-0^2\rho(0)\frac{d(0)}{dx}$$

$$\frac{2K}{x^2mG4 \pi}=\rho (x)$$

Turning x to r since our answer is in r

$$\frac{2K}{r^2mG4 \pi}=\rho (r)$$