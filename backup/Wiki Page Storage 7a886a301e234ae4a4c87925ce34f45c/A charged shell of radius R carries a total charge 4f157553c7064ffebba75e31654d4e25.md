# A charged shell of radius R carries a total charge Q. Given \Phi as the flux of electric field through a closed cylindrical surface of h, radius r and with its center same as that of the shell. Here, center of the cylinder is a point on the axis of the cylinder which is equidistanc from its top and bottom surfaces.

Column: Sep 24, 2020 1:36 PM
Last edited by: Soutrik das
Parent: JEE%20ADV%202019%20paper%201%206e969e4fdf724b4eba045ad8c9ac0feb.md
Tags: adv, physics, question

![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled.png)

> This is a charged **shell**  not a charged **volume**

# Option A

---

The first option will be true , because if the height is more than 2R and $r>R$ then the cylinder encapsulates the sphere , hence all the charge of the sphere contributes to making flux

![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/option1.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/option1.png)

~~For all the other options than option 1 , we will have to find out the volume of the cylinder and use that to our advantage maybe ? But not always does the volume of cylinder fully encompass a charge~~ 

![https://i.postimg.cc/1XjCPwt0/cylindersphereintersection.gif](https://i.postimg.cc/1XjCPwt0/cylindersphereintersection.gif)

This animation is totally wrong . here , the charge is in the volume , which it is not true ! This image is from [postimg.cc](http://postimg.cc) and plays perfectly. 

![https://i.postimg.cc/ht6LmKtm/cylindersphereintersection2.gif](https://i.postimg.cc/ht6LmKtm/cylindersphereintersection2.gif)

This is how it actually is 

[]()

# Option 2

---

So when we start at height =4R/5 

![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%201.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%201.png)

We get this point whose x coordinate we can find out from the equation $x^2+y^2=R^2$

And we get $x=\frac 35 R$

Which means we are just barely inside

![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%202.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%202.png)

~~So we can directly use the volume of the cylinder = $\pi (\frac 35 R)^2 (\frac 4 5 R)$= $\pi R^3 \frac{36}{125}$~~

$$V_c=\pi R^3 \frac{36}{125}$$

~~So the fraction of charge inside this cylinder is~~ 

$$\rho=\rho\\
\frac Q {V_s}=\frac{Q'}{V_c}$$

$$Q'/Q=V_c/V_s$$

$$Q'=Q\times (\frac {27}{125})$$

~~But the option has $\Phi=0$ so the option is incorrect~~ 

But [this site](https://www.toppr.com/ask/question/a-charged-shell-of-radius-r-carries-a-total-charge/)  and even some others claim its correct , that $\Phi=0$ is true for this case , but how ?

Because the charge is distributed in the shell , and the cylinder is just barely inside it , meaning that it encompasses no charge , hence $\Phi =0$

**option B is correct**

# Option C

---

- Failed try

    This time we are in a bit of trouble 

    ![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%203.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%203.png)

    We need to integrate

    However , [this site](https://www.toppr.com/ask/question/a-charged-shell-of-radius-r-carries-a-total-charge/)  have used [Solid angle ](Solid%20angle%20f91c78e4c3ab459daa183aea0504c8ff.md) to find the volume , but how is that possible 

    - We need to integrate the area not volume

        $$dA=2\pi (R \cos \theta )\times (Rd\theta )$$

        ![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/WhatsApp_Image_2020-09-24_at_07.38.17.jpeg](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/WhatsApp_Image_2020-09-24_at_07.38.17.jpeg)

    ![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/new.jpg](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/new.jpg)

    But the question comes from where to where do we integrate ? 

    ![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/new%201.jpg](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/new%201.jpg)

    $$V(x) =\pi R^2\int \cos ^2 \theta d\theta $$

    $$V(x) =\frac {\pi R^2}{2}(\int \cos  2\theta d\theta+\int  1d\theta )$$

    For this option the $x=3R/5$ which means the theta is 

    ![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%204.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%204.png)

    $$\theta =37 \degree$$

    $$V(\theta) =\frac {\pi R^2}{2}(\frac{\sin 2\theta}{2}+\theta )$$

    $$V(\theta) =\frac {\pi R^2}{2}(\frac{4}{2\times 5}+\frac{37\times \pi}{180} )$$

    This is a very weird number , can we even have a good fraction come out of it ?

![https://i.postimg.cc/N03Fk9ps/optionc.gif](https://i.postimg.cc/N03Fk9ps/optionc.gif)

![https://i.postimg.cc/kgD5rFHM/optionc2.gif](https://i.postimg.cc/kgD5rFHM/optionc2.gif)

So we can indeed use [Solid angle ](Solid%20angle%20f91c78e4c3ab459daa183aea0504c8ff.md) to find the area of these pieces. 

$$A=2\pi R^2 (1-\cos \theta)$$

and from the formula of solid angle $(\Omega=\frac{A}{R^2})$  , we get to know that 

$$\Omega =2\pi (1-\cos \theta )$$

Where $\theta$ is the angle of this cone 

![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%205.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%205.png)

Matter of fact we can find the solid angle , with just the angle of the cone 

Which can be founf out 

![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%206.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%206.png)

Now we only need the $\cos \theta$ of this angle , which is $\cos  \theta=\frac 35$ 

Now using this formula , we find that the area of One of those pieces is 

$$A=2\pi R^2 (1-\cos \theta)$$

$$A=2\pi R^2 (\frac 2 5)=\frac 15 (4 \pi R^2)$$

Therefore the area of two of those pieces is 

$$A_T=\frac{2}{5}(4\pi R^2)$$

Which means charge enclosed in it is $\frac{2Q}{5}$

So **option C is incorrect**

# Option D

---

This is just like option C , we will only need $\cos \theta$ which is 

![A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%207.png](A%20charged%20shell%20of%20radius%20R%20carries%20a%20total%20charge%204f157553c7064ffebba75e31654d4e25/Untitled%207.png)

$$\cos \theta =\frac 45$$

Using the formula for area of one of the pieces we get

$$A=2\pi R^2 (1-\cos \theta)$$

$$A=2\pi R^2 (\frac 1 5)$$

For two , we will get 

$$A_T=2A=\frac{1}{5}(4 \pi R^2)$$

Hence the charge enclosed in it will be $\frac 1 5 Q_0$ 

Which means **Option D is correct**