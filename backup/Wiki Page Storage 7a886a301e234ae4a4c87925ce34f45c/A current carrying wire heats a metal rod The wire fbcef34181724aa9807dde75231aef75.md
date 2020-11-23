# A current carrying wire heats a metal rod. The wire provides a constant power (P) to the rod. The metal rod is enclosed in an insulated container. It is observed that  the temperature (T) in the metal rod changes with time (t)as T(t)=T_0(1+\beta t^{\frac 14}) where \beta is a constant with appropriate dimension while T_0 is a constant with dimension of Temperature. What is the heat capacity of the metal?

Column: Sep 23, 2020 2:31 PM
Last edited by: Soutrik das
Parent: JEE%20ADV%202019%20paper%201%206e969e4fdf724b4eba045ad8c9ac0feb.md
Tags: adv, physics, question

![A%20current%20carrying%20wire%20heats%20a%20metal%20rod%20The%20wire%20fbcef34181724aa9807dde75231aef75/Untitled.png](A%20current%20carrying%20wire%20heats%20a%20metal%20rod%20The%20wire%20fbcef34181724aa9807dde75231aef75/Untitled.png)

First of all lets write what we are given

- So there is a rod and there is a current carryiong wire ( how are they connected ? a series ?)
- The wire Provides $P$ power to rod , what is power in current electricity ? $VI$ is power so $VI=P$
- Metal Rod insulated in a container ( WHy ? )
- $T(t)=T_0(1+\beta t^{\frac 14})$

What do we know about heat capacity ?

- Heat capacity is the Heat to increae 1 degree of temperature , $c=\frac{q}{\Delta T}$
- Specific heat is the heat to increase i degree for 1 unit mass

So basically we have to find how much is temperature rises with how much heat is being produced , 

All the work is converted to Heat ? then per second ( Power is work per second right) the Heat produced is $P$ , in $t$ seconds the heat produced will be $Pt$ 

The change in temperature ( should I take $\Delta T$ or $\text dT$ ? because a function is given for Temp ) 

$$⁍ $$

$$⁍$$

$$⁍$$

$$c=\frac{dP}{dt} \frac{dt}{dT(t)}$$

$$c=P\times  \frac{1}{T_0(\frac 14\beta t^{-\frac 34})}$$

I think we can find the answer by rearranging this 

$$c=\frac{4Pt^{\frac 34}}{\beta T_0}$$

Lets go back to the original equation , we might need to substitute somethings

$$⁍$$

$$\frac{T(t)-T_0}{\beta T_0}=t^{\frac 14}$$

on cubing

$$\left( \frac{T(t)-T_0}{\beta T_0} \right)^3 =t^{\frac 34}$$

$$c=\frac{4P\left( \frac{T(t)-T_0}{\beta T_0} \right)^3}{\beta T_0}$$

$$c=\frac{4P(T(t)-T_0)^3}{\beta ^4T_0^4}$$

There we go