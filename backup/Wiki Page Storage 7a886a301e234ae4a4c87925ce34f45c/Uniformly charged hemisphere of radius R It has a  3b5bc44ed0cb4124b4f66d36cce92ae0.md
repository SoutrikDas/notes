# Uniformly charged hemisphere of radius R. It has a volume charge density \rho. If the electric field at point 2R above its center is E, then what is the electric field at the point 2R below its center?

Column: Oct 9, 2020 9:40 PM
Last edited by: Soutrik das
Tags: doubt, doubt cleared, physics

![Uniformly%20charged%20hemisphere%20of%20radius%20R%20It%20has%20a%20%203b5bc44ed0cb4124b4f66d36cce92ae0/WhatsApp_Image_2020-09-05_at_20.22.04.jpeg](Uniformly%20charged%20hemisphere%20of%20radius%20R%20It%20has%20a%20%203b5bc44ed0cb4124b4f66d36cce92ae0/WhatsApp_Image_2020-09-05_at_20.22.04.jpeg)

Is this a question of electrostatic pressure ? 

- Trying to Integrate ?

    ## Electric Field of a ring on its axis

    $$E=\frac{kqx}{(x^2+R^2)^{\frac 32}}$$

    ## Electric Field of a Hollow Hemisphere on its axis

    ---

    ![Uniformly%20charged%20hemisphere%20of%20radius%20R%20It%20has%20a%20%203b5bc44ed0cb4124b4f66d36cce92ae0/Untitled.png](Uniformly%20charged%20hemisphere%20of%20radius%20R%20It%20has%20a%20%203b5bc44ed0cb4124b4f66d36cce92ae0/Untitled.png)

    Area of each strip is 

    $$A=(Rd\theta)\times2 \pi (R\cos \theta)$$

    Charge of each small strip is 

    $$ dq= \sigma \times (Rd\theta)\times2 \pi (R\cos \theta)$$

    So using [this](https://www.notion.so/Uniformly-charged-hemisphere-of-radius-R-It-has-a-volume-charge-density-rho-If-the-electric-field-33180abd90c2452db7cc17116dc57238#9af7ca18c3a04ef4987d8c04debba565) equation we get 

    $$dE=\frac{k(dq)(x+R\cos \theta)}{((x+R\cos \theta)^2+R^2 \sin^2\theta)^{\frac 32}}$$

    i probably wont come out of this alive 

    $$dE=\frac{k(\sigma \times (Rd\theta)\times2 \pi (R\cos \theta))(x+R\cos \theta)}{((x+R\cos \theta)^2+R^2 \sin^2\theta)^{\frac 32}}$$

# Using Symmetry

---

![Uniformly%20charged%20hemisphere%20of%20radius%20R%20It%20has%20a%20%203b5bc44ed0cb4124b4f66d36cce92ae0/Untitled%201.png](Uniformly%20charged%20hemisphere%20of%20radius%20R%20It%20has%20a%20%203b5bc44ed0cb4124b4f66d36cce92ae0/Untitled%201.png)

Electric field due to 2 at A is E , so electric field due to 1 at B is also E 

What we want is : Elec field of 2 at B 

Now we Know 

$$\text{E due to whole sphere at B}=\text{E due to 1 at B}+\text{E due to 2 at B}$$

$$\overbrace{\frac{kq}{4R^2}}^\text{E due to whole sphere at B}=\overbrace{E}^{\text{we know this from symmetry}}+\text{E due to 2 at B}$$

$$k\frac{\frac{4}{3}\pi R^3 \rho}{4R^2}=k \frac{\pi R \rho}{3}$$

$$\frac{R\rho}{12\epsilon_0}-E$$