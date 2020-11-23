# Capacitance

Child: In%20the%20circuit%20shown,%20initially%20there%20is%20no%20charge%208e5f10ffb6b346daa9f3f9e216ba0a67.md, Redistributing%20Charges%20Grounding%20(%20Connecting%20char%20629b314ecb0341b380fa2ecb23d86d71.md, Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb.md, Two%20uncharged%20identical%20Capacitors%20A%20and%20B%20,%20each%20%209b1d619e7a424dbb9cbfc826d9049eed.md
Column: Sep 26, 2020 12:02 PM
Last edited by: Soutrik das
Parent: Electric%20Potential%206271e75f33a14a86a800bca3330eebb2.md, Dielectric%20224a5f771d714fb78f404df0bcf63c22.md, Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843.md
Tags: physics

This is one of those chapters that I did not wish to cover , simply because its so easy to forget everything , and there are so many nuances with series parallel , energy going here , there blah blah 

and not all capacitors are really parallel plate capacitors , there are spherical , there are cylindrical ,

But what really is capacitance ? and how is it derived ? 

Capacitance as traditionally described , is $C=Q/V$ what does that mean ? Connect two conductors , with a battery , that will create a potential difference accross them , and then see the charge being accumulated on each of those conductors , take the ratio and Wallah , you have yourself  the capacitance 

# What is Capacitance ?

---

## Self Capacitance

---

In electrical circuits, the term capacitance is usually a shorthand for the mutual capacitance between two adjacent conductors, such as the two plates of a capacitor. However, for an isolated conductor, there also exists a property called self capacitance, which is the amount of electric charge that must be added to an isolated conductor to raise its [electric potential](https://en.wikipedia.org/wiki/Electric_potential) by one unit (i.e. one volt, in most measurement systems).[[3]](https://en.wikipedia.org/wiki/Capacitance#cite_note-3) The reference point for this potential is a theoretical hollow conducting sphere, of infinite radius, with the conductor centered inside this sphere.

Mathematically, the self capacitance of a conductor is defined by

{\displaystyle C={\frac {q}{V}},}

## Mutual Capacitance

---

## What is Capacitance for isolated conductors

---

![Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled.png](Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled.png)

## What is Capacitance for common capacitors

---

The amount of charge that can be stored per unit increase in potential 

$$C=\frac {\Delta Q}{\Delta V}$$

# Charge Redistribution

---

![Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%201.png](Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%201.png)

It can be done in two ways [Redistributing Charges Grounding ( Connecting charged spheres with more charged Spheres ) ](Redistributing%20Charges%20Grounding%20(%20Connecting%20char%20629b314ecb0341b380fa2ecb23d86d71.md) 

The two ways are 

- Equating the potentials at the contact point
    - Quite literally equating it $\frac{kq_1}{R_1}=\frac{kq_2}{R_2}$
    - Using capacitance , $V_1=V_2$ so $C_1q_1=C_2q_2$

# Value of Capacitance with Dielectric Slabs

---

$$C=\frac{\varepsilon_{0} A}{\left(\underbrace{d-t_{1}-t_{2}-\ldots-t_{n}}_{\text{empty space}}\right)+\left(\frac{t_{1}}{K_{1}}+\frac{t_{2}}{K_{2}}+\ldots+\frac{t_{n}}{K_{n}}\right)}$$

# Some Easy Questions on Capacitance

---

## Objective Level 1

---

### Answers

![Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%202.png](Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%202.png)

### Questions

---

Q1: The seperation between the plates of a charged parallel-plate capacitor is increased. The force between the plates :

![Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%203.png](Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%203.png)

Is this force due to Coulumb force between the two charges ? and nothing else ? 

~~Lets calculate the charges , CV and -CV , so the force is~~ 

$$F=\frac{kC^2V^2}{d^2}$$

~~The force should decrease from this formula~~ 

~~But it doesnt ? Why and how come ? Probably because Capacitance is also dependent on distance~~ 

$$C=\frac{A\epsilon_0}{d}$$

~~Which makes the equation of force into :~~

$$F=\frac{kA^2 \epsilon_0^2V^2}{d^4}$$

This coulumb force equation is only for point charges 

Here , we can first find out the electric field due to one plate and then use the charge of the other plate to find the force of attraction 

$$E_1=\frac{\sigma}{2\epsilon_0}=\frac{q}{2A\epsilon_0}$$

the force is 

$$F=\frac{q^2}{2A\epsilon_0}=\frac{(CV)^2}{2A\epsilon_0}$$

Which is independant of force 

We can also use Gauss law , since charge will remain same , and the area also remains same , the electric field has to remain same in magnitude , hence the force will also remain same 

![Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%204.png](Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%204.png)

---

![Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%205.png](Capacitance%20caeded92469e47e098a21d1ef36e2d0c/Untitled%205.png)

If we connect the two plates of a capacitor then it will become a conductor , so what is the capacitance of a conductor ?

No matter how much potential you apply , you cannot store any charge on a conductor , so the Capacitance is 0 

because it defines the capacity of charge that can be stored.

# Potential difference across a capacitor

---

If you are going from left , take into calculation , the charge of the right plate 

![Capacitance%20caeded92469e47e098a21d1ef36e2d0c/capacitancepotentialdiff11.gif](Capacitance%20caeded92469e47e098a21d1ef36e2d0c/capacitancepotentialdiff11.gif)

Going from left to right potential decreases 

When you are going from right to left , then take into calculation , the charge on the left plate

![Capacitance%20caeded92469e47e098a21d1ef36e2d0c/capacitancepotentialdiff2.gif](Capacitance%20caeded92469e47e098a21d1ef36e2d0c/capacitancepotentialdiff2.gif)

Goign from right to left , potential increases