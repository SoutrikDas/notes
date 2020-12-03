# Fluid Statics ( Hydrostatics )

Child: A%20wooden%20block%20with%20a%20coin%20placed%20on%20its%20top,%20floa%20e33a6cc030d043d08c37db5a3cca2028.md, Complex%20Archimedes%20Theorem%20problems%2084ec5cd7bac740948ca77c6ca45bce0a.md, A%20block%20of%20ice%20with%20a%20lead%20shot%20embedded%20in%20it%20is%20%20b8fe2b50973d4541879baf170aaa6cb3.md, A%20hemispherical%20portion%20of%20Radius%20R%20is%20removed%20fro%20dc8f43cec2fa405dbddd4ec7768a3056.md, A%20thin%20uniform%20cylindrical%20shell%20,%20closed%20at%20both%20%2028ba4f3fa05c436190ec50c21b8c9d62.md, A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7.md, Concave%20v%20s%20Convex%20e158c7e95e5542e8941bd3b43c191a5b.md
Column: Sep 23, 2020 8:51 AM
Last edited by: Soutrik das
Tags: chapter, physics

As far as I know there are some main concepts 

- pressure
- pascals law
- archimedes principle and buyoncy
- viscosity
- Surface tension and Surface Energy

According to physics wallah , the three major parts of fluids are 

- Static
- Dynamic
- Surface Tension and Viscosity

In static Fluids we will only talk about Ideal Fluid , What is a Ideal Fluid ?

- Incompressible ( therefore only liquid , not gas , as gas is easily compressible )
    - Density constant
    - Fixed mass
    - Fixed Volume
- Non Viscous
- Fluid should be at rest with respect to the vessel its kept within

But later in the course we will cover fluid which will have Viscous force

# Pressure

---

Pressure is a scalar property , and its also isotropic 

By isotropic , we mean the value of pressure at any point , is same for any direction 

### Units

$$1 \text{atm}=1.013\times 10^5 \text{ Pa}$$

$$1 \text{ bar}=10^5 \text{ Pa}$$

$$1 \text{atm}=760 \text{ mm of Hg} \\
$$

$$1 \text{atm}=760 \text{ torr} \\
$$

$$1 \text{atm}=76 \text{ cm of Hg} \\
$$

## Variation of Pressure with Depth

---

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled.png)

Suppose given the pressure at surface is $P_o$ we want to find the pressure at the marked point , then we zoom into the imaginary cylinder , 

Since the liquid in the cylinder is not flowing upwards , netiher downwards , it means the net force on the imaginary cylindrical body of fluid is 0 , 

On balancing the forces we get 

$$P_oA \downarrow+mg\downarrow=PA\uparrow$$

Now this $m$ can be written in terms of $h$ and $A$ 

$$P_oA \downarrow+(hA\rho )g\downarrow=PA\uparrow$$

Now cutting $A$ from LHs and RHS we get

$$P_o \downarrow+(h\rho )g\downarrow=P\uparrow$$

Or simply 

$$\overbrace{P-P_o}^{\text{Gauge Pressure}}=\rho gh$$

$$\overbrace{P}^{\text{Absolute Pressure}}=P_o+\rho gh$$

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%201.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%201.png)

From this we can write that at some height $P_1=P_o+\rho gh_1$ and at some other height $P_2=P_o+\rho gh_2$ 

Substracting we get 

$$\Delta P=\rho g\Delta h$$

### Variation of Pressure vertically doesnt depend on the shape of the container

---

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%202.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%202.png)

## Variation of Pressure Horizontally  of a Non ( horizontally ) Accelerated Fluid

---

For a non accelerated fluid , since the net acceleration horizontally is 0 , $P_1A=P_2A$ hence there is no pressure variance at all 

However this is going to change in dynamic fluid or maybe when we have a moving static fluid ( beaker on a moving platform ) 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%203.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%203.png)

Q: Relate the pressure at $A$ , $B$ and $C$

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%204.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%204.png)

The answer is C , that $P_A=P_B=P_C$

Why ? 

1. Because pressure of a non horizontally accelerated fluid , is same on a horizontal line 
2. Intuitively , the slanted walls of the container apply some froce which cause the pressure at B and C to equal that of A 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%205.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%205.png)

Q: Find the force at the bottom of the glass , and find the force applied by the glass on water 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%206.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%206.png)

To find the force on the bottom of the glass , we will first find the pressure then use it to find force , 

$$P_b=P_o+\rho g(0.1 \text m)$$

$$F_b=P_b\times 10^{-3}\text{m$^2$}$$

But now , how do we find the force that the sides of the  glass exerts on the water , how does it even look , is the question talking about normal force ?

So the force that the sides of the glass applies , is $F_4$ 

$$F_4+P_bA=mg+P_oA$$

So from this equation we can find $F_4$ ( we know m , because $\rho$ and $V$ is given , $V=1 \text L$ )

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%207.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%207.png)

## Variation in Presure in accelerated Fluid

---

### Vertical Acceleration

---

From the frame of the container , there is a pseudo force acting on the water ( on the opposite side of $\vec a$ 

So on balancing the forces we get that 

$$P_oA\downarrow+mg\downarrow+ma\downarrow=PA\uparrow$$

now we know that $m=\rho A h$

$$P_oA\downarrow+(\rho A h)g\downarrow+(\rho A h)a\downarrow=PA\uparrow$$

Cutting A from both sides we get 

$$P_o\downarrow+\overbrace{(\rho  h)g\downarrow+(\rho  h)a\downarrow }^{\text{Gauge Pressure}}=P\uparrow$$

So we can write it as 

$$P=P_o+\rho (\overbrace{g+a}^\text{g effective})h$$

$$P=P_o+\rho g_{\small {eff}}h$$

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%208.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%208.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%209.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%209.png)

### Horizontal Acceleration

---

In any free surface of a liquid , the Resultant Force on surface is always perpendicular to the surface

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2010.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2010.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2011.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2011.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2012.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2012.png)

Now if you look from the frame of the beaker , the pseudo force will act on the opposite side of $\vec a$

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2013.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2013.png)

Which will result in something like this 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2014.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2014.png)

Now , if we draw a horizontal cylinder , like the one we did over [here](https://www.notion.so/soutrik/Fluid-Statics-Hydrostatics-81f1af117a754b2c990c63bc2ee42d1b#5ef70ed318b446a59ff33279c401edb7)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2015.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2015.png)

Now if we try to balance the forces ( along with pseudo force ) then we will get this 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2016.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2016.png)

This fluid , from the frame of beaker is in rest , hence we can balance the forces 

$$\overset{\leftarrow}{ma}+\overset{\leftarrow}{P_1A}=\overset{\rightarrow}{P_2A}$$

and again we know that $m=\rho g l$ ( here $l$ instead of $h$ , but with the same significance ) 

So putting that in , we get 

$$P_2-P_1=+\rho al$$

Use your intuition to understand where the pressure is high , and according to that put $P_b-P_a$ or $P_a-P_b$

If you move water to left , then pressure will increase as you go to right 
If you move beaker to right , then pressure will increase as you go left 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2017.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2017.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2018.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2018.png)

$$\tan \theta =\frac {h}l$$

But this $h$ might not be given , so how to find it ? 

We can use two equations 

$$P_E=P_A+\rho g h$$

$$P_E=P_F+\rho a l$$

and we know that $P_A=P_F=\text{atmospheric pressure }$

$$\rho gh=\rho al$$

$$\frac {h}{l}=\frac {a}{g}$$

$$\boxed{\tan \theta =\frac {h}{l}= \frac{a}{g}}$$

Q: Find the expression of pressure at a distance $r$ from the axis 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2019.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2019.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2020.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2020.png)

Force in the outward direction ( at $r$ radial distance ) is $m\omega^2 r$ , acceleration is $\omega^2 r$

so if we draw a cylinder 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2021.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2021.png)

But this acceleration is changing at every point , therefore integration . But what exactly are we integrating ? We cant integrate pressure over area ( we cant bring $dr$ into the equation ) 

So I guess we will integrate change in pressure as we move from $H$ to $I$ 

so for every $dr$ length , the increase in pressure is $\rho (\omega^2 r) dr$

$$\int_{P_H}^{P_I}dP=\int_0^x\rho\omega^2rdr$$

$$P_I-P_H=\rho \omega^2 \frac 12 x^2$$

# ( Torricilli's ) Barometer

---

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/new.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/new.png)

The empty space in the tube is vaccum

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2022.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2022.png)

Since pressure is same on a vertical line for a non accelerated fluid , so $P_1=P_2$ 

$$P_o=\rho_{\text{mercury}}gh$$

$$\rho_{\text{mercury}}=13600\text{ kg/m$^3$}$$

Density of mercury is 13.6 times than water ( RD is 13.6 )

[Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-19h19m33s-Class_11_chap_10____Fluids_03_____Barometer_and_Manometer_and_U_-_Tube_problems_JEE_MAINS__NEET___(_480_X_854_).mp4-.mp4](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-19h19m33s-Class_11_chap_10____Fluids_03_____Barometer_and_Manometer_and_U_-_Tube_problems_JEE_MAINS__NEET___(_480_X_854_).mp4-.mp4)

significance of 76cm of $Hg$

- WHy use mercury instead of water ?

    If you use water then to depic 1 atm , the height of water required is 10.1 m , which is too large 

# Manometer

---

Why use Manometer ? To measure pressure of an enclosed gas 

[Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-19h28m38s-Class_11_chap_10____Fluids_03_____Barometer_and_Manometer_and_U_-_Tube_problems_JEE_MAINS__NEET___(_480_X_854_).mp4-.mp4](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-19h28m38s-Class_11_chap_10____Fluids_03_____Barometer_and_Manometer_and_U_-_Tube_problems_JEE_MAINS__NEET___(_480_X_854_).mp4-.mp4)

# Archimedes principle

---

This is a rather common topic .

Upthrust acts on the center of mass of displaced fluid , while weight acts on the center of mass of solid 

if the body has area same throughout ( for example a cylinder ) 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2023.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2023.png)

Then we can derive an easier to use formula from Archimedes principle 

$$V_f\rho_fg=V_s\rho_sg$$

$$(A\times h_f)\rho_f=(A \times h_s)\rho_s$$

$$h_f\rho_f=h_s\rho_s$$

# Fluid Dynamics

---

In fluid dynamics the fluid we will look at will have the following properties 

- incompressible , no change in density
- non viscous
- Irrotational ( no vortex flow ) $\omega =0$

## Rules of Steady / Streamline Flow

---

Rules of Steady flow 

- At any point in space the velocity of fluid molecules remains constant with time
- Any Particle follows the path the preceeding particle

[Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-20h02m14s-Fluids_05____Fluid_Dynamics_1____Introduction___Bernoullis_Theorem__JEE_MAINS___NEET_(_480_X_854_).mp4-.mp4](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-20h02m14s-Fluids_05____Fluid_Dynamics_1____Introduction___Bernoullis_Theorem__JEE_MAINS___NEET_(_480_X_854_).mp4-.mp4)

We will assume these conditions for all the following fluid dynamics topics 

## Equation of Continuity

---

Applicable only for fluid that follows ideal fluid ( incompressible , no change in density , irrotational , streamline ) 

$$A_1v_1=v_2A_2$$

This is valid for any two cross sections ( the cross sections need not be real ) 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2024.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2024.png)

## Bernoulli's theorem

---

> The total energy per unit volume for a flowing fluid is constant

Take any two imaginary or real cross sections and let them have the following properties 

$$P+\rho gh+\frac 12 \rho v^2=\text{constant}$$

$$\underbrace{\overbrace{P}^{\text{Pressure nrg / unit vol}}+\overbrace{\rho gh}^{\text{potential nrg / unit vol}}+\overbrace{\frac 12 \rho v^2}^{\text{kinetic nrg / unit vol}}}_{\text{Total energy of a fluid}}=\text{constant}$$

[Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-20h21m29s-Fluids_05____Fluid_Dynamics_1____Introduction___Bernoullis_Theorem__JEE_MAINS___NEET_(_480_X_854_).mp4-.mp4](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-20h21m29s-Fluids_05____Fluid_Dynamics_1____Introduction___Bernoullis_Theorem__JEE_MAINS___NEET_(_480_X_854_).mp4-.mp4)

### Venturimeter

---

Why or what is this used for ? 

To measure the **rate of flow** ($\text{Vol/sec}$)  

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2025.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2025.png)

There are two circles drawn in the above pitcure , name the center of these circles as $A$ and $B$ , now the height of $A$ and $B$ is same 

so if we write the bernoulli equation , $h_1=h_2$ 

$$P_1+\rho gh_1+\frac 12 \rho v_1^2=P_2+\rho gh_2+\frac 12 \rho v_2^2$$

[Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-20h31m58s-Fluid_06___Applicaion_of_Bernoullis_Principle_-Venturimeter__Speed_of_efflux-_Torricellis_Theorem_(_480_X_854_).mp4-.mp4](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-20h31m58s-Fluid_06___Applicaion_of_Bernoullis_Principle_-Venturimeter__Speed_of_efflux-_Torricellis_Theorem_(_480_X_854_).mp4-.mp4)

$$P_1+\frac 12 \rho v_1^2=P_2+\frac 12 \rho v_2^2$$

$$P_1-P_2=\frac 12 \rho v_2^2-\frac 12 \rho v_1^2$$

$$P_1-P_2=\frac 12 \rho (v_2^2-v_1^2)$$

[Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-20h34m00s-Fluid_06___Applicaion_of_Bernoullis_Principle_-Venturimeter__Speed_of_efflux-_Torricellis_Theorem_(_480_X_854_).mp4-.mp4](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-12-20h34m00s-Fluid_06___Applicaion_of_Bernoullis_Principle_-Venturimeter__Speed_of_efflux-_Torricellis_Theorem_(_480_X_854_).mp4-.mp4)

$$\bcancel \rho gh=\frac 12 \bcancel\rho (v_2^2-v_1^2)$$

$$2gh=v_2^2-v_1^2 \tag 1$$

Now using Equation of Continuity $A_1v_1=A_2v_2$

$$\frac {v_2}{v_1}=\frac{A_1}{A_2} \tag 2$$

Now using equation 2 in equation 1

$$v^2_1(\frac{v_2^2}{v_1^2}-1)=2gh$$

$$v^2_1(\frac{A_1^2}{A_2^2}-1)=2gh$$

$$v^2_1(A_1^2-A_2^2)=2gh\times A_2^2$$

$$v_1=\sqrt{\frac{2ghA_2^2}{A_1^2-A_2^2}}$$

$$v_1=A_2\sqrt{\frac{2gh}{A_1^2-A_2^2}}$$

If you want to find $v_2$ directly you can use the following ( but honestly if you find $v_1$ first then just use equation of continuity ) 

$$v_2=A_1\sqrt{\frac{2gh}{A_1^2-A_2^2}}$$

### Speed of Efflux - Toricceli's Theorem

---

Why or what is this topic about ?

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2026.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2026.png)

Given the height of the hole , we can find the velocity of the fluid that is coming out , using this topic 

If we write bernoulli's equation for both points ($1$ and $2$ ) then we get 

$$P_1+\rho gh_1+\frac 12 \rho v_1^2=P_2+\rho gh_2^2+\frac 12 \rho v_2^2$$

Since both the holes are exposed to air , both of their pressure is equal to atmospheric pressure 

$$P_1=P_2=\text{atmospheric pressure }$$

$$\cancel P_1+\rho gh_1+\frac 12 \rho v_1^2=\cancel P_2+\rho gh_2^2+\frac 12 \rho v_2^2$$

Also cancel the density from both sides

$$ gh_1+\frac 12  v_1^2= gh_2^2+\frac 12  v_2^2$$

$$2g(\Delta h) =v^2_2-v_1^2$$

**This is always true**

But if $A_2 <<<A_1$ 

$$A_1v_1=A_2v_2$$

$$\frac{v_1}{v_2}=\overbrace{\frac{A_2}{A_1} }^{\text{this tends to 0 }}$$

therefore $v_1$ tends to 0 

then and only then 

$$\overbrace{v_2=\sqrt {2gh}}^{\text{only valid when A$_1$ << A$_2$}}$$

This is toricelli's Theorem 

# Viscosity

---

### Velocity Gradient and Friction force at Surface Contact

---

> Change in velocity per unity height

As you go away from river bed , the velocity changes 

Now it can vary non linearly or linearly , but generally we are given a constant velocity gradient 

If we are given $v=f(z)$ then the velocity gradient is $dv/dz$ 

But since its $v$ is a linear function of $z$ , sometimes they dont give the function , but just give $v_1,v_2$ and two different heights , then we have to assume that its a linear function 

$$\frac{\text{Change in velocity }}{\text{Change in height }}=\frac{\Delta v}{\Delta z}$$

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2027.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2027.png)

The formula for Friction force is 

$$F=-\eta A\frac{dv}{dz}$$

Units of $\eta$ are 

- 1 Poise = $10^{-1} \text{ $\frac{N-s}{m^2}$ }$

## Stokes Theorem and Friction when solid is immersed in liquid

---

> Stokes theorem says that the friction on a spherical solid body immersed in a liquid is $6\pi \eta R v$

### Terminal Velocity

---

When a body is falling it experiences some forces 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2028.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2028.png)

Friction force is dependent on velocity , so when you just drop the ball ( $v=0$ ) then there is almost no friction force , but as the ball gains velocity , the opposing force ( friction ) also increases , and at one point the ball has 0 acceleration , and that state is a stable equilibrium.

At that point we can balance the forces 

$$6\pi \eta Rv_t+\overbrace V^{volume}\rho_l g=V\rho _s g$$

Where 

- $v_t$ is the terminal  velocity
- $V$ is volume
- $\rho _l$ is density of the fluid in which this is happening
- $\rho _s$ is density of the solid ball
- $R$ is the radius of the Solid ball

$$6\pi \eta R v_t+\frac 43 \pi R^3 \rho_lg=\frac 43 \pi R^3 \rho _s g$$

$$6 \pi \eta R v=\frac 43\pi R^3g(\rho _s - \rho _l)$$

$$v=\frac 43 \frac {\pi R^3g}{6\pi \eta R}(\rho _s - \rho _l)$$

Cleaning this equation up we get 

$$v=\frac{2}{9} \frac{R^2g}{\eta}(\rho_s -\rho _l)$$

Sometime the terminal velocity may come to be negative , and that happens only when $\rho s <\rho_l$ and one good example of this is an air bubble in water ( or any other fluid ) , density of air is less than density of water . 
Negative Terminal velocity  signifies that the object will rise upward ( instead of going downward ) 

# Surface Tension ($S$ or $T$ )

---

> Surface has some extra energy that the bulk does not have , and Nature being nature , always trying to minimize energy ,  The property of liquid by virtue of which the liquid tends to minimize the surface area is called Surface Tension

If you draw an imaginary line on a soap film , then the 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2029.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2029.png)

Left side wants to try and Pull the right side , and vice versa 

Now the Perpendicular force ( on this line ) divided by the length of the line is defined as Surface Tension

$$S=\frac{F_{\perp}}{l}$$

And this is a constant 

So how will you use it ? In questions the Value of $S$ or Surface tension wil be given , and from that you have to find the force 

$$F_{\perp}=S \times l$$

For example if you weigh a object on a liquid frame 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2030.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2030.png)

Then for this case $S\times l =W$

Value of Surface Tension 

- For Water $0.075 \frac{\text{N}}{\text m}$
- For Soap $0.03 \frac{\text{N}}{\text m}$
- For mercury $0.4 \frac{\text{N}}{\text m}$ ( this is pretty high , even in lab , when i spilt mercury , it was still a complete sphere )

Q Find the value of $m$ so that the wire remains in equilibrium 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2031.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2031.png)

$F=l\times S$ so 

$$mg=F=l\times S$$

$$m\times 10=\frac 1{10}\times 0.03$$

$$m=0.0003 \text{ kg} ❌$$

But thats wrong ❌

Soap Films are always double Layered ( one from front and one from behind ) 

$$F=2S\times l $$

$$m\times 10=2\times \frac 1{10} \times 0.03$$

$$m=0.0006 \text{ kg} $$

This is correct 

## Surface Energy ( $U$ , $\Delta U$ )

---

Surface Molecules are not in an equilibrium ( due to unbalanced forces ) compared to bulk molecules

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2032.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2032.png)

So one second they are on the top , then their friends pull them down and they go on the top , and this fighting always happens , and it has been observed that molecules at the surface contain more energy than the molecules of bulk .

Due to this ( and the fact that nature always wants to reduce energy ) we get the tendency of liquids to always try to have minimum surface area ( to minimize this extra energy that ONLY the surface molecules have ) 

How to determine Surface Energy ? The change in Surface energy is more relevant than Surface Energy .

To find the change , we do work on the Surface ( to expand the surface , thereby increasing its energy ) which results in a change 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2033.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2033.png)

Soap Films have $F=2\times S\times l$

The work done by external agent is 

$$W=2\times S\times l \times \Delta x$$

but we can Express the $2l \Delta x$ part as $\Delta A$ , how and why ? how is below , as to why , maybe we will use this formula for shapes other than rectangular , so we want a more general formula 

 

$$A_i=\overbrace{2}^{\text{due to two layers}} \times lx$$

$$A_f=2l(x+\Delta x)$$

$$\Delta A=2l\Delta x$$

Therefore the Work we did can be written as 

$$W=S\Delta A$$

Which is the change in surface energy 

$$\Delta U=S\Delta A$$

From this formula we can get another definition of Surface Tension $S$( constant ) : The surface energy per unit area ( $J/m^2$ )

Q: Find the work required to increase the radius of a **soap** bubble from 2cm to 5cm  ( S=0.03 N/m)

For this we need the change in area 

$$A_i=4\pi \times 10^{-4}$$

$$A_f=25\pi \times 10^{-4}$$

$$\Delta A=21\pi \times 10 ^{-4}$$

Now we can Calculate the work required 

$$W_{required}=S\Delta A=0.03\times 21\pi \times 10^{-4}$$

$$W_{required}=63\pi \times 10^{-6} \text J ❌$$

Which is wrong ❌ because soap is double layered 

$$A_i=2\times 4\pi \times 10^{-4}$$

$$A_f=2\times 25\pi \times 10^{-4}$$

$$\Delta A=2\times 21\pi \times 10 ^{-4}$$

$$W_{required}=2 \times 0.03\times 21\pi \times 10^{-4}=126\pi \times 10^{-6} \text J$$

Q: A big liquid droplet $R=0.01m$ breaks into $K=10^\alpha$ small droplets such that the change in Surface energy is $10^{-3}J$ , Given $S=0.1/4\pi$ , find alpha $\alpha$

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2034.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2034.png)

**THis is not soap** 

$$A_i=4\pi R^2$$

final radius is 

$$K\times \frac 4 3 \pi r^3=\frac 4 3 \pi R^3$$

$$r=R\times 10^{-\frac {\alpha}3}$$

So final Surface Area is 

$$A_f=10^{\alpha}\times 4\pi r^2$$

$$A_f=10^{\alpha}\times 4\pi (R\times 10^{-\frac {\alpha}3})^2$$

$$A_f=10^{\alpha}\times 4\pi (R^2\times 10^{-\frac {2\alpha}3})$$

Now we know the change in surface energy , equating that value to $S\Delta A$ 

$$10^{-3}=\frac{0.1}{4\pi}\times \{ 10^{\alpha}\times 4\pi (R^2\times 10^{-\frac {2\alpha}3})-4\pi R^2\}$$

To solve this we need one more approximation to find that $\alpha =6$ 

## Excess Pressure in a Liquid / Bubble Drop

---

For a liquid drop like so , we can say that the boundary ( or any other point for that matter ) is in equilibrium ( $F=0$ ) So we should be able to say that 

$$P_{int}=P_{ext}$$

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2035.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2035.png)

But that would have been true only if there wasnt any **Surface Tension**  , If we take that into account , then the picture looks something like this 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2036.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2036.png)

Which means that if we balance forces on the boundary at any point 

$$\overset{\rightarrow}{F_L}=\overset{\leftarrow}{F_E} +\overset{\leftarrow}{F_S}$$

Therefore inside , the liquid pressure is **excess**  when compared to the outside pressure ( and the reason is surface tension ) and the formula for this excess pressure is : 

$$P_L-P_E=\frac{2S}{R}$$

$$P_{\text{inside}}-P_{\text{outside}}=\frac{2S}{R}$$

$$P_{\text{concave}}-P_{\text{convex}}=\frac{2S}{R}$$

![A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/Untitled%202.png](A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/Untitled%202.png)

But why is this the formula ? For the short derivation go [here](https://youtu.be/Us7sk1OrcUc?t=852) 

**For Soap**  

$$P_{\text{inside}}-P_{\text{outside}}=\frac{4S}{R}$$

[Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-13-10h13m03s-Fluid_10____Surface_Tension_02____Excess_Pressure_inside_a_Liquid_Drop_IIT_JEE_MAINS___NEET____(_480_X_854_).mp4-.mp4](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/vlc-record-2020-09-13-10h13m03s-Fluid_10____Surface_Tension_02____Excess_Pressure_inside_a_Liquid_Drop_IIT_JEE_MAINS___NEET____(_480_X_854_).mp4-.mp4)

Q: In an Air chamber , the pressure is $8 N/m^2$ , in it are two soap bubbles $A$ ( $R_A=2cm$) and $B$ ( $R_B=4cm$ ) and S=0.04 N/m 

Then find $n_b/n_a$ where $n$ represent no. of moles in respective bubbles 

Using the formula of excess pressure we can find the pressure inside , and then assuming that the gas is ideal we can use $PV=nRT$ to get ratio of $n$ 

Pressure inside A =

$$P_A=\frac {2S}{R_A}+P_o$$

$$P_B=\frac {2S}{R_B}+P_o$$

We know value of $R_A$ , $R_B$ , $P_o$ therefore we know the value of $P_A$ and $P_B$ 

now we know $V_A$ and $V_B$ because volume of a sphere is $\frac 43 \pi R^3$ , from that we get 

$$\frac{n_b}{n_a}=\frac{P_B\times V_B}{P_A \times V_A}$$

Putting all the values we will get the answer 

## Contact Angle  $\theta$

---

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2037.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2037.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2038.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2038.png)

But how did we know that angle of contact is not these ? 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2039.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2039.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2040.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2040.png)

Because there are certain rules which we have to keep in mind when drawing lines to form angle 

- Take Point of contanct

![A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/contactangle01.gif](A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/contactangle01.gif)

- For Liquid Draw tangent ( away from solid )

![A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/contactangle02.gif](A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/contactangle02.gif)

- For Solid Draw Tangent ( towards the liquid )

![A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/contactangle03.gif](A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/contactangle03.gif)

Now doing it all together we have 

![A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/contactangle041.gif](A%20cylindrical%20capillary%20tube%20of%200%202%20mm%20radius%20is%20m%202b54ce7ef00a455592040d1fec07c0a7/contactangle041.gif)

Those curves that the liquid forms where its touching the glass rod , is called meniscus , in the pictures above there was only concave meniscus , but a convex meniscus is also possible 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2041.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2041.png)

Here is how you get the contact angle for a convex meniscus 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/contactangle05.gif](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/contactangle05.gif)

### Wetting and not Wetting

---

We say that a liquid has wetted a solid if the contact angle with the solid is Less than 90 ie $\theta < 90 \degree$

So if a liquid forms Concave meniscus then we will say that it has "**wet the solid**"  and if a liquid forms convex meniscus we say that the "**liquid doesnt wet the solid**" 

But now the question comes , why do liquids even form these meniscus ? 

### Cohesive and Adhesive force

---

Cohesive - Between same molecules 

Adhesive - Between different molecules 

The thing is , ( take water and glass ) , the cohesive force of water ( force between water and water ) is less than that of adhesive force between water and glass , that is why the glass pulls water towards itself 

$$\text{Cohesive}<\text{Adhesive }$$

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2042.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2042.png)

And we know that in a static liquid , the Free surface is always perpendicular to net force , so that also holds up 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2043.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2043.png)

Whereas for mercury , the reverse happens , the cohesive force is so large that the glass is not able to pull at all , it forms a depression 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2044.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2044.png)

Convex Meniscus 

$$\text{Cohesive}>\text{Adhesive}$$

## Capillary Action

---

If contact angle $<90\degree$ then the liquid rises in a capillary tube ( a tube with very small radius ) 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2045.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2045.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2046.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2046.png)

If contact angle $>90\degree$ then the liquid depresses in a capillary tube 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2047.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2047.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2048.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2048.png)

### When Capillary is cylindrical

---

For general case we find that the height can be found out theoretically using 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2049.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2049.png)

$$h_{\text{vertical}}=\frac{2S\cos \theta}{r\rho g}$$

Where 

- $r$ is radius of capillary tube

The crux of the derivation , is that the meniscus that is exposed to air ( in capillary tube ) has two surfaces , Concave and convex 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2050.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2050.png)

From the concept of excess pressure inside water bubble we know that 

$$P_{\text{concave}}-P_{\text{convex}}=\frac{2S}{R}$$

therefore the pressure under the meniscus will be 

Where 

- $R$ is NOT the radius of capillary , but the radius of the meniscus

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2051.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2051.png)

Which can be expressed in the terms of $r$ which is the radius of capillary tube 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2052.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2052.png)

$$R\cos \theta = r$$

$$P_{\text{inside meniscus}}=P_o-\frac{2S\cos \theta }{r}$$

Now we can use the fact that  Pressure at $X$ and $Y$ are same , and the fact that Pressure at $Y$ is $P_o$ 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2053.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2053.png)

$$P_x=P_o-\frac{2S\cos \theta }{r}+\rho gh_{\text{vertical}}$$

$$P_y=P_o$$

Equating these two we get 

$$\rho gh_{\text{vertical}} =\frac{2S\cos \theta }{r}$$

On rearranging we get 

$$h_{vertical}=\frac{2S \cos \theta}{r \rho g}$$

Q: If the calculated value of $h_{\text{vertical}}=\frac{2S \cos \theta}{r\rho g}$ is coming to be 1 cm , in a cylindrical capillary tube of 4cm , then if we slant the tube at an angle of $60 \degree$ with horizontal , then what will be the value of $l$ 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2054.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2054.png)

That is where the $h_{vertical}$ comes in , the calculated height has to be the vertical height , which means $l$ , the slant height will be more than $1cm$ and in fact it is $\frac 2 {\sqrt 3}$cm

This concept of h vertical can be understood from the fact that even if the column is slanted , when measureing the change in pressure using $\Delta P=\rho g \Delta h$ we take the vertical height only 

### When Capillary is conical

---

If the capillary is not of cylindrical shape , it may cause some changes , for example 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2055.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2055.png)

Pressure inside is 

$$P_{convex}=P_o-\frac{2S}{R}$$

Now the problem is this time the relation between $R$ and radius of capillary at that point $b$ might not be same 

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2056.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2056.png)

![Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2057.png](Fluid%20Statics%20(%20Hydrostatics%20)%2081f1af117a754b2c990c63bc2ee42d1b/Untitled%2057.png)

This time the relation is 

$$R\cos (\frac \alpha 2 +\theta)$$

The rest of the steps should be same , so finally we get that 

$$h_{\text{vertical}}=\frac{2S \cos (\frac \alpha 2 +\theta)}{r \rho g}$$

### Tube of Insufficient Length ( When capillary height $h_{\text{vertical}}=\frac{2S\cos \theta}{r\rho g}$ < Length of Tube )

---

What happens then ? 

We only have two options 

- Overflow of water  ( if this happened , then it would be like putting a capillary in a beaker and water would rise up , and fall out of capillary into the beaker and then go up again )  Perpetual motion ! Which doesnt happen

![https://i.ibb.co/Fs2J6XH/image.png](https://i.ibb.co/Fs2J6XH/image.png)

- Liquid will rise to the top and change is meniscus angle

Before 

$$h<l$$

$$\frac{2S\cos \theta _i}{r \rho g}<l$$

$$\frac{2S\cos \theta _f}{r \rho g}=l$$

$$\theta _f=\cos ^{-1} \left(\frac{r \rho g l}{2S } \right)$$